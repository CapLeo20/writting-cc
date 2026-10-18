---
id: pattern-reply-presentation
type: pattern
title: 场景一：回复的表述与交付形式
author: 本仓库整理
year:
lang: zh
scenarios: [1]
sections: [sentence, whole]
source: guide-minto-pyramid-principle, guide-anthropic-prompting-format-length, guide-ruanyf-document-style-guide, guide-pinker-2014-sense-of-style, guide-humanizer-zh, guide-williams-style-clarity-grace
verified: 判断
added: 2026-10-18
status: 初稿
---

# 场景一：回复的表述与交付形式

**一句话**：只规定"怎么说"，不规定"说什么"。目标是让读者用最短时间抓住结论和重点。

## 用户的要求（2026-10-18）

只优化表述方式，不固定内容和结构，因为每次回复的内容不同。要的是易读、清楚、能快速抓住内容和重点。规则要能放进 Claude Code 和网页版。

因此 v0.1 里规定内容顺序的条目（"讲论文按问题→识别→结果→假设"、"讲方法按问题→直觉→公式→例子"）从输出风格里移除，保留在 pattern-plain-explanation 作为可选参考。

## 规则

### 1. 结论先行

第一句就是答案、判断或最重要的发现。需要前提时先给结论，再说前提。依据：Minto 金字塔原理"答案先行"；Anthropic 官方"先说结果"。

### 2. 按篇幅选形态（三档）

| 篇幅 | 形态 |
| --- | --- |
| 一两句能说清 | 直接回答，不加标题、列表、加粗 |
| 一般解释 | 短段落；每段只讲一件事，第一句是这一段的要点 |
| 内容多、分几个方面 | 先用两三句或 2–4 条要点给出全貌，再用简短小标题分块 |

依据：Minto"上层概括下层"；Williams 和 Pinker 关于段落主题句的做法；新模型的官方建议是说清什么时候用格式，而不是一律禁止。

**实验发现（v0.1）**：一律禁止标题后，模型改用单独一行的加粗字当小标题。所以 v0.2 明确：长回答用真正的小标题，不用加粗行代替。

**实验发现（v0.2）**：约 550 字的判断题也被分成了三个小标题。v0.2.1 加了门槛：全文不到约 600 字时不用小标题；小标题用 `##` 写。

### 3. 格式工具各有用途

- 编号列表：有先后顺序的步骤。
- 无序列表：彼此独立的并列项；每项是完整的短句；不超过一层嵌套。
- 表格：两个以上对象在几个方面比较。
- 加粗：只标结论或关键数字，全文少量。
- 代码块：代码、命令、路径、需要原样复制的内容。
- 公式：网页版可用 LaTeX；Claude Code 终端不渲染 LaTeX，用纯文本写。

### 4. 句子和用词

- 短句；一句一个主要信息；条件和例外放在结论之后。依据：阮一峰写作规范。
- 常用词；术语首次出现写中文加英文或缩写，之后说法一致。依据：glossary/econ-fin-terms.md。
- 数字带单位和参照；区分百分比和百分点。
- 一句话点名常见套话（"值得注意的是""总之""不是……而是……"）。v0.2 曾删掉防套话清单，v0.2.1 的回答里又出现了一次"值得注意"，所以加回一句短的。完整清单见 anti-pattern-ai-tells-zh。

### 5. 让重点和不确定性都看得见

- 分清事实、推断和不确定之处；不确定就直说，并说明怎么核实。
- 保留原文限定：相关不写成因果。依据：Humanizer-zh 的第一优先级。
- 确实有需要读者决定或动手的事项时，放在最后单独一段；没有就直接结束。除此之外不写结尾总结和客套话。

  **实验发现（v0.2）**：原来的写法让 6 个回答全部以"需要你决定"结尾，有的是硬凑的。v0.2.1 改成"确实有才写，没有就直接结束"。

### 6. 长度

由问题决定。宁可短而完整，追问再展开；不为变短省掉关键前提。

## 应用

- Claude Code：`.claude/output-styles/econ-plain-zh.md`（v0.2）
- 网页版：`web/claude-ai-instructions.md`
- 评测：`evals/scenario1/`

## 依据

- guide-minto-pyramid-principle、guide-anthropic-prompting-format-length、guide-ruanyf-document-style-guide、guide-pinker-2014-sense-of-style、guide-humanizer-zh、guide-williams-style-clarity-grace
