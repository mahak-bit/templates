# The AI Website Copy Kit

*50 Ready-to-Use AI Prompts for Better Website Content*

| File | What it is |
|---|---|
| `dist/The-AI-Website-Copy-Kit.pdf` | **The product.** 84-page A4 PDF, ivory / charcoal / cobalt, Playfair Display + Inter, clickable contents and bookmarks |
| `dist/AI-Website-Copy-Kit-Prompt-Library.txt` | All 50 prompts as clean plain text for copy-paste (PDF copying can add line breaks) |
| `dist/The-AI-Website-Copy-Kit-editable.docx` | Editable Word version of the whole kit |
| `dist/Client-and-Business-Brief-fillable.docx` | The reusable brief on its own, for typing into or sending to clients |
| `canva/Canva-Page-Plan.md` | Page-by-page Canva rebuild plan for the redesign (specs, layouts, all 84 pages) |
| `source/` | Single source of truth (`prompts.py`, `matter.py`) and build scripts |

Rebuild: `./build.sh` (needs python3 with pypdf and python-docx, node with playwright, Chromium, Inter installed).
Before selling: set `PUBLISHER` in `source/matter.py` if you want your name on the licence page, then rebuild.
