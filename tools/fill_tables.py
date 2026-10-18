"""Regenerate the tables that sit between marker comments in the documents, from data/*.csv.
Usage: python3 -I tools/fill_tables.py [repo_root]
  <!-- source-index:XX:start --> ... <!-- source-index:XX:end -->  active rows of category XX in documents 01 to 07
  <!-- dataset-table:start -->  ... <!-- dataset-table:end -->      data/datasets.csv in document 03
  <!-- questions-attention:start/end -->, <!-- questions-optional:start/end -->, <!-- questions-register:start/end -->
      data/questions.csv in document 10 (paragraph pairs for the questions, a table for the answer register)"""
import csv
import sys
from pathlib import Path

repo = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
DOCS = {"GV": "01-genetic-variation-layer.md", "GD": "02-genotype-x-drug-evidence.md", "DS": "03-data-resources.md",
        "KB": "04-prior-knowledge-bases.md", "MD": "05-perturbation-models.md", "WM": "06-world-models.md",
        "EV": "07-evaluation-and-pitfalls.md"}


def esc(s):
    return s.replace("|", "\\|").replace("\n", " ")


def dash(s):
    return "\u2014" if s in ("", "NA") else s


def replace_block(text, name, body):
    start, end = f"<!-- {name}:start -->", f"<!-- {name}:end -->"
    i, j = text.index(start), text.index(end)
    return text[: i + len(start)] + "\n" + body + "\n" + text[j:]


with open(repo / "data" / "sources.csv", encoding="utf-8", newline="") as fh:
    src = list(csv.DictReader(fh))
for cat, fname in DOCS.items():
    rows = ["| ID | Tier | Source | So what | \u610f\u4e49\uff08\u4e2d\u6587\uff09 |", "|---|---|---|---|---|"]
    sel = [r for r in src if r["category"] == cat and r["status"] == "active"]
    for r in sel:
        rows.append(f"| {r['id']} | {r['tier']} | [{esc(r['title'])}](<{r['url']}>) | {esc(dash(r['so_what_en']))} | "
                    f"{esc(dash(r['so_what_zh']))} |")
    p = repo / "docs" / fname
    p.write_text(replace_block(p.read_text(encoding="utf-8"), f"source-index:{cat}", "\n".join(rows)), encoding="utf-8")
    print(cat, len(sel), "active rows ->", fname)

with open(repo / "data" / "datasets.csv", encoding="utf-8", newline="") as fh:
    ds = list(csv.DictReader(fh))
out = ["| Dataset | Scale | \u89c4\u6a21\uff08\u4e2d\u6587\uff09 | Genotype information | \u57fa\u56e0\u578b\u4fe1\u606f\uff08\u4e2d\u6587\uff09 | Sources | Caveats | \u6ce8\u610f\u4e8b\u9879\uff08\u4e2d\u6587\uff09 |",
       "|---|---|---|---|---|---|---|---|"]
for r in ds:
    cells = [esc(dash(r[k])) for k in ("name", "scale_reported_en", "scale_reported_zh", "genotype_info_en",
                                       "genotype_info_zh", "source_id", "caveats_en", "caveats_zh")]
    cells[5] = cells[5].replace(";", ", ")
    out.append("| " + " | ".join(cells) + " |")
p = repo / "docs" / "03-data-resources.md"
p.write_text(replace_block(p.read_text(encoding="utf-8"), "dataset-table", "\n".join(out)), encoding="utf-8")
print("datasets", len(ds))

# ---- document 10: open questions --------------------------------------------------------------
qpath, qdoc = repo / "data" / "questions.csv", repo / "docs" / "10-open-questions.md"
if qpath.exists() and qdoc.exists():
    with open(qpath, encoding="utf-8", newline="") as fh:
        qs = list(csv.DictReader(fh))
    TYPE_ZH = {"decision": "\u51b3\u7b56", "missing-information": "\u7f3a\u5931\u4fe1\u606f", "attention": "\u5173\u6ce8\u4e8b\u9879"}
    PRIO_EN = {"needs-your-attention": "needs your attention", "optional": "optional"}
    PRIO_ZH = {"needs-your-attention": "\u9700\u8981\u4f60\u5173\u6ce8", "optional": "\u53ef\u9009"}

    def pair(r):
        en = (f"**{r['id']}** ({r['type']}; {PRIO_EN[r['priority']]}; status: {r['status']}). {r['question_en']} "
              f"Why: {r['why_en']} Default: {r['default_en']} If the answer differs: {r['if_changed_en']} Affects: {r['affects']}.")
        zh = (f"> **{r['id']}**\uff08{TYPE_ZH[r['type']]}\uff1b{PRIO_ZH[r['priority']]}\uff1b\u72b6\u6001\uff1a{r['status']}\uff09\u3002"
              f"{r['question_zh']} \u539f\u56e0\uff1a{r['why_zh']} \u9ed8\u8ba4\u503c\uff1a{r['default_zh']} "
              f"\u82e5\u7b54\u6848\u4e0d\u540c\uff1a{r['if_changed_zh']} \u5f71\u54cd\u8303\u56f4\uff1a{r['affects']}\u3002")
        return en + "\n\n" + zh

    text = qdoc.read_text(encoding="utf-8")
    first = [r for r in qs if r["priority"] == "needs-your-attention"]
    rest = [r for r in qs if r["priority"] != "needs-your-attention"]
    text = replace_block(text, "questions-attention", "\n" + "\n\n".join(pair(r) for r in first) + "\n")
    text = replace_block(text, "questions-optional", "\n" + "\n\n".join(pair(r) for r in rest) + "\n")
    reg = ["| ID | Type | Priority | Status | Answer | Answered on | Applied on |", "|---|---|---|---|---|---|---|"]
    for r in qs:
        reg.append("| " + " | ".join(esc(dash(x)) for x in (r["id"], r["type"], r["priority"], r["status"], r["answer"],
                                                               r["answered_on"], r["applied_on"])) + " |")
    text = replace_block(text, "questions-register", "\n".join(reg))
    qdoc.write_text(text, encoding="utf-8")
    print("questions", len(qs), f"({len(first)} need attention)")
