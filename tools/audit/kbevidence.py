"""Build <data>/<ID>/evidence.md for every row: the recorded row, metadata, abstract and context windows around the
numbers and key terms of the recorded claims. Usage: python3 -I kbevidence.py <repo_root> <data_dir> [ID,ID,...]"""
import csv
import json
import re
import sys
from pathlib import Path

repo, data = Path(sys.argv[1]), Path(sys.argv[2])
with open(repo / "data" / "sources.csv", encoding="utf-8", newline="") as fh:
    rows = list(csv.DictReader(fh))
want = set(sys.argv[3].split(",")) if len(sys.argv) > 3 and sys.argv[3] else None

NUM = re.compile(r"(?<![\w.])\d[\d,]*(?:\.\d+)?%?")
TERM = re.compile(r"\b(?:[A-Z][A-Za-z0-9]*[A-Z0-9][A-Za-z0-9-]*|[A-Z][a-z]+-[A-Za-z0-9]+)\b")
STOP = {"The", "This", "That", "SNP", "RNA", "DNA", "NA", "FDR", "GxE", "UMI", "MD", "GD", "GV", "DS", "KB", "WM", "EV"}


def squash(s):
    return re.sub(r"\s+", " ", s)


def windows(text, token, width=230, limit=3):
    out, start = [], 0
    pat = re.compile(re.escape(token))
    for m in pat.finditer(text):
        a, b = max(0, m.start() - width), min(len(text), m.end() + width)
        out.append("…" + squash(text[a:b]) + "…")
        if len(out) >= limit:
            break
    return out


def numbers(s):
    toks = []
    for m in NUM.finditer(s):
        t = m.group(0).rstrip(",")
        digits = t.replace(",", "").rstrip("%")
        core = digits.replace(".", "")
        if "." in digits and len(core) >= 2 or len(core) >= 3 or (len(core) == 2 and not t.endswith("%")):
            toks.append(t)
    return list(dict.fromkeys(toks))


for r in rows:
    if want and r["id"] not in want:
        continue
    d = data / r["id"]
    if not d.exists():
        continue
    meta = json.loads((d / "meta.json").read_text(encoding="utf-8")) if (d / "meta.json").exists() else {}
    ft = d / "fulltext.txt"
    text = ft.read_text(encoding="utf-8", errors="replace") if ft.exists() else ""
    src_note = (d / "fulltext_source.txt").read_text(encoding="utf-8").strip() if (d / "fulltext_source.txt").exists() else "none"
    flat = squash(text)
    flat_nocomma = re.sub(r"(?<=\d),(?=\d{3}\b)", "", flat)
    L = [f"# {r['id']} - {r['title']}", "", "## Recorded row (to be audited)",
         f"- status {r['status']}; tier {r['tier']}; verified {r['verified']}; kind {r['kind']}; year {r['year']}; "
         f"track {r['track']}; variant_class {r['variant_class']}; relevance {r['relevance']}",
         f"- urls: {r['url']}" + ("" if r['url_alt'] == 'NA' else " ; " + r['url_alt']),
         f"- key_claim_en: {r['key_claim_en']}", f"- so_what_en: {r['so_what_en']}", f"- caveat_en: {r['caveat_en']}", ""]
    L.append("## Metadata")
    for k in ("crossref", "crossref_pii", "openalex", "europepmc", "europepmc_pmc", "europepmc_title", "europepmc_extra", "arxiv", "biorxiv", "openalex_title"):
        v = meta.get(k)
        if v:
            slim = {a: b for a, b in v.items() if a not in ("abstract", "authors", "relation", "license", "pii") or a == "authors"}
            if "authors" in slim and isinstance(slim["authors"], list):
                slim["authors"] = slim["authors"][:6]
            if "authors" in slim and isinstance(slim["authors"], str):
                slim["authors"] = slim["authors"][:200]
            L.append(f"- {k}: {json.dumps(slim, ensure_ascii=False)[:700]}")
    abstract = ""
    for k in ("biorxiv", "arxiv", "europepmc", "europepmc_pmc", "europepmc_title", "europepmc_extra"):
        a = (meta.get(k) or {}).get("abstract")
        if a:
            abstract = squash(re.sub(r"<[^>]+>", " ", str(a)))
            break
    L += ["", "## Abstract (from metadata)", abstract[:3000] or "(none retrieved)", ""]
    L += ["## Text on disk", f"- fulltext.txt: {len(text)} chars; source: {src_note}", ""]
    L.append("## Context windows for the numbers and terms of the recorded claim")
    claims = " ".join((r["key_claim_en"], r["caveat_en"], r["so_what_en"]))
    for tok in numbers(claims)[:24]:
        hay = flat_nocomma if "," in tok else flat
        probe = tok.replace(",", "")
        ws = windows(hay, probe.rstrip("%"), limit=2) if text else []
        if not ws and abstract:
            ws = [w for w in windows(abstract, probe.rstrip("%"), limit=1)]
            ws = [w + " [abstract]" for w in ws]
        L.append(f"### number {tok}")
        L += [f"- {w}" for w in ws] if ws else ["- NOT FOUND in the text on disk or the abstract"]
    terms = [t for t in dict.fromkeys(TERM.findall(r["key_claim_en"])) if t not in STOP][:8]
    for t in terms:
        ws = windows(flat, t, limit=1) if text else []
        L.append(f"### term {t}")
        L += [f"- {w}" for w in ws] if ws else ["- NOT FOUND in the text on disk"]
    (d / "evidence.md").write_text("\n".join(L), encoding="utf-8")
print("evidence written")
