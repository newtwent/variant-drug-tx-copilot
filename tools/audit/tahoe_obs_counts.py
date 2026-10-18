"""Count cells per (cell line, pass_filter) and per (plate, pass_filter) in the Tahoe-100M obs_metadata table.
Only three columns are read, by HTTP range requests, so the 100-million-row table is never downloaded.
Usage: python3 -I tahoe_obs_counts.py <libs_dir_with_pyarrow_and_requests> <out.json>
The numbers derived from this output and from the small metadata tables are in derived_tahoe.txt (page DS07, query Q137);
tahoe_drivers.py reads out.json and the cell-line metadata table to count driver genes per line."""
import collections
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # hf_range.py sits beside this file
import hf_range as hr  # noqa: E402  (it adds the libs directory sys.argv[1] to sys.path and imports pyarrow)
import pyarrow.parquet as pq  # noqa: E402

url = "https://huggingface.co/datasets/tahoebio/Tahoe-100M/resolve/main/metadata/obs_metadata.parquet"
f = hr.RangeFile(url)
pf = pq.ParquetFile(f)
cnt = collections.Counter()
plate_cnt = collections.Counter()
t0 = time.time()
for rg in range(pf.metadata.num_row_groups):
    t = pf.read_row_group(rg, columns=["cell_name", "pass_filter", "plate"])
    cn = t.column("cell_name").to_pylist()
    pfl = t.column("pass_filter").to_pylist()
    pl = t.column("plate").to_pylist()
    for a, b, c in zip(cn, pfl, pl):
        cnt[(a, b)] += 1
        plate_cnt[(c, b)] += 1
    if rg % 8 == 0:
        print("rg", rg, "elapsed", round(time.time() - t0), "bytes", f.bytes, flush=True)
out = {"cell_name_pass": {f"{k[0]}|{k[1]}": v for k, v in cnt.items()}, "plate_pass": {f"{k[0]}|{k[1]}": v for k, v in plate_cnt.items()}}
json.dump(out, open(sys.argv[2], "w"))
print("done", len(cnt), "bytes", f.bytes)
