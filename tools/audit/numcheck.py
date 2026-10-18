"""Independent check of the audit: every multi-digit number or decimal in the English key point of an active row must occur in
the text that was stored for that row (full text for tier T1; metadata, abstract and partial text for tiers T2 and T3).
Usage: python3 -I numcheck.py <repo_root> <scratch_dir>
<scratch_dir> holds audit_data/<ID>/ (stored texts, outside the repository) and, for rows added from the held list,
audit_data/_holds/<candidate>/ plus verdicts/S1.json.checked.json.added.json (candidate -> new ID).
Years 2010 to 2029 are skipped; thousands separators and spaces are ignored. Presence is necessary, not sufficient."""
import csv
import json
import re
import sys
from pathlib import Path

repo, scr = Path(sys.argv[1]), Path(sys.argv[2])
rows = list(csv.DictReader(open(repo / "data" / "sources.csv", encoding="utf-8")))
added_path = scr / "verdicts" / "S1.json.checked.json.added.json"
h_of = {v: k for k, v in json.loads(added_path.read_text(encoding="utf-8")).items()} if added_path.exists() else {}
NUM = re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})+|\d+\.\d+|\d{2,})(?![\w])")
strip = lambda s: re.sub(r"[,\s]", "", s)
total = missing = 0
report = []
for r in rows:
    if r["status"] != "active":
        continue
    d = scr / "audit_data" / r["id"]
    if r["tier"] == "T1":
        p = d / "fulltext.txt"
        if not p.exists() and r["id"] in h_of:
            p = scr / "audit_data" / "_holds" / h_of[r["id"]] / "fulltext.txt"
        blob = p.read_text(encoding="utf-8", errors="replace")
    else:
        blob = "".join(f.read_text(encoding="utf-8", errors="replace") for f in sorted(d.iterdir()) if f.name != "raw.html")
    flat = strip(blob)
    miss = []
    for m in NUM.finditer(r["key_claim_en"]):
        n = m.group(1)
        if re.fullmatch(r"20[12]\d", n):
            continue
        total += 1
        if strip(n) not in flat:
            miss.append(n)
    if miss:
        missing += len(miss)
        report.append((r["id"], r["tier"], miss))
print(f"numbers checked {total}; not found in the stored text {missing}; rows affected {len(report)}")
for item in report:
    print(*item)
