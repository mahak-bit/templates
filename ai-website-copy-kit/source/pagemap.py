"""Read real page numbers from the PDF outline (bookmarks) -> pages.json.
Maps our anchor ids to the physical page on which each section heading lands."""
import json, re, sys
from pypdf import PdfReader
from prompts import CATEGORIES
import matter as M

pdf, out = sys.argv[1], sys.argv[2]
r = PdfReader(pdf)
flat = []
def walk(items):
    for it in items:
        if isinstance(it, list): walk(it)
        else: flat.append((it.title.strip(), r.get_destination_page_number(it) + 1))
walk(r.outline)
norm = lambda s: re.sub(r"\s+", "", s).lower()
by_title = {}
for t, p in flat: by_title.setdefault(norm(t), []).append(p)

want = {
  "sec-licence": M.LICENCE["heading"], "sec-intro": M.INTRO["heading"], "sec-quick": M.QUICKSTART["heading"],
  "sec-finder": M.FINDER["heading"], "sec-anatomy": M.ANATOMY["heading"], "sec-brief": M.BRIEF["heading"],
  "sec-example": "Saltgrain Bakehouse", "sec-checklist": M.CHECKLIST["heading"], "sec-closing": M.CLOSING["heading"],
}
for c in CATEGORIES:
    want[f"cat-{c['n']}"] = c["title"]
    for p in c["prompts"]: want[f"p-{p['n']}"] = p["title"]
pages, missing = {}, []
for k, title in want.items():
    ps = by_title.get(norm(title))
    if not ps: missing.append(k); continue
    pages[k] = ps[-1] if k.startswith("sec-") and k in ("sec-closing",) else ps[0]
json.dump(pages, open(out, "w"), indent=1)
print("outline entries:", len(flat), "| mapped:", len(pages), "| missing:", missing)
