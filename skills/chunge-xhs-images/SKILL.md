---
name: chunge-xhs-images
description: Generate Xiaohongshu (Little Red Book) image series from an article, note, outline, or pasted text. Use when the user asks for 小红书图片, XHS images, RedNote infographics, 封面图+配图, 图文拆图, or wants a Xiaohongshu carousel generated directly inside Codex without configuring an external image SDK key.
---

# Chunge XHS Images

Create Xiaohongshu image series from source content and generate the final visuals directly in Codex.

This skill is based on the `baoyu-xhs-images` workflow, but it is adapted for environments where the user does not have local AI image SDK keys.

Do not require the user to configure OpenAI, Replicate, Gemini, AI SDK image providers, or any other local credential for this workflow. The default behavior is to write the page plan and prompts in the workspace, then generate the visuals using the image generation capability available to Codex in the current session.

## When To Use

Use this skill when the user wants any of the following:

- Xiaohongshu image carousel generation
- RedNote infographic or knowledge-card images
- A cover image plus inner pages for a social post
- A text/article converted into 1-10 visual slides
- A Xiaohongshu-style breakdown of a document, note, or outline

## Inputs

Accept any of these as source material:

- A Markdown file
- A text file
- A pasted article or outline
- A topic plus a few bullet points

If the source is long, extract only the strongest points for a Xiaohongshu carousel. Do not try to visualize every paragraph.

## Output Goals

Produce a complete XHS image-set workflow:

1. Analyze the source and identify the most shareable angle.
2. Choose a visual direction and information layout.
3. Break the content into 1-10 pages.
4. Write one final image prompt per page.
5. Generate the images directly in Codex.
6. Save prompts and outputs into a clean session directory when the user wants files organized in the workspace.

If the user only asks to create the skill itself, focus on authoring or updating the skill files, not on generating an example image set unless they ask for a demo run.

## Visual Dimensions

Choose one style and one layout.

### Styles

- `cute`: sweet, soft, rounded, classic Xiaohongshu look
- `fresh`: clean, light, airy, healthy-lifestyle feel
- `warm`: cozy, human, personal, emotionally approachable
- `bold`: high-contrast, urgent, attention-grabbing
- `minimal`: premium, restrained, clean editorial style
- `retro`: nostalgic, vintage, textured
- `pop`: vibrant, playful, energetic
- `notion`: hand-drawn, knowledge-card, intellectual
- `chalkboard`: educational, illustrated teaching board
- `study-notes`: handwritten notes, highlighted annotations
- `screen-print`: poster-like, graphic, symbolic, cinematic

### Layouts

- `sparse`: 1-2 key points, maximum visual impact
- `balanced`: 3-4 points, standard carousel page
- `dense`: 5-8 points, knowledge-card style
- `list`: enumerated bullets or rankings
- `comparison`: before/after or side-by-side contrast
- `flow`: steps, progression, timeline
- `mindmap`: central idea with branches
- `quadrant`: four-part categorization

## Preset Suggestions

- `knowledge-card`: `notion` + `dense`
- `checklist`: `notion` + `list`
- `concept-map`: `notion` + `mindmap`
- `swot`: `notion` + `quadrant`
- `tutorial`: `chalkboard` + `flow`
- `classroom`: `chalkboard` + `balanced`
- `study-guide`: `study-notes` + `dense`
- `cute-share`: `cute` + `balanced`
- `girly`: `cute` + `sparse`
- `cozy-story`: `warm` + `balanced`
- `product-review`: `fresh` + `comparison`
- `warning`: `bold` + `list`
- `versus`: `bold` + `comparison`
- `clean-quote`: `minimal` + `sparse`
- `pro-summary`: `minimal` + `balanced`
- `retro-ranking`: `retro` + `list`
- `pop-facts`: `pop` + `list`
- `poster`: `screen-print` + `sparse`
- `editorial`: `screen-print` + `balanced`

Detailed preset mappings: `references/style-presets.md`

## Workflow

Use this sequence unless the user explicitly asks for a lighter or faster pass:

### Step 0: Preference Check

If the project already contains a local preference file, use it. Suggested project-level path:

```text
.codex/skills/chunge-xhs-images/EXTEND.md
```

The preference file is optional for this skill. If it does not exist, continue without blocking. A minimal preference file can store:

- preferred language
- preferred style or preset
- default page count range
- watermark text and position
- notes about recurring brand colors or mascots

### Step 1: Analyze The Source

Read the provided source and extract:

- content type such as sharing, tutorial, comparison, warning, review, or knowledge card
- target audience
- strongest hook
- most save-worthy points
- best visual opportunities
- recommended page count

When writing files, save the analysis into `analysis.md`.

### Step 2: Confirm The Direction

Before generating images, briefly confirm the recommended direction unless the user clearly asked for a direct fast pass.

Present:

- chosen strategy: story-driven, information-dense, or visual-first
- recommended style
- recommended layout
- recommended page count
- short reason for the recommendation

If the user does not want back-and-forth, proceed with the best default.

### Step 3: Build The Outline

Create a page-by-page plan in `outline.md`.

Use a structure like:

- cover
- hook or pain point
- key point 1
- key point 2
- key point 3
- summary or CTA

For dense educational content, use 6-8 pages. For lighter lifestyle content, use 4-6 pages.

### Step 4: Write Page Prompts

Write one Markdown prompt file per page under `prompts/`.

Each prompt should include:

- page role
- visual style
- layout
- subject matter
- text density target
- color direction
- composition constraints
- Xiaohongshu-friendly tone
- consistency notes for the whole series

### Step 5: Generate Images In Codex

Generate the actual images directly in Codex.

Do not ask the user to run a local SDK, configure API keys, or install an image-generation package when the current Codex session can generate the visuals directly.

When possible, keep visual consistency by treating the cover page as the anchor and reusing its palette, character language, and decorative motifs across the rest of the set.

### Step 6: Save Artifacts

If creating files is useful, use a session folder like:

```text
skills-output/xhs-images/{topic-slug}/
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

If the user wants an initialized workspace structure before writing prompts, run:

```bash
python3 skills/chunge-xhs-images/scripts/init_xhs_project.py --title "AI Tools"
```

This creates the session folder, `source.md`, `analysis.md`, `outline.md`, and one prompt stub per page. The script avoids overwriting an existing session directory by appending a timestamp suffix when needed.

## Prompt Writing Rules

- Optimize for square or portrait social-post composition unless the user asks otherwise.
- Keep text inside images minimal and intentional.
- Prefer symbolic visuals, icons, callouts, diagrams, stickers, notes, arrows, tape, or hand-drawn emphasis where relevant.
- Keep each page visually distinct but clearly part of the same set.
- Mention Chinese social-content aesthetics when helpful, but avoid forcing stereotyped pink-only designs unless the content calls for it.
- If a page is text-heavy, convert long copy into labels, short bullets, or diagram fragments.
- Preserve factual correctness from the source. Do not invent claims, statistics, or product details.
- Keep text rendering requests conservative. Prefer short headings and labels over paragraph-sized text inside the image.

## Decision Heuristics

- Knowledge, SaaS, productivity, AI tools: prefer `notion`, `study-notes`, or `chalkboard`
- Tutorials and step-by-step guides: prefer `flow`
- Warnings, myths, mistakes, or pitfalls: prefer `bold` + `list`
- Comparison content: prefer `comparison`
- Emotional sharing or life stories: prefer `warm` + `balanced`
- Strong opinion, film, culture, or essay-style content: prefer `screen-print`

## File And Naming Rules

- Create a short topic slug in kebab-case.
- Name pages with numeric prefixes such as `01-cover`, `02-hook`, `03-key-point-1`, `04-key-point-2`, `05-summary`.
- Save one Markdown prompt file per image when generating assets for the workspace.
- If a target directory already exists, create a timestamp-suffixed directory instead of overwriting it.
- If the user only wants the images and not the saved prompts, prioritize the final visuals over extra file creation.

## Response Style

When using this skill:

- First explain the chosen visual direction in 1-3 short sentences.
- Then show the page plan.
- Then generate the images.
- If file output was created, mention where the assets were saved.

## References

- `references/workflow.md`: execution checklist and page planning guide
- `references/style-presets.md`: preset-to-style-layout mappings

## Examples

- `Use $chunge-xhs-images to turn this article into a 6-page Xiaohongshu carousel`
- `Use $chunge-xhs-images to make a cover plus 4 content cards from this note`
- `Use $chunge-xhs-images with a notion knowledge-card style for this AI tools post`
- `Use $chunge-xhs-images to create RedNote infographic images directly in Codex without external API keys`

Read `references/workflow.md` when you need a tighter execution checklist.
