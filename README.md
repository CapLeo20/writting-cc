# writting-cc：经济学写作的经验与审美素材库

收集经济学、金融学写作的经验和风格样本，再把它们提炼成 Claude Code 可以直接使用的规则和模板。

> **GitHub 简介（About）建议填写**：经济学/金融学写作经验与风格素材库，为 Claude Code 提炼三类写作场景（日常回复、论文写作、agent 交接）的规则与模板。
>
> **Topics 建议**：`economics` `academic-writing` `claude-code` `writing-style` `chinese`

## 这个仓库解决什么问题

| 场景 | 读者 | 目标 | 当前可用 |
| --- | --- | --- | --- |
| 一、日常阅读学习时的回复 | 我自己 | 清楚、少格式、用常用术语 | 输出风格 `econ-plain-zh`（v0.1） |
| 二、论文学术写作 | 编辑、审稿人 | 准确之外有经济学叙事 | 素材库积累中 |
| 三、agent 之间的对话与交接 | 另一个 agent 或新会话 | 准确、可核对、省 token | 模板见 `library/patterns/agent-brief-handoff.md` |

目标期刊：《经济研究》《经济学动态》《数量经济技术经济研究》《财经研究》；International Review of Economics & Finance、Economic Analysis and Policy。

## 三层结构

```
来源（不入库）  →  素材库 library/  →  应用 .claude/
原文、PDF、书       经验与风格卡片       给 Claude Code 用的输出风格和 skill
```

1. **来源**：原文、书、网页。仓库只记出处和链接；PDF 放在 `_private/`，不提交。
2. **素材库**（`library/`）：从来源提炼的卡片，一个文件一张。素材库可以一直加，不会直接改变 Claude Code 的行为。
3. **应用**（`.claude/`）：从素材库提炼出的输出风格和 skill，每个文件注明依据的卡片。素材积累到一定程度，就"蒸馏"一次应用层。

这样分层的好处是：收集和使用分开。随手收录不会让 Claude 的行为变得不稳定；应用层每次改动都能追溯到依据。

## 目录

```
writting-cc/
├── README.md                 本文件
├── CLAUDE.md                 Claude 维护本仓库的规则
├── library/                  素材库（经验与审美积累）
│   ├── README.md             分类说明
│   ├── INDEX.md              自动生成的总目录
│   ├── STYLE-DIMENSIONS.md   拆解风格时的观察维度
│   ├── guides/               写作指南：econ/ finance/ general/ zh/ agents/
│   ├── scholars/             学者档案
│   ├── journals/             期刊档案
│   ├── papers/               范文拆解（_candidates.md 是候选清单）
│   ├── patterns/             跨来源归纳的写法
│   └── anti-patterns/        要避免的写法
├── glossary/                 术语表（范里安、罗默、伍德里奇译名）
├── templates/                新建卡片时复制的模板
├── .claude/
│   └── output-styles/        场景一：econ-plain-zh.md
├── research/                 调研报告
├── scripts/build_index.py    校验卡片、生成索引
└── _private/                 本地 PDF（不提交）
```

## 素材怎么分类

一张卡片只放在一个目录里（按**类型**），其他维度用卡片开头的元数据当标签：

- **类型**（目录）：写作指南、学者、期刊、范文、写法、反面模式
- **场景**：1 日常回复、2 论文写作、3 agent 交接
- **论文部位**：标题、摘要、引言、文献、制度背景、假说、识别、结果、机制、稳健性、结论……
- **领域与语言**：finance、metrics、china……；zh、en
- **核实程度**：原文 / 摘要 / 待核实 / 判断

详见 [library/README.md](library/README.md)，完整目录见 [library/INDEX.md](library/INDEX.md)。

## 怎么添加素材

最简单的方式是直接告诉 Claude，例如：

- "把 Cochrane 的写作指南收录进素材库"
- "拆解 `_private/wang2020.pdf` 的引言，建一张范文卡片"
- "把《经济研究》这几篇范文的观察汇总到期刊档案"

Claude 会按 [CLAUDE.md](CLAUDE.md) 里的流程做。手动添加的步骤：

1. 从 `templates/` 复制对应模板到 `library/` 的相应目录；
2. 填写元数据和正文；
3. 运行 `python3 scripts/build_index.py` 校验并更新索引；
4. 提交。

## 怎么使用场景一的输出风格

在本仓库里打开 Claude Code，输入 `/output-style econ-plain-zh`。

想在所有项目里使用，把文件复制到用户目录：

```bash
mkdir -p ~/.claude/output-styles
cp .claude/output-styles/econ-plain-zh.md ~/.claude/output-styles/
```

## 路线图

- [x] 调研三类场景的现有资源（`research/01`）
- [x] 调研同类仓库（`research/02`）
- [x] 搭建素材库结构、模板和索引脚本
- [x] 术语表 v0.1
- [x] 场景一输出风格 v0.1
- [ ] 拆解目标期刊范文（每刊 3–5 篇）
- [ ] 核对术语表与三本教材中译本
- [ ] 场景二 skill：`econ-write-zh`（以 hanlulong/econ-writing-skill 为骨架，按中文期刊改写）
- [ ] 场景三 skill：`brief` 和 `handoff`

## 相关项目

- [hanlulong/econ-writing-skill](https://github.com/hanlulong/econ-writing-skill)：英文经济学写作 skill，综合 50 多份指南
- [brycewang-stanford/Awesome-Journal-Skills](https://github.com/brycewang-stanford/Awesome-Journal-Skills)：按期刊定制的投稿 skill，含《经济研究》《数技经》等，附官方来源核查表
- 更多见 [research/02-同类仓库调研.md](research/02-同类仓库调研.md)

## 版权

卡片是读书笔记性质的转述和评论。不收录论文和书籍全文；每张卡片最多摘一两句原文并注明出处。
