"""Apply reviewed audit verdicts to data/sources.csv.
Usage: python3 -I kbapply.py <repo_root> <verdicts.json> <YYYY-MM-DD> [--qtext Q134] [--qrepo Q135] [--dry]
A verdict may carry "_skip": true (not applied) and "_override": {field: value} (applied last)."""
import csv
import json
import re
import sys
from pathlib import Path

repo, vpath, today = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
args = sys.argv[4:]
opt = {a: args[i + 1] for i, a in enumerate(args) if a.startswith("--q") and i + 1 < len(args)}
dry = "--dry" in args
CJK = re.compile(r"[㐀-䶿一-鿿]")
KINDS = {"journal", "preprint", "org-page", "repo", "NA", "proceedings", "news", "blog", "social", "talk"}

csv_path = repo / "data" / "sources.csv"
with open(csv_path, encoding="utf-8", newline="") as fh:
    rd = csv.DictReader(fh)
    fields = rd.fieldnames
    rows = list(rd)
byid = {r["id"]: r for r in rows}
verdicts = json.loads(vpath.read_text(encoding="utf-8"))
log = []


def setf(r, key, val):
    if r[key] != val:
        log.append((r["id"], key, r[key][:70], val[:70]))
        r[key] = val


for o in verdicts:
    if o.get("_skip"):
        continue
    r = byid.get(o["id"])
    if r is None:
        print("unknown id", o["id"])
        continue
    new = {k: o.get(k) for k in ("new_key_claim_en", "new_key_claim_zh", "new_so_what_en", "new_so_what_zh")}
    for en, zh, ek, zk in (("new_key_claim_en", "new_key_claim_zh", "key_claim_en", "key_claim_zh"),
                           ("new_so_what_en", "new_so_what_zh", "so_what_en", "so_what_zh")):
        if new[en] and new[zh] and new[en] != "NA":
            assert CJK.search(new[zh]) and not CJK.search(new[en]), (o["id"], ek)
            setf(r, ek, new[en])
            setf(r, zk, new[zh])
    if o.get("new_caveat_en_changed") and o.get("new_caveat_en") and o.get("new_caveat_zh"):
        assert CJK.search(o["new_caveat_zh"]) and not CJK.search(o["new_caveat_en"]), (o["id"], "caveat")
        retire_en = re.search(r"Retired \d{4}-\d{2}-\d{2} \(R\d\):.*$", r["caveat_en"])
        retire_zh = re.search(r"已于 \d{4}-\d{2}-\d{2} 退役（R\d）：.*$", r["caveat_zh"])
        cav_en, cav_zh = o["new_caveat_en"], o["new_caveat_zh"]
        if retire_en and retire_zh:
            cav_en, cav_zh = cav_en + " " + retire_en.group(0), cav_zh + " " + retire_zh.group(0)
        setf(r, "caveat_en", cav_en)
        setf(r, "caveat_zh", cav_zh)
    tier = o.get("tier_rec")
    if tier in ("T1", "T2", "T3"):
        setf(r, "tier", tier)
        setf(r, "verified", "Y" if tier == "T1" else "N")
        if tier == "T1":
            setf(r, "accessed", today)
    tr = (o.get("title_rec") or "").strip()
    if tr and tr != r["title"] and not CJK.search(tr) and len(tr) > 8:
        setf(r, "title", tr)
    if re.fullmatch(r"\d{4}", str(o.get("year_rec", ""))):
        setf(r, "year", str(o["year_rec"]))
    if o.get("kind_rec") in KINDS:
        setf(r, "kind", o["kind_rec"])
    if o.get("keep_rec") == "retire" and r["status"] != "retired":
        why_en, why_zh = o.get("keep_reason", "").rstrip(". "), o.get("keep_reason_zh", "").rstrip("。 ")
        assert why_en and why_zh and CJK.search(why_zh), (o["id"], "retire reason")
        setf(r, "status", "retired")
        setf(r, "caveat_en", (r["caveat_en"].rstrip() + f" Retired {today} (R7): {why_en}.").strip())
        setf(r, "caveat_zh", (r["caveat_zh"].rstrip() + f" 已于 {today} 退役（R7）：{why_zh}。").strip())
    if o.get("reading_depth") in ("full text", "page") and opt.get("--qtext"):
        q = r["query_id"].split("; ") if r["query_id"] != "NA" else []
        tag = opt["--qrepo"] if (r["kind"] == "repo" and opt.get("--qrepo")) else opt["--qtext"]
        if tag not in q:
            setf(r, "query_id", "; ".join(q + [tag]))
    for k, v in (o.get("_override") or {}).items():
        setf(r, k, v)

print(len(log), "field changes in", len({x[0] for x in log}), "rows")
if not dry:
    with open(csv_path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(rows)
    Path(str(vpath) + ".applied.log").write_text("\n".join("\t".join(x) for x in log), encoding="utf-8")
    print("written")
