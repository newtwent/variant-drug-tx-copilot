"""Group the active rows into audit batches (by category, about 20 rows each) and print their IDs.
Usage: python3 -I make_batches.py <repo_root> <size>"""
import csv
import sys
from pathlib import Path

repo, size = Path(sys.argv[1]), int(sys.argv[2])
with open(repo / "data" / "sources.csv", encoding="utf-8", newline="") as fh:
    rows = [r for r in csv.DictReader(fh) if r["status"] == "active"]
by_cat = {}
for r in rows:
    by_cat.setdefault(r["category"], []).append(r["id"])
batches = []
for cat in ("GV", "GD", "DS", "KB", "MD", "WM", "EV"):
    ids = by_cat.get(cat, [])
    n = max(1, round(len(ids) / size))
    step = -(-len(ids) // n)
    for i in range(n):
        chunk = ids[i * step:(i + 1) * step]
        if chunk:
            batches.append((f"{cat}{i + 1}", chunk))
for name, chunk in batches:
    print(name, len(chunk), ",".join(chunk))
print("total rows", sum(len(c) for _, c in batches), "batches", len(batches))
