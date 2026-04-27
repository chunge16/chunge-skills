---
name: chunge-xhs-post
description: Orchestrate a full Xiaohongshu post package by coordinating image generation and caption writing. Use when the user wants 一整套小红书图文, 小红书配图+文案, image cards plus 标题正文话题, RedNote post package, or asks to use baoyu-image-cards together with chunge-xhs-content to produce coordinated publish-ready content.
---

# Chunge XHS Post

Build a coordinated Xiaohongshu post package in one workflow. This skill is the top-level orchestrator for `baoyu-image-cards` and `chunge-xhs-content`.

Use this skill when the user wants the whole package, not just one asset.

## Companion Skills

This skill delegates to:

- `baoyu-image-cards` for image cards, cover images, or visual direction
- `chunge-xhs-content` for title, body, and hashtags

Do not reinvent their detailed rules here. Use them as specialist companions and keep this skill focused on sequencing, alignment, and delivery.

## Default Deliverable

When the user asks for a full Xiaohongshu post package, aim to deliver:

1. image direction or image set
2. publish-ready title
3. publish-ready body
4. publish-ready hashtags

If images cannot be generated in the current run, still produce:

1. recommended image direction
2. title
3. body
4. hashtags

This skill also supports partial deliverables:

- `text-only`: title, body, hashtags only
- `image-only`: image direction or image set only

## Routing

Choose one path quickly:

- `full-package`: user wants both images and copy
- `image-led`: user mainly cares about visuals, but still needs matching copy
- `copy-led`: user mainly cares about copy, but wants it aligned to likely images
- `text-only`: user explicitly wants only title, body, and hashtags
- `image-only`: user explicitly wants only visuals or image direction

Default to `full-package` when the user asks for a 小红书图文 or similar bundled deliverable.

## Main Workflow

### 1. Lock the post angle

Before doing anything else, reduce the request to:

- one topic
- one audience
- one post intent
- one dominant angle

If the user gives many points, compress them. The final package should feel unified.

### 2. Decide the visual strategy

If the selected path includes images, call on `baoyu-image-cards` thinking:

- what style fits the topic?
- what layout fits the information density?
- does the post need emotional hook or knowledge density?

Read these when useful:

- `/Users/shi/.codex/skills/baoyu-image-cards/SKILL.md`
- `/Users/shi/.codex/skills/chunge-xhs-content/references/combo-playbook.md`

### 3. Decide the caption strategy

If the selected path includes copy, use `chunge-xhs-content` to produce the final caption package:

- title with a clear hook
- body in plain text, easy to paste
- hashtags that match topic, audience, and lane

Read these when useful:

- `/Users/shi/.codex/skills/chunge-xhs-content/SKILL.md`
- `/Users/shi/.codex/skills/chunge-xhs-content/references/examples.md`

### 4. Align image and copy

Before finalizing, make sure:

- the title fits the image mood
- the body does not repeat card text line by line
- the hashtags match both topic and visual lane
- the package feels authored together

### 5. Deliver in publish order

When possible, present outputs in this order:

1. `图片`
2. `标题`
3. `正文`
4. `话题`

Keep `正文` as plain text lines. Do not wrap the final copy in code fences unless the user explicitly asks.

For partial paths:

- `text-only`: deliver `标题` + `正文` + `话题`
- `image-only`: deliver `图片`

## Output Rules

- Optimize for publish-ready output, not analysis.
- Keep the package concise and coordinated.
- If only part of the package is possible, clearly provide the missing part as a recommendation rather than pretending it was generated.
- When images already exist, prioritize writing copy that complements them.
- When the user asks for direct posting format, output only the usable deliverables.
- When the user explicitly says not to generate images, do not include image direction unless they ask for it.
- When the user explicitly says text only, route directly to caption delivery.

## References

Use these references as needed:

- `references/workflow-examples.md`
- `references/delivery-template.md`
