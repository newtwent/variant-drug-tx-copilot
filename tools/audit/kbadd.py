"""Append accepted screening verdicts as new rows of data/sources.csv (IDs are never reused: retired rows count).
Usage: python3 -I kbadd.py <repo_root> <date> <qtag> <holds_rows.json> <verdict.checked.json> [more.json ...] [--dry]
Only verdicts with keep_rec == keep and an empty duplicate_of are added; the mapping candidate -> new ID is printed and
written to <first verdict>.added.json."""
import csv
import json
import re
import sys
from pathlib import Path

repo, today, qtag, holds_path = Path(sys.argv[1]), sys.argv[2], sys.argv[3], Path(sys.argv[4])
dry = "--dry" in sys.argv
paths = [Path(a) for a in sys.argv[5:] if not a.startswith("--")]
CJK = re.compile(r"[㐀-䶿一-鿿]")
CATS = ("GV", "GD", "DS", "KB", "MD", "WM", "EV")
KINDS = {"journal", "preprint", "org-page", "repo", "NA", "proceedings", "news", "blog", "social", "talk"}
RELS = {"mechanism", "modeling", "data", "evaluation", "prior", "context"}

csv_path = repo / "data" / "sources.csv"
with open(csv_path, encoding="utf-8", newline="") as fh:
    rd = csv.DictReader(fh)
    fields, rows = rd.fieldnames, list(rd)
used = {r["url"] for r in rows}
nxt = {c: max(int(r["id"][2:]) for r in rows if r["id"].startswith(c)) + 1 for c in CATS}
held = {r["id"]: r for r in json.loads(holds_path.read_text(encoding="utf-8"))}
added = {}
for p in paths:
    for o in json.loads(p.read_text(encoding="utf-8")):
        if o.get("keep_rec") != "keep" or o.get("duplicate_of"):
            continue
        assert o.get("_issues", []) == [], (o["id"], o["_issues"])
        cat = o["category_rec"]
        assert cat in CATS and o["kind_rec"] in KINDS and o["relevance_rec"] in RELS, o["id"]
        url = o.get("url_rec") or held[o["id"]]["url"]
        if url in used:
            print("skip duplicate url", o["id"], url)
            continue
        for k in ("new_key_claim", "new_so_what", "new_caveat"):
            assert o[k + "_en"] != "NA" and CJK.search(o[k + "_zh"]) and not CJK.search(o[k + "_en"]), (o["id"], k)
        rid = f"{cat}{nxt[cat]:02d}"
        nxt[cat] += 1
        q = [held[o["id"]]["query"], qtag]
        row = {"id": rid, "title": o["title_rec"], "url": url, "url_alt": "NA", "year": str(o["year_rec"]), "kind": o["kind_rec"],
               "category": cat, "track": o["track_rec"], "variant_class": o["variant_class_rec"], "relevance": o["relevance_rec"],
               "tier": o["tier_rec"], "verified": "Y" if o["tier_rec"] == "T1" else "N",
               "key_claim_en": o["new_key_claim_en"], "key_claim_zh": o["new_key_claim_zh"],
               "so_what_en": o["new_so_what_en"], "so_what_zh": o["new_so_what_zh"],
               "caveat_en": o["new_caveat_en"], "caveat_zh": o["new_caveat_zh"],
               "accessed": today, "query_id": "; ".join(q), "status": "active"}
        assert list(row) == fields, (list(row), fields)
        rows.append(row)
        used.add(url)
        added[o["id"]] = rid
        print(o["id"], "->", rid, o["title_rec"][:80])
if not dry and added:
    with open(csv_path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(rows)
    Path(str(paths[0]) + ".added.json").write_text(json.dumps(added, indent=1), encoding="utf-8")
print(len(added), "rows added" + (" (dry run)" if dry else ""))
