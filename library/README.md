# 素材库

这里收录写作经验和风格样本，是"经验与审美积累"的部分。素材库本身不直接改变 Claude Code 的行为；`.claude/` 下的输出风格和 skill 定期从这里提炼。

完整目录见 [INDEX.md](INDEX.md)（自动生成）。

## 怎么分类

一张卡片只放在一个目录里（按**类型**），其他维度写在卡片开头的元数据里当标签。

| 目录 | 类型 | 收什么 | 例子 |
| --- | --- | --- | --- |
| `guides/` | 写作指南 | 教人怎么写的书、文章、讲义、官方文档 | Cochrane 写作指南、Head 引言五步法 |
| `scholars/` | 学者档案 | 一人一档：代表作、写作主张、风格观察 | 范里安、伍德里奇 |
| `journals/` | 期刊档案 | 一刊一档：定位、格式要点、风格观察、范文 | 《经济研究》、IREF |
| `papers/` | 范文拆解 | 一篇一档：逐段拆解引言和关键部分 | （待补） |
| `patterns/` | 写法提炼 | 跨来源归纳的做法 | 叙事骨架、引言结构 |
| `anti-patterns/` | 反面模式 | 要避免的写法 | AI 腔、欧化句式、论文套话 |

`guides/` 下再按来源领域分子目录：`econ/`（经济学）、`finance/`（金融）、`general/`（通用写作）、`zh/`（中文写作）、`agents/`（agent 沟通）。

**标签**（元数据字段）：

- `scenarios`：1 日常回复、2 论文写作、3 agent 交接
- `sections`：论文部位，如 `intro`、`results`、`conclusion`
- `fields`：领域，如 `finance`、`metrics`、`china`
- `verified`：原文 / 摘要 / 待核实 / 判断

## 三种积累方式

1. **从写作指南里提取**：读一份指南，写一张 guide 卡片。适合"经验"。
2. **从学者和期刊的作品里提取**：拆解范文，写 paper 卡片，再把观察汇总到 scholar 和 journal 卡片。适合"审美"。观察维度见 [STYLE-DIMENSIONS.md](STYLE-DIMENSIONS.md)。
3. **跨来源归纳**：几张卡片说的是同一件事时，合成一张 pattern 卡片。应用层（`.claude/`）主要引用 pattern 卡片。

## 规则

- 不存原文全文和 PDF。PDF 放在仓库根目录的 `_private/`（已加入 .gitignore）。
- 每张卡片最多摘一两句原文，注明出处。
- 没读过原文的写 `verified: 摘要`；凭印象的一律写"待核实"或"待补"，不要编。
- 改完运行 `python3 scripts/build_index.py` 更新索引。
