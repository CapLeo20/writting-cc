#!/bin/bash
# 用同一组问题，比较三种条件下 Claude 的回复：
#   base：不加任何规则
#   cc  ：Claude Code 输出风格 .claude/output-styles/econ-plain-zh.md
#   web ：网页版文字 web/claude-ai-instructions.md（用 --append-system-prompt 模拟）
# 用法：bash evals/scenario1/run.sh [条件...]   默认三种都跑
# 结果写到 evals/scenario1/out/，再运行 lint_reply.py 统计。
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
OUT="$HERE/out"
WORK="$(mktemp -d)"
mkdir -p "$OUT"
CONDS=("${@:-base cc web}")
read -r -a CONDS <<< "${CONDS[*]}"

# 每种条件一个干净的工作目录，避免读到本仓库的 CLAUDE.md
mkdir -p "$WORK/base" "$WORK/web" "$WORK/cc/.claude/output-styles"
cp "$ROOT/.claude/output-styles/econ-plain-zh.md" "$WORK/cc/.claude/output-styles/"
echo '{"outputStyle": "econ-plain-zh"}' > "$WORK/cc/.claude/settings.json"
# 网页版文字取 "粘贴内容" 下代码块里的部分
WEB_TEXT="$(awk '/^## 粘贴内容/{f=1;next} f&&/^```/{n++;next} f&&n==1{print}' "$ROOT/web/claude-ai-instructions.md")"

mapfile -t LINES < "$HERE/prompts.tsv"
for line in "${LINES[@]}"; do
  id="${line%%$'\t'*}"; q="${line#*$'\t'}"
  for cond in "${CONDS[@]}"; do
    extra=()
    [ "$cond" = web ] && extra=(--append-system-prompt "$WEB_TEXT")
    # --tools "" 关掉工具；< /dev/null 防止 claude 把标准输入里的其他题目读进去
    ( cd "$WORK/$cond" && timeout 400 claude -p "$q" --output-format text --tools "" \
        --permission-mode dontAsk "${extra[@]}" < /dev/null > "$OUT/$id-$cond.md" 2> "$OUT/$id-$cond.err" ) &
  done
done
wait
rm -rf "$WORK"
echo "完成。统计：python3 $HERE/lint_reply.py $OUT/*.md"
