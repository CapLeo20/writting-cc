---
id: pattern-plain-explanation
type: pattern
title: 场景一：怎样把一篇论文、一个方法讲清楚
author: 本仓库整理
year:
lang: zh
scenarios: [1]
sections: [sentence]
source: guide-anthropic-prompting-format-length, guide-stulz-jfe-tips-for-authors, guide-pinker-2014-sense-of-style, guide-ruanyf-document-style-guide, guide-humanizer-zh
verified: 判断
added: 2026-10-18
status: 初稿
---

# 场景一：怎样把一篇论文、一个方法讲清楚

**一句话**：第一句给答案；按"问题 → 识别 → 结果 → 前提"的顺序讲；用常用术语；默认写段落。

## 做法

1. **第一句就是答案**。不复述问题，不写开场白（Anthropic：先说结果）。
2. **讲论文按固定顺序**：研究问题 → 识别策略（用的是什么变异）→ 主要结果（带量级）→ 关键假设和可能的问题。
3. **讲方法按教材顺序**：要解决什么问题 → 直觉 → 公式或步骤 → 一个例子 → 什么时候会失效。这是伍德里奇《导论》式的讲法，待拆解教材后补充。
4. **读者设定**：学过中级微观、宏观和计量，但不熟悉这个细分领域（Stulz："MBA 班也能听懂"；Pinker：警惕知识的诅咒）。
5. **用词**：常用说法；术语用 [术语表](../../glossary/econ-fin-terms.md) 的译名，第一次出现附英文。
6. **格式**：默认用段落；真正并列的条目、步骤、需要对比的数字才用列表或表格；少用加粗，不用多级标题。
7. **句子**：一句尽量不超过 30 字，超过 40 字一定拆（阮一峰）。
8. **不夸大**：相关不说成因果，"可能"不说成"一定"，原文的限定条件要保留（Humanizer-zh 的第一优先级）。

## 应用

- 已写成输出风格：`.claude/output-styles/econ-plain-zh.md`。

## 依据

- guide-anthropic-prompting-format-length、guide-stulz-jfe-tips-for-authors、guide-pinker-2014-sense-of-style、guide-ruanyf-document-style-guide、guide-humanizer-zh
