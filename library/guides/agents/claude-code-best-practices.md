---
id: guide-claude-code-best-practices
type: guide
title: Claude Code 官方文档：Best practices / Memory / Output styles / Skills
author: Anthropic
year: 2026
lang: en
scenarios: [1, 3]
fields: [general]
source: https://code.claude.com/docs/en/best-practices
verified: 原文
added: 2026-10-18
status: 初稿
---

# Claude Code 官方：规则文件该怎么写

**一句话**：规则要具体、要短；不同用途放进不同机制（CLAUDE.md、输出风格、skill、hook）。

## 要点

- **CLAUDE.md**：每一行都问"删掉它会不会让 Claude 出错"，不会就删。单个文件目标 200 行以内。规则要具体（写"用 2 空格缩进"，不写"格式规范"）。强调词（IMPORTANT）只用在一两行。可以规定压缩时保留什么。
- **好的任务说明**是自包含的：写明涉及的文件和接口，写明不做什么，以端到端的验证收尾。
- **输出风格**：对整个会话每次回复生效，管语气和格式；放在 `~/.claude/output-styles/` 或项目 `.claude/output-styles/`；`keep-coding-instructions: true` 保留编程行为；对子 agent 不生效（fork 除外）。
- **skill**：按需加载；SKILL.md 控制在 500 行以内，细节放进同目录的参考文件；description 决定何时自动触发，要把主要用途写在前面。
- **hook**：必须每次都发生的事用 hook，不靠指令。

| 想要的效果 | 用什么 |
| --- | --- |
| 每次回复的语气、长度、格式 | 输出风格 |
| 项目约定、命令、结构 | CLAUDE.md |
| 某一类任务的做法 | skill |
| 必须每次执行 | hook |
| 独立上下文的专门助手 | 子 agent |

## 可以怎么用

- 决定本仓库三类场景各用什么机制：场景一用输出风格，场景二用 skill，场景三用 skill + CLAUDE.md 约定。

## 出处

- https://code.claude.com/docs/en/best-practices
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/output-styles
- https://code.claude.com/docs/en/skills
