---
id: guide-anthropic-context-engineering
type: guide
title: Effective context engineering for AI agents
author: Anthropic
year: 2025
lang: en
scenarios: [3]
fields: [general]
source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
verified: 原文
added: 2026-10-18
status: 初稿
---

# Anthropic：上下文工程

**一句话**：上下文是有限的注意力预算，要找"能最大化期望结果的最小高信号 token 集合"。

## 要点

- **子 agent 回报要浓缩**：子 agent 可以用几万 token 探索，但只回传 1,000–2,000 token 的摘要。
- **结构化笔记**：把进度写进上下文之外的文件（如 NOTES.md、待办清单），上下文重置后读回来继续。
- **压缩时保留什么**：架构决策、未解决的问题、实现细节；丢掉冗余内容。调整压缩提示时先保证不漏（召回），再删多余（精度）。
- **合适的高度**：提示词既不要写成僵硬的 if-else，也不要笼统到默认对方知道背景。

## 可以怎么用

- 场景三交接文档的长度和取舍标准。
- 写 CLAUDE.md、skill 时的总原则：每一行都要有信号。

## 出处

- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents （已读原文）
