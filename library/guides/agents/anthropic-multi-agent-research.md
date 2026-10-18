---
id: guide-anthropic-multi-agent-research
type: guide
title: How we built our multi-agent research system
author: Anthropic
year: 2025
lang: en
scenarios: [3]
fields: [general]
source: https://www.anthropic.com/engineering/multi-agent-research-system
verified: 原文
added: 2026-10-18
status: 初稿
---

# Anthropic：多 agent 研究系统的委派经验

**一句话**：委派任务时写清目标、输出格式、工具和来源、任务边界，否则子 agent 会重复劳动或留下空白。

## 要点

- 每个子 agent 需要四样东西：目标（objective）、输出格式、可用工具和信息来源的指引、明确的任务边界。
- 早期主 agent 只给简短指令，子 agent 误解任务，或者和其他子 agent 做同样的搜索。原文："没有详细的任务描述，agent 会重复工作、留下空白，或者找不到必要的信息。"
- 按难度分配投入：简单查事实 1 个 agent、3–10 次工具调用；直接比较 2–4 个子 agent、各 10–15 次；复杂研究 10 个以上子 agent，分工明确。早期曾出现简单问题派出 50 个子 agent 的情况。

## 可以怎么用

- 场景三"委派简报"的四个必填项直接来自这里，见 pattern-agent-brief-handoff。

## 出处

- https://www.anthropic.com/engineering/multi-agent-research-system （已读原文）
