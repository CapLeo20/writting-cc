#!/usr/bin/env python3
"""按场景一的表述规则给回复计数。

用法：python3 evals/scenario1/lint_reply.py evals/scenario1/out/*.md
文件名形如 q1-cc.md，会按条件汇总。只统计形式，不判断内容对错。
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

BANNED = r"不(仅|只|是)[^。！？\n]{0,25}(而是|更是)|值得(注意|一提)|深入(探讨|分析)|赋能|(重要|深远)的?(意义|价值)|希望(这|以上|对你)|总之|综上所述|总的来说|让我们"
STEM = r"鲁棒|实验组|因变量|自变量|仿真"
ENDING = r"^(需要你决定|下一步)"


def paragraphs(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    blocks = [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip()]
    # 只把普通文字段落算作段落：去掉标题、列表、表格、引用块
    return [b for b in blocks if not re.match(r"(#|[-*+] |\d+[.)、] |\||>)", b)]


def analyze(text):
    lines = text.splitlines()
    plain = re.sub(r"```.*?```", "", text, flags=re.S)
    sents = [s for s in re.split(r"[。！？；\n]", re.sub(r"[#*>|`]", "", plain)) if len(s.strip()) >= 4]
    lens = [len(re.sub(r"\s", "", s)) for s in sents]
    paras = [len(re.sub(r"\s", "", p)) for p in paragraphs(text)]
    first = next((l.strip() for l in lines if l.strip()), "")
    last = next((l.strip() for l in reversed(lines) if l.strip()), "")
    return {
        "汉字": len(re.findall(r"[一-鿿]", text)),
        "首行是标题": int(bool(re.match(r"(#|\*\*[^*]+\*\*\s*$)", first))),
        "标题": sum(1 for l in lines if re.match(r"\s*#{1,6}\s", l)),
        "加粗行": sum(1 for l in lines if re.match(r"\s*\*\*[^*]+\*\*[。：:]?\s*$", l)),
        "列表行": sum(1 for l in lines if re.match(r"\s*([-*+]|\d+[.)、])\s", l)),
        "加粗": text.count("**") // 2,
        "表格行": sum(1 for l in lines if l.strip().startswith("|")),
        "LaTeX": len(re.findall(r"\$[^$\n]+\$|\\\(|\\\[", text)),
        "平均句长": round(sum(lens) / len(lens), 1) if lens else 0,
        ">40字句": sum(1 for n in lens if n > 40),
        "最长段": max(paras) if paras else 0,
        "套话": len(re.findall(BANNED, text)),
        "理工科用语": len(re.findall(STEM, text)),
        "结尾决定段": int(bool(re.match(ENDING, last.lstrip("*")))),
    }


def main(paths):
    keys = None
    by_cond = defaultdict(list)
    rows = []
    for p in sorted(paths):
        r = analyze(Path(p).read_text(encoding="utf-8"))
        keys = keys or list(r)
        name = Path(p).stem
        rows.append((name, r))
        by_cond[name.split("-", 1)[-1]].append(r)
    print("| 文件 | " + " | ".join(keys) + " |")
    print("|" + " --- |" * (len(keys) + 1))
    for name, r in rows:
        print(f"| {name} | " + " | ".join(str(r[k]) for k in keys) + " |")
    print()
    print("按条件合计（平均句长取平均，最长段取最大）：")
    print("| 条件 | " + " | ".join(keys) + " |")
    print("|" + " --- |" * (len(keys) + 1))
    for cond, rs in by_cond.items():
        agg = {}
        for k in keys:
            vals = [r[k] for r in rs]
            agg[k] = round(sum(vals) / len(vals), 1) if k == "平均句长" else (max(vals) if k == "最长段" else sum(vals))
        print(f"| {cond}（{len(rs)} 题） | " + " | ".join(str(agg[k]) for k in keys) + " |")


if __name__ == "__main__":
    main(sys.argv[1:])
