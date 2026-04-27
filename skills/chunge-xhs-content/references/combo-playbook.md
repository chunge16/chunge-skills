# Combo Playbook

Use this playbook when the user wants both Xiaohongshu image cards and copy as one coordinated package.

## Core idea

Treat the post as one system:

- `baoyu-image-cards` handles visual hook, layout, and card density
- `chunge-xhs-content` handles title, caption body, and hashtags
- both should point to the same audience, promise, and tone

## Recommended sequence

### Path A: Topic -> Images -> Copy

Use when the user starts with a topic and wants a complete post package.

1. Define the post angle first.
2. Use `baoyu-image-cards` to shape the image series.
3. Observe the resulting style, layout, density, and emotional tone.
4. Use `chunge-xhs-content` to write the matching title, body, and hashtags.

Best for:

- knowledge cards
- product recommendations
- before/after or checklist posts
- themed lifestyle content

### Path B: Images -> Copy

Use when the user already has images or cards.

1. Read the images.
2. Infer topic, audience, and the amount of visible information.
3. Write copy that complements, frames, and lightly extends the image content.

Best for:

- completed card sets
- designer-made covers
- screenshots or visual drafts

### Path C: Copy -> Image-aware rewrite

Use when the user already has a draft caption but still wants strong image alignment.

1. Identify the draft's main hook.
2. Infer what image style or card layout would pair with it.
3. Rewrite the copy so it feels visually compatible with a Xiaohongshu carousel or cover.

Best for:

- existing brand copy
- rough draft cleanup
- turning long notes into post-ready captions

## Matching rules

### If the visual style is dense

- shorten the body
- reduce repeated details
- make the title clearer rather than longer
- use hashtags for discoverability, not extra explanation

### If the visual style is sparse

- allow the title to carry more hook
- let the first line of the body add context
- use the body to complete the emotional or practical story

### If the visual style is cute / soft

- use warmer tone
- avoid overly sharp warning language
- keep icons lighter and friendlier

### If the visual style is bold / warning

- sharpen contrast in the title
- keep body lines short
- emphasize takeaway or caution quickly

### If the visual style is notion / knowledge-card

- use clearer takeaway language
- keep the body save-worthy
- avoid sounding too emotional

## Final package checklist

Before finishing a combo workflow, check:

- the title matches the cover mood
- the body adds value beyond card text
- the hashtags fit both topic and audience
- the image and caption feel authored together
- the caption is still easy to paste directly into Xiaohongshu

## Ready-to-use prompt patterns

### Full package prompt

```text
先用 baoyu-image-cards 生成一组关于“[主题]”的小红书图片卡片，再用 $chunge-xhs-content 生成配套标题、正文和话题。正文必须是纯文本，方便我直接复制发布，文案要和图片风格一致。
```

### Existing images prompt

```text
参考这组图片 / 卡片内容，用 $chunge-xhs-content 帮我写一版配套小红书文案。不要重复图片上已经写清楚的内容，正文保持简洁、可直接复制。
```

### Rewrite for image alignment prompt

```text
这是我现有的小红书文案草稿，请用 $chunge-xhs-content 按照更适合图片卡片发布的方式重写，让标题、正文和话题更适合和 baoyu-image-cards 风格的配图一起发。
```
