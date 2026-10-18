---
id: guide-anthropic-long-running-harness
type: guide
title: Effective harnesses for long-running agents
author: Anthropic
year: 2025
lang: en
scenarios: [3]
fields: [general]
source: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
verified: 原文
added: 2026-10-18
status: 初稿
---

# Anthropic：跨会话长任务的交接

**一句话**：每个新会话都没有记忆，所以要用"结构化清单 + 进度日志 + 启动脚本 + git"交接。

## 要点

- **四样交接物**：
  - 功能清单（JSON）：每项有类别、描述、测试步骤和 `passes` 字段（初始为 false），后续 agent 只能改 `passes`；
  - 进度日志 `claude-progress.txt`：之前的 agent 做了什么；
  - 启动脚本 `init.sh`：新会话不用重新摸索怎么运行；
  - git 提交：每次会话提交，写清提交信息，方便回滚。
- **新会话启动顺序**：确认工作目录 → 读 git 日志和进度文件 → 读功能清单，选优先级最高的未完成项 → 跑一遍基础测试，先发现上一轮留下的问题。
- **用 JSON 而不用 Markdown 存清单**：模型更不容易误改或覆盖 JSON 文件。
- 每次只做一项，避免一次铺开太多。

## 可以怎么用

- 经济学研究的长任务（数据清洗、一组回归、一篇稿子的多轮修改）可以照搬：任务清单用 JSON，进度用文本笔记，结果用 git 记录。

## 出处

- https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents （已读原文）
- Prompting best practices 的"状态管理"部分有同样的建议。
