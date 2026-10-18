"""Audit harness: fetch metadata and full texts for the rows of data/sources.csv into a scratch directory.
Downloaded material is untrusted data: it is written under <data>/<ID>/ and only ever read as text.
Usage: python3 -I kbaudit.py <cmd> <repo_root> <data_dir> [ID,ID,...]
  cmd = ids      parse identifiers from the URLs and write <data>/<ID>/ids.json
        meta     fetch Crossref / arXiv / Europe PMC / OpenAlex / bioRxiv metadata -> meta.json
        text     fetch the best available full text -> fulltext.txt (+ fulltext_source.txt)
"""
import csv
import json
import os
import re
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote, unquote, urlparse

import requests
from bs4 import BeautifulSoup
from lxml import etree

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36 kb-audit/1.0"
INTERVAL = {  # minimum seconds between request starts per host
    "www.biorxiv.org": 100.0, "api.biorxiv.org": 0.6, "arxiv.org": 3.2, "export.arxiv.org": 3.2,
    "eutils.ncbi.nlm.nih.gov": 0.5, "www.ebi.ac.uk": 0.25, "api.crossref.org": 0.15, "api.openalex.org": 1.1,
    "pmc.ncbi.nlm.nih.gov": 1.0, "www.ncbi.nlm.nih.gov": 1.0, "www.nature.com": 1.2, "link.springer.com": 1.2,
}
_last, _locks, _glock = {}, {}, threading.Lock()


def polite_get(url, timeout=60, tries=3, **kw):
    host = urlparse(url).hostname or ""
    with _glock:
        lock = _locks.setdefault(host, threading.Lock())
    for attempt in range(tries):
        with lock:
            gap = INTERVAL.get(host, 0.6) - (time.time() - _last.get(host, 0))
            if gap > 0:
                time.sleep(gap)
            _last[host] = time.time()
        try:
            r = requests.get(url, timeout=timeout, headers={"User-Agent": UA}, **kw)
        except requests.RequestException as e:
            if attempt == tries - 1:
                return None, f"EXC {type(e).__name__}"
            time.sleep(3 * (attempt + 1))
            continue
        if r.status_code in (429, 503) and attempt < tries - 1 and host != "www.biorxiv.org":
            time.sleep(min(60, int(r.headers.get("retry-after", "10")) + 2))
            continue
        return r, f"{r.status_code}"
    return None, "FAILED"


def load_rows(repo):
    with open(Path(repo) / "data" / "sources.csv", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def urls_of(r):
    return [r["url"]] + ([] if r["url_alt"] == "NA" else r["url_alt"].split(" ; "))


# ---------------------------------------------------------------- identifiers
def parse_ids(r):
    out = {"doi": [], "arxiv": [], "pmcid": [], "pii": [], "github": [], "other": []}
    for u in urls_of(r):
        h = urlparse(u).hostname or ""
        path = unquote(urlparse(u).path)
        full = unquote(u)
        m = re.search(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", full)
        if m:
            out["arxiv"].append(m.group(1))
        m = re.search(r"(PMC\d+)", full)
        if m and ("ncbi.nlm.nih.gov" in h):
            out["pmcid"].append(m.group(1))
        m = re.search(r"(?:bio|med)rxiv\.org/content/(?:early/\d{4}/\d{2}/\d{2}/)?(10\.\d{4,5}/[0-9.]+?)(?:v\d+)?(?:\.full|\.source|\.pdf|\.abstract|$|/)", full)
        if m:
            out["doi"].append(m.group(1).rstrip("."))
        elif re.search(r"(?:bio|med)rxiv\.org/content/(10\.\d+/[0-9.]+)", full):
            out["doi"].append(re.search(r"(?:bio|med)rxiv\.org/content/(10\.\d+/[0-9.]+)", full).group(1).rstrip("."))
        m = re.search(r"doi\.org/(10\.\d{4,9}/[^\s?#]+)", full)
        if m:
            out["doi"].append(m.group(1))
        m = re.search(r"science\.org/doi/(?:full/|abs/|pdf/)?(10\.1126/[^\s?#]+)", full)
        if m:
            out["doi"].append(m.group(1))
        m = re.search(r"nature\.com/articles/(s\d{5}-\d{3}-\d{5}-[\dxX]|s\d{5}-\d{3}-\d{5}-\d+|[a-z]\d{5,}-\d{3}-\d{5}-\w)", full)
        if m:
            out["doi"].append("10.1038/" + m.group(1))
        elif "nature.com/articles/" in full:
            m = re.search(r"nature\.com/articles/([A-Za-z0-9._-]+)", full)
            if m:
                out["doi"].append("10.1038/" + m.group(1))
        m = re.search(r"link\.springer\.com/article/(10\.\d{4,9}/[^\s?#]+)", full)
        if m:
            out["doi"].append(m.group(1))
        m = re.search(r"biomedcentral\.com/articles/(10\.\d{4,9}/[^\s?#]+)", full)
        if m:
            out["doi"].append(m.group(1))
        m = re.search(r"journals\.plos\.org/.*[?&]id=(10\.\d{4,9}/[^\s&#]+)", full)
        if m:
            out["doi"].append(m.group(1))
        m = re.search(r"elifesciences\.org/articles/(\d+)", full)
        if m:
            out["doi"].append("10.7554/eLife." + m.group(1))
        m = re.search(r"(?:pnas\.org|embopress\.org|frontiersin\.org|academic\.oup\.com|aacrjournals\.org|wiley\.com)/.*?(10\.\d{4,9}/[^\s?#]+)", full)
        if m:
            out["doi"].append(m.group(1))
        m = re.search(r"cell\.com/.*/fulltext/(S[\dX-]+\(\d+\)[\dX-]+-[\dX])", full)
        if m:
            out["pii"].append(m.group(1))
        m = re.search(r"sciencedirect\.com/science/article/(?:abs/)?pii/(S\w+)", full)
        if m:
            out["pii"].append(m.group(1))
        m = re.search(r"github\.com/([\w.-]+)/([\w.-]+)", full)
        if m and h == "github.com":
            out["github"].append(f"{m.group(1)}/{m.group(2)}")
        m = re.search(r"proceedings\.neurips\.cc|proceedings\.mlr\.press", full)
        if m:
            out["other"].append(u)
    for k in out:
        seen, res = set(), []
        for v in out[k]:
            v = v.rstrip(").,;")
            if v not in seen:
                seen.add(v)
                res.append(v)
        out[k] = res
    return out


# ---------------------------------------------------------------- text helpers
def html_to_text(content, selectors=("div.c-article-body", "div#main-content", "article", "main", "body")):
    soup = BeautifulSoup(content, "lxml")
    for t in soup(["script", "style", "nav", "footer", "header", "noscript", "svg", "form"]):
        t.decompose()
    node = None
    for sel in selectors:
        node = soup.select_one(sel)
        if node is not None and len(node.get_text(" ", strip=True)) > 3000:
            break
    node = node or soup
    text = node.get_text("\n", strip=True)
    return re.sub(r"\n{3,}", "\n\n", text)


def jats_to_text(xml_bytes):
    root = etree.fromstring(xml_bytes, parser=etree.XMLParser(recover=True, resolve_entities=False, no_network=True))
    parts = []
    for tag in ("article-title", "abstract"):
        for el in root.iter(tag):
            parts.append("".join(el.itertext()))
    for body in root.iter("body"):
        for sec in body.iter():
            if sec.tag in ("p", "title", "caption", "td", "th", "label"):
                parts.append(" ".join("".join(sec.itertext()).split()))
    return "\n".join(p for p in parts if p)


def pdf_to_text(pdf_path, txt_path):
    subprocess.run(["pdftotext", "-nopgbrk", str(pdf_path), str(txt_path)], check=False, timeout=180,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        return Path(txt_path).read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return ""


# ---------------------------------------------------------------- commands
def cmd_ids(rows, data):
    for r in rows:
        d = data / r["id"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "ids.json").write_text(json.dumps(parse_ids(r), indent=1), encoding="utf-8")
    print("ids written for", len(rows), "rows")


def crossref(doi):
    r, st = polite_get("https://api.crossref.org/works/" + quote(doi, safe="/"))
    if r is not None and r.status_code == 200:
        m = r.json()["message"]
        yr = None
        for k in ("published", "published-print", "published-online", "issued", "created"):
            dp = (m.get(k) or {}).get("date-parts") or [[None]]
            if dp[0] and dp[0][0]:
                yr = dp[0][0]
                break
        return {"title": " ".join(m.get("title") or []), "container": " ".join(m.get("container-title") or []),
                "year": yr, "type": m.get("type"), "authors": [f"{a.get('family','')}, {a.get('given','')}" for a in m.get("author", [])][:40],
                "relation": m.get("relation", {}), "license": [x.get("URL") for x in m.get("license", [])][:3],
                "pii": m.get("alternative-id", []), "doi": m.get("DOI")}
    return {"error": st}


def arxiv_meta(aid):
    """export.arxiv.org does not resolve from this environment, so read the abstract page's citation meta tags."""
    r, st = polite_get(f"https://arxiv.org/abs/{aid}")
    if r is not None and r.status_code == 200:
        soup = BeautifulSoup(r.content, "lxml")

        def meta(name, many=False):
            tags = soup.find_all("meta", attrs={"name": name})
            vals = [" ".join((x.get("content") or "").split()) for x in tags]
            return vals if many else (vals[0] if vals else "")

        sub = soup.find("div", class_="submission-history")
        return {"title": meta("citation_title"), "published": meta("citation_date").replace("/", "-"),
                "updated": meta("citation_online_date").replace("/", "-"), "authors": meta("citation_author", True)[:40],
                "abstract": meta("citation_abstract"), "journal_ref": "", "comment": "",
                "doi": meta("citation_doi"), "history": " ".join(sub.get_text(" ").split())[:400] if sub else ""}
    return {"error": st}


def europepmc(query):
    r, st = polite_get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=" + quote(query) +
                       "&format=json&resultType=core&pageSize=3")
    if r is not None and r.status_code == 200:
        res = r.json().get("resultList", {}).get("result", [])
        if res:
            x = res[0]
            return {"title": x.get("title"), "year": x.get("pubYear"), "journal": (x.get("journalInfo") or {}).get("journal", {}).get("title"),
                    "pmcid": x.get("pmcid"), "doi": x.get("doi"), "abstract": x.get("abstractText"),
                    "isOpenAccess": x.get("isOpenAccess"), "source": x.get("source"), "id": x.get("id"),
                    "authors": x.get("authorString"), "license": x.get("license"), "pubTypeList": x.get("pubTypeList")}
    return {"error": st}


def openalex(doi=None, title=None):
    if doi:
        url = "https://api.openalex.org/works/doi:" + quote(doi, safe="/")
    else:
        url = "https://api.openalex.org/works?per-page=3&filter=title.search:" + quote(re.sub(r"[^\w\s-]", " ", title)[:200])
    r, st = polite_get(url)
    if r is not None and r.status_code == 200:
        j = r.json()
        if "results" in j:
            j = j["results"][0] if j["results"] else {}
        if j:
            loc = j.get("best_oa_location") or {}
            return {"title": j.get("display_name"), "year": j.get("publication_year"), "date": j.get("publication_date"),
                    "doi": j.get("doi"), "type": j.get("type"), "venue": ((j.get("primary_location") or {}).get("source") or {}).get("display_name"),
                    "oa": (j.get("open_access") or {}).get("is_oa"), "oa_pdf": loc.get("pdf_url"), "oa_landing": loc.get("landing_page_url"),
                    "authors": [a["author"]["display_name"] for a in j.get("authorships", [])][:40]}
    return {"error": st}


def biorxiv_api(doi):
    server = "medrxiv" if "medrxiv" in doi else "biorxiv"
    r, st = polite_get(f"https://api.biorxiv.org/details/{server}/{doi}")
    if r is not None and r.status_code == 200:
        c = r.json().get("collection", [])
        if c:
            x = c[-1]
            return {"title": x.get("title"), "authors": x.get("authors"), "date": x.get("date"), "version": x.get("version"),
                    "published": x.get("published"), "license": x.get("license"), "category": x.get("category"),
                    "abstract": x.get("abstract"), "jatsxml": x.get("jatsxml"), "server": server,
                    "corresponding": x.get("author_corresponding")}
    return {"error": st}


def one_meta(r, data):
    d = data / r["id"]
    ids = json.loads((d / "ids.json").read_text(encoding="utf-8"))
    meta = {"id": r["id"], "csv_title": r["title"], "csv_year": r["year"]}
    doi = ids["doi"][0] if ids["doi"] else None
    if doi:
        meta["doi"] = doi
        if doi.startswith(("10.1101/", "10.64898/")):
            meta["biorxiv"] = biorxiv_api(doi)
        meta["crossref"] = crossref(doi)
        meta["europepmc"] = europepmc(f'DOI:"{doi}"')
    if ids["arxiv"]:
        meta["arxiv"] = arxiv_meta(ids["arxiv"][0])
    if ids["pmcid"]:
        meta["europepmc_pmc"] = europepmc("PMCID:" + ids["pmcid"][0])
    if not (doi or ids["arxiv"] or ids["pmcid"]) and r["kind"] in ("journal", "preprint", "proceedings") and not r["title"].startswith("("):
        clean = re.sub(r"\.\.\.|\(.*?\)", "", r["title"]).strip()
        ep = europepmc('TITLE:"' + re.sub(r'[\"]', " ", clean)[:160] + '"')
        if "error" in ep or not ep.get("title"):
            ep = openalex(title=clean)
            meta["openalex_title"] = ep
        else:
            meta["europepmc_title"] = ep
    (d / "meta.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False), encoding="utf-8")
    return r["id"]


def meta_complete(r, data):
    p = data / r["id"] / "meta.json"
    if not p.exists():
        return False
    try:
        m = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return False
    return not any(isinstance(v, dict) and "error" in v and v.get("error") not in ("200", "404") for v in m.values())


def cmd_meta(rows, data, workers=6):
    rows = [r for r in rows if not meta_complete(r, data)]
    print("rows to fetch:", len(rows), flush=True)
    with ThreadPoolExecutor(workers) as ex:
        for i in ex.map(lambda r: one_meta(r, data), rows):
            pass
    print("meta written for", len(rows), "rows")


def save_htmlmeta(d, content, url):
    """Keep the citation_* meta tags of a fetched HTML page as metadata (title, DOI, date, journal, authors)."""
    try:
        soup = BeautifulSoup(content, "lxml")
        out = {"url": url}
        for name in ("citation_title", "citation_doi", "citation_publication_date", "citation_online_date", "citation_date",
                     "citation_journal_title", "citation_abstract", "dc.title", "dc.date", "og:title", "description"):
            tags = soup.find_all("meta", attrs={"name": name}) or soup.find_all("meta", attrs={"property": name})
            vals = [" ".join((x.get("content") or "").split()) for x in tags]
            if vals:
                out[name] = vals[0]
        authors = [" ".join((x.get("content") or "").split()) for x in soup.find_all("meta", attrs={"name": "citation_author"})]
        if authors:
            out["citation_author"] = authors[:30]
        if soup.title and soup.title.string:
            out["page_title"] = " ".join(soup.title.string.split())[:300]
        (d / "htmlmeta.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    except Exception:
        pass


def save_text(d, text, source, kind):
    (d / "fulltext.txt").write_text(text, encoding="utf-8")
    (d / "fulltext_source.txt").write_text(f"{kind}\t{source}\t{len(text)} chars\n", encoding="utf-8")


def try_text(r, data):
    d = data / r["id"]
    ids = json.loads((d / "ids.json").read_text(encoding="utf-8"))
    meta = json.loads((d / "meta.json").read_text(encoding="utf-8")) if (d / "meta.json").exists() else {}
    log = []
    ft = d / "fulltext.txt"
    if ft.exists() and ft.stat().st_size > 12000:
        return r["id"], "cached"

    def ok(text):
        return text and len(text) > 12000

    # 1. Europe PMC full text XML (open access subset)
    pmcids = list(ids["pmcid"])
    for k in ("europepmc", "europepmc_pmc", "europepmc_title"):
        p = (meta.get(k) or {}).get("pmcid")
        if p and p not in pmcids:
            pmcids.append(p)
    for p in pmcids[:2]:
        resp, st = polite_get(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{p}/fullTextXML")
        log.append(f"epmc {p} {st}")
        if resp is not None and resp.status_code == 200 and len(resp.content) > 5000:
            text = jats_to_text(resp.content)
            if ok(text):
                save_text(d, text, f"europepmc:{p}", "jats")
                (d / "tried.txt").write_text("\n".join(log), encoding="utf-8")
                return r["id"], "epmc"
    # 1b. published version of a preprint (bioRxiv API 'published' field, Crossref relation)
    pubs = []
    pub = (meta.get("biorxiv") or {}).get("published")
    if pub and pub != "NA":
        pubs.append(pub)
    for rel in (((meta.get("crossref") or {}).get("relation") or {}).get("is-preprint-of") or []):
        if rel.get("id-type") == "doi" and rel["id"] not in pubs:
            pubs.append(rel["id"])
    for pdoi in pubs[:1]:
        ep = europepmc(f'DOI:"{pdoi}"')
        pm = ep.get("pmcid")
        log.append(f"published {pdoi} pmcid={pm}")
        if pm:
            resp, st = polite_get(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pm}/fullTextXML")
            log.append(f"epmc-published {pm} {st}")
            if resp is not None and resp.status_code == 200 and len(resp.content) > 5000:
                text = jats_to_text(resp.content)
                if ok(text):
                    save_text(d, text, f"europepmc:{pm} (published version {pdoi})", "jats-published")
                    (d / "tried.txt").write_text("\n".join(log), encoding="utf-8")
                    return r["id"], "epmc-published"
        resp, st = polite_get(f"https://doi.org/{pdoi}", timeout=90)
        log.append(f"doi.org {pdoi} {st}")
        if resp is not None and resp.status_code == 200 and "html" in resp.headers.get("content-type", ""):
            text = html_to_text(resp.content)
            if ok(text) and "Just a moment" not in text[:2000]:
                save_text(d, text, resp.url + f" (published version {pdoi})", "html-published")
                (d / "tried.txt").write_text("\n".join(log), encoding="utf-8")
                return r["id"], "html-published"
    # 2. arXiv pdf
    for a in ids["arxiv"][:1]:
        resp, st = polite_get(f"https://arxiv.org/pdf/{a}", timeout=120)
        log.append(f"arxiv {a} {st}")
        if resp is not None and resp.status_code == 200 and resp.content[:4] == b"%PDF":
            (d / "raw.pdf").write_bytes(resp.content)
            text = pdf_to_text(d / "raw.pdf", d / "raw_pdf.txt")
            if ok(text):
                save_text(d, text, f"arxiv:{a}", "pdf")
                (d / "tried.txt").write_text("\n".join(log), encoding="utf-8")
                return r["id"], "arxiv"
    # 3. direct html on open publishers
    cand = []
    for u in urls_of(r):
        h = urlparse(u).hostname or ""
        if r["kind"] in ("org-page", "news", "blog", "social", "talk", "NA") and "github.com" not in h:
            cand.append(u)
            continue
        if any(x in h for x in ("nature.com", "springer.com", "biomedcentral.com", "plos.org", "mdpi.com", "frontiersin.org",
                                "elifesciences.org", "huggingface.co", "readthedocs.io", "github.io", "genome.cshlp.org",
                                "proceedings.neurips.cc", "proceedings.mlr.press", "pnas.org", "embopress.org", "zenodo.org",
                                "parsebiosciences.com", "arcinstitute.org", "virtualcellchallenge.org", "deepmind.google",
                                "platform-docs.opentargets.org", "pharmvar.org", "cpicpgx.org", "omnipathdb.org", "ai.meta.com",
                                "genbio.ai", "idekerlab.ucsd.edu", "broadinstitute.org", "hal-emse.ccsd.cnrs.fr", "alphaxiv.org")):
            cand.append(u)
    for u in cand[:3]:
        resp, st = polite_get(u, timeout=90)
        log.append(f"html {u} {st}")
        if resp is None or resp.status_code != 200:
            continue
        if resp.content[:4] == b"%PDF":
            (d / "raw.pdf").write_bytes(resp.content)
            text = pdf_to_text(d / "raw.pdf", d / "raw_pdf.txt")
        else:
            (d / "raw.html").write_bytes(resp.content)
            save_htmlmeta(d, resp.content, u)
            text = html_to_text(resp.content)
        if ok(text):
            save_text(d, text, u, "html")
            (d / "tried.txt").write_text("\n".join(log), encoding="utf-8")
            return r["id"], "html"
        elif text and len(text) > (ft.stat().st_size if ft.exists() else 0):
            save_text(d, text, u, "html-short")
    # 3b. doi.org redirect for rows with a DOI that is not a bioRxiv/medRxiv DOI
    for doi in ids["doi"][:1]:
        if doi.startswith(("10.1101/", "10.64898/")):
            break
        resp, st = polite_get(f"https://doi.org/{doi}", timeout=90)
        log.append(f"doi.org {doi} {st}")
        if resp is not None and resp.status_code == 200:
            if resp.content[:4] == b"%PDF":
                (d / "raw.pdf").write_bytes(resp.content)
                text = pdf_to_text(d / "raw.pdf", d / "raw_pdf.txt")
            elif "html" in resp.headers.get("content-type", ""):
                save_htmlmeta(d, resp.content, resp.url)
                text = html_to_text(resp.content)
            else:
                text = ""
            if ok(text) and "Just a moment" not in text[:2000]:
                save_text(d, text, resp.url, "doi.org")
                (d / "tried.txt").write_text("\n".join(log), encoding="utf-8")
                return r["id"], "doi.org"
    # 4. OpenAlex OA pdf / landing
    for k in ("openalex", "openalex_title"):
        o = meta.get(k) or {}
        for u in (o.get("oa_pdf"), o.get("oa_landing")):
            if not u or "biorxiv.org" in u or "arxiv.org" in u:
                continue
            resp, st = polite_get(u, timeout=90)
            log.append(f"oa {u} {st}")
            if resp is not None and resp.status_code == 200:
                if resp.content[:4] == b"%PDF":
                    (d / "raw.pdf").write_bytes(resp.content)
                    text = pdf_to_text(d / "raw.pdf", d / "raw_pdf.txt")
                else:
                    text = html_to_text(resp.content)
                if ok(text):
                    save_text(d, text, u, "oa")
                    (d / "tried.txt").write_text("\n".join(log), encoding="utf-8")
                    return r["id"], "oa"
    (d / "tried.txt").write_text("\n".join(log), encoding="utf-8")
    return r["id"], "none"


def cmd_text(rows, data, workers=6):
    res = {}
    with ThreadPoolExecutor(workers) as ex:
        for i, how in ex.map(lambda r: try_text(r, data), rows):
            res[i] = how
    import collections
    print(collections.Counter(res.values()))
    (data / "_text_status.json").write_text(json.dumps(res, indent=1), encoding="utf-8")


if __name__ == "__main__":
    cmd, repo, data = sys.argv[1], sys.argv[2], Path(sys.argv[3])
    data.mkdir(parents=True, exist_ok=True)
    rows = load_rows(repo)
    if len(sys.argv) > 4 and sys.argv[4]:
        want = set(sys.argv[4].split(","))
        rows = [r for r in rows if r["id"] in want]
    {"ids": cmd_ids, "meta": cmd_meta, "text": cmd_text}[cmd](rows, data)
