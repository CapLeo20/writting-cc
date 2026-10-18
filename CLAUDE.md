# 本仓库的维护规则

这是一个经济学写作的经验与风格素材库。三层结构：来源（不入库）→ `library/` 素材卡片 → `.claude/` 应用（输出风格、skill）。用户是从理工科转到经济学的博士生，主要用中文写作。

## 写作风格

本仓库所有文字按 `.claude/output-styles/econ-plain-zh.md` 的要求写：先给结论、常用词、短句、少格式。术语用 `glossary/econ-fin-terms.md` 的译名。提到任何人时用名字或"作者"，不要凭名字推断性别代词。

## 新增卡片

1. 判断类型：写作指南 guide、学者 scholar、期刊 journal、范文 paper、写法 pattern、反面模式 anti-pattern。
2. 复制 `templates/` 下的模板到 `library/<类型目录>/`。guide 再按来源放进 `econ/ finance/ general/ zh/ agents/`。
3. 文件名用小写英文和连字符；`id` 以类型开头，例如 `guide-cochrane-2005-writing-tips`、`journal-jjyj`、`paper-wang-2020-robots`。
4. 元数据只用扁平的 `key: value`，列表写成 `[a, b]`。取值范围见 `scripts/build_index.py` 顶部。
5. 运行 `python3 scripts/build_index.py`，确认没有错误、索引已更新。

## 核实与诚实

- `verified` 如实填写：读过原文写"原文"；只看到检索摘要或别人转述写"摘要"；没有依据写"待核实"；自己的归纳写"判断"。
- 正文里没有出处的说法，标"待核实"或写进"待补"，不要编。不确定的期号、页码、年份写"待核"。
- 范文卡片必须写明期刊归属在哪里核实过。不要把《管理世界》《中国工业经济》的论文记成《经济研究》（见 `library/journals/jjyj.md` 的避坑表）。
- 转引其他仓库（如 Awesome-Journal-Skills）的事实时注明转引和对方的核查日期。

## 版权

- 不提交论文、书籍全文和 PDF。PDF 放在 `_private/`（已在 .gitignore 中）。
- 每张卡片最多摘一两句原文，注明页码或段落。其余用自己的话转述。

## 拆解范文

- 按 `library/STYLE-DIMENSIONS.md` 的维度观察，重点是引言的逐段"动作序列"。
- 只写从原文看得到的东西。观察汇总到对应的 scholar 和 journal 卡片时，注明来自哪张 paper 卡片。

## 修改应用层（.claude/ 和 web/）

- 先改素材卡片（通常是 pattern 卡片），再把变化同步到 `.claude/` 和 `web/` 下的文件，并在文件开头的注释里列出依据的卡片 id。
- 场景一的规则只管表述方式，不规定回答内容（用户 2026-10-18 的要求）。依据卡片是 `library/patterns/reply-presentation.md`；Claude Code 版和网页版要同步修改。
- 改了场景一的规则后，运行 `bash evals/scenario1/run.sh` 重测，把结果更新到 `evals/scenario1/RESULTS.md`。
- 输出风格要短；skill 的 SKILL.md 控制在 500 行以内，细节放进同目录的参考文件。
- 用正面的说法写规则（"用段落写"），少用禁止句。

## 提交前

- `python3 scripts/build_index.py --check` 必须通过（CI 也会跑）。
