# chunge-xhs-images

Generate Xiaohongshu image sets directly in Codex, without requiring the user to configure a separate local AI image SDK key.

This skill is designed for article-to-carousel, note-to-infographic, and cover-plus-inner-pages workflows for Xiaohongshu and RedNote content.

## What Makes This Version Different

This skill is inspired by `baoyu-xhs-images`, but it is adapted for a simpler execution model:

- No external image SDK setup required
- No local OpenAI or other provider image key required
- Codex handles the image generation step directly in-session
- Still keeps the useful XHS workflow structure: analysis, outline, prompt writing, and final image series generation

## Best For

- 小红书图文
- RedNote carousel posts
- Knowledge cards
- Product comparison cards
- Tutorial step cards
- Cover image plus content pages

## Install This Skill

Install the full repository:

```bash
npx skills add chunge16/chunge-skills
```

Install just this skill:

```bash
npx skills add chunge16/chunge-skills --skill chunge-xhs-images
```

List available skills first:

```bash
npx skills add chunge16/chunge-skills --list
```

## Example Prompts

```text
Use $chunge-xhs-images to turn this article into a 6-page Xiaohongshu carousel
```

```text
Use $chunge-xhs-images to create a cover and 5 content pages for this AI tools note
```

```text
Use $chunge-xhs-images with a notion dense knowledge-card style for this document
```

```text
Use $chunge-xhs-images to generate RedNote infographic images directly in Codex
```

## Workflow Summary

1. Read the source file or pasted content
2. Extract the most shareable angle
3. Decide the number of pages
4. Choose a style and layout
5. Write one image prompt per page
6. Generate the images directly in Codex
7. Save prompt files and outputs into a clean session folder when useful

## Optional Workspace Scaffolding

This skill now includes a small helper script that prepares a clean session folder before image generation.

From the repository root:

```bash
python3 skills/chunge-xhs-images/scripts/init_xhs_project.py --title "AI Tools for Solo Founders"
```

With a source file and preset:

```bash
python3 skills/chunge-xhs-images/scripts/init_xhs_project.py \
  --title "AI Tools for Solo Founders" \
  --source /path/to/article.md \
  --preset knowledge-card \
  --pages 6
```

The script creates:

- `source.md`
- `analysis.md`
- `outline.md`
- `prompts/*.md`

## Supported Visual Styles

- `cute`
- `fresh`
- `warm`
- `bold`
- `minimal`
- `retro`
- `pop`
- `notion`
- `chalkboard`
- `study-notes`
- `screen-print`

## Supported Layouts

- `sparse`
- `balanced`
- `dense`
- `list`
- `comparison`
- `flow`
- `mindmap`
- `quadrant`

## Suggested Presets

- `knowledge-card`: notion + dense
- `checklist`: notion + list
- `tutorial`: chalkboard + flow
- `study-guide`: study-notes + dense
- `cute-share`: cute + balanced
- `product-review`: fresh + comparison
- `warning`: bold + list
- `clean-quote`: minimal + sparse
- `poster`: screen-print + sparse

For the fuller preset table, see [references/style-presets.md](./references/style-presets.md).

## Output Layout

When files are created in the workspace, a typical session output looks like this:

```text
skills-output/xhs-images/<topic-slug>/
├── source.md
├── analysis.md
├── outline.md
├── prompts/
│   ├── 01-cover.md
│   ├── 02-page.md
│   └── ...
├── 01-cover.png
├── 02-page.png
└── ...
```

## Notes

- This skill is intended for Codex sessions that can generate images directly.
- If the user only wants prompt files, the skill can stop after prompt generation.
- If the user wants a fully finished image set, the skill should continue through image generation instead of handing work back to the user.
- Workflow execution notes are in [references/workflow.md](./references/workflow.md).
