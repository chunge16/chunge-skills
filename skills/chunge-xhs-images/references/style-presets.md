# Style Presets

Use presets as a shortcut for `style + layout`.

## Knowledge And Learning

| Preset | Style | Layout | Best For |
|--------|-------|--------|----------|
| `knowledge-card` | `notion` | `dense` | AI 工具、概念科普、SaaS 干货 |
| `checklist` | `notion` | `list` | 清单、建议、避坑合集 |
| `concept-map` | `notion` | `mindmap` | 概念关系、知识脉络 |
| `swot` | `notion` | `quadrant` | 四象限分析、分类法 |
| `tutorial` | `chalkboard` | `flow` | 教程步骤、工作流、操作方法 |
| `classroom` | `chalkboard` | `balanced` | 教学讲解、课堂感知识页 |
| `study-guide` | `study-notes` | `dense` | 学习笔记、复习重点、总结 |

## Lifestyle And Sharing

| Preset | Style | Layout | Best For |
|--------|-------|--------|----------|
| `cute-share` | `cute` | `balanced` | 日常分享、种草图文 |
| `girly` | `cute` | `sparse` | 氛围封面、颜值内容 |
| `cozy-story` | `warm` | `balanced` | 个人经历、情绪表达、生活感 |
| `product-review` | `fresh` | `comparison` | 产品对比、优缺点评测 |
| `nature-flow` | `fresh` | `flow` | 护肤、健康、自然生活方式 |

## Strong Opinion And Alerts

| Preset | Style | Layout | Best For |
|--------|-------|--------|----------|
| `warning` | `bold` | `list` | 避坑、误区、提醒 |
| `versus` | `bold` | `comparison` | 正反对比、方案选择 |
| `clean-quote` | `minimal` | `sparse` | 金句、观点封面 |
| `pro-summary` | `minimal` | `balanced` | 专业总结、商务内容 |

## Culture And Editorial

| Preset | Style | Layout | Best For |
|--------|-------|--------|----------|
| `retro-ranking` | `retro` | `list` | 怀旧排行、经典盘点 |
| `throwback` | `retro` | `balanced` | 怀旧分享、复古表达 |
| `pop-facts` | `pop` | `list` | 轻知识、趣味事实 |
| `poster` | `screen-print` | `sparse` | 海报感封面、书影乐评 |
| `editorial` | `screen-print` | `balanced` | 观点文章、文化评论 |

## Override Rule

If a preset is chosen and the user also specifies `style` or `layout`, the explicit `style` or `layout` wins.

Examples:

- `preset=knowledge-card + style=chalkboard` => `chalkboard + dense`
- `preset=poster + layout=quadrant` => `screen-print + quadrant`
