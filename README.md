# Agent Skills Collection

[中文说明](./README.zh.md)

Skills shared for improving day-to-day engineering workflows with Codex and compatible Agent Skills runtimes.

This repository is organized as a skill collection. Each skill lives under `skills/<skill-name>/` and can include `SKILL.md`, `README.md`, helper scripts, references, assets, and optional UI metadata in `agents/openai.yaml`.

## Prerequisites

- Node.js installed
- Able to run `npx bun`

## Installation

Install skills from this repository with the `skills` CLI.

### Quick Install (Recommended)

Install this repository:

```bash
npx skills add chunge16/chunge-skills
```

Install a specific skill from this repository:

```bash
npx skills add chunge16/chunge-skills --skill git-activity-report
```

List the skills available in this repository before installing:

```bash
npx skills add chunge16/chunge-skills --list
```

Install globally instead of project-local:

```bash
npx skills add chunge16/chunge-skills --skill git-activity-report --global
```

### Repository Layout

```text
chunge-skills/
├── README.md
├── LICENSE
└── skills/
    └── git-activity-report/
        ├── README.md
        ├── SKILL.md
        ├── LICENSE.txt
        ├── agents/
        │   └── openai.yaml
        ├── scripts/
        │   └── generate_report.py
        └── references/
            └── periods.md
```

## Available Skills

Skills in this repository are organized by practical workflow category.

### Reporting Skills

Skills for turning repository activity into structured engineering updates.

#### `git-activity-report`

Generate daily, weekly, and monthly reports from git commit history across one repository or many repositories under a projects root.

Typical use cases:

- Daily engineering status reports
- Weekly and monthly summaries
- Multi-repo development activity rollups
- Author-filtered contribution summaries

Quick usage examples:

```text
Use $git-activity-report to generate today's daily report
Use $git-activity-report to generate this week's weekly report
Use $git-activity-report to summarize all repos under /path/to/projects
Use $git-activity-report to generate a monthly report for /path/to/repo
Use $git-activity-report to generate a weekly report with --author "alice"
Use $git-activity-report to generate yesterday's report with --since 2026-04-01 --until 2026-04-01T18:00:00
Use $git-activity-report to export a monthly report as JSON with --format json
```

Docs:

- [git-activity-report README](./skills/git-activity-report/README.md)
- [git-activity-report SKILL.md](./skills/git-activity-report/SKILL.md)

### Social Content Skills

Skills for turning source material into publishable social-media visuals.

#### `chunge-xhs-images`

Generate Xiaohongshu and RedNote image carousels directly in Codex from articles, notes, and outlines, without requiring a separately configured local image SDK key.

Typical use cases:

- Turn an article into a 5-7 page Xiaohongshu carousel
- Generate a cover plus content images for a RedNote post
- Produce knowledge-card style AI, SaaS, study, or tutorial visuals
- Create comparison cards, checklist cards, and infographic-style social slides

Quick usage examples:

```text
Use $chunge-xhs-images to turn this article into a 6-page Xiaohongshu carousel
Use $chunge-xhs-images to create a cover and 5 content pages for this note
Use $chunge-xhs-images with a notion dense knowledge-card style
Use $chunge-xhs-images to generate RedNote infographic images directly in Codex
```

Docs:

- [chunge-xhs-images README](./skills/chunge-xhs-images/README.md)
- [chunge-xhs-images SKILL.md](./skills/chunge-xhs-images/SKILL.md)

## Notes

- Skill-specific installation, usage examples, configuration, and output samples belong in each skill's own `README.md`.
- `SKILL.md` remains optimized for Codex triggering and runtime guidance rather than for GitHub readers.

## Contributing

When adding a new skill:

1. Create a new directory under `skills/`
2. Add a `SKILL.md`
3. Add a `README.md` for user-facing documentation
4. Add `agents/openai.yaml` when UI metadata is useful
5. Add `scripts/`, `references/`, or `assets/` only when needed
6. Add a `LICENSE.txt` inside the skill directory
7. Add the skill to the `Available Skills` section in this README

## License

The repository license is in [LICENSE](./LICENSE).

Each skill may also include its own license file, such as [skills/git-activity-report/LICENSE.txt](./skills/git-activity-report/LICENSE.txt).
