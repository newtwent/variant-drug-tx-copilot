"""Machine-check the audit verdict files: schema, length caps, language and parity rules, and literal quotes.
Usage: python3 -I kbcheckquotes.py <data_dir> <verdict.json> [more.json ...]   -> prints a summary, writes <verdict>.checked.json"""
import json
import re
import sys
from pathlib import Path

data = Path(sys.argv[1])
CJK = re.compile(r"[㐀-䶿一-鿿]")
NUM = re.compile(r"\d+(?:[.,]\d+)*")
IDTOK = re.compile(r"\b(?:GV|GD|DS|KB|MD|WM|EV)\d{2}\b")
LEAK = re.compile("claude[- ]?\\d|claude-[a-z0-9]|" + "|".join(("son" + "net", "op" + "us", "fa" + "ble", "hai" + "ku")), re.I)
KEYS = ["id", "identity_ok", "identity_note", "reading_depth", "checks", "new_key_claim_en", "new_key_claim_zh",
        "new_so_what_en", "new_so_what_zh", "new_caveat_en", "new_caveat_en_changed", "new_caveat_zh", "tier_rec",
        "tier_reason", "keep_rec", "keep_reason", "keep_reason_zh", "title_rec", "year_rec", "kind_rec", "problems"]


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("−", "-").replace("–", "-").replace("—", "-").replace(" ", " ")
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s


def words(s):
    return len(s.split())


def parity(en, zh):
    miss = [n for n in NUM.findall(en) if n not in zh]
    ids = [t for t in IDTOK.findall(en) if t not in zh]
    return miss, ids


texts = {}


def corpus(rid):
    if rid not in texts:
        d = data / rid
        parts = []
        for name in ("fulltext.txt", "evidence.md"):
            p = d / name
            if p.exists():
                parts.append(p.read_text(encoding="utf-8", errors="replace"))
        meta = d / "meta.json"
        if meta.exists():
            parts.append(meta.read_text(encoding="utf-8", errors="replace"))
        texts[rid] = norm(" ".join(parts))
        texts[rid + ":nocomma"] = re.sub(r"(?<=\d),(?=\d{3}\b)", "", texts[rid])
    return texts[rid]


total = {"rows": 0, "checks": 0, "quote_ok": 0, "quote_bad": 0, "schema_bad": 0, "other_bad": 0}
for path in sys.argv[2:]:
    arr = json.loads(Path(path).read_text(encoding="utf-8"))
    out = []
    for o in arr:
        total["rows"] += 1
        issues = []
        for k in KEYS:
            if k not in o:
                issues.append(f"missing key {k}")
        rid = o.get("id", "?")
        if not (data / rid).exists():
            issues.append("unknown id")
        text = corpus(rid) if (data / rid).exists() else ""
        for c in o.get("checks", []):
            total["checks"] += 1
            q = norm(c.get("quote") or "")
            st = c.get("status")
            if st in ("verified", "contradicted") and not q:
                issues.append(f"check without quote: {str(c.get('claim'))[:60]}")
                total["quote_bad"] += 1
            elif q:
                if q in text:
                    total["quote_ok"] += 1
                else:
                    issues.append(f"quote not found: {q[:80]}")
                    total["quote_bad"] += 1
            if st == "verified" and q:
                nums = [n.replace(",", "") for n in NUM.findall(c.get("claim", "")) if len(n.replace(",", "").replace(".", "")) >= 2]
                qn = re.sub(r"(?<=\d),(?=\d{3}\b)", "", q)
                gone = [n for n in nums if n not in qn]
                if gone:
                    issues.append(f"verified claim numbers {gone} absent from its quote: {str(c.get('claim'))[:60]}")
        for pair, cap in (("key_claim", 45), ("so_what", 30)):
            en, zh = o.get(f"new_{pair}_en", ""), o.get(f"new_{pair}_zh", "")
            if words(en) > cap:
                issues.append(f"{pair} too long ({words(en)} words)")
            if en != "NA" and (CJK.search(en) or not CJK.search(zh)):
                issues.append(f"{pair} language rule")
            miss, ids = parity(en, zh)
            if miss or ids:
                issues.append(f"{pair} parity numbers {miss} ids {ids}")
            if LEAK.search(en) or LEAK.search(zh):
                issues.append(f"{pair} model identifier")
        en, zh = o.get("new_caveat_en", ""), o.get("new_caveat_zh", "")
        if words(en) > 35:
            issues.append(f"caveat too long ({words(en)} words)")
        if en != "NA" and (CJK.search(en) or not CJK.search(zh)):
            issues.append("caveat language rule")
        miss, ids = parity(en, zh)
        if miss or ids:
            issues.append(f"caveat parity numbers {miss} ids {ids}")
        if o.get("tier_rec") not in ("T1", "T2", "T3"):
            issues.append("bad tier_rec")
        if o.get("keep_rec") not in ("keep", "retire", "hold"):
            issues.append("bad keep_rec")
        if o.get("reading_depth") not in ("full text", "abstract", "page", "none"):
            issues.append("bad reading_depth")
        # numbers kept in the new key claim must occur in the text on disk
        for n in NUM.findall(o.get("new_key_claim_en", "")):
            nn = n.replace(",", "")
            if len(nn.replace(".", "")) >= 2 and nn not in texts.get(rid + ":nocomma", ""):
                issues.append(f"new key claim number {n} not found in the text on disk")
        o["_issues"] = issues
        if issues:
            total["other_bad"] += 1
        out.append(o)
    Path(str(path) + ".checked.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(path, "rows with issues:", sum(1 for o in out if o["_issues"]), "of", len(out))
print(total)
