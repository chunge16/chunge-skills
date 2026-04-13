#!/usr/bin/env python3
"""Initialize a workspace folder for an XHS image generation session."""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path


DEFAULT_PAGES = 6
DEFAULT_OUTPUT_ROOT = Path("skills-output/xhs-images")

PRESETS: dict[str, tuple[str, str]] = {
    "knowledge-card": ("notion", "dense"),
    "checklist": ("notion", "list"),
    "concept-map": ("notion", "mindmap"),
    "swot": ("notion", "quadrant"),
    "tutorial": ("chalkboard", "flow"),
    "classroom": ("chalkboard", "balanced"),
    "study-guide": ("study-notes", "dense"),
    "cute-share": ("cute", "balanced"),
    "girly": ("cute", "sparse"),
    "cozy-story": ("warm", "balanced"),
    "product-review": ("fresh", "comparison"),
    "nature-flow": ("fresh", "flow"),
    "warning": ("bold", "list"),
    "versus": ("bold", "comparison"),
    "clean-quote": ("minimal", "sparse"),
    "pro-summary": ("minimal", "balanced"),
    "retro-ranking": ("retro", "list"),
    "throwback": ("retro", "balanced"),
    "pop-facts": ("pop", "list"),
    "poster": ("screen-print", "sparse"),
    "editorial": ("screen-print", "balanced"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize an XHS image session directory."
    )
    parser.add_argument(
        "--title",
        required=True,
        help="Working title or topic for the image set.",
    )
    parser.add_argument(
        "--source",
        help="Optional source file. If omitted, source.md is created as a placeholder.",
    )
    parser.add_argument(
        "--style",
        help="Visual style name.",
    )
    parser.add_argument(
        "--layout",
        help="Information layout name.",
    )
    parser.add_argument(
        "--preset",
        help="Preset name that maps to style + layout.",
    )
    parser.add_argument(
        "--pages",
        type=int,
        default=DEFAULT_PAGES,
        help=f"Number of image pages to scaffold. Default is {DEFAULT_PAGES}.",
    )
    parser.add_argument(
        "--output-root",
        default=str(DEFAULT_OUTPUT_ROOT),
        help=f"Root directory for generated sessions. Default is {DEFAULT_OUTPUT_ROOT}.",
    )
    return parser.parse_args()


def slugify(value: str) -> str:
    lowered = value.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", lowered)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "xhs-topic"


def resolve_base_dir(output_root: Path, slug: str) -> Path:
    candidate = output_root / slug
    if not candidate.exists():
        return candidate

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return output_root / f"{slug}-{timestamp}"


def resolve_style_layout(
    style: str | None,
    layout: str | None,
    preset: str | None,
) -> tuple[str | None, str | None]:
    preset_style = None
    preset_layout = None
    if preset:
        if preset not in PRESETS:
            valid = ", ".join(sorted(PRESETS))
            raise SystemExit(f"Unknown preset: {preset}. Valid presets: {valid}")
        preset_style, preset_layout = PRESETS[preset]
    return style or preset_style, layout or preset_layout


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def source_content(args: argparse.Namespace) -> str:
    if args.source:
        return Path(args.source).read_text(encoding="utf-8")
    return "# Source\n\nPaste the source article, notes, or outline here.\n"


def analysis_template(title: str, style: str | None, layout: str | None) -> str:
    return (
        f"# Analysis\n\n"
        f"- Topic: {title}\n"
        f"- Content type:\n"
        f"- Target audience:\n"
        f"- Best hook:\n"
        f"- Core takeaways:\n"
        f"- Recommended style: {style or 'TBD'}\n"
        f"- Recommended layout: {layout or 'TBD'}\n"
        f"- Recommended strategy:\n"
        f"- Recommended page count:\n"
        f"- Shareable angle:\n"
        f"- Core promise:\n"
        f"- Risks or facts to preserve:\n"
    )


def outline_template(title: str, pages: int) -> str:
    lines = [
        "# Outline",
        "",
        f"- Working title: {title}",
        f"- Target pages: {pages}",
        "",
    ]
    default_labels = page_labels(pages)
    for index in range(1, pages + 1):
        label = default_labels[index - 1]
        lines.append(f"- {index:02d}. {label}:")
    lines.append("")
    return "\n".join(lines)


def page_labels(pages: int) -> list[str]:
    if pages <= 1:
        return ["cover"]
    if pages == 2:
        return ["cover", "ending"]
    if pages == 3:
        return ["cover", "content-1", "ending"]

    middle_count = pages - 2
    labels = ["cover"]
    labels.extend(f"content-{index}" for index in range(1, middle_count + 1))
    labels.append("ending")
    return labels


def prompt_template(
    page_number: int,
    page_name: str,
    title: str,
    style: str | None,
    layout: str | None,
) -> str:
    return (
        f"# Prompt {page_number:02d}: {page_name}\n\n"
        f"- Topic: {title}\n"
        f"- Page role: {page_name}\n"
        f"- Style: {style or 'TBD'}\n"
        f"- Layout: {layout or 'TBD'}\n"
        f"- Key message:\n"
        f"- Visual subject:\n"
        f"- Text density:\n"
        f"- Color direction:\n"
        f"- Composition notes:\n"
        f"- Consistency notes for full series:\n"
        f"\n"
        f"Final image prompt:\n"
    )


def main() -> int:
    args = parse_args()
    style, layout = resolve_style_layout(args.style, args.layout, args.preset)
    slug = slugify(args.title)
    base_dir = resolve_base_dir(Path(args.output_root), slug)
    prompts_dir = base_dir / "prompts"
    prompts_dir.mkdir(parents=True, exist_ok=True)

    write_text(base_dir / "source.md", source_content(args))
    write_text(base_dir / "analysis.md", analysis_template(args.title, style, layout))
    write_text(base_dir / "outline.md", outline_template(args.title, args.pages))

    page_names = page_labels(args.pages)
    for number in range(1, args.pages + 1):
        page_name = page_names[number - 1]
        prompt_path = prompts_dir / f"{number:02d}-{page_name}.md"
        write_text(
            prompt_path,
            prompt_template(number, page_name, args.title, style, layout),
        )

    print(base_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
