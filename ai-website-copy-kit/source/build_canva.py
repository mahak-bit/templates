# -*- coding: utf-8 -*-
import os, json
from prompts import CATEGORIES
import matter as M
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=json.load(open(os.path.join(ROOT,'_build','pages3.json')))
o=[]
w=o.append
w(f"# Canva Page Plan: {M.TITLE}\n")
w(f"*{M.SUBTITLE}* · 80 pages · A4 portrait\n")
w("""> **Honest note.** I could not create a native Canva file from this environment (no Canva tool is connected). The finished PDF in `dist/` is the product. This plan lets you rebuild or restyle it in Canva exactly, page by page. Canva's PDF import may also give you an editable starting point, but I have not tested how faithfully it converts, so check fonts and spacing after importing.

---

## 1. Document setup
| Setting | Value |
|---|---|
| Size | A4 portrait, 210 × 297 mm (Canva: Custom size, mm) |
| Margins (content pages) | Top 20 · Left/Right 18 · Bottom 22 mm. Use Canva's *Show margins* guides |
| Full-bleed pages | Cover, 10 category dividers, closing page: no margins, background fills the page |
| Footer (content pages only) | Left: *THE AI WEBSITE COPY KIT* · Inter Medium 6.8 pt, +140 tracking, uppercase, charcoal 62%. Right: page number · Inter Medium 8 pt, cobalt. Baseline about 12 mm from the bottom edge |

## 2. Colour palette (add as Brand Kit colours)
| Name | Hex | Use |
|---|---|---|
| Warm Ivory | `#F9F8F6` | Page background on all content pages; text on cobalt pages |
| Charcoal | `#161616` | Body text, headings, rules, checkbox outlines |
| Cobalt Blue | `#002FA7` | Kickers, placeholders, numerals, rules, buttons, divider and closing backgrounds |
| Charcoal tint | `#161616` at 4.5% opacity | Prompt box fill (or use `#F1F0EE`) |
| Cobalt tint | `#002FA7` at 6–10% opacity | Callout fill, [NEEDS INFO] highlight |

Never add other colours. Contrast: charcoal on ivory and ivory on cobalt are both comfortably readable.

## 3. Typography
Fonts: **Playfair Display** (headings, numerals, pull-quotes) and **Inter** (body, labels, tables). Both are open-source and, to my knowledge, in Canva's library; confirm in the font picker. Sizes below are print points (pt). On a Canva A4 document the on-screen font-size box is in px-like units, roughly pt × 1.33, so tune by eye.

| Style | Font | Size / leading | Notes |
|---|---|---|---|
| Cover title | Playfair Display SemiBold | 60 / 59 | "Website" in Playfair Italic, cobalt |
| Divider numeral | Playfair Display SemiBold | 168 / 150 | Ivory, tracking −50 |
| Divider title | Playfair Display SemiBold | 36 / 39 | Ivory |
| Page title (H1) | Playfair Display SemiBold | 31 / 33 (prompt pages 28) | Charcoal |
| Section head (H2) | Playfair Display SemiBold | 17 / 20 | |
| Lead / intro line | Playfair Display Italic | 13 / 19 (prompt "use it when": 12) | |
| Body | Inter Regular | 9.6 / 15 | |
| Prompt text | Inter Regular | 9.1 / 14.4 | Inside prompt box |
| Kicker / label | Inter SemiBold | 6.8–7 / 8, +180–200 tracking, uppercase | Cobalt (or charcoal 68% for secondary) |
| Placeholder | Inter SemiBold | same as surrounding text | Cobalt `#002FA7` |
| AI marker `[NEEDS INFO: …]` | Inter SemiBold | same | Charcoal on cobalt 10% tint |

## 4. Grid and components
* **Grid:** one 174 mm text column. Two-column layouts use two 82 mm columns with a 10 mm gutter.
* **Rules:** thin charcoal rule 0.35 mm under page headers; light rule (charcoal 16%) 0.25 mm between table rows; short cobalt accent rule 18 × 0.8 mm under H1 on front-matter pages.
* **Prompt box:** rectangle fill charcoal 4.5%, 0.9 mm cobalt rule on the left edge, 6 mm inner padding, text left-aligned, no justification.
* **Callout (plain):** cobalt 6% fill, no edge rule, 5 mm padding.
* **Bullets:** 1.6 mm cobalt squares, 5 mm indent.
* **Checkbox:** 3.6 mm square, 0.35 mm charcoal outline, no fill.
* **Button (example pages):** cobalt fill, ivory Inter SemiBold 8 pt text, 2.2 × 4 mm padding, 0.6 mm corner radius.
* **Imagery:** none. The system is typographic; whitespace and the cobalt blocks carry the design. Avoid stock photos and icons.

---

## 5. Master layouts (build these six as templates, then duplicate)
**A. Cover (p.1).** Ivory background. Cobalt panel right: x 144–210 mm, full height. Left column x 20 mm, width 118 mm: kicker "A PRACTICAL PROMPT LIBRARY" at y 28; title block starts y 90 (three lines: *The AI / Website / Copy Kit*); 18 mm cobalt rule; subtitle Inter 13.5 pt, 96 mm wide. Bottom-left (y ≈ 262): audience line Inter Medium 8 pt, then "EDITION 1.0 · 2026" cobalt label. In the panel: "50" Playfair 140 pt ivory at x 152, bottom aligned to y 241; "PROMPTS" Inter SemiBold 8 pt +300 tracking beneath; one 8.4 pt line of description at the bottom.

**B. Front-matter page.** Ivory, margins as above. Kicker (cobalt, 7 pt) → H1 → cobalt accent rule → lead line → content.

**C. Category divider (10 pages).** Full-bleed cobalt. Kicker "CATEGORY 0N / 10" top-left at 20 × 20 mm. Large numeral at 20 × 30 mm. Title at y 104 mm (36 pt, max 150 mm wide). Blurb Inter 11.2 pt, 142 mm wide. List of the five prompts: number in Playfair SemiBold 10 pt, title in Inter Medium 10.5 pt, 0.3 mm ivory rules at 35–55% opacity between rows. "SUGGESTED ORDER" label and one sentence anchored at y 262 mm.

**D. Prompt page (50 pages).** Ivory. Top row: category kicker (left, charcoal 68%) and "PROMPT N / 50" (right, cobalt), with a 0.35 mm charcoal rule beneath. H1 (28 pt) → "use it when" line (Playfair Italic 12) → label "FILL IN" → two-column table (placeholder in cobalt, 62 mm; hint, remaining width) → small line "Also uses from your brief:" with Core Six placeholders in cobalt → label "THE PROMPT — COPY EVERYTHING IN THE BOX" → prompt box → "TIP" label (cobalt) with one sentence.

**E. Brief form page.** Two-column grid of questions (Inter 8.3 pt) each followed by an 8 mm writing line (0.3 mm charcoal 32%). Section headers: cobalt Playfair letter (15 pt) + uppercase label with a 0.35 mm charcoal rule beneath.

**F. Checklist page.** Two columns; group title Playfair 12 pt with rule; each item = checkbox + Inter 8.7 pt text.

**Closing (p.80).** Full-bleed cobalt; kicker, "Thank You" 46 pt, lead, three numbered next steps between ivory rules, closing sentence in Playfair Italic 17 pt at the bottom.

---

## 6. Page-by-page build list
Content source for every page: the files in `source/` (`prompts.py`, `matter.py`) or the editable DOCX.

| Page | Layout | Content |
|---|---|---|
| 1 | A | Cover |
""")
rows=[]
def add(pg,lay,txt): rows.append((pg,lay,txt))
add(P['sec-licence'],'B',"Licence & Notes: six definition rows (term in Playfair 10 pt, text in Inter 9.2 pt), small print at the foot")
add(3,'B',"Contents: three grouped lists (Start here / The 50 prompts / Put it into practice) with dotted-style row rules and cobalt page numbers")
add(4,'B',"All 50 prompts: two-column index grouped by category, cobalt prompt numbers and page numbers")
add(P['sec-intro'],'B',"Introduction: lead line, two paragraphs, two-column lists (Who it is for / What is inside), callout *What it is not*")
add(P['sec-quick'],'B',"Quick-Start Guide: five numbered steps (cobalt Playfair numerals 21 pt, time estimate right-aligned), then two bullet columns")
add(P['sec-finder'],'B',"Which Prompt Do I Need?: 11-row table (situation, prompt numbers in cobalt) and a six-to-nine-cell *sensible order* strip")
add(P['sec-anatomy'],'B',"How Every Prompt Works: four definition rows, Fact Guard in a prompt box, marker definitions")
add(P['sec-brief'],'E',"Brief part 1: the Core Six as a 2×3 grid of cells with cobalt top rules and writing space")
add(P['sec-brief']+1,'E',"Brief part 2: sections A–D, two columns")
add(P['sec-brief']+2,'E',"Brief part 3: sections E–I, two columns")
add(P['sec-brief']+3,'B',"Your Context Block: the template in a prompt box")
for c in CATEGORIES:
    add(P[f"cat-{c['n']}"],'C',f"Divider {c['n']:02d}: {c['title']} (blurb, five prompt titles, suggested order)")
    for p in c['prompts']:
        add(P[f"p-{p['n']}"],'D',f"Prompt {p['n']}: {p['title']}")
add(P['sec-example'],'B',"Worked example 1/5: fictional-business notice, eight key facts, Core Six filled in")
add(P['sec-example']+1,'B',"Worked example 2/5: Prompt 1 filled in, three hero angles (headline Playfair 15 pt, sub, cobalt button), recommendation callout")
add(P['sec-example']+2,'B',"Worked example 3/5: custom-cakes service page shown inside a prompt-style box, Fact Guard callout")
add(P['sec-example']+3,'B',"Worked example 4/5: four FAQs, two title/meta examples with character counts")
add(P['sec-example']+4,'B',"Worked example 5/5: seven-line review (Pass/Flag), *What to notice*")
add(P['sec-checklist'],'F',"Quality checklist 1/2: groups 1–4")
add(P['sec-checklist']+1,'F',"Quality checklist 2/2: groups 5–8, red-flag phrase pills (0.3 mm outline, fully rounded), note")
add(P['sec-closing'],'Closing',"Thank You: three next steps and closing line")
rows.sort()
for pg,lay,txt in rows: w(f"| {pg} | {lay} | {txt} |")
w("""
## 7. Canva build steps
1. Create a custom A4 design. Add the three colours and two fonts to a Brand Kit.
2. Build layouts A–F once each, using the measurements above. Group repeated elements (footer, rule, label) and duplicate pages.
3. Paste text from the DOCX or from `AI-Website-Copy-Kit-Prompt-Library.txt`. Then select each placeholder in square brackets and set it to cobalt SemiBold.
4. Turn the contents entries and index entries into page links (Canva: select text → Link → *A page in this design*).
5. Turn off the footer on pages 1, the ten dividers and page 80.
6. Export as **PDF Standard** (screen) and check: all fonts present, no clipped text, page count 80, links work.
""")
open(os.path.join(ROOT,'canva','Canva-Page-Plan.md'),'w',encoding='utf-8').write('\n'.join(o))
print('rows',len(rows)+1)
