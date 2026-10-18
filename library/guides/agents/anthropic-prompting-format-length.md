---
id: guide-anthropic-prompting-format-length
type: guide
title: Prompting best practices（格式与长度部分）/ Prompting Claude Opus 5
author: Anthropic
year: 2026
lang: en
scenarios: [1, 3]
fields: [general]
source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
verified: 原文
added: 2026-10-18
status: 初稿
---

# Anthropic 官方：怎样控制回复的格式和长度

**一句话**：告诉模型该怎么写，而不是不许怎么写；长度要直接写明。

## 要点

**格式**（Prompting best practices）：

- 说"回复由连贯的段落组成"，而不是"不要用 markdown"。
- 可以用 XML 标签标明格式要求。
- 提示词本身的格式会影响输出：提示词里少用 markdown，回复里的 markdown 也会少。
- 需要精细控制时写详细规则。官方示例 `<avoid_excessive_markdown_and_bullet_points>`：长回答用完整段落；只有真正并列的条目或用户要求时才用列表；不要输出一串过短的要点。
- 官方提醒：较新的模型本身格式就少，强约束可能把内容需要的结构也压掉。

**长度**（Prompting Claude Opus 5）：

- 这一代默认回复偏长；effort 控制"想多少"，不控制"说多少"，要直接写长度要求。
- 示例："Keep responses focused, brief, and concise. Keep disclaimers and caveats short, and spend most of the response on the main answer."
- 写成文件的文档也偏长，可加："长度匹配任务需要，不加填充章节、重复摘要和套话。"
- 汇报时先说结果：第一句回答"发生了什么"或"发现了什么"。
- 给正面示例比列禁止事项更有效。

## 可以怎么用

- 场景一输出风格的写法依据。
- 场景三：委派 agent 时同样要写明输出长度。

## 出处

- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
