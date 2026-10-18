---
id: pattern-agent-brief-handoff
type: pattern
title: 场景三：委派简报与交接文档
author: 本仓库整理
year:
lang: zh
scenarios: [3]
source: guide-anthropic-multi-agent-research, guide-anthropic-context-engineering, guide-anthropic-long-running-harness, guide-claude-code-best-practices
verified: 判断
added: 2026-10-18
status: 初稿
---

# 场景三：委派简报与交接文档

**一句话**：交接文档要"可核对"，不追求"好读"：区分已核实和未核实，写明路径和命令，记下失败的尝试，写清什么算完成。

## 十条写法

1. 固定骨架：每次用同样的标题顺序。
2. 分开四类信息：事实、已做的决定、假设、待办。
3. 能定位就定位：绝对路径、行号、命令、提交哈希、数据版本。
4. 写清完成标准，最好是一个能执行的检查。
5. 记下失败的尝试和原因。
6. 状态用 JSON 或表格，叙述用短段落（JSON 更不容易被误改）。
7. 术语和变量名只在一处定义。
8. 数字带单位、样本和来源。
9. 不铺垫、不客套、不重复总结。
10. 子 agent 的回报控制在 1,000–2,000 token，详细材料写进文件，回报里给路径。

## 委派简报模板

```markdown
## 目标
一句话：要回答什么问题，或要产出什么。

## 背景
只写对方完成任务必须知道的：研究问题、数据位置、已知结论。

## 输入
- 数据：/abs/path/to/data.dta（2011–2020 县级面板，N=…）
- 代码：/abs/path/to/code/main.do

## 要做的
1. …

## 不做的
- 不改动原始数据
- 不换估计方法，除非发现明显错误并先说明

## 输出格式
- 结论：3–5 句
- 证据：表格或文件路径
- 未核实的地方：逐条列出

## 完成标准
可执行的检查，例如：运行后生成 output/table3.tex，第 2 列系数与日志一致。
```

## 交接文档模板

```markdown
# 交接：<任务名> <日期>

## 当前状态（三句话以内）

## 已完成
- [已核实] 清洗后样本 N=…，见 output/log/clean.log 第 120 行
- [未核实] …

## 进行中
- 正在做：…；卡在：…

## 已做的决定（附理由）
- 聚类到县一级：处理在县级分配

## 试过但失败的
- 用 xx 做工具变量：第一阶段 F 值约 3，弱工具，放弃

## 下一步（按优先级）
1. …

## 运行方式
cd /abs/path && stata -b do main.do
```

## 依据

- 委派四要素：guide-anthropic-multi-agent-research
- 回报长度、笔记文件：guide-anthropic-context-engineering
- JSON 清单、启动顺序：guide-anthropic-long-running-harness
- 自包含的任务说明：guide-claude-code-best-practices
- 社区 handoff skill 的常见字段（当前状态、进行中、阻塞、下一步、决定附理由、已核实/未核实）见 research/01 第 4.2 节。
