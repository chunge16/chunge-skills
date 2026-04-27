# Usage Examples

Use these examples as realistic prompts for `chunge-xhs-content`.

## Basic invocation

```text
Use $chunge-xhs-content 给我写一条小红书文案，主题是“早八通勤淡妆”，要标题 + 正文 + 话题，语气自然一点。
```

## Beauty / Skincare

```text
Use $chunge-xhs-content 根据这款敏感肌面霜，生成适合小红书发布的标题、正文和话题。要简洁有力，正文用纯 text 输出，方便我直接复制发布。
```

```text
Use $chunge-xhs-content 帮我写一条小红书护肤文案，主题是“换季泛红怎么稳定下来”。偏经验分享，不要太像广告。
```

## Food / Cafe

```text
Use $chunge-xhs-content 帮我写一条上海咖啡店探店文案，突出环境、咖啡口感和适合拍照，直接输出可复制版本。
```

```text
Use $chunge-xhs-content 给我写一条小红书美食文案，主题是“最近吃到的一家会想二刷的日料店”，语气轻松一点。
```

## Productivity / Tools / AI

```text
Use $chunge-xhs-content 帮我写一条小红书内容，主题是“我最近在用的 AI 总结工具”。要偏种草风，突出省时间，给我可直接复制的标题、正文、话题。
```

```text
Use $chunge-xhs-content 围绕“Notion 管理工作流”写一条小红书文案，重点写清楚它帮我解决了什么问题，不要空话。
```

## Knowledge / Study

```text
Use $chunge-xhs-content 把“如何提高专注力”的几条笔记整理成一条小红书文案。要简单易懂，像真正的小红书博主会发的内容。
```

```text
Use $chunge-xhs-content 帮我把这段读书笔记改成适合发小红书的标题、正文和话题，风格清晰一点，少说教感。
```

## Home / Lifestyle

```text
Use $chunge-xhs-content 围绕“租房卧室改造”写一条小红书文案，突出预算不高但氛围提升很明显，直接给可发布版本。
```

```text
Use $chunge-xhs-content 帮我写一条家居收纳文案，主题是“桌面乱的人真的需要这几个小东西”，要有一点种草感。
```

## Fashion / Outfit

```text
Use $chunge-xhs-content 帮我写一条穿搭文案，主题是“初夏通勤穿搭”，突出显瘦、好搭、不费力，正文要方便直接复制。
```

## Travel / Local Guide

```text
Use $chunge-xhs-content 帮我写一条杭州周末出游文案，主题是“适合放空的一日路线”，语气轻松一点，给我标题、正文、话题。
```

## Multi-variant prompts

```text
Use $chunge-xhs-content 围绕“租房卧室改造”写小红书文案，给我 3 个版本：克制版、种草版、爆点版。正文必须是纯文本，方便复制。
```

```text
Use $chunge-xhs-content 帮我给这款护肤精华写 3 个不同风格的小红书版本，分别偏真实分享、偏种草、偏强钩子。
```

## Direct publish format

```text
Use $chunge-xhs-content 根据以下信息直接输出可发布成品，不要解释，不要代码块，不要加分析：
产品：通勤帆布包
卖点：轻、能装、好搭衣服
人群：上班族女生
场景：通勤、周末出门
```

## With source notes

```text
Use $chunge-xhs-content 把下面这些零散笔记整理成小红书文案，保留重点但不要写得太长，正文要是纯文本方便复制：
1. 这个台灯亮度够但不刺眼
2. 放桌面很省位置
3. 晚上办公舒服很多
4. 拍照也挺好看
```

## Image-first prompts

```text
Use $chunge-xhs-content 根据这组图片帮我反推一版小红书文案。要标题、正文、话题，正文必须是纯 text，方便我直接复制发布。不要重复图片上已经写过的每一句话。
```

```text
Use $chunge-xhs-content 参考这张封面的视觉氛围，帮我写一版更适合小红书发布的标题、正文和话题。语气自然一点，不要太硬广。
```

## With baoyu-image-cards

```text
Use $chunge-xhs-content 根据这组 baoyu-image-cards 生成的小红书卡片，帮我写一版配套文案。要求标题有钩子，正文简洁，话题可直接复制。
```

```text
Use $chunge-xhs-content 先参考这些 baoyu-image-cards 的风格和卡片信息，再生成一版适合发布的小红书文案。不要逐字重复图上的内容，要写得更像发帖配文。
```

## Combined image + copy workflow

```text
先用 baoyu-image-cards 生成一组“小红书效率工具分享”的图片卡片，再用 $chunge-xhs-content 生成对应的标题、正文和话题。正文必须是纯文本，方便我直接复制发布。
```

```text
我想发一组“租房卧室改造”的小红书图文。先参考 baoyu-image-cards 的风格做图片方向，再用 $chunge-xhs-content 生成一版和图片调性一致的文案。
```

```text
先用 baoyu-image-cards 做一组“敏感肌换季护肤”信息卡，再用 $chunge-xhs-content 输出配套标题、正文和话题。不要重复图上的知识点，要更像真实发帖配文。
```

```text
我已经有一组 baoyu-image-cards 生成的知识卡，请用 $chunge-xhs-content 帮我补一版适合发布的小红书配文，重点写清楚这组内容适合谁看、为什么值得收藏。
```

## Expected output shape

Single-version outputs should usually look like this:

```text
标题
✨ 这个方法真的省时间

正文
✅ 先说结论：最近真的离不开它
🧩 最打动我的是上手快，不用重新适应
📌 日常用下来，最明显的是节省了很多零碎时间
🙋 如果你也经常被琐事打断，真的可以试试

话题
#效率提升 #时间管理 #实用工具 #工作流 #好物分享
```
