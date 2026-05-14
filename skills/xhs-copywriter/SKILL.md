---
name: xhs-copywriter
description: Generate concise, copy-ready Xiaohongshu (小红书) post copy from images, generated image cards, article context, notes, product/finance/knowledge summaries, or rough ideas. Use when the user asks for 小红书标题, 小红书正文, 话题, hashtags, 可直接复制, text格式, 发布文案, 图文配文, or wants a punchy plain-text post with light icon symbols and topics.
---

# XHS Copywriter

## Output Goal

Produce Xiaohongshu-ready copy that the user can copy in one action.

Always output copyable plain text only. Unless the user explicitly asks for explanation, options, or analysis, return exactly one fenced `text` block and nothing else. This is a hard rule for requests containing “可复制”, “text格式”, “直接复制”, “一键复制”, “小红书文案”, or “发布文案”.

## Workflow

1. Read the image, image-card content, article, notes, or conversation context.
2. Extract the core hook, target audience, key facts, emotional angle, and caution/disclaimer needs.
3. Draft a concise post with:
   - 3-5 title options with light icon symbols.
   - A short body with light icon symbols.
   - A compact topic/hashtag line.
4. Keep it punchy, useful, and easy to scan on mobile.
5. If source data has dates, preserve the dates. If financial, medical, legal, or other high-stakes content is involved, include a short neutral disclaimer.

## Output Modes

Pick the mode from the user's wording. If unspecified, use `standard`.

| Mode | Use when | Output |
| --- | --- | --- |
| `standard` | Default post copy | 3-5 title options + concise body + topics |
| `short` | User says 简洁, 精简, 短一点 | 3 title options + 120-250 Chinese characters + topics |
| `titles` | User asks for 标题, 标题备选 | 5-8 icon title options only, optionally plus one recommended title |
| `knowledge-card` | Source is image cards, infographic, learning notes | Summarize the strongest 3-5 takeaways |
| `finance-note` | ETF, stocks, funds, investment, finance | Preserve dates/numbers and add neutral disclaimer |
| `product-share` | Product/tool/app/course recommendations | Lead with use case, value, who it suits, and caveat |

When the user asks only for “标题和内容”, include topics unless they explicitly say no topics.

## Length Defaults

- `short`: 120-250 Chinese characters, 2-4 short sections, 6-8 topics.
- `standard`: 250-500 Chinese characters, 3-5 short sections, 8-10 topics.
- `detailed`: 500-800 Chinese characters, only when the source is complex or the user asks for more detail, 8-10 topics.

When the user says “简洁一些”, reduce the previous draft by 30-50% and keep only the strongest hook, 2-3 key points, one caution, and topics.

## Default Format

Use this structure unless the user requests another format:

```text
标题参考：
1. 📌 ...
2. 💡 ...
3. ✅ ...

正文：
...

话题：
#话题1 #话题2 #话题3
```

If the user asks for “更像小红书” or “适合发布”, this format can be slightly more natural:

```text
标题参考：
1. 📌 标题一句话
2. 💡 标题一句话
3. ✅ 标题一句话

正文第一段：先给结论或反差。

📌 核心信息
...

📈 关键看点
...

⚠️ 注意点
...

✅ 一句话总结
...

#话题1 #话题2 #话题3
```

## Style Rules

- Use Chinese by default when the source/user request is Chinese.
- Keep the body concise: use the length defaults above.
- Use 3-6 icon symbols total, not every line.
- Prefer common icons: 📌 📈 🧩 ⚠️ ✅ 🔍 💡 📝.
- Keep paragraphs short, usually 1-3 lines each.
- Use direct, concrete phrasing. Avoid fluffy marketing adjectives.
- Start with a conclusion, contrast, or surprising detail. Avoid slow openings like “今天给大家介绍”, “本文将”, “我们可以看到”.
- Prefer Xiaohongshu-native phrasing: “简单说”, “买前先看”, “一句话总结”, “适合收藏”, “别只看...”.
- Preserve important numbers, dates, names, and caveats from the source.
- For finance/investment content, do not write buy/sell advice. Use “非投资建议，仅做学习记录” or equivalent.
- For images with many cards, synthesize instead of transcribing every card.
- Avoid Markdown bullets if the user asks for pure text; simple numbered lines are fine.
- Avoid tables because they copy poorly into Xiaohongshu.

## Title Rules

Generate 3-5 title options by default. If the user asks only for titles, provide 5-8 options. Each title should start with one light icon symbol.

Recommended title icons:

- 📌 for core point / must-read.
- 💡 for insight / method / learning.
- ✅ for conclusion / checklist / summary.
- ⚠️ for risk reminders.
- 🔍 for analysis / detail discovery.
- 📈 for finance, growth, market, data.

Good title patterns:

- 反差：📌 这只A股ETF，前两大持仓竟是...
- 结果：✅ 一页看懂...
- 风险提醒：⚠️ 别只看涨幅，先看...
- 清单：💡 买前先看这...点
- 人群：📌 适合...的人先收藏

Keep titles short: usually 12-24 Chinese characters after the icon. Avoid clickbait that overpromises.

## Topic Rules

Include 6-10 topics by default. Never exceed 10 topics unless the user explicitly asks for more. Put them on one line after `话题：`.

Topic selection:

- 2-4 broad discovery topics, e.g. `#投资理财 #基金投资 #小白理财`.
- 2-5 domain topics, e.g. `#半导体ETF #跨境ETF #QDII基金`.
- 1-3 specific entity topics, e.g. `#513310 #中韩半导体ETF`.
- 1 safety/context topic when needed, e.g. `#非投资建议`.

For each post, compose topics in this order:

1. Broad category topics.
2. Domain/topic-specific tags.
3. Entity tags such as product name, ticker, brand, person, place, or tool.
4. Audience/use-case tags such as `#小白理财`, `#学习笔记`, `#效率工具`.
5. Safety/context tag when needed.

Do not overstuff with unrelated hot tags.
Prefer the highest-signal tags first and cut lower-value tags to stay within the 10-topic cap.

## Image Input Handling

When the input is an image or image-card series:

- Summarize the visible claim, numbers, entities, and warnings.
- Do not mention “图片中显示” unless useful.
- If OCR/text is uncertain, do not invent exact numbers, names, dates, or claims. Use cautious phrasing such as “图中未清晰显示具体数值” only when necessary, or ask for clarification when the missing detail is essential.
- If the image contains already-designed cards, create matching post copy instead of restating every card verbatim.

## Examples

### Finance ETF

```text
标题参考：
1. 📈 这只A股ETF，前两大持仓是三星+SK海力士
2. ⚠️ 别只看涨幅，先看这只跨境ETF
3. 🔍 一页看懂中韩半导体ETF513310

正文：
513310，中韩半导体ETF华泰柏瑞。

它不是普通A股半导体ETF，而是“韩国存储 + 中国半导体核心资产”的跨境ETF。

📌 基础信息
类型：QDII / 跨境ETF / 被动指数型
跟踪：中证韩交所中韩半导体指数

📈 看点
前十大持仓合计67.92%，三星电子和SK海力士合计34.37%。

⚠️ 注意
高弹性也意味着高波动，跨境ETF还要看溢价、汇率和交易时差。

✅ 一句话
适合先研究，不适合只看涨幅冲进去。

非投资建议，仅做学习记录。

话题：
#ETF投资 #A股ETF #半导体ETF #中韩半导体ETF #513310 #QDII基金 #跨境ETF #投资笔记 #非投资建议
```

### Short Finance Version

```text
标题参考：
1. 📈 这只A股ETF，前两大持仓是三星+SK海力士
2. ⚠️ 跨境ETF别只看涨幅
3. 🔍 513310到底投了什么

正文：
513310，中韩半导体ETF华泰柏瑞。

简单说，它是“韩国存储 + 中国半导体核心资产”的跨境ETF。

📌 看点
前十大持仓合计67.92%，三星电子和SK海力士合计34.37%。

⚠️ 注意
高弹性也意味着高波动，跨境ETF还要看溢价、汇率和交易时差。

非投资建议，仅做学习记录。

话题：
#ETF投资 #A股ETF #半导体ETF #中韩半导体ETF #513310 #QDII基金 #跨境ETF #投资笔记 #非投资建议
```

### Knowledge Summary

```text
标题参考：
1. 💡 一页看懂这个概念
2. 📌 真正重要的不是定义
3. ✅ 把复杂问题拆简单

正文：
这个概念最重要的不是定义，而是它解决了什么问题。

📌 核心
把复杂流程拆成几个可重复执行的小步骤。

💡 价值
降低理解成本，也方便复盘和传播。

✅ 记住一句话
好内容不是信息堆满，而是让人马上抓住重点。

话题：
#知识分享 #学习笔记 #认知提升 #方法论 #自我成长 #干货分享
```

### Product / Tool Share

```text
标题参考：
1. 📌 这个工具适合先收藏
2. 💡 写发布文案不用从0开始
3. ✅ 内容工作流可以这样省时间

正文：
如果你经常要把复杂内容整理成可发布文案，这类工具很适合放进工作流。

📌 适合谁
做内容、写笔记、整理资料、需要快速产出发布文案的人。

💡 亮点
能把零散信息变成标题、正文和话题，减少从0开始写的压力。

⚠️ 注意
最终发布前还是要检查事实、语气和敏感表达。

话题：
#效率工具 #AI工具 #内容创作 #小红书运营 #写作工具 #自媒体 #工作流 #效率提升
```
