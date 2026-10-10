# -*- coding: utf-8 -*-
"""Canva rebuild plan for edition 2 (bracket-motif design). Page numbers come from the real PDF page map."""
import os, json
from prompts import CATEGORIES
import matter as M
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = json.load(open(os.path.join(ROOT, '_build', 'pages3.json')))
o = []; w = o.append
w(f"# Canva Page Plan: {M.TITLE}\n")
w(f"*{M.SUBTITLE}* · 84 pages · A4 portrait · matches `dist/The-AI-Website-Copy-Kit.pdf` (edition 2, bracket-motif design)\n")
w("""> **Honest note.** I could not create a native Canva file from this environment (no Canva tool is connected). The PDF in `dist/` is the finished product; this plan lets you rebuild it in Canva. Canva's PDF import may give you an editable starting point, but I have not tested how faithfully it converts. Check fonts and spacing after importing. Check Canva's current creator rules before listing anything for sale on Canva.

---

## 1. The idea in one line
Every placeholder a buyer fills in is a **[bracket]**. Thin cobalt brackets are the one signature graphic: they frame the cover, the prompt numerals, the prompt cards, the closing page. Nothing else is decorative.

## 2. Document setup
| Setting | Value |
|---|---|
| Size | A4 portrait, 210 × 297 mm (Canva: Custom size, mm) |
| Content-page margins | Top 18 · Left/Right 20 · Bottom 24 mm (content box 170 × 255 mm) |
| Full-bleed pages | Cover, 10 dividers, closing: no margins |
| Page background | Ivory `#F9F8F6` on every light page |
| Footer (content pages only) | Left: *THE AI WEBSITE COPY KIT · MAHAK'S STUDIO*, Inter SemiBold 7.4 pt, +160 tracking, uppercase, charcoal 58%. Right: page number, Playfair Display Medium 11 pt, cobalt, lining numerals. About 14 mm from the bottom edge |
| Running head (content pages) | Top of the content box: left label, right cobalt label, Inter SemiBold 7.6 pt, +200 tracking, uppercase; 0.25 mm charcoal rule beneath; 8 mm gap to content |

## 3. Colour (add to Brand Kit; use nothing else)
| Name | Hex | Use |
|---|---|---|
| Warm Ivory | `#F9F8F6` | Page background; text on dark pages |
| Charcoal | `#161616` | Text, rules, checkbox outlines, Fact Guard card, even-numbered dividers |
| Cobalt Blue | `#002FA7` | Numerals, brackets, kickers, buttons, placeholders, odd-numbered dividers, closing page |
| Placeholder wash | Cobalt at 7% | Behind placeholders on light pages |
| Marker wash | Cobalt at 13% | Behind [NEEDS INFO] / [CHECK] markers |
| Hairline | Charcoal at 18% | Row rules |

On charcoal cards, placeholders flip to an ivory chip with cobalt text.

## 4. Type (Playfair Display + Inter; both open-source, believed to be in Canva's library, so confirm)
Sizes are print points. Canva's size box on an A4 page is roughly pt × 1.33, so tune by eye. **Use lining numerals** in Playfair for all numbers (Canva: if unavailable, check the font's number style or use Inter for numerals).

| Style | Font | Size / leading |
|---|---|---|
| Cover title | Playfair Display Medium, tracking −35, *Website* in Italic cobalt, closing cobalt square after "Kit" | 76 / 73 |
| Divider numeral | Playfair Display Regular, tracking −50 | 200 / 164 |
| Divider title | Playfair Display Medium | 42 / 44 |
| Page title (H1) | Playfair Display Medium | 38 / 40 |
| Prompt title | Playfair Display Medium | 28 / 31 |
| Prompt numeral | Playfair Display Regular, cobalt, inside two thin brackets | 64 |
| Section head | Playfair Display Medium | 19–23 |
| Deck / lead | Playfair Display Italic | 13–14.5 / 20 |
| Body | Inter Regular | 10.4 / 16.6 |
| Prompt text | Inter Regular | 9.8 / 15.4, left-aligned |
| Kicker / label | Inter SemiBold, +200–220 tracking, uppercase | 7.6–7.8 |
| Rail hint text | Inter Regular | 9 / 13 |
| Placeholder chip | Inter SemiBold, cobalt, 7% cobalt wash | same as surrounding |

## 5. Components
* **Bracket.** Two L-shaped strokes (a vertical line with short horizontals toward the content). Cover: 26 × 172 mm, 1.5 mm stroke, cobalt. Prompt card: 5 mm arms, 0.6 mm stroke, full card height, 10 mm text inset. Prompt numeral: 2.6 mm arms, 0.5 mm stroke. Closing page: 22 × 190 mm, 1.4 mm, ivory. Build one, group, duplicate.
* **Kicker.** Cobalt 1.7 mm square, 2.4 mm gap, uppercase label.
* **Numbered rows (contents, quick-start, intro).** 0.3 mm charcoal rule above each row; numeral in Playfair cobalt at left; title in Playfair; description in Inter.
* **Prompt card.** No fill. Brackets left and right. Text inside.
* **Tags (worked example).** Input = charcoal outline; Prompt = cobalt outline; Output = cobalt fill with ivory text. Inter SemiBold 7.4 pt, +200 tracking, uppercase, 1.5 × 2.8 mm padding.
* **Checkbox.** 4.4 mm square, 0.4 mm charcoal outline, no fill.
* **Button (example pages).** Cobalt fill, ivory Inter SemiBold 8.4 pt, 2.6 × 5 mm padding, square corners.
* **Pill (red-flag phrases).** 0.35 mm charcoal outline, fully rounded, Inter Medium 9.2 pt.

---

## 6. Master layouts (build once, duplicate)
**A. Cover (p.1).** Ivory. Top row at y 18 mm: *MAHAK'S STUDIO* (left, charcoal) and *EDITION 1.0 / 2026* (right, cobalt). Brackets: left bracket at x 20, right bracket at x 164 (right edge 190), both y 50–222. Text block at x 46 mm, y 68 mm, 130 mm wide: kicker, title (3 lines), subtitle in Playfair Italic 17 pt. Stat row at y 236 mm: four columns, 0.3 mm charcoal rule above; big cobalt Playfair numeral 34 pt + uppercase label. Audience line at y ≈ 276 mm, Inter 9 pt, charcoal 62%.

**B. Content page.** Running head → kicker → H1 → deck → body. Use for licence, intro, quick-start, anatomy, brief, example, checklist.

**C. Divider (10 pages).** Full bleed. Odd categories cobalt, even categories charcoal. Top row (y 18 mm): *CATEGORY 0N OF 10* left, *THE AI WEBSITE COPY KIT* right, ivory. Numeral at x 17 mm, y 30 mm. Progress index at right (x 181–190 mm, y 34 mm): ten rows 6.2 mm tall, numerals 01–10 in Inter 8 pt; the current one bold with a long ivory dash, others at 50% with a short dash. Title at y 108 mm; blurb Inter 11.4 pt, 136 mm wide; list of five prompts (numeral Playfair 14 pt, title Playfair Medium 12 pt) between 0.3 mm ivory rules. *SUGGESTED ORDER* label and sentence at y 267 mm.

**D. Prompt page (50 pages).** Running head: *CATEGORY 0N — TITLE* left, *PROMPT N / 50* right. Header row: numeral in brackets (left), title (right of it, 28 pt). Body grid: **left rail 54 mm**, gap 9 mm, **right card 107 mm**. Rail, top to bottom: *use it when* in Playfair Italic 11.6 pt with a charcoal rule under it; *FILL IN* label then each placeholder chip with its hint below; *FROM YOUR BRIEF* line in charcoal 62%; *TIP* pinned to the bottom of the rail with a 0.5 mm cobalt rule above. Card: label row (*THE PROMPT* cobalt left, *COPY EVERYTHING BETWEEN THE BRACKETS* grey right), then the bracketed prompt text.

**E. Brief form page.** Section letter in Playfair cobalt 30 pt beside an uppercase label with 0.3 mm charcoal rule; questions in Inter 9.2 pt; each followed by a writing line (0.3 mm, charcoal 34%) 7–12 mm tall (taller on later pages).

**F. Checklist page.** Two-column grid, group numeral Playfair cobalt 22 pt + group title Playfair 13 pt; items with checkbox, hairline rule below each.

**G. Closing (p.84).** Full-bleed cobalt. Ivory brackets (22 × 190 mm) at y 46 mm. Centre text block between brackets: kicker, *Thank You* 58 pt, deck, three numbered next steps between ivory rules. Bottom: closing sentence in Playfair Italic 19 pt left; title and © right.

---

## 7. Page-by-page build list
| Page | Layout | Content |
|---|---|---|
| 1 | A | Cover |
""")
rows = []
add = lambda pg, lay, t: rows.append((pg, lay, t))
add(P['sec-licence'], 'B', "Licence & Notes: six numbered terms in a 2 × 3 grid, colophon at the foot")
add(P['sec-contents'] if 'sec-contents' in P else 3, 'B', "Contents: left rail (Start here / In practice) and ten large numbered categories with page numbers")
add(P['sec-index'] if 'sec-index' in P else 4, 'B', "The 50 prompts at a glance (1/2): categories 1–5 in two columns")
add((P['sec-index'] if 'sec-index' in P else 4) + 1, 'B', "The 50 prompts at a glance (2/2): categories 6–10")
add(P['sec-intro'], 'B', "Introduction: headline in Playfair 41 pt, deck, two-column text with cobalt drop cap, three *Who it is for* columns")
add(P['sec-intro'] + 1, 'B', "Everything you need: five numbered rows, *What it is not* inside brackets")
add(P['sec-quick'], 'B', "Quick-Start Guide: five large-numeral steps with time tags")
add(P['sec-quick'] + 1, 'B', "Follow-up requests, good habits (2 × 2), a sensible order for a five-page site (3 × 3)")
add(P['sec-finder'], 'B', "Which Prompt Do I Need?: eleven rows, prompt numbers as cobalt outlined squares")
add(P['sec-anatomy'], 'B', "How Every Prompt Works: wireframe of a prompt page with four numbered pins, Fact Guard in a charcoal card, marker definitions")
add(P['sec-brief'], 'E', "Brief 1/5: the Core Six as a 2 × 3 grid of cards with writing lines")
for k in range(1, 4):
    add(P['sec-brief'] + k, 'E', f"Brief {k+1}/5: detailed questions, sections {['A–C','D–F','G–I'][k-1]}")
add(P['sec-brief'] + 4, 'B', "Your Context Block: template and the filled Saltgrain example, each inside brackets")
for c in CATEGORIES:
    add(P[f"cat-{c['n']}"], 'C', f"Divider {c['n']:02d} ({'cobalt' if c['n'] % 2 else 'charcoal'}): {c['title']}")
    for p in c['prompts']:
        add(P[f"p-{p['n']}"], 'D', f"Prompt {p['n']}: {p['title']}")
add(P['sec-example'], 'B', "Worked example 1/5: *Saltgrain Bakehouse*, Input lanes (eight facts, Core Six), legend and fictional-business note")
add(P['sec-example'] + 1, 'B', "Worked example 2/5: Prompt 1 filled in, three hero cards, recommendation")
add(P['sec-example'] + 2, 'B', "Worked example 3/5: custom-cakes page in a framed page mock, Fact Guard callout")
add(P['sec-example'] + 3, 'B', "Worked example 4/5: four FAQs, two search-result previews with character counts")
add(P['sec-example'] + 4, 'B', "Worked example 5/5: review ledger (Pass/Flag pills), *What to notice*")
add(P['sec-checklist'], 'F', "Quality Checklist 1/2: groups 1–4")
add(P['sec-checklist'] + 1, 'F', "Quality Checklist 2/2: groups 5–8, red-flag phrase pills")
add(P['sec-closing'], 'G', "Thank You")
rows.sort()
for pg, lay, t in rows: w(f"| {pg} | {lay} | {t} |")
w("""
## 8. Build steps in Canva
1. Create a custom A4 design (210 × 297 mm). Add the three colours and two fonts to a Brand Kit.
2. Build the bracket once, group it, and keep it in your uploads or as a duplicated group.
3. Build layouts A–G once each with the measurements above, then duplicate pages.
4. Paste text from the editable DOCX or `AI-Website-Copy-Kit-Prompt-Library.txt`. Set each [PLACEHOLDER] to cobalt SemiBold.
5. Link the contents and index entries to their pages (Canva: select text → Link → *A page in this design*).
6. Turn the footer off on pages 1, the ten dividers and page 84.
7. Export as **PDF Standard**. Check fonts, page count (84), links, and that prompt text copies cleanly. If it does not, avoid ligatures and contextual alternates in the font settings.
""")
open(os.path.join(ROOT, 'canva', 'Canva-Page-Plan.md'), 'w', encoding='utf-8').write('\n'.join(o))
print('rows', len(rows) + 1)
