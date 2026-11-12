---
id: anti-pattern-ai-tells-zh
type: anti-pattern
title: 中文 AI 腔、欧化句式与经济学论文套话
author: 本仓库整理
year:
lang: zh
scenarios: [1, 2]
sections: [sentence, title, abstract, intro, conclusion]
source: guide-humanizer-zh, guide-yu-guangzhong-europeanized-chinese, guide-ruanyf-document-style-guide, guide-cjyj-abstract-referee-comments, guide-liu-xichuan-knowledge-increment, guide-yao-yang-research-three-steps
verified: 判断
added: 2026-10-18
status: 初稿
---

# 中文 AI 腔、欧化句式与经济学论文套话

**一句话**：这些是检查线索，不是禁词表。命中后回到上下文判断：是否空泛、重复、歧义或不合文体。

## 改写的优先级（照搬 Humanizer-zh）

1. 保留信息和确定程度：不把相关改成因果、可能改成确定，不丢限定条件。
2. 遵守用户要求的编辑范围和文体。
3. 匹配作者声音。
4. 最后才改表达。

## A. AI 腔

| 模式 | 例子 | 改法 |
| --- | --- | --- |
| 假对比 | "这不仅是 X，更是 Y" | 直接说 Y |
| 起跑式铺垫 | "接下来让我们深入看看……" | 删掉，直接说内容 |
| 强凑三项 | "创新、突破和全新的可能" | 只保留有独立信息的项 |
| 意义拔高 | "具有深远的意义""开辟了新的视角" | 说具体意义，没有就删 |
| 套话收尾 | "总之，……值得我们深思" | 删掉 |
| 客服腔 | "希望这对你有帮助！" | 删掉 |
| 格式滥用 | 到处加粗、一行一个短要点、多级标题 | 默认写段落 |

## B. 欧化中文

| 模式 | 例子 | 改法 |
| --- | --- | --- |
| "进行/作出 + 名词" | "对样本进行检验""作出调整" | "检验样本""调整" |
| 层叠的"的" | "政策的实施对于企业的创新水平的提升" | "政策提高了企业创新水平" |
| 被字句堆叠 | "该变量被定义为……被用于……" | 改主动句 |
| 无主语句 | "通过对……的分析，发现……" | "本文分析……，发现……" |
| "随着……的发展"开头 | "随着数字经济的快速发展，……" | 直接从事实或问题开始 |

## C. 经济学论文套话

| 模式 | 例子 | 改法 |
| --- | --- | --- |
| 空洞贡献 | "丰富了现有研究""为……提供了新视角" | 和具体文献对比，说清多做了什么 |
| 空洞意义 | "具有重要的理论价值和现实意义" | 说清对谁、在哪个问题上有用 |
| 泛泛政策建议 | "应加强监管、完善制度、推进改革" | 谁、在哪个环节、做什么，且能从本文证据推出 |
| 显著当量级 | "具有显著的正向促进作用" | 报告量级，见 pattern-reporting-magnitude |
| 首次 | "本文首次……" | 除非确实核实过，改成和具体文献对比 |
| 自我评价 | "系统揭示""丰富和深化"（摘要里） | 删掉，只留实质结论和方法 |
| 空白式开头 | "鲜有学者关注……" | 先写空白背后的现实关切 |
| 机制大词 | "外部压力机制和内部治理机制" | 写到具体渠道，如"增加媒体报道、投资者实地调研" |
| 只说有影响 | "使不同企业的产能利用率产生分化" | 说清方向：谁升、谁降 |
| 标题式疑问 | "×××对×××的影响研究" | 写成能检验的疑问，或像《经济学（季刊）》建议的那样让题目反映结论 |
| 影响因素清单 | "××的影响因素研究" | 选定一个机制，控制其他变量把它讲清楚 |

C 组前五行参考了 Awesome-Journal-Skills 的 er-style 黑名单（未经本仓库核实）。"自我评价"到"只说有影响"四行来自《财经研究》公众号转述的审稿意见（guide-cjyj-abstract-referee-comments）；"标题式疑问"来自 guide-liu-xichuan-knowledge-increment；"影响因素清单"来自 guide-yao-yang-research-three-steps。

## 学术文体里可以保留的

Humanizer-zh 明确说：学术文本里被动句、四字格、名词化表达可以符合文体，不强行口语化。"首先、其次"说明顺序、"与此同时"表达同时发生、"不过"表达转折，都可以保留。

## 依据

- guide-humanizer-zh、guide-yu-guangzhong-europeanized-chinese、guide-ruanyf-document-style-guide
- C 组新增行：guide-cjyj-abstract-referee-comments、guide-liu-xichuan-knowledge-increment、guide-yao-yang-research-three-steps
