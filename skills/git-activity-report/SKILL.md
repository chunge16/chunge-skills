---
name: git-activity-report
description: Generate a daily, weekly, or monthly work report from git commit history across one repository or a whole projects root. Use when the user asks Codex to summarize recent development progress, produce a日报/周报/月报, infer completed work from commits, or turn git activity into a status update. Default to a daily report when the user does not specify a period.
---

# Git Activity Report

Generate a structured report from git commits in one repository or across multiple repositories under a root directory.

## Workflow

1. Determine the reporting scope.
Use `--repo` when the user clearly wants one repository.
Use `--root` when the user wants all repositories under a projects directory.
If neither is provided, the script resolves the root from environment variables or defaults to the current working directory.

2. Determine the reporting period.
Default to `day`.
Use `week` or `month` when the user explicitly asks for 周报 or 月报.
Use `--since` and `--until` for yesterday, last week, last month, or any custom window.

3. Run the bundled script.

```bash
python3 skills/git-activity-report/scripts/generate_report.py
```

4. Polish wording only after facts are collected.
Do not invent work not supported by the commit history.

## Parameters

- `--period day|week|month`: Reporting period. Default is `day`.
- `--root PATH`: Scan all repositories under a root directory.
- `--repo PATH`: Target a single repository.
- `--author TEXT`: Filter by author name or email substring.
- `--since ISO_DATETIME`: Override the start time.
- `--until ISO_DATETIME`: Override the end time.
- `--format markdown|json`: Output format. Default is `markdown`.
- `--max-commits N`: Limit the final commit list.
- `--cutoff-hour N`: Default cutoff hour when `--until` is omitted. Default is `18`.

## Environment Variables

- `GIT_ACTIVITY_REPORT_ROOT`
- `GIT_ACTIVITY_REPORT_CUTOFF_HOUR`
- `GIT_ACTIVITY_REPORT_MAX_COMMITS`

CLI arguments take priority over environment variables.

## Output Rules

- Always include the exact reporting window.
- Keep a summary section and a commit detail section.
- Include the repository name in commit details when aggregating multiple repositories.
- If no commits are found, say that clearly.

## Examples

- `Use $git-activity-report to generate today's daily report`
- `Use $git-activity-report to generate this week's weekly report`
- `Use $git-activity-report to summarize all repos under /path/to/projects`
- `Use $git-activity-report to generate yesterday's report with --since and --until`

Read `references/periods.md` for practical command examples.
