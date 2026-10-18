"""Second chance for rows without an abstract: resolve PII (Cell Press, Elsevier) to a DOI through Crossref, then get the
PubMed abstract through Europe PMC; also try Europe PMC by title for rows that still have no abstract."""
import importlib.util, json, re, sys
from pathlib import Path
from urllib.parse import quote
scr = Path(sys.argv[1])
spec = importlib.util.spec_from_file_location('kbaudit', scr / 'kbaudit.py'); kb = importlib.util.module_from_spec(spec); spec.loader.exec_module(kb)
data = scr / 'audit_data'
rows = kb.load_rows(sys.argv[2])
fixed = 0
for r in rows:
    d = data / r['id']
    mp = d / 'meta.json'
    if not mp.exists():
        continue
    meta = json.loads(mp.read_text(encoding='utf-8'))
    have_abs = any((meta.get(k) or {}).get('abstract') for k in ('biorxiv', 'arxiv', 'europepmc', 'europepmc_pmc', 'europepmc_title'))
    ft = d / 'fulltext.txt'
    if have_abs or (ft.exists() and ft.stat().st_size > 12000) or r['kind'] in ('repo', 'org-page', 'news', 'blog', 'social', 'talk'):
        continue
    ids = json.loads((d / 'ids.json').read_text(encoding='utf-8'))
    doi = None
    for pii in ids['pii'][:1]:
        resp, st = kb.polite_get('https://api.crossref.org/works?rows=2&filter=alternative-id:' + quote(pii))
        if resp is not None and resp.status_code == 200:
            items = resp.json()['message'].get('items', [])
            if items:
                m = items[0]
                doi = m.get('DOI')
                meta['crossref_pii'] = {'title': ' '.join(m.get('title') or []), 'container': ' '.join(m.get('container-title') or []),
                                        'doi': doi, 'year': ((m.get('issued') or {}).get('date-parts') or [[None]])[0][0]}
    if not doi:
        doi = ids['doi'][0] if ids['doi'] else None
    ep = {}
    if doi:
        ep = kb.europepmc(f'DOI:"{doi}"')
    if (not ep or not ep.get('abstract')) and not r['title'].startswith('('):
        clean = re.sub(r"\.\.\.|\(.*?\)", '', r['title']).strip()
        ep2 = kb.europepmc('TITLE:"' + re.sub(r'[\\"]', ' ', clean)[:160] + '"')
        if ep2 and ep2.get('abstract'):
            ep = ep2
    if ep and ep.get('abstract'):
        meta['europepmc_extra'] = ep
        mp.write_text(json.dumps(meta, indent=1, ensure_ascii=False), encoding='utf-8')
        fixed += 1
        print(r['id'], 'abstract from europepmc', (meta.get('crossref_pii') or {}).get('doi') or doi)
    else:
        mp.write_text(json.dumps(meta, indent=1, ensure_ascii=False), encoding='utf-8')
        print(r['id'], 'still no abstract', doi)
print('fixed', fixed)
