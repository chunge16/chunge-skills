# Workflow Notes

Use this file when you need the operational checklist while running `chunge-xhs-images`.

## Fast Checklist

1. Ingest the source and decide whether it is best treated as story-driven, information-dense, or visual-first.
2. Pick a style, layout, and page count.
3. Summarize the recommendation for the user.
4. Write `analysis.md` and `outline.md` if the workspace output matters.
5. Create one prompt file per page.
6. Generate the images directly in Codex.
7. Report the save location and the chosen direction.

## Default Output Shape

Recommended default is 6 pages:

1. Cover
2. Hook or problem
3. Key point 1
4. Key point 2
5. Key point 3
6. Summary or CTA

Use 4-5 pages for lighter content.
Use 6-8 pages for dense educational content.

## Analysis Checklist

Capture the following in `analysis.md`:

- Topic
- Content type
- Target audience
- Main hook
- Core takeaways
- Recommended strategy
- Recommended style and layout
- Recommended page count
- Notes about facts that must remain accurate

## Outline Strategies

### Story-Driven

Use when the source is personal, reflective, or transformation-based.

Suggested page flow:

1. Emotional hook
2. Original pain point
3. Turning point
4. What changed
5. What the audience can learn
6. CTA

Preferred styles:

- `warm`
- `cute`
- `fresh`

### Information-Dense

Use when the source is educational, analytical, or tool-focused.

Suggested page flow:

1. Big claim or problem statement
2. Condensed framework
3. Key point 1
4. Key point 2
5. Key point 3
6. Summary and recommendation

Preferred styles:

- `notion`
- `study-notes`
- `chalkboard`
- `minimal`

### Visual-First

Use when aesthetics and mood matter more than text density.

Suggested page flow:

1. Hero cover
2. Core mood or product
3. Detail page
4. Context page
5. Highlight page
6. CTA

Preferred styles:

- `screen-print`
- `retro`
- `pop`
- `minimal`

## Prompt Checklist

Each prompt should define:

- Page role
- Central subject
- Style
- Layout
- Composition
- Color direction
- Text density
- Decorative language
- Constraints to keep the whole set consistent

Use short on-image text. Prefer concise Chinese headings or labels over long body copy.

## Consistency Rules

- Keep the same palette family across all pages.
- Reuse 2-3 decorative motifs across the series.
- Keep typography feeling implied rather than over-specified.
- Do not overload every page with equal density; alternate dense and light pages when possible.
- Cover page should be the strongest visual anchor.
- If the image generator supports reference-style continuity, use the first generated page as the visual anchor for later pages.
