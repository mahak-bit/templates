"""Read real page numbers from the PDF's named destinations (one per linked anchor) -> pages.json."""
import json, sys
from pypdf import PdfReader
pdf, out = sys.argv[1], sys.argv[2]
r = PdfReader(pdf)
pages = {k.lstrip('/'): r.get_destination_page_number(v) + 1 for k, v in r.named_destinations.items()}
json.dump(pages, open(out, "w"), indent=1)
need = ['sec-licence','sec-intro','sec-quick','sec-finder','sec-anatomy','sec-brief','sec-example','sec-checklist','sec-closing'] \
     + [f'cat-{i}' for i in range(1,11)] + [f'p-{i}' for i in range(1,51)]
missing = [k for k in need if k not in pages]
print("destinations:", len(pages), "| missing:", missing)
sys.exit(1 if missing else 0)
