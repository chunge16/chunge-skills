# git-activity-report

Generate daily, weekly, and monthly reports from git commit history.

This skill can be used:

- As a Codex skill via `SKILL.md`
- As a standalone CLI script via `scripts/generate_report.py`

## Features

- Generate daily, weekly, and monthly reports
- Aggregate commits from a whole projects root
- Target a single repository when needed
- Filter by author
- Override time windows with `--since` and `--until`
- Use a configurable default cutoff hour
- Output either Markdown or JSON
- Include repository names in aggregated commit details

## Requirements

- Python 3.9+
- `git` available on the command line
- Access to the repositories you want to scan

No third-party Python packages are required.

## Install This Skill

Recommended repository install:

```bash
npx skills add chunge16/chunge-skills
```

Install only `git-activity-report` with the `skills` CLI:

```bash
npx skills add chunge16/chunge-skills --skill git-activity-report
```

Install globally instead of project-local:

```bash
npx skills add chunge16/chunge-skills --skill git-activity-report --global
```

List the skills available in this repository:

```bash
npx skills add chunge16/chunge-skills --list
```

## Run as a Script

From the repository root:

```bash
python3 skills/git-activity-report/scripts/generate_report.py
```

## Configuration

The script resolves settings in this order:

1. Explicit CLI flags
2. Environment variables
3. Built-in defaults

Supported environment variables:

- `GIT_ACTIVITY_REPORT_ROOT`
- `GIT_ACTIVITY_REPORT_CUTOFF_HOUR`
- `GIT_ACTIVITY_REPORT_MAX_COMMITS`

Example:

```bash
export GIT_ACTIVITY_REPORT_ROOT=/Users/shi/Desktop/asiainfo/project
export GIT_ACTIVITY_REPORT_CUTOFF_HOUR=18
export GIT_ACTIVITY_REPORT_MAX_COMMITS=200
```

## Command Usage

```bash
python3 skills/git-activity-report/scripts/generate_report.py [options]
```

Common options:

- `--period day|week|month`
- `--root /path/to/projects`
- `--repo /path/to/repo`
- `--author "name-or-email"`
- `--since 2026-04-01`
- `--until 2026-04-01T18:00:00`
- `--format markdown|json`
- `--max-commits 200`
- `--cutoff-hour 18`

## Usage Examples

Generate a daily report from the configured root or current directory:

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

Generate yesterday's report with an explicit time window:

```bash
python3 skills/git-activity-report/scripts/generate_report.py \
  --since 2026-04-01 \
  --until 2026-04-01T18:00:00
```

Generate a weekly report for one author only:

```bash
python3 skills/git-activity-report/scripts/generate_report.py \
  --period week \
  --author "alice"
```

Generate JSON output for downstream processing:

```bash
python3 skills/git-activity-report/scripts/generate_report.py \
  --period month \
  --format json
```

## Option Examples

Use `--root` to aggregate multiple repositories under one projects directory:

```bash
python3 skills/git-activity-report/scripts/generate_report.py \
  --period week \
  --root /Users/shi/Desktop/asiainfo/project
```

Use `--repo` to target one repository only:

```bash
python3 skills/git-activity-report/scripts/generate_report.py \
  --period month \
  --repo /Users/shi/Desktop/asiainfo/project/ymukj-buss-backend
```

Use `--author` to filter one contributor:

```bash
python3 skills/git-activity-report/scripts/generate_report.py \
  --period week \
  --author "chunge"
```

Use `--since` and `--until` for a custom reporting window:

```bash
python3 skills/git-activity-report/scripts/generate_report.py \
  --since 2026-04-01 \
  --until 2026-04-01T18:00:00
```

Use `--format json` for downstream processing:

```bash
python3 skills/git-activity-report/scripts/generate_report.py \
  --period month \
  --format json
```

Use `--cutoff-hour` to override the default daily cutoff:

```bash
python3 skills/git-activity-report/scripts/generate_report.py \
  --period day \
  --cutoff-hour 20
```

Use `--max-commits` to limit the final output size:

```bash
python3 skills/git-activity-report/scripts/generate_report.py \
  --period week \
  --max-commits 50
```

More examples are available in [references/periods.md](./references/periods.md).

## Example Skill Invocation

- `Use $git-activity-report to generate today's daily report`
- `Use $git-activity-report to generate this week's weekly report`
- `Use $git-activity-report to summarize all repos under /path/to/projects`
- `Use $git-activity-report to generate yesterday's report with --since and --until`
- `Use $git-activity-report to generate a monthly report for /path/to/repo`

## Example Markdown Output

```markdown
# Git Week Report

- Repository count: `2`
- Period: `week`
- Window: `2026-03-30 00:00:00 ~ 2026-04-02 18:00:00`
- Commit count: `3`

## Summary

- add amount type filter
- sync order metric title with amount type
- show applicant name in high seas detail

## Commit Details

- `2026-04-01 17:54` `7b6c5dc` fix(application): show applicant name in high seas detail (alice @ backend-app)
- `2026-04-01 15:44` `45d4118` fix(orderPrediction): sync order metric title with amount type (alice @ backend-app)
- `2026-04-01 10:53` `7ba4eab` feat(orderPrediction): add amount type filter (alice @ backend-app)
```

## Notes

- When `--until` is omitted, the script uses the current day at the configured cutoff hour, or `now` if it is earlier.
- When `--repo` is provided, root scanning is skipped.
- When scanning many repositories, unreadable or broken repositories are reported as warnings instead of aborting the entire run.
