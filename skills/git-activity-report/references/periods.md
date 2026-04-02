# Period Examples

Use this file when the user needs concrete commands for daily, weekly, monthly, or custom windows.

## Defaults

- Default period is `day`
- Default cutoff hour is `18`
- CLI flags override environment variables

## Environment Setup

```bash
export GIT_ACTIVITY_REPORT_ROOT=/Users/shi/Desktop/asiainfo/project
export GIT_ACTIVITY_REPORT_CUTOFF_HOUR=18
export GIT_ACTIVITY_REPORT_MAX_COMMITS=200
```

## Daily Report

```bash
python3 skills/git-activity-report/scripts/generate_report.py
python3 skills/git-activity-report/scripts/generate_report.py --root /path/to/projects
python3 skills/git-activity-report/scripts/generate_report.py --repo /path/to/repo
```

## Weekly Report

```bash
python3 skills/git-activity-report/scripts/generate_report.py --period week
python3 skills/git-activity-report/scripts/generate_report.py --period week --author "alice"
```

## Monthly Report

```bash
python3 skills/git-activity-report/scripts/generate_report.py --period month
python3 skills/git-activity-report/scripts/generate_report.py --period month --format json
```

## Yesterday

```bash
python3 skills/git-activity-report/scripts/generate_report.py \
  --since 2026-04-01 \
  --until 2026-04-01T18:00:00
```

## Last Week

```bash
python3 skills/git-activity-report/scripts/generate_report.py \
  --period week \
  --since 2026-03-23 \
  --until 2026-03-29T18:00:00
```
