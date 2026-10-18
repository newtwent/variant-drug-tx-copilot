"""Automatic first pass of the audit: identity, year and numeric-claim checks.
Usage: python3 -I kbverify.py <repo_root> <data_dir> > report.tsv   (also writes <data>/_report.json)"""
import csv
import difflib
import json
import re
import sys
from pathlib import Path

repo, data = Path(sys.argv[1]), Path(sys.argv[2])
with open(repo / "data" / "sources.csv", encoding="utf-8", newline="") as fh:
    rows = list(csv.DictReader(fh))


def norm_title(s):
    s = re.sub(r"\(.*?title.*?\)", " ", s or "", flags=re.I)
    s = s.replace("...", " ")
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def sim(a, b):
    a, b = norm_title(a), norm_title(b)
    if not a or not b:
        return 0.0
    if a in b or b in a:
        return 1.0
    return difflib.SequenceMatcher(None, a, b).ratio()


def meta_titles(m):
    out = []
    for k in ("crossref", "crossref_pii", "openalex", "europepmc", "arxiv", "biorxiv", "europepmc_pmc", "europepmc_title", "europepmc_extra", "openalex_title"):
        v = m.get(k) or {}
        if v.get("title"):
            out.append((k, v["title"]))
    return out


def meta_years(m):
    ys = {}
    cr = m.get("crossref") or {}
    if cr.get("year"):
        ys["crossref"] = str(cr["year"])
    for k in ("openalex", "openalex_title"):
        v = m.get(k) or {}
        if v.get("year"):
            ys[k] = str(v["year"])
    ep = m.get("europepmc") or m.get("europepmc_pmc") or m.get("europepmc_title") or {}
    if ep.get("year"):
        ys["europepmc"] = str(ep["year"])
    ar = m.get("arxiv") or {}
    if ar.get("published"):
        ys["arxiv_first"] = ar["published"][:4]
    bx = m.get("biorxiv") or {}
    if bx.get("date"):
        ys["biorxiv_first"] = bx["date"][:4]
    return ys


NUM = re.compile(r"(?<![\w.])\d[\d,]*(?:\.\d+)?")


def claim_numbers(s):
    """numbers in a claim that are worth checking (drop 1-2 digit ordinals)."""
    out = []
    for m in NUM.finditer(s):
        tok = m.group(0).rstrip(",")
        digits = tok.replace(",", "")
        if len(digits.replace(".", "")) <= 1:
            continue
        out.append(digits)
    return list(dict.fromkeys(out))


def text_forms(text):
    t = text.replace("−", "-").replace("–", "-").replace("—", "-")
    t = re.sub(r"(?<=\d),(?=\d{3}\b)", "", t)  # 1,319,138 -> 1319138
    return t.lower()


report = []
for r in rows:
    d = data / r["id"]
    rec = {"id": r["id"], "status": r["status"], "tier": r["tier"], "kind": r["kind"], "csv_year": r["year"],
           "title": r["title"][:80]}
    meta = json.loads((d / "meta.json").read_text(encoding="utf-8")) if (d / "meta.json").exists() else {}
    titles = meta_titles(meta)
    best = max(((sim(r["title"], t), k) for k, t in titles), default=(0.0, None))
    rec["title_sim"], rec["title_src"] = round(best[0], 2), best[1]
    ys = meta_years(meta)
    rec["meta_years"] = ys
    ft = d / "fulltext.txt"
    text = ft.read_text(encoding="utf-8", errors="replace") if ft.exists() else ""
    rec["fulltext_chars"] = len(text)
    abstracts = " ".join(str((meta.get(k) or {}).get("abstract") or "") for k in ("arxiv", "biorxiv", "europepmc", "europepmc_pmc", "europepmc_title", "europepmc_extra"))
    rec["abstract_chars"] = len(abstracts)
    corpus = text_forms(text + "\n" + abstracts)
    nums = claim_numbers(r["key_claim_en"])
    miss = [n for n in nums if n not in corpus]
    rec["claim_numbers"] = nums
    rec["missing_numbers"] = miss
    rec["sources_tried"] = (d / "tried.txt").read_text(encoding="utf-8").splitlines()[-6:] if (d / "tried.txt").exists() else []
    report.append(rec)

(data / "_report.json").write_text(json.dumps(report, indent=1, ensure_ascii=False), encoding="utf-8")
print("id\tstatus\ttier\tkind\tfulltext\tabstract\ttitle_sim\tcsv_year\tmeta_years\tmissing_numbers")
for x in report:
    print("\t".join(str(v) for v in (x["id"], x["status"], x["tier"], x["kind"], x["fulltext_chars"], x["abstract_chars"],
                                      x["title_sim"], x["csv_year"], ",".join(sorted(set(x["meta_years"].values()))),
                                      ",".join(x["missing_numbers"]))))
