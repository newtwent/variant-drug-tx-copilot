"""Validate the knowledge base. Usage: python3 -I tools/validate_kb.py [repo_root]
Errors fail the run (exit 1); warnings are listed for manual review. See CLAUDE.md sections 1 to 10."""
import csv
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

args = [a for a in sys.argv[1:] if not a.startswith("--")]
repo = Path(args[0]) if args else Path(__file__).resolve().parent.parent
ONLY = [a for a in sys.argv[1:] if a.startswith("--docs=")]
ONLY = set(ONLY[0][len("--docs="):].split(",")) if ONLY else None  # check only these markdown files (repo-relative)
errors, warnings, notes = [], [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


CJK = re.compile(r"[㐀-䶿一-鿿]")
NUM = re.compile(r"\d+(?:[.,]\d+)*")
IDGROUP = re.compile(r"\[([A-Z]{2}\d{2}(?:, [A-Z]{2}\d{2})*)\]")
IDANY = re.compile(r"\b(?:GV|GD|DS|KB|MD|WM|EV)\d{2}\b")
QTOK = re.compile(r"\bQ(\d{2,3})\b")
SRC_COLS = ["id", "title", "url", "url_alt", "year", "kind", "category", "track", "variant_class", "relevance", "tier",
            "verified", "key_claim_en", "key_claim_zh", "so_what_en", "so_what_zh", "caveat_en", "caveat_zh", "accessed",
            "query_id", "status"]
DS_PAIRS = ["modality", "scale_reported", "perturbation_type", "genotype_info", "dose_time_axes", "relevance"]
DS_COLS = (["name"] + [f"{k}_{lang}" for k in DS_PAIRS[:5] for lang in ("en", "zh")] + ["access_url", "source_id"]
           + ["relevance_en", "relevance_zh", "caveats_en", "caveats_zh"])
KINDS = {"journal", "preprint", "org-page", "repo", "NA", "proceedings", "news", "blog", "social", "talk"}
RELEVANCE = {"mechanism", "modeling", "data", "evaluation", "prior", "context"}
CAPS = {"key_claim": 45, "so_what": 30, "caveat": 35}


def parity(label, en, zh):
    miss = [n for n in NUM.findall(en) if n not in zh]
    if miss:
        err(f"{label}: numbers missing in ZH {sorted(set(miss))}")
    miss_ids = [t for t in IDANY.findall(en) if t not in zh]
    if miss_ids:
        err(f"{label}: ids missing in ZH {sorted(set(miss_ids))}")


def lang_pair(label, en, zh, cap=None):
    if not en.strip() or not zh.strip():
        err(f"{label}: empty field")
        return
    if (en == "NA") != (zh == "NA"):
        err(f"{label}: languages disagree on NA")
        return
    if en == "NA":
        return
    if CJK.search(en):
        err(f"{label}: EN contains CJK")
    if not CJK.search(zh):
        err(f"{label}: ZH has no CJK")
    if cap and len(en.split()) > cap:
        err(f"{label}: {len(en.split())} words exceed the cap of {cap}")
    parity(label, en, zh)


# ---- CSVs ---------------------------------------------------------------------------------
try:
    with open(repo / "data" / "sources.csv", encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh, strict=True)
        src_header, src = rd.fieldnames, list(rd)
    with open(repo / "data" / "datasets.csv", encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh, strict=True)
        ds_header, ds = rd.fieldnames, list(rd)
except Exception as e:  # noqa
    sys.exit(f"CSV parse failure: {e}")
if src_header != SRC_COLS:
    err(f"sources.csv header differs: {src_header}")
if ds_header != DS_COLS:
    err(f"datasets.csv header differs: {ds_header}")
for tag, rows_ in (("sources.csv", src), ("datasets.csv", ds)):
    for n, r in enumerate(rows_, 2):
        if None in r or any(v is None for v in r.values()):
            err(f"{tag} row {n}: wrong field count")

ids = [r["id"] for r in src]
if len(ids) != len(set(ids)):
    err("sources.csv: duplicate ids")
idset = set(ids)
retired = {r["id"] for r in src if r["status"] == "retired"}
byid = {r["id"]: r for r in src}
log_text = (repo / "docs" / "search-log.md").read_text(encoding="utf-8")
qrows = re.findall(r"^\| (Q\d{2,3}) \|", log_text, re.M)
qset = set(qrows)
if len(qrows) != len(qset):
    err("search-log: duplicate query ids in the table")
if qrows != [f"Q{n:02d}" for n in range(1, len(qrows) + 1)]:
    err("search-log: query ids are not contiguous and in order")
qmax = len(qrows)

for r in src:
    i = r["id"]
    if not re.fullmatch(r"(GV|GD|DS|KB|MD|WM|EV)\d{2}", i):
        err(f"bad id format: {i}")
    if r["category"] != i[:2]:
        err(f"{i}: category mismatch")
    if not r["title"].strip():
        err(f"{i}: empty title")
    if r["status"] == "active" and ("..." in r["title"] or "title truncated" in r["title"].lower()):
        warn(f"{i}: active row with a truncated title")
    if r["tier"] not in ("T1", "T2", "T3"):
        err(f"{i}: bad tier {r['tier']}")
    if r["verified"] not in ("Y", "N"):
        err(f"{i}: bad verified {r['verified']}")
    if (r["verified"] == "Y") != (r["tier"] == "T1"):
        err(f"{i}: verified=Y must coincide with tier T1 (tier {r['tier']}, verified {r['verified']})")
    if r["status"] not in ("active", "retired"):
        err(f"{i}: bad status {r['status']}")
    if r["relevance"] not in RELEVANCE:
        err(f"{i}: bad relevance {r['relevance']}")
    if r["kind"] not in KINDS:
        err(f"{i}: bad kind {r['kind']}")
    if r["track"] not in ("S", "G", "B"):
        err(f"{i}: bad track {r['track']}")
    vc = r["variant_class"]
    if vc != "NA" and not all(p in {"1", "2", "3", "4", "5"} for p in vc.split(";")):
        err(f"{i}: bad variant_class {vc}")
    if r["year"] != "NA" and not (re.fullmatch(r"\d{4}", r["year"]) and 1990 <= int(r["year"]) <= 2027):
        err(f"{i}: bad year {r['year']}")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["accessed"]):
        err(f"{i}: bad accessed {r['accessed']}")
    for q in ([] if r["query_id"] == "NA" else r["query_id"].split("; ")):
        if not re.fullmatch(r"Q\d{2,3}", q) or q not in qset:
            err(f"{i}: query id {q!r} not in the search-log table")
    active = r["status"] == "active"
    lang_pair(f"{i}.key_claim", r["key_claim_en"], r["key_claim_zh"], CAPS["key_claim"] if active else None)
    lang_pair(f"{i}.so_what", r["so_what_en"], r["so_what_zh"], CAPS["so_what"] if active else None)
    lang_pair(f"{i}.caveat", r["caveat_en"], r["caveat_zh"], CAPS["caveat"] if active else None)
    if active and r["so_what_en"] == "NA":
        err(f"{i}: active row without a so_what")
    if r["status"] == "retired":
        if not re.search(r"Retired \d{4}-\d{2}-\d{2} \(R\d\):", r["caveat_en"]):
            err(f"{i}: retired row lacks a retirement note in caveat_en")
        if "退役" not in r["caveat_zh"]:
            err(f"{i}: retired row lacks a retirement note in caveat_zh")
    elif "Retired" in r["caveat_en"]:
        err(f"{i}: active row carries a retirement note")
    if r["tier"] == "T1" and r["accessed"] == "NA":
        err(f"{i}: T1 row without an accessed date")

urls = {}
for r in src:
    for u in [r["url"]] + ([] if r["url_alt"] == "NA" else r["url_alt"].split(" ; ")):
        if not re.fullmatch(r"https?://[^\s<>]+", u):
            err(f"{r['id']}: bad url syntax {u}")
        if u in urls and urls[u] != r["id"]:
            other = byid[urls[u]]
            if not (urls[u] in r["caveat_en"] or r["id"] in other["caveat_en"] or "Same page as" in r["caveat_en"]):
                err(f"duplicate url {u} in {urls[u]} and {r['id']}")
        urls.setdefault(u, r["id"])

names = [r["name"] for r in ds]
if len(names) != len(set(names)):
    err("datasets.csv: duplicate names")
for r in ds:
    label = f"datasets.csv[{r['name']}]"
    for s in r["source_id"].split(";"):
        if s != "NA" and s not in idset:
            err(f"{label}: dangling source id {s}")
        elif s in retired:
            err(f"{label}: cites retired source {s}")
    lang_pair(label + ".caveats", r["caveats_en"], r["caveats_zh"])
    for key in DS_PAIRS:
        lang_pair(f"{label}.{key}", r[key + "_en"], r[key + "_zh"])




# ---- questions.csv ------------------------------------------------------------------------
Q_COLS = ["id", "type", "priority", "question_en", "question_zh", "why_en", "why_zh", "default_en", "default_zh", "affects",
          "if_changed_en", "if_changed_zh", "status", "answer", "answered_on", "applied_on"]
Q_TYPES = {"decision", "missing-information", "attention"}
Q_PRIO = {"needs-your-attention", "optional"}
Q_STATUS = {"open", "answered", "default"}
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
questions = []
qpath = repo / "data" / "questions.csv"
if qpath.exists():
    try:
        with open(qpath, encoding="utf-8", newline="") as fh:
            rd = csv.DictReader(fh, strict=True)
            q_header, questions = rd.fieldnames, list(rd)
    except Exception as e:  # noqa
        sys.exit(f"questions.csv parse failure: {e}")
    if q_header != Q_COLS:
        err(f"questions.csv header differs: {q_header}")
    qids = [r["id"] for r in questions]
    if len(qids) != len(set(qids)):
        err("questions.csv: duplicate ids")
    for n, r in enumerate(questions, 2):
        if None in r or any(v is None for v in r.values()):
            err(f"questions.csv row {n}: wrong field count")
            continue
        i = r["id"]
        if not re.fullmatch(r"UQ\d{2}", i):
            err(f"bad question id format: {i}")
        if r["type"] not in Q_TYPES:
            err(f"{i}: bad type {r['type']}")
        if r["priority"] not in Q_PRIO:
            err(f"{i}: bad priority {r['priority']}")
        if r["status"] not in Q_STATUS:
            err(f"{i}: bad status {r['status']}")
        for key in ("question", "why", "default", "if_changed"):
            lang_pair(f"{i}.{key}", r[key + "_en"], r[key + "_zh"])
        if not r["affects"].strip():
            err(f"{i}: empty affects")
        for tok in IDANY.findall(" ".join(r[k] for k in r if k.endswith("_en"))):
            if tok not in idset:
                err(f"{i}: unknown source id {tok}")
        if r["status"] == "open" and (r["answer"].strip() or r["answered_on"].strip()):
            err(f"{i}: status open but an answer or answer date is present")
        if r["status"] == "answered" and not r["answer"].strip():
            err(f"{i}: status answered without an answer")
        if r["status"] in ("answered", "default") and not DATE.fullmatch(r["answered_on"].strip()):
            err(f"{i}: status {r['status']} needs answered_on as YYYY-MM-DD")
        if r["applied_on"].strip():
            if not DATE.fullmatch(r["applied_on"].strip()):
                err(f"{i}: bad applied_on")
            if r["status"] == "open":
                err(f"{i}: applied_on set on an open question")
uqset = {r["id"] for r in questions}

LABEL = re.compile(r"\b[A-Z]{1,3}\d+[a-z]?\b")
NUMTOK = re.compile(r"(?<![\w.])\d[\d,]*(?:\.\d+)?%?")


def row_text(i):
    r = byid.get(i)
    if not r:
        return ""
    parts = [r["title"], r["key_claim_en"], r["so_what_en"], r["caveat_en"]]
    for d in ds:
        if i in d["source_id"].split(";"):
            parts += [d[k] for k in d if k.endswith("_en")]
    return " ".join(parts)


def norm_num(t):
    return t.replace(",", "").rstrip("%").rstrip(".")


def trace_numbers(name, body, cited_ids):
    """Warn about numbers in an English paragraph that occur in none of the rows it cites."""
    hay = " ".join(row_text(i) for i in cited_ids)
    hay_nums = {norm_num(t) for t in NUMTOK.findall(hay)}
    text = LABEL.sub(" ", IDGROUP.sub(" ", body))
    text = re.sub(r"\bdocuments? \d{2}(?:(?:,| and| to) \d{2})*", " ", text)
    text = re.sub(r"[A-Za-z][A-Za-z0-9-]*\d[A-Za-z0-9-]*", " ", text)  # names such as Tahoe-100M or CD34
    missing = []
    for t in NUMTOK.findall(text):
        n = norm_num(t)
        core = n.replace(".", "")
        if len(core) < 2 or (len(n) == 4 and 2015 <= int(core) <= 2027 and "." not in n):
            continue
        if n not in hay_nums:
            missing.append(t)
    if missing:
        warn(f"{name}: numbers not found in the cited rows {sorted(set(missing))}: {body[:60]!r}")


# ---- markdown -------------------------------------------------------------------------------
def blocks(text):
    out, cur, fence = [], [], False
    for line in text.splitlines():
        if line.startswith("```"):
            cur.append(line)
            if fence:
                out.append(("code", "\n".join(cur)))
                cur, fence = [], False
            else:
                fence = True
            continue
        if fence:
            cur.append(line)
            continue
        if line.strip() == "":
            if cur:
                out.append((None, "\n".join(cur)))
                cur = []
            continue
        cur.append(line)
    if cur:
        out.append((None, "\n".join(cur)))
    res = []
    for kind, body in out:
        if kind:
            res.append((kind, body))
        elif body.startswith("#"):
            res.append(("heading", body))
        elif body.startswith("|"):
            res.append(("table", body))
        elif body.startswith(">"):
            res.append(("quote", body))
        elif body.startswith("<!--"):
            res.append(("comment", body))
        else:
            res.append(("para", body))
    return res


NOTFOUND = re.compile(r"\b(not found|none found|no [\w\- ]{0,40}\bfound|did not find|could not find|EMPTY)\b", re.I)
md_files = [repo / "README.md", repo / "CLAUDE.md"] + sorted((repo / "docs").glob("*.md"))
if ONLY:
    md_files = [f for f in md_files if f.relative_to(repo).as_posix() in ONLY]
pairs, cited = 0, set()
for f in md_files:
    text = f.read_text(encoding="utf-8")
    name = f.relative_to(repo).as_posix()
    bl = blocks(text)
    generated = False
    for i, (k, body) in enumerate(bl):
        if k == "comment":
            if body.rstrip().endswith(":start -->"):
                generated = True
            elif body.rstrip().endswith(":end -->"):
                generated = False
        if k == "table" and not generated and name.startswith("docs/0") and not name.endswith("search-log.md"):
            for ln in body.splitlines()[2:]:
                cells = [c.strip() for c in ln.strip().strip("|").split("|")]
                en_cells = [c for c in cells if not CJK.search(c)]
                row_ids = sorted(set(IDANY.findall(ln)))
                if row_ids and en_cells:
                    trace_numbers(name, " ".join(en_cells), row_ids)
        if k in ("para", "quote", "table", "heading"):
            for g in IDGROUP.findall(body):
                for tok in g.split(", "):
                    if tok in retired:
                        err(f"{name}: bracketed citation of retired source {tok}")
        if k == "table":
            rows_ = [ln for ln in body.splitlines() if ln.strip().startswith("|")]
            if len({len(re.findall(r"(?<!\\)\|", ln)) for ln in rows_}) != 1:
                err(f"{name}: table with ragged rows near {rows_[0][:60]!r}")
        if k == "para":
            if CJK.search(body):
                err(f"{name}: English paragraph contains CJK: {body[:60]!r}")
            nxt = bl[i + 1] if i + 1 < len(bl) else None
            if not nxt or nxt[0] != "quote":
                err(f"{name}: paragraph without translation: {body[:60]!r}")
                continue
            zh = nxt[1]
            pairs += 1
            zh_nums = set(NUM.findall(zh))
            miss = [n for n in NUM.findall(body) if n not in zh_nums]
            if miss:
                err(f"{name}: numbers missing in translation {sorted(set(miss))}: {body[:50]!r}")
            en_ids = [t for g in IDGROUP.findall(body) for t in g.split(", ")]
            zh_ids = [t for g in IDGROUP.findall(zh) for t in g.split(", ")]
            if set(en_ids) != set(zh_ids):
                err(f"{name}: ID sets differ EN={sorted(set(en_ids))} ZH={sorted(set(zh_ids))}")
            en_any, zh_any = set(IDANY.findall(body)), set(IDANY.findall(zh))
            if en_any != zh_any:
                err(f"{name}: id tokens differ EN-only={sorted(en_any - zh_any)} ZH-only={sorted(zh_any - en_any)}: {body[:50]!r}")
            cited.update(en_ids)
            if en_ids and name.startswith("docs/0") and not name.endswith("search-log.md"):
                trace_numbers(name, body, sorted(set(en_ids)))
            if NOTFOUND.search(body) and not QTOK.search(body) and name not in ("README.md", "CLAUDE.md"):
                warn(f"{name}: absence statement without a query id: {body[:90]!r}")
            if re.match(r"\*\*J\d+", body) and "confidence" not in body[:200].lower():
                warn(f"{name}: judgment without a stated confidence near start: {body[:70]!r}")
        elif k == "quote":
            prev = bl[i - 1] if i > 0 else None
            if not prev or prev[0] != "para":
                err(f"{name}: blockquote not preceded by a paragraph: {body[:60]!r}")
            if not CJK.search(body):
                err(f"{name}: blockquote without Chinese: {body[:60]!r}")
    for tok in IDANY.findall(text):
        if tok not in idset:
            err(f"{name}: unknown source id token {tok}")
    for tok in sorted(set(re.findall(r"\bUQ\d{2}\b", text))):
        if tok not in uqset:
            err(f"{name}: unknown question id {tok}")
    for m in re.finditer(r"\[([A-Z]{2}\d{2}[^\]]*)\]", text):
        if not IDGROUP.fullmatch(m.group(0)) and "](" not in text[m.start(): m.end() + 2]:
            err(f"{name}: malformed id group {m.group(0)}")
    for m in QTOK.finditer(text):
        if int(m.group(1)) > qmax:
            err(f"{name}: query id {m.group(0)} beyond the log")
    for bad in ("TODO", "FIXME", "TBD", "XXX", "{{", "}}", "lorem"):
        if bad in text:
            err(f"{name}: placeholder text {bad!r}")

# ---- labels: each judgment, insight, principle, assumption, hypothesis and milestone is defined once ----
LABEL_PAT = r"(?:J\d{1,2}|I\d|P\d|LC\d|E\d{1,2}|A[1-9]|X[1-9]|M\d|H[A-D])"
DEF_PARA = re.compile(r"^(?:\*\*)?(J\d{1,2}|I\d|P\d|LC\d|E\d{1,2}|A[1-9]|X[1-9]|M\d)(?=[ .,(:*])")
DEF_HEAD = re.compile(r"^#{2,4} [\d.]* ?(H[A-D])\b")
REF_LABEL = re.compile(r"(?<![\w-])(" + LABEL_PAT + r")(?![\w-])")
defs, refs = {}, {}
for f in [repo / "README.md"] + sorted((repo / "docs").glob("*.md")):
    nm = f.relative_to(repo).as_posix()
    for k, body in blocks(f.read_text(encoding="utf-8")):
        if k in ("para", "heading"):
            first = body.splitlines()[0]
            m = DEF_PARA.match(first) if k == "para" else DEF_HEAD.match(first)
            if m:
                if m.group(1) in defs:
                    err(f"label {m.group(1)} defined twice ({defs[m.group(1)]} and {nm})")
                defs[m.group(1)] = nm
        if k == "para":
            for t in REF_LABEL.findall(IDGROUP.sub(" ", body)):
                refs.setdefault(t, set()).add(nm)
for t, where in sorted(refs.items()):
    if t not in defs and not t.startswith("LC") or (t.startswith("LC") and t not in defs):
        err(f"label {t} is referenced but never defined: {sorted(where)}")

# ---- counts stated in the README ----------------------------------------------------------
active_n = len(src) - len(retired)
actual = dict(total=len(src), active=active_n, retired=len(retired), queries=qmax, datasets=len(ds),
              t1=sum(r["tier"] == "T1" for r in src), questions=len(questions))
CLAIMED = [(r"(\d+) sources \(", "total"), (r"(\d+) 条来源（", "total"), (r"(\d+) active", "active"), (r"(\d+) 条 active", "active"),
           (r"(\d+) retired", "retired"), (r"(\d+) 条 retired", "retired"), (r"(\d+) (?:log )?entries", "queries"),
           (r"(\d+) 条日志", "queries"), (r"(\d+) datasets", "datasets"), (r"(\d+) 个数据集", "datasets"),
           (r"(\d+) at tier T1", "t1"), (r"(\d+) 条 T1 级", "t1"), (r"(\d+) open questions", "questions"),
           (r"(\d+) 个待确认问题", "questions")]
readme = (repo / "README.md").read_text(encoding="utf-8")
for pat, key in CLAIMED:
    for m in re.finditer(pat, readme):
        if int(m.group(1)) != actual[key]:
            err(f"README claims {m.group(0)!r} but the data say {key}={actual[key]}")

# ---- leaks, secrets, forbidden files -------------------------------------------------------
LEAK = re.compile("claude[- ]?\\d|claude-[a-z0-9]|" + "|".join(("son" + "net", "op" + "us", "fa" + "ble", "hai" + "ku")), re.I)
SECRET = re.compile(r"ghp_[A-Za-z0-9]{20,}|github_" r"pat_|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|"
                    r"-----BEGIN [A-Z ]*PRIVATE KEY-----|xox[baprs]-|Bearer [A-Za-z0-9._-]{20,}")
for f in [p for p in repo.rglob("*") if p.is_file() and ".git" not in p.relative_to(repo).parts
          and "__pycache__" not in p.relative_to(repo).parts]:
    rel = f.relative_to(repo).as_posix()
    if f.suffix.lower() in (".pdf", ".zip", ".gz", ".h5ad", ".xlsx", ".parquet", ".xml"):
        err(f"forbidden file type: {rel}")
    if f.stat().st_size > 3_000_000:
        err(f"large file: {rel} ({f.stat().st_size} bytes)")
    try:
        content = f.read_text(encoding="utf-8")
    except Exception:
        err(f"non-text file: {rel}")
        continue
    for n, line in enumerate(content.splitlines(), 1):
        if LEAK.search(line):
            err(f"{rel}:{n}: possible model identifier: {line[:80]!r}")
        if SECRET.search(line):
            err(f"{rel}:{n}: possible secret")

q_doc = repo / "docs" / "10-open-questions.md"
if questions:
    if not q_doc.exists():
        err("docs/10-open-questions.md is missing")
    else:
        q_text = q_doc.read_text(encoding="utf-8")
        for i in sorted(uqset):
            if i not in q_text:
                err(f"docs/10-open-questions.md does not list {i} (run tools/fill_tables.py)")
uncited = sorted(i for i in idset - cited if i not in retired)
notes.append(f"paragraph/translation pairs checked: {pairs}")
notes.append(f"sources: {len(src)} (active {active_n}, retired {len(retired)}, tier T1 {actual['t1']}); datasets: {len(ds)}; "
             f"log entries: {qmax}")
notes.append(f"open questions: {len(questions)} (status open {sum(r['status'] == 'open' for r in questions)})")
notes.append(f"active sources not cited in bracketed prose (present only in the index tables): {len(uncited)}")
print("\n".join(notes))
if warnings:
    print(f"\n{len(warnings)} warning(s):")
    for w in (warnings if "--all" in sys.argv else warnings[:100]):
        print(" ~", w)
if errors:
    print(f"\n{len(errors)} problem(s):")
    for e in (errors if "--all" in sys.argv else errors[:150]):
        print(" -", e)
    sys.exit(1)
print("\nALL CHECKS PASSED")
