# xhs-copywriter

Generate concise, copy-ready Xiaohongshu post copy from images, notes, article excerpts, knowledge cards, product summaries, and finance-related source material.

This skill is optimized for one-step delivery: title options, a short publishable body, and compact hashtags that can be pasted into Xiaohongshu with minimal cleanup.

## Best For

- 小红书标题和正文
- 图文配文
- 知识卡配套文案
- 产品分享文案
- 金融学习记录类文案
- 需要“可直接复制”输出的发布场景

## Install This Skill

Install the full repository:

```bash
npx skills add chunge16/chunge-skills
```

Install just this skill:

```bash
npx skills add chunge16/chunge-skills --skill xhs-copywriter
```

List available skills first:

```bash
npx skills add chunge16/chunge-skills --list
```

## What It Produces

By default, the skill returns:

- 3-5 title options
- one concise Xiaohongshu body
- 6-10 relevant hashtags

For copy-first requests such as “可复制”, “直接复制”, or “发布文案”, the skill is instructed to return one plain fenced `text` block only.

## Supported Modes

- `standard`: default title + body + topics output
- `short`: shorter body for compact posts
- `titles`: title options only
- `knowledge-card`: summarize the strongest takeaways from cards or notes
- `finance-note`: preserve dates and numbers, add a neutral disclaimer
- `product-share`: focus on use case, value, audience, and caveats

## Example Prompts

```text
Use $xhs-copywriter to write a Xiaohongshu caption for this image card set
```

```text
Use $xhs-copywriter to turn these article notes into a concise Xiaohongshu post
```

```text
Use $xhs-copywriter in finance-note mode for this ETF summary
```

```text
Use $xhs-copywriter to give me copyable title, body, and hashtags in text format
```

## Writing Rules

- Keep the copy short and mobile-friendly
- Start with a conclusion, contrast, or strong hook
- Preserve important names, dates, numbers, and caveats
- Avoid tables and bloated formatting
- Use a small number of light icons instead of heavy decoration
- Avoid explicit buy/sell advice in finance-related posts

## Notes

- This skill is purpose-built for copy output, not image generation.
- If the user provides dense image cards, the skill should synthesize rather than transcribe.
- If OCR details are unclear, the skill should avoid inventing exact claims or figures.
