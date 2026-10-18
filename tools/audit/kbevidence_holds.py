"""Evidence files for the held candidates: <data>/_holds/<H>/evidence.md. Usage: python3 -I kbevidence_holds.py <data_dir>"""
import json
import re
import sys
from pathlib import Path

base = Path(sys.argv[1]) / "_holds"
rows = json.loads((base / "_rows.json").read_text(encoding="utf-8"))


def squash(s):
    return re.sub(r"\s+", " ", s)


for r in rows:
    d = base / r["id"]
    meta = json.loads((d / "meta.json").read_text(encoding="utf-8")) if (d / "meta.json").exists() else {}
    ft = d / "fulltext.txt"
    text = ft.read_text(encoding="utf-8", errors="replace") if ft.exists() else ""
    src = (d / "fulltext_source.txt").read_text(encoding="utf-8").strip() if (d / "fulltext_source.txt").exists() else "none"
    L = [f"# {r['id']} - {r['title']}", "", "## Held candidate (to be screened)",
         f"- hold code {r['code']} (M1 title or snippet only; M2 overlaps an included row; M3 plausible link not stated); search query {r['query']}",
         f"- url: {r['url']}", ""]
    L.append("## Metadata")
    for k in ("crossref", "crossref_pii", "openalex", "europepmc", "europepmc_pmc", "europepmc_title", "europepmc_extra", "arxiv", "biorxiv", "openalex_title"):
        v = meta.get(k)
        if v:
            slim = {a: b for a, b in v.items() if a not in ("abstract", "relation", "license", "pii")}
            if isinstance(slim.get("authors"), list):
                slim["authors"] = slim["authors"][:6]
            if isinstance(slim.get("authors"), str):
                slim["authors"] = slim["authors"][:200]
            L.append(f"- {k}: {json.dumps(slim, ensure_ascii=False)[:700]}")
    abstract = ""
    for k in ("biorxiv", "arxiv", "europepmc", "europepmc_pmc", "europepmc_title", "europepmc_extra", "openalex"):
        a = (meta.get(k) or {}).get("abstract")
        if a:
            abstract = squash(re.sub(r"<[^>]+>", " ", str(a)))
            break
    L += ["", "## Abstract (from metadata)", abstract[:3000] or "(none retrieved)", ""]
    L += ["## Text on disk", f"- fulltext.txt: {len(text)} chars; source: {src}", ""]
    (d / "evidence.md").write_text("\n".join(L), encoding="utf-8")
print("evidence written for", len(rows))
