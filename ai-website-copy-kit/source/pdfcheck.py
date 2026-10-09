"""PDF-level fragmentation check: every text fragment of section i must appear on PDF page i (and the
page count must equal the section count). Catches spill/overlap that DOM measurement can miss."""
import json, re, sys
from pypdf import PdfReader
leaves = json.load(open(sys.argv[1])); r = PdfReader(sys.argv[2])
n = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
print("sections", len(leaves), "| pdf pages", len(r.pages))
bad = 0
if len(leaves) != len(r.pages): print("PAGE COUNT MISMATCH"); bad += 1
for sec in leaves:
    page = n(r.pages[sec["i"] - 1].extract_text())
    miss = [l for l in sec["leaves"] if n(l) and n(l) not in page]
    if miss:
        bad += 1; print(f"  page {sec['i']} ({sec['id']}): {len(miss)} fragments not on this page, e.g. {miss[0][:60]!r}")
print("FRAGMENTATION PROBLEMS:", bad)
sys.exit(1 if bad else 0)
