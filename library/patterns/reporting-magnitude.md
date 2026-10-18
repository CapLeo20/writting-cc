---
id: pattern-reporting-magnitude
type: pattern
title: 报告回归结果：把系数换成经济量级
author: 本仓库整理
year:
lang: zh
scenarios: [1, 2]
sections: [results, abstract, intro]
source: guide-cochrane-2005-writing-tips, guide-evans-2020-intro-dev-econ
verified: 判断
added: 2026-10-18
status: 初稿
---

# 报告回归结果：把系数换成经济量级

**一句话**：不只说"显著为正"，要说"大到什么程度、相对什么"。

## 做法

1. **先说方向和量级，再说显著性。**
2. **选一个读者能感受的参照系**：
   - 相对样本均值："相当于均值的 X%"；
   - 相对标准差："X 提高一个标准差，Y 提高 0.04 个标准差"；
   - 相对政策规模或其他效应："约相当于 [某政策] 效果的一半"。
3. **区分"%"和"个百分点"**，全文一致。
4. **"显著"只用于统计意义**；经济意义用"可观""较大""有限"。
5. 对数、交互项、标准化变量，写出换算后的含义，不让读者自己算。

## 例子（虚构）

> 改前：回归结果显示，政策的实施对企业的创新水平具有显著的正向促进作用。
>
> 改后：双重差分估计显示，政策使企业专利申请量提高约 8%，约为样本均值的四分之一，在 1% 水平上显著。

## 场景一的用法

Claude 给你讲论文时，也按这个顺序复述结果："作者发现 X 使 Y 提高约多少，相当于什么"，而不是只说"作者发现显著影响"。

## 依据

- guide-cochrane-2005-writing-tips（写具体发现）、guide-evans-2020-intro-dev-econ（结果占引言最大篇幅）
- Awesome-Journal-Skills 的 er-style 也有类似的"表格无解读 → 给出经济量级"对照，未经本仓库核实。
