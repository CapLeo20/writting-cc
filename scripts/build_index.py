#!/usr/bin/env python3
"""扫描 library/ 下所有卡片的元数据，校验格式并生成 library/INDEX.md。

用法：
    python3 scripts/build_index.py          # 校验并重写 INDEX.md
    python3 scripts/build_index.py --check  # 只校验；INDEX.md 过期或有错误时返回非零

只用标准库。元数据写在文件开头两行 --- 之间，只支持扁平的 key: value，
列表写成 [a, b, c]。
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIBRARY = ROOT / "library"
INDEX = LIBRARY / "INDEX.md"

TYPE_DIRS = {
    "guide": "guides",
    "scholar": "scholars",
    "journal": "journals",
    "paper": "papers",
    "pattern": "patterns",
    "anti-pattern": "anti-patterns",
}
TYPE_NAMES = {
    "guide": "写作指南",
    "scholar": "学者档案",
    "journal": "期刊档案",
    "paper": "范文拆解",
    "pattern": "写法提炼",
    "anti-pattern": "反面模式",
}
SCENARIOS = {"1": "日常回复", "2": "论文写作", "3": "agent 交接"}
SECTIONS = {
    "whole": "全文结构",
    "title": "标题",
    "abstract": "摘要",
    "intro": "引言",
    "lit": "文献综述",
    "background": "制度背景",
    "hypothesis": "理论与假说",
    "data": "数据",
    "identification": "识别策略",
    "results": "结果报告",
    "mechanism": "机制",
    "robustness": "稳健性",
    "conclusion": "结论与政策含义",
    "tables": "图表",
    "response": "回复审稿",
    "sentence": "句子与用词",
}
VERIFIED = ["原文", "摘要", "待核实", "判断"]
STATUS = ["初稿", "完善", "待补"]
LANGS = ["zh", "en"]
REQUIRED = ["id", "type", "title", "lang", "scenarios", "verified", "added", "status"]
LIST_KEYS = {"scenarios", "sections", "fields"}


def parse_front_matter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    meta = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return meta
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"无法解析的元数据行：{line!r}")
        key, value = line.split(":", 1)
        value = value.split(" #", 1)[0].strip()
        key = key.strip()
        if key in LIST_KEYS:
            value = value.strip("[]")
            meta[key] = [v.strip() for v in value.split(",") if v.strip()]
        else:
            meta[key] = value.strip('"')
    raise ValueError("元数据缺少结束的 ---")


def load_cards():
    cards, errors = [], []
    for path in sorted(LIBRARY.rglob("*.md")):
        rel = path.relative_to(ROOT)
        # 跳过说明类文件：大写文件名（README、INDEX、STYLE-DIMENSIONS）和下划线开头的清单
        if path.name.startswith("_") or path.stem.isupper():
            continue
        try:
            meta = parse_front_matter(path.read_text(encoding="utf-8"))
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue
        if meta is None:
            errors.append(f"{rel}: 缺少元数据（文件应以 --- 开头）")
            continue
        missing = [k for k in REQUIRED if not meta.get(k)]
        if missing:
            errors.append(f"{rel}: 缺少必填字段 {', '.join(missing)}")
            continue
        ctype = meta["type"]
        if ctype not in TYPE_DIRS:
            errors.append(f"{rel}: type={ctype} 不在 {list(TYPE_DIRS)} 中")
            continue
        top_dir = rel.parts[1] if len(rel.parts) > 2 else ""
        if top_dir != TYPE_DIRS[ctype]:
            errors.append(f"{rel}: type={ctype} 的卡片应放在 library/{TYPE_DIRS[ctype]}/")
        if not meta["id"].startswith(ctype + "-"):
            errors.append(f"{rel}: id 应以 '{ctype}-' 开头")
        if meta["lang"] not in LANGS:
            errors.append(f"{rel}: lang={meta['lang']} 应为 {LANGS}")
        bad = [s for s in meta["scenarios"] if s not in SCENARIOS]
        if bad:
            errors.append(f"{rel}: scenarios 只能取 1/2/3，发现 {bad}")
        bad = [s for s in meta.get("sections", []) if s not in SECTIONS]
        if bad:
            errors.append(f"{rel}: sections 取值不在列表中：{bad}")
        if meta["verified"] not in VERIFIED:
            errors.append(f"{rel}: verified 应为 {VERIFIED}")
        if meta["status"] not in STATUS:
            errors.append(f"{rel}: status 应为 {STATUS}")
        meta["path"] = rel
        cards.append(meta)
    seen = {}
    for card in cards:
        if card["id"] in seen:
            errors.append(f"id 重复：{card['id']}（{seen[card['id']]} 与 {card['path']}）")
        seen[card["id"]] = card["path"]
    return cards, errors


def link(card):
    return f"[{card['title']}]({card['path'].relative_to('library').as_posix()})"


def render(cards):
    out = [
        "# 素材库索引",
        "",
        "> 本文件由 `python3 scripts/build_index.py` 自动生成，请勿手工编辑。",
        "",
        f"共 {len(cards)} 张卡片。",
        "",
        "| 类型 | 数量 |",
        "| --- | --- |",
    ]
    for ctype, name in TYPE_NAMES.items():
        n = sum(1 for c in cards if c["type"] == ctype)
        out.append(f"| {name}（{TYPE_DIRS[ctype]}/） | {n} |")
    out.append("")

    for ctype, name in TYPE_NAMES.items():
        group = [c for c in cards if c["type"] == ctype]
        if not group:
            continue
        out += [f"## {name}", "", "| 卡片 | 作者/机构 | 年份 | 语言 | 场景 | 核实 | 状态 |", "| --- | --- | --- | --- | --- | --- | --- |"]
        for c in sorted(group, key=lambda c: c["id"]):
            scen = "、".join(SCENARIOS[s] for s in c["scenarios"] if s in SCENARIOS)
            out.append(
                f"| {link(c)} | {c.get('author', '')} | {c.get('year', '')} | {c['lang']} | {scen} | {c['verified']} | {c['status']} |"
            )
        out.append("")

    out += ["## 按场景查找", ""]
    for key, name in SCENARIOS.items():
        group = [c for c in cards if key in c["scenarios"]]
        out.append(f"**{key}. {name}**（{len(group)}）：" + "；".join(link(c) for c in sorted(group, key=lambda c: c["id"])))
        out.append("")

    out += ["## 按论文部位查找", ""]
    for key, name in SECTIONS.items():
        group = [c for c in cards if key in c.get("sections", [])]
        if group:
            out.append(f"**{name}**（{len(group)}）：" + "；".join(link(c) for c in sorted(group, key=lambda c: c["id"])))
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def main():
    check_only = "--check" in sys.argv[1:]
    cards, errors = load_cards()
    for err in errors:
        print("错误：" + err)
    content = render(cards)
    current = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
    if check_only:
        if content != current:
            print("错误：library/INDEX.md 不是最新，请运行 python3 scripts/build_index.py")
            errors.append("index")
        print(f"检查完成：{len(cards)} 张卡片，{len(errors)} 个问题。")
        return 1 if errors else 0
    if content != current:
        INDEX.write_text(content, encoding="utf-8")
        print(f"已更新 library/INDEX.md（{len(cards)} 张卡片）。")
    else:
        print(f"library/INDEX.md 已是最新（{len(cards)} 张卡片）。")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
