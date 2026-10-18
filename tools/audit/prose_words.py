"""Count English prose words (paragraphs only: no blockquotes, tables, code, headings or generated blocks) of a markdown file.
Usage: python3 -I prose_words.py <file.md> [<other.md> ...]"""
import re, sys
def words(path):
    text = open(path, encoding="utf-8").read()
    text = re.sub(r"<!--.*?:start -->.*?<!--.*?:end -->", "", text, flags=re.S)
    n = 0
    for p in re.split(r"\n\s*\n", text):
        p = p.strip()
        if not p or p[0] in ">|#`<":
            continue
        n += len(p.split())
    return n
for f in sys.argv[1:]:
    print(f, words(f))
