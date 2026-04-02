#!/usr/bin/env python3
"""Generate daily, weekly, or monthly git activity reports."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from collections import OrderedDict
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Iterable


LOCAL_TZ = datetime.now().astimezone().tzinfo
DEFAULT_CUTOFF_HOUR = 18
DEFAULT_MAX_COMMITS = 200
IGNORED_DIR_NAMES = {
    ".git",
    "node_modules",
    ".pnpm-store",
    ".yarn",
    ".next",
    "dist",
    "build",
    "__pycache__",
}


@dataclass
class Commit:
    repo: str
    sha: str
    author: str
    email: str
    date: datetime
    subject: str


def env_default_root() -> str:
    return os.environ.get("GIT_ACTIVITY_REPORT_ROOT", ".")


def env_default_cutoff_hour() -> int:
    value = os.environ.get("GIT_ACTIVITY_REPORT_CUTOFF_HOUR")
    return int(value) if value else DEFAULT_CUTOFF_HOUR


def env_default_max_commits() -> int:
    value = os.environ.get("GIT_ACTIVITY_REPORT_MAX_COMMITS")
    return int(value) if value else DEFAULT_MAX_COMMITS


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a work report from git commit history."
    )
    parser.add_argument(
        "--period",
        choices=("day", "week", "month"),
        default="day",
        help="Reporting period. Defaults to day.",
    )
    parser.add_argument(
        "--root",
        default=env_default_root(),
        help="Root directory used to scan multiple git repositories.",
    )
    parser.add_argument(
        "--repo",
        help="Path to a single target git repository.",
    )
    parser.add_argument(
        "--author",
        help="Filter commits by author name or email substring.",
    )
    parser.add_argument(
        "--since",
        help="Override start time, for example 2026-04-01 or 2026-04-01T09:00:00.",
    )
    parser.add_argument(
        "--until",
        help="Override end time, for example 2026-04-01T18:00:00.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format. Defaults to markdown.",
    )
    parser.add_argument(
        "--max-commits",
        type=int,
        default=env_default_max_commits(),
        help="Maximum commits to include in the final output.",
    )
    parser.add_argument(
        "--cutoff-hour",
        type=int,
        default=env_default_cutoff_hour(),
        help="Default cutoff hour in 24h format when --until is omitted.",
    )
    return parser.parse_args()


def parse_datetime(value: str) -> datetime:
    for candidate in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, candidate).replace(tzinfo=LOCAL_TZ)
        except ValueError:
            continue
    raise ValueError(
        f"Unsupported datetime format: {value!r}. "
        "Use YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS."
    )


def parse_git_datetime(value: str) -> datetime:
    normalized = value.strip()
    if normalized.endswith("Z"):
        normalized = normalized[:-1] + "+00:00"
    return datetime.fromisoformat(normalized).astimezone(LOCAL_TZ)


def resolve_range(
    period: str,
    since: str | None,
    until: str | None,
    cutoff_hour: int,
) -> tuple[datetime, datetime]:
    now = datetime.now(LOCAL_TZ)
    cutoff_today = now.replace(hour=cutoff_hour, minute=0, second=0, microsecond=0)
    end = parse_datetime(until) if until else min(now, cutoff_today)

    if since:
        return parse_datetime(since), end

    if period == "day":
        start = end.replace(hour=0, minute=0, second=0, microsecond=0)
    elif period == "week":
        start = (end - timedelta(days=end.weekday())).replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )
    else:
        start = end.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    return start, end


def ensure_repo(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Repository path does not exist: {path}")
    result = subprocess.run(
        ["git", "-C", str(path), "rev-parse", "--is-inside-work-tree"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0 or result.stdout.strip() != "true":
        raise RuntimeError(f"Not a git repository: {path}")


def should_skip_dir(dirname: str) -> bool:
    return dirname in IGNORED_DIR_NAMES


def discover_repos(root: Path) -> list[Path]:
    if not root.exists():
        raise FileNotFoundError(f"Root path does not exist: {root}")

    repos: set[Path] = set()
    for current_root, dirnames, _ in os.walk(root):
        if ".git" in dirnames:
            repo_path = Path(current_root).resolve()
            repos.add(repo_path)
            dirnames[:] = []
            continue
        dirnames[:] = [name for name in dirnames if not should_skip_dir(name)]
    return sorted(repos)


def load_commits(
    repo: Path,
    start: datetime,
    end: datetime,
    author: str | None,
    max_commits: int,
) -> list[Commit]:
    git_format = "%H%x1f%an%x1f%ae%x1f%ad%x1f%s"
    cmd = [
        "git",
        "-C",
        str(repo),
        "log",
        "--date=iso-strict",
        f"--max-count={max_commits}",
        f"--pretty=format:{git_format}",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git log failed")

    commits: list[Commit] = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        sha, author_name, email, date_str, subject = line.split("\x1f", 4)
        if author:
            needle = author.lower()
            if needle not in author_name.lower() and needle not in email.lower():
                continue
        commit_date = parse_git_datetime(date_str)
        if not (start <= commit_date <= end):
            continue
        commits.append(
            Commit(
                repo=repo.name,
                sha=sha,
                author=author_name,
                email=email,
                date=commit_date,
                subject=subject.strip(),
            )
        )
    return commits


def load_commits_from_sources(
    repos: list[Path],
    start: datetime,
    end: datetime,
    author: str | None,
    max_commits: int,
) -> tuple[list[Commit], list[str]]:
    commits: list[Commit] = []
    warnings: list[str] = []
    for repo in repos:
        try:
            commits.extend(load_commits(repo, start, end, author, max_commits))
        except Exception as exc:  # noqa: BLE001
            warnings.append(f"{repo}: {exc}")
    commits.sort(key=lambda commit: commit.date, reverse=True)
    return commits[:max_commits], warnings


def normalize_subject(subject: str) -> str:
    text = subject.strip()
    prefixes = (
        "feat:",
        "fix:",
        "docs:",
        "refactor:",
        "test:",
        "chore:",
        "perf:",
        "build:",
        "ci:",
    )
    lower = text.lower()
    for prefix in prefixes:
        if lower.startswith(prefix):
            return text[len(prefix):].strip()
    return text


def summarize(commits: Iterable[Commit]) -> list[str]:
    grouped: "OrderedDict[str, int]" = OrderedDict()
    for commit in commits:
        item = normalize_subject(commit.subject) or "(empty subject)"
        grouped[item] = grouped.get(item, 0) + 1

    return [
        f"- {item}{' (' + str(count) + ' commits)' if count > 1 else ''}"
        for item, count in grouped.items()
    ]


def render_markdown(
    repos: list[Path],
    period: str,
    start: datetime,
    end: datetime,
    commits: list[Commit],
    warnings: list[str],
) -> str:
    lines = [
        f"# Git {period.title()} Report",
        "",
        f"- Repository count: `{len(repos)}`",
        f"- Period: `{period}`",
        f"- Window: `{start.strftime('%Y-%m-%d %H:%M:%S')} ~ {end.strftime('%Y-%m-%d %H:%M:%S')}`",
        f"- Commit count: `{len(commits)}`",
        "",
    ]

    if repos:
        preview = ", ".join(f"`{repo.name}`" for repo in repos[:20])
        lines.append(f"- Repositories: {preview}")
        if len(repos) > 20:
            lines.append(f"- Additional repositories: `{len(repos) - 20}`")
        lines.append("")

    if warnings:
        lines.append("## Warnings")
        lines.append("")
        lines.extend(f"- {warning}" for warning in warnings)
        lines.append("")

    lines.append("## Summary")
    lines.append("")
    if commits:
        lines.extend(summarize(commits))
    else:
        lines.append("- No commits found in the selected window.")

    lines.append("")
    lines.append("## Commit Details")
    lines.append("")
    if commits:
        for commit in commits:
            lines.append(
                f"- `{commit.date.strftime('%Y-%m-%d %H:%M')}` `{commit.sha[:7]}` "
                f"{commit.subject} ({commit.author} @ {commit.repo})"
            )
    else:
        lines.append("- None")
    return "\n".join(lines)


def render_json(
    repos: list[Path],
    period: str,
    start: datetime,
    end: datetime,
    commits: list[Commit],
    warnings: list[str],
) -> str:
    payload = {
        "repos": [str(repo) for repo in repos],
        "period": period,
        "since": start.isoformat(),
        "until": end.isoformat(),
        "commit_count": len(commits),
        "summary": [line[2:] for line in summarize(commits)],
        "warnings": warnings,
        "commits": [
            {
                "sha": commit.sha,
                "author": commit.author,
                "email": commit.email,
                "date": commit.date.isoformat(),
                "subject": commit.subject,
                "repo": commit.repo,
            }
            for commit in commits
        ],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def main() -> int:
    args = parse_args()
    try:
        start, end = resolve_range(args.period, args.since, args.until, args.cutoff_hour)
        if args.repo:
            repo = Path(args.repo).expanduser().resolve()
            ensure_repo(repo)
            repos = [repo]
        else:
            root = Path(args.root).expanduser().resolve()
            repos = discover_repos(root)
            if not repos:
                raise RuntimeError(f"No git repositories found under: {root}")
        commits, warnings = load_commits_from_sources(
            repos,
            start,
            end,
            args.author,
            args.max_commits,
        )
    except Exception as exc:  # noqa: BLE001
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.format == "json":
        print(render_json(repos, args.period, start, end, commits, warnings))
    else:
        print(render_markdown(repos, args.period, start, end, commits, warnings))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
