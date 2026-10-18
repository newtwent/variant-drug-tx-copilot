"""Slow, polite bioRxiv/medRxiv full-text fetcher (the site rate-limits this egress address hard).
Usage: python3 -I biorxiv_fetch.py <scratch_dir> <queue.txt>   queue lines: "<ID> <doi>"
Fetches the JATS XML (fallback: full PDF) with >= 100 s between requests and writes <data>/<ID>/fulltext.txt."""
import importlib.util
import json
import sys
import time
from pathlib import Path

import requests

scr = Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("kbaudit", scr / "kbaudit.py")
kb = importlib.util.module_from_spec(spec)
sys.argv_backup = sys.argv
spec.loader.exec_module(kb)
data = scr / "audit_data"
UA = kb.UA
MIN_GAP = 420.0
last = [0.0]


def get(url, **kw):
    for attempt in range(10):
        gap = MIN_GAP - (time.time() - last[0])
        if gap > 0:
            time.sleep(gap)
        last[0] = time.time()
        try:
            r = requests.get(url, headers={"User-Agent": UA}, timeout=90, allow_redirects=False, **kw)
        except requests.RequestException as e:
            print("  exc", type(e).__name__, flush=True)
            continue
        if r.status_code == 429:
            ra = int(r.headers.get("retry-after", "30"))
            print(f"  429 retry-after {ra}", flush=True)
            time.sleep(ra + 15)
            continue
        if r.status_code in (301, 302, 303, 307, 308):
            url = requests.compat.urljoin(url, r.headers["location"])
            print("  redirect ->", url, flush=True)
            last[0] = time.time() - MIN_GAP + 20  # a redirect hop is cheap, but do not hammer
            continue
        return r, url
    return None, url


queue = [ln.split() for ln in Path(sys.argv[2]).read_text().splitlines() if ln.strip()]
for rid, doi in queue:
    d = data / rid
    ft = d / "fulltext.txt"
    if ft.exists() and ft.stat().st_size > 12000:
        print(rid, "cached", flush=True)
        continue
    d.mkdir(exist_ok=True)
    meta = json.loads((d / "meta.json").read_text(encoding="utf-8")) if (d / "meta.json").exists() else {}
    jats = (meta.get("biorxiv") or {}).get("jatsxml")
    if not jats:
        r0, _ = kb.polite_get(f"https://api.biorxiv.org/details/biorxiv/{doi}")
        try:
            jats = r0.json()["collection"][-1]["jatsxml"]
        except Exception:
            jats = None
    print(rid, doi, jats, flush=True)
    done = False
    if jats:
        r, final = get(jats)
        if r is not None and r.status_code == 200 and len(r.content) > 5000:
            text = kb.jats_to_text(r.content)
            if len(text) > 8000:
                kb.save_text(d, text, final, "jats")
                print("  saved jats", len(text), flush=True)
                done = True
    if not done:
        pdf_url = f"https://www.biorxiv.org/content/{doi}v1.full.pdf"
        r, final = get(pdf_url)
        if r is not None and r.status_code == 200 and r.content[:4] == b"%PDF":
            (d / "raw.pdf").write_bytes(r.content)
            text = kb.pdf_to_text(d / "raw.pdf", d / "raw_pdf.txt")
            if len(text) > 8000:
                kb.save_text(d, text, final, "pdf")
                print("  saved pdf", len(text), flush=True)
                done = True
    if not done:
        print("  FAILED", rid, flush=True)
print("queue finished", flush=True)
