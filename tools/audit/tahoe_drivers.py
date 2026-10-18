"""Count driver genes, variants and lineage-matched contrasts over the Tahoe-100M panel lines (page DS07, query Q137).
Usage: python3 -I tahoe_drivers.py <libs_dir_with_pyarrow> <work_dir>
<work_dir> holds tahoe_obs_counts.json (output of tahoe_obs_counts.py) and tahoe_meta/cell_line_metadata.parquet
(the metadata table of the dataset, downloaded in full); tahoe_panel.json is written there."""
import collections
import json
import sys

sys.path.insert(0, sys.argv[1])
import pyarrow.parquet as pq

base = sys.argv[2]
counts = json.load(open(base + "/tahoe_obs_counts.json"))
per_line = collections.Counter()
for k, v in counts["cell_name_pass"].items():
    name, flt = k.rsplit("|", 1)
    per_line[(name, flt)] += v
filters = sorted({k[1] for k in per_line})
print("filter values", filters, {f: sum(v for (n, fl), v in per_line.items() if fl == f) for f in filters})
passing = {n for (n, fl), v in per_line.items() if fl in ("full", "pass", "True", "true") and v > 0}
print("lines (any status):", len({n for (n, _f) in per_line}), "lines with passing cells:", len(passing))
cells_by_line = collections.Counter()
for (n, fl), v in per_line.items():
    if fl in ("full", "pass", "True", "true"):
        cells_by_line[n] += v
vals = sorted(cells_by_line.values())
print("cells per passing line: min %d median %d max %d" % (vals[0], vals[len(vals) // 2], vals[-1]))
print("smallest", sorted(cells_by_line.items(), key=lambda kv: kv[1])[:5])
meta = pq.read_table(base + "/tahoe_meta/cell_line_metadata.parquet").to_pylist()
inpanel = [r for r in meta if r["cell_name"] in passing]
lines_meta = {r["cell_name"] for r in meta}
print("panel lines found in metadata:", len({r["cell_name"] for r in inpanel}), "of", len(passing), "missing:", sorted(passing - lines_meta)[:10])
g = collections.defaultdict(set)
for r in inpanel:
    if r["Driver_Gene_Symbol"]:
        g[r["Driver_Gene_Symbol"]].add(r["cell_name"])
top = sorted(g.items(), key=lambda kv: -len(kv[1]))[:25]
print("driver gene -> number of panel lines:", [(k, len(v)) for k, v in top])
org = collections.Counter()
seen = set()
for r in inpanel:
    if r["cell_name"] not in seen:
        seen.add(r["cell_name"]); org[r["Organ"]] += 1
print("organs", org.most_common())
# specific variants
var = collections.defaultdict(set)
for r in inpanel:
    if r["Driver_Gene_Symbol"] in ("TP53", "KRAS", "BRAF", "PIK3CA", "EGFR", "NRAS", "PTEN"):
        var[(r["Driver_Gene_Symbol"], r["Driver_ProtEffect_or_CdnaEffect"], r["Driver_VarType"])].add(r["cell_name"])
print("top variants:", sorted(((k, len(v)) for k, v in var.items()), key=lambda kv: -kv[1])[:20])
json.dump({"passing": sorted(passing), "cells_by_line": dict(cells_by_line)}, open(base + "/tahoe_panel.json", "w"))
