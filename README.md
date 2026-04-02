# Agent Skills Collection

Skills shared for improving day-to-day engineering workflows with Codex and compatible Agent Skills runtimes.

This repository is organized as a skill collection. Each skill lives under `skills/<skill-name>/` and can include `SKILL.md`, `README.md`, helper scripts, references, assets, and optional UI metadata in `agents/openai.yaml`.

## Prerequisites

- Codex or a compatible Agent Skills runtime
- Python 3.9+ for Python-based helper scripts
- `git` on the command line for git-based skills

## Installation

Install skills from this repository with the `skills` CLI.

### Quick Install

Install the `git-activity-report` skill from this repository:

```bash
npx skills add https://github.com/chunge16/chunge-skills --skill git-activity-report
```

GitHub shorthand also works:

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

Quick examples:

```bash
# Daily report
python3 skills/git-activity-report/scripts/generate_report.py

# Weekly report across a projects root
python3 skills/git-activity-report/scripts/generate_report.py --period week --root /path/to/projects

# Monthly report for one repository
python3 skills/git-activity-report/scripts/generate_report.py --period month --repo /path/to/repo
```

Docs:

- [git-activity-report README](./skills/git-activity-report/README.md)
- [git-activity-report SKILL.md](./skills/git-activity-report/SKILL.md)

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
