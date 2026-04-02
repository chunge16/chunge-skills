# git-activity-report-skill

A shareable Agent Skill repository for generating daily, weekly, and monthly reports from git commit history.

This repository is organized to match the Agent Skills layout used by Codex and the wider `skills` ecosystem: each skill lives in its own folder under `skills/`.

## Repository Layout

```text
git-activity-report-skill/
├── README.md
├── LICENSE
└── skills/
    └── git-activity-report/
        ├── SKILL.md
        ├── LICENSE.txt
        ├── agents/
        │   └── openai.yaml
        ├── scripts/
        │   └── generate_report.py
        └── references/
            └── periods.md
```

## What This Skill Does

The `git-activity-report` skill generates:

- Daily reports
- Weekly reports
- Monthly reports

It supports:

- Single repository mode with `--repo`
- Multi-repository aggregation with `--root`
- Configurable cutoff hour
- Markdown or JSON output
- Optional author filtering

## Default Resolution Rules

The script resolves settings in this order:

1. Explicit CLI flags
2. Environment variables
3. Built-in defaults

Supported environment variables:

- `GIT_ACTIVITY_REPORT_ROOT`
- `GIT_ACTIVITY_REPORT_CUTOFF_HOUR`
- `GIT_ACTIVITY_REPORT_MAX_COMMITS`

## Quick Start

Generate a daily report from the current directory tree:

```bash
python3 skills/git-activity-report/scripts/generate_report.py
```

Generate a weekly report across a projects root:

```bash
python3 skills/git-activity-report/scripts/generate_report.py \
  --period week \
  --root /path/to/projects
```

Generate a monthly report for a single repository:

```bash
python3 skills/git-activity-report/scripts/generate_report.py \
  --period month \
  --repo /path/to/repo
```

## Example Skill Invocation

- `Use $git-activity-report to generate today's daily report`
- `Use $git-activity-report to generate this week's weekly report`
- `Use $git-activity-report to summarize all repos under /path/to/projects`
- `Use $git-activity-report to generate yesterday's report for one repo`

## License

The repository license is in [LICENSE](./LICENSE).

The skill-specific license is in [skills/git-activity-report/LICENSE.txt](./skills/git-activity-report/LICENSE.txt).
