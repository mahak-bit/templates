# -*- coding: utf-8 -*-
"""The AI Website Copy Kit, edition 2: editorial redesign.

Design concept: the square bracket. Every placeholder a buyer fills in is a [BRACKET],
so thin cobalt brackets frame the cover, numerals, prompt cards and closing page.

Usage: build_html.py [pages.json]   (anchor id -> page number; optional)
"""
import html, json, os, re, sys
from prompts import CATEGORIES, CORE_SIX, FACT_GUARD, expanded
import matter as M

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = {}
if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
    PAGES = json.load(open(sys.argv[1]))

PH_RE = re.compile(r"(\[[A-Z][A-Z0-9 &/'’,\-\.\(\)]*\]|\[(?:NEEDS INFO|CHECK):[^\]]*\])")
MK_RE = re.compile(r"^\[(?:NEEDS INFO|CHECK):")
core_names = [c[0] for c in CORE_SIX]


def esc(s):
    return html.escape(s, quote=False)


def md(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    return s


def _wrap(s, fmt):
    out = []
    for part in PH_RE.split(s):
        if not part:
            continue
        if PH_RE.fullmatch(part):
            cls = "mk" if MK_RE.match(part) else "ph"
            out.append(f'<span class="{cls}">{esc(part)}</span>')
        else:
            out.append(fmt(part))
    return "".join(out)


def rich(s):
    return _wrap(s, esc)


def rich_md(s):
    return _wrap(s, md)


def straight(t):
    """Straight quotes in copyable prompt text (Inter's curly closing quote extracts as a lookalike glyph)."""
    return t.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")


def pg(key):
    return PAGES.get(key, "–")


def humanise(ph):
    return " ".join(w if w == "of" else w.capitalize() for w in ph.strip("[]").lower().split())


def bracket(side, w, h, sw, color="var(--cobalt)", cls=""):
    """Inline SVG bracket, drawn in mm so stroke weight stays exact."""
    k = sw / 2
    d = (f"M{w},{k} H{k} V{h-k} H{w}" if side == "l" else f"M0,{k} H{w-k} V{h-k} H0")
    return (f'<svg class="bk {cls}" xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}">'
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="square"/></svg>')


CSS = r"""
@font-face{font-family:"Playfair Display";font-style:normal;font-weight:400 900;src:url("../fonts/PlayfairDisplay-normal.woff2") format("woff2");}
@font-face{font-family:"Playfair Display";font-style:italic;font-weight:400 900;src:url("../fonts/PlayfairDisplay-italic.woff2") format("woff2");}
:root{--ivory:#F9F8F6;--ink:#161616;--cobalt:#002FA7;--hair:rgba(22,22,22,.18);--soft:rgba(22,22,22,.62);--wash:rgba(0,47,167,.07);}
@page{size:A4;margin:18mm 20mm 24mm 20mm;background:#F9F8F6;
  @bottom-left{content:"The AI Website Copy Kit  \00B7  Mahak's Studio";font:600 7.4pt/1 "Inter",sans-serif;letter-spacing:.16em;text-transform:uppercase;color:rgba(22,22,22,.58);vertical-align:top;padding-top:8mm;}
  @bottom-right{content:counter(page);font:500 11pt/1 "Playfair Display",serif;font-variant-numeric:lining-nums;color:#002FA7;vertical-align:top;padding-top:7mm;}
}
@page full{margin:0;@bottom-left{content:none}@bottom-right{content:none}}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;font-feature-settings:"calt" 0,"case" 0 !important;font-variant-ligatures:none !important}
html{background:var(--ivory)}
body{background:var(--ivory);color:var(--ink);font:400 10.4pt/1.6 "Inter",sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
h1,h2,h3,.serif{font-family:"Playfair Display",Georgia,serif;font-weight:500;letter-spacing:-.012em;font-variant-numeric:lining-nums}
a{color:inherit;text-decoration:none}
strong{font-weight:600}
svg.bk{display:block;flex:none}

/* ---------- frames ---------- */
.pg{break-before:page;height:255mm;display:flex;flex-direction:column;position:relative}
.pg.flow{height:auto;min-height:255mm}
.full{page:full;height:296.6mm;width:210mm;position:relative;overflow:hidden;break-before:page}
.rh{display:flex;justify-content:space-between;align-items:baseline;font:600 7.6pt/1 "Inter",sans-serif;letter-spacing:.2em;text-transform:uppercase;padding-bottom:3.2mm;border-bottom:.25mm solid var(--ink);margin-bottom:8mm}
.rh .r{color:var(--cobalt)}
.kick{font:600 7.8pt/1.2 "Inter",sans-serif;letter-spacing:.22em;text-transform:uppercase;color:var(--cobalt)}
.sq{display:inline-block;width:1.7mm;height:1.7mm;background:var(--cobalt);margin-right:2.4mm;vertical-align:.08em}
h1{font-size:38pt;line-height:1.04;margin:4mm 0 5mm}
h2{font-size:19pt;line-height:1.18;margin:0 0 3mm}
h3{font-size:13.5pt;line-height:1.25;margin:0 0 1.5mm}
.deck{font:italic 400 14.5pt/1.45 "Playfair Display",Georgia,serif;max-width:132mm;color:var(--ink)}
.label{font:600 7.6pt/1.2 "Inter",sans-serif;letter-spacing:.2em;text-transform:uppercase;color:var(--soft)}
.label.c{color:var(--cobalt)}
p{margin-bottom:3.4mm}
.ph{color:var(--cobalt);font-weight:600;background:var(--wash);padding:0 .9mm;border-radius:.5mm;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.mk{font-weight:600;color:var(--ink);background:rgba(0,47,167,.13);padding:0 .9mm;border-radius:.5mm;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.small{font-size:8.8pt;line-height:1.55;color:var(--soft)}
.num-s{font:400 15pt/1 "Playfair Display",serif;color:var(--cobalt);font-variant-numeric:lining-nums}
.hair{border-top:.25mm solid var(--hair)}
.avoid{break-inside:avoid}
.tag{display:inline-block;font:600 7.4pt/1 "Inter",sans-serif;letter-spacing:.2em;text-transform:uppercase;padding:1.5mm 2.8mm;border:.3mm solid var(--ink)}
.tag.pr{border-color:var(--cobalt);color:var(--cobalt)}
.tag.out{background:var(--cobalt);border-color:var(--cobalt);color:var(--ivory)}
.cardb{position:relative;padding:5.5mm 10mm}
.cardb:before,.cardb:after{content:"";position:absolute;top:0;bottom:0;width:5mm;border:.6mm solid var(--cobalt)}
.cardb:before{left:0;border-right:0}
.cardb:after{right:0;border-left:0}
.pre{white-space:pre-wrap;font:400 9.8pt/1.57 "Inter",sans-serif}
.btn{display:inline-block;background:var(--cobalt);color:var(--ivory);font:600 8.4pt/1 "Inter",sans-serif;padding:2.6mm 5mm}

/* ---------- cover ---------- */
.cover{background:var(--ivory)}
.cover .top{position:absolute;left:20mm;right:20mm;top:18mm;display:flex;justify-content:space-between;font:600 7.8pt/1 "Inter",sans-serif;letter-spacing:.24em;text-transform:uppercase}
.cover .top span:last-child{color:var(--cobalt)}
.cover .bkL{position:absolute;left:20mm;top:50mm}
.cover .bkR{position:absolute;right:20mm;top:50mm}
.cover .mid{position:absolute;left:46mm;top:68mm;width:130mm}
.cover .mid .kick{margin-bottom:12mm}
.cover h1.t{font:500 76pt/.96 "Playfair Display",serif;letter-spacing:-.035em;margin:0 0 11mm}
.cover h1.t i{color:var(--cobalt);font-weight:400}
.cover h1.t .dot{display:inline-block;width:.15em;height:.15em;background:var(--cobalt);margin-left:.06em}
.cover .sub{font:italic 400 17pt/1.35 "Playfair Display",serif;max-width:104mm}
.cover .stats{position:absolute;left:20mm;right:20mm;top:236mm;display:grid;grid-template-columns:repeat(4,1fr);gap:6mm;border-top:.3mm solid var(--ink);padding-top:5mm}
.cover .stats b{display:block;font:400 34pt/1 "Playfair Display",serif;color:var(--cobalt);font-variant-numeric:lining-nums;letter-spacing:-.02em;margin-bottom:1.8mm}
.cover .stats span{font:600 7.4pt/1.35 "Inter",sans-serif;letter-spacing:.18em;text-transform:uppercase}
.cover .aud{position:absolute;left:20mm;right:20mm;bottom:15mm;font:400 9pt/1.5 "Inter",sans-serif;color:var(--soft)}

/* ---------- licence ---------- */
.lic .grid{display:grid;grid-template-columns:1fr 1fr;gap:13mm 12mm;margin-top:5mm}
.lic .it{border-top:.3mm solid var(--ink);padding-top:3.6mm}
.lic .it .n{font:400 11pt/1 "Playfair Display",serif;color:var(--cobalt);margin-bottom:2.4mm;font-variant-numeric:lining-nums}
.lic .it h3{font-size:15.5pt;margin-bottom:2.4mm}
.lic .it p{font-size:10.4pt;line-height:1.62;margin:0}
.colophon{margin-top:auto;display:flex;justify-content:space-between;gap:8mm;align-items:flex-end;border-top:.3mm solid var(--ink);padding-top:5mm}
.colophon .t{font:500 15pt/1.2 "Playfair Display",serif;white-space:nowrap}
.colophon .s{font-size:8.6pt;line-height:1.6;color:var(--soft)}

/* ---------- contents ---------- */
.toc .layout{display:grid;grid-template-columns:44mm 1fr;gap:12mm;flex:1}
.toc .rail .grp{margin-bottom:9mm}
.toc .rail .grp .label{margin-bottom:3mm}
.toc .rail a{display:flex;justify-content:space-between;gap:3mm;font-size:9.4pt;line-height:1.3;padding:2.1mm 0;border-top:.25mm solid var(--hair)}
.toc .rail a b{font:500 10.5pt/1.2 "Playfair Display",serif;color:var(--cobalt);font-variant-numeric:lining-nums}
.toc .cats a{display:grid;grid-template-columns:15mm 1fr auto;gap:3mm;align-items:baseline;padding:3.3mm 0 3.2mm;border-top:.25mm solid var(--ink)}
.toc .cats a:last-child{border-bottom:.25mm solid var(--ink)}
.toc .cats .n{font:400 22pt/1 "Playfair Display",serif;color:var(--cobalt);font-variant-numeric:lining-nums}
.toc .cats .t{font:500 15pt/1.2 "Playfair Display",serif}
.toc .cats .t small{display:block;font:500 8.2pt/1.4 "Inter",sans-serif;color:var(--soft);margin-top:.8mm;letter-spacing:.02em}
.toc .cats .p{font:500 15pt/1 "Playfair Display",serif;color:var(--cobalt);font-variant-numeric:lining-nums}

/* ---------- prompt index ---------- */
.idx .cols{display:grid;grid-template-columns:1fr 1fr;gap:11mm 14mm;align-content:start}
.idx .blk .hd{display:grid;grid-template-columns:13mm 1fr;align-items:baseline;border-bottom:.3mm solid var(--ink);padding-bottom:2.2mm}
.idx .blk .hd .n{font:400 22pt/1 "Playfair Display",serif;color:var(--cobalt);font-variant-numeric:lining-nums}
.idx .blk .hd .t{font:500 12.5pt/1.2 "Playfair Display",serif}
.idx .blk a{display:grid;grid-template-columns:8mm 1fr auto;gap:2mm;padding:2.1mm 0;border-bottom:.25mm solid var(--hair);font-size:9.2pt;line-height:1.35}
.idx .blk a i{font:500 9.6pt/1.3 "Playfair Display",serif;font-style:normal;color:var(--cobalt);font-variant-numeric:lining-nums}
.idx .blk a b{font:500 10pt/1.3 "Playfair Display",serif;color:var(--cobalt);font-variant-numeric:lining-nums}

/* ---------- intro ---------- */
.intro .hl{font:500 41pt/1.04 "Playfair Display",serif;letter-spacing:-.025em;max-width:150mm;margin:0 0 6mm}
.intro .hl em{color:var(--cobalt);font-weight:400}
.intro .cols2{display:grid;grid-template-columns:1fr 1fr;gap:0 12mm;margin-top:9mm;align-items:start}
.intro .cols2 p{font-size:10.6pt;line-height:1.65}
.intro .cols2 p.dc::first-letter{font:400 46pt/.78 "Playfair Display",serif;color:var(--cobalt);float:left;padding:1.2mm 2.2mm 0 0}
.who{display:grid;grid-template-columns:repeat(3,1fr);gap:9mm;margin-top:auto}
.who .w{border-top:.3mm solid var(--ink);padding-top:3.4mm}
.who .w .n{font:400 30pt/1 "Playfair Display",serif;color:var(--cobalt);margin-bottom:3mm;font-variant-numeric:lining-nums}
.who .w h3{font-size:12.5pt}
.who .w p{font-size:9.4pt;margin:0;color:var(--ink)}
.inside .row{display:grid;grid-template-columns:22mm 1fr;gap:4mm;padding:6.6mm 0;border-top:.3mm solid var(--ink)}
.inside .row:last-of-type{border-bottom:.3mm solid var(--ink)}
.inside .row .n{font:400 30pt/.9 "Playfair Display",serif;color:var(--cobalt);font-variant-numeric:lining-nums}
.inside .row h3{font-size:16pt;margin-bottom:1mm}
.inside .row p{margin:0;font-size:10.2pt}
.notbox{margin-top:auto;position:relative;padding:8mm 14mm}
.notbox:before,.notbox:after{content:"";position:absolute;top:0;bottom:0;width:6mm;border:.6mm solid var(--cobalt)}
.notbox:before{left:0;border-right:0}.notbox:after{right:0;border-left:0}
.notbox p{margin:2mm 0 0;font:italic 400 12.5pt/1.55 "Playfair Display",serif}

/* ---------- quick start ---------- */
.qs .step{display:grid;grid-template-columns:24mm 1fr 25mm;gap:5mm;padding:5.2mm 0;border-top:.3mm solid var(--ink)}
.qs .step:last-of-type{border-bottom:.3mm solid var(--ink)}
.qs .step .n{font:400 44pt/.85 "Playfair Display",serif;color:var(--cobalt);font-variant-numeric:lining-nums;letter-spacing:-.03em}
.qs .step h3{font-size:15pt;margin-bottom:1.6mm}
.qs .step p{margin:0;font-size:10pt;line-height:1.55}
.qs .step .tm{justify-self:end;align-self:start;font:600 7.4pt/1.2 "Inter",sans-serif;letter-spacing:.14em;text-transform:uppercase;border:.3mm solid var(--cobalt);color:var(--cobalt);padding:1.6mm 2.6mm;white-space:nowrap}
.say{display:grid;grid-template-columns:1fr;gap:0}
.say div{font:italic 400 13pt/1.35 "Playfair Display",serif;padding:2.7mm 0 2.7mm 9mm;border-top:.25mm solid var(--hair);position:relative}
.say div:before{content:"";position:absolute;left:0;top:4.9mm;width:4.6mm;height:.5mm;background:var(--cobalt)}
.hab{display:grid;grid-template-columns:1fr 1fr;gap:7mm 10mm}
.hab .h{border-top:.3mm solid var(--ink);padding-top:3mm;font-size:10.2pt}
.hab .h .n{font:400 20pt/1 "Playfair Display",serif;color:var(--cobalt);margin-bottom:2mm;font-variant-numeric:lining-nums}
.seq{display:grid;grid-template-columns:repeat(3,1fr);gap:4.5mm 8mm}
.seq .s{border-top:.5mm solid var(--cobalt);padding-top:2.6mm}
.seq .s .n{font:400 9pt/1 "Inter",sans-serif;font-weight:600;color:var(--soft);letter-spacing:.12em;margin-bottom:1.4mm}
.seq .s b{display:block;font:500 15pt/1.15 "Playfair Display",serif;color:var(--cobalt);margin-bottom:1mm;font-variant-numeric:lining-nums}
.seq .s span{font-size:9.2pt;line-height:1.4}

/* ---------- finder ---------- */
.find .r{display:grid;grid-template-columns:1fr auto;gap:8mm;align-items:center;padding:3.6mm 0;border-top:.25mm solid var(--hair)}
.find .r:first-of-type{border-top:.3mm solid var(--ink)}
.find .r:last-of-type{border-bottom:.3mm solid var(--ink)}
.find .r .q{font:500 13pt/1.3 "Playfair Display",serif}
.find .r .nums{display:flex;gap:1.6mm}
.find .r .nums span{min-width:8mm;text-align:center;border:.3mm solid var(--cobalt);color:var(--cobalt);font:600 9pt/1 "Inter",sans-serif;padding:1.9mm 1mm;font-variant-numeric:lining-nums}

/* ---------- anatomy ---------- */
.anat .top{display:grid;grid-template-columns:70mm 1fr;gap:12mm}
.mini{position:relative;height:84mm;border:.3mm solid var(--ink);padding:5mm 4.5mm;background:var(--ivory)}
.mini .mh{display:grid;grid-template-columns:11mm 1fr;gap:2mm;align-items:end;margin-bottom:4mm}
.mini .mh .a{font:400 22pt/.8 "Playfair Display",serif;color:var(--cobalt);font-variant-numeric:lining-nums}
.mini .mh .b{height:3.4mm;background:var(--ink);width:80%}
.mini .mb{display:grid;grid-template-columns:17mm 1fr;gap:3mm}
.mini .rl .l{height:1.6mm;background:rgba(22,22,22,.22);margin-bottom:1.5mm}
.mini .rl .l.i{background:var(--cobalt);width:70%;height:2.6mm;margin-bottom:2.4mm}
.mini .rl .t{border:.25mm solid var(--cobalt);margin-top:5mm;padding:1.6mm}
.mini .cd{position:relative;padding:3.2mm 3.4mm;height:54mm}
.mini .cd:before,.mini .cd:after{content:"";position:absolute;top:0;bottom:0;width:2mm;border:.4mm solid var(--cobalt)}
.mini .cd:before{left:0;border-right:0}.mini .cd:after{right:0;border-left:0}
.mini .cd .l{height:1.5mm;background:rgba(22,22,22,.25);margin-bottom:1.5mm}
.mini .cd .l.p{width:48%;background:var(--cobalt);height:2.2mm}
.pin{position:absolute;width:5.2mm;height:5.2mm;background:var(--cobalt);color:var(--ivory);font:600 7.6pt/5.2mm "Inter",sans-serif;text-align:center}
.parts .pt{display:grid;grid-template-columns:9mm 1fr;gap:3mm;padding:3.4mm 0;border-top:.25mm solid var(--hair)}
.parts .pt:first-child{border-top:.3mm solid var(--ink)}
.parts .pt .pin{position:static}
.parts .pt h3{font-size:13pt;margin-bottom:.6mm}
.parts .pt p{margin:0;font-size:9.6pt;line-height:1.5}
.dark{background:var(--ink);color:var(--ivory);padding:9mm 11mm}
.dark .ph{background:var(--ivory);color:var(--cobalt)}
.dark .mk{background:var(--cobalt);color:var(--ivory)}
.dark .label{color:rgba(249,248,246,.75)}
.dark .pre{font-size:10.4pt;line-height:1.65}
.mkr{display:grid;grid-template-columns:1fr 1fr;gap:8mm}
.mkr .m{border-top:.3mm solid var(--ink);padding-top:3mm;font-size:9.6pt;line-height:1.5}
.mkr .m .mk{display:inline-block;margin-bottom:1.8mm;font-size:9pt}

/* ---------- brief ---------- */
.six{display:grid;grid-template-columns:1fr 1fr;gap:5mm 10mm;flex:1}
.six .c{border-top:.5mm solid var(--cobalt);padding-top:3mm;display:flex;flex-direction:column}
.six .c .n{font:400 30pt/.9 "Playfair Display",serif;color:var(--cobalt);font-variant-numeric:lining-nums}
.six .c h3{font-size:14pt;margin:2mm 0 1mm}
.six .c .d{font-size:8.8pt;line-height:1.5;color:var(--soft);margin-bottom:3mm}
.six .c .w{margin-top:auto;border-bottom:.3mm solid rgba(22,22,22,.34);height:8mm}
.six .c .w+.w{margin-top:0}
.bsec{break-inside:avoid;margin-bottom:6mm}
.bsec .hd{display:grid;grid-template-columns:13mm 1fr;align-items:baseline;border-bottom:.3mm solid var(--ink);padding-bottom:2.2mm;margin-bottom:2mm}
.bsec .hd b{font:400 30pt/.9 "Playfair Display",serif;color:var(--cobalt)}
.bsec .hd span{font:600 8pt/1.2 "Inter",sans-serif;letter-spacing:.18em;text-transform:uppercase}
.f{break-inside:avoid;margin-bottom:1.4mm}
.f .q{font-size:9.2pt;line-height:1.4;padding-top:2.4mm}
.f .a{height:var(--lh,8mm);border-bottom:.3mm solid rgba(22,22,22,.34)}
.bcols{display:grid;grid-template-columns:1fr 1fr;gap:0 12mm;align-items:start}

/* ---------- divider ---------- */
.divider{background:var(--cobalt);color:var(--ivory)}
.divider.dk{background:var(--ink)}
.divider .top{position:absolute;left:20mm;right:20mm;top:18mm;display:flex;justify-content:space-between;font:600 7.8pt/1 "Inter",sans-serif;letter-spacing:.24em;text-transform:uppercase}
.divider .big{position:absolute;left:17mm;top:30mm;font:400 200pt/.82 "Playfair Display",serif;letter-spacing:-.05em;font-variant-numeric:lining-nums}
.divider .idxr{position:absolute;right:20mm;top:34mm;width:9mm}
.divider .idxr div{height:6.2mm;display:flex;align-items:center;justify-content:flex-end;gap:2mm;font:500 8pt/1 "Inter",sans-serif;opacity:.5;font-variant-numeric:lining-nums}
.divider .idxr div:before{content:"";width:5mm;height:.25mm;background:var(--ivory)}
.divider .idxr div.on{opacity:1;font-weight:700}
.divider .idxr div.on:before{width:9mm;height:.8mm}
.divider .body{position:absolute;left:20mm;right:20mm;top:108mm}
.divider h1{font:500 42pt/1.05 "Playfair Display",serif;letter-spacing:-.025em;margin:0 0 6mm;max-width:150mm}
.divider p.b{font:400 11.4pt/1.62 "Inter",sans-serif;max-width:136mm;margin-bottom:9mm}
.divider .list{border-top:.3mm solid var(--ivory)}
.divider .list .r{display:grid;grid-template-columns:14mm 1fr;align-items:baseline;padding:2.9mm 0;border-bottom:.3mm solid rgba(249,248,246,.38);font:500 12pt/1.3 "Playfair Display",serif}
.divider .list .r b{font:400 14pt/1 "Playfair Display",serif;font-variant-numeric:lining-nums}
.divider .order{position:absolute;left:20mm;right:20mm;bottom:15mm;display:grid;grid-template-columns:34mm 1fr;gap:6mm;font:400 9.4pt/1.55 "Inter",sans-serif}
.divider .order span{font:600 7.6pt/1.5 "Inter",sans-serif;letter-spacing:.2em;text-transform:uppercase}

/* ---------- prompt page ---------- */
.pp .head{display:grid;grid-template-columns:auto 1fr;gap:8mm;align-items:end;margin-bottom:7mm}
.pp .num{position:relative;font:400 64pt/.8 "Playfair Display",serif;color:var(--cobalt);font-variant-numeric:lining-nums;letter-spacing:-.04em;padding:0 6mm;white-space:nowrap;min-width:20mm;text-align:center}
.pp .num:before,.pp .num:after{content:"";position:absolute;top:1mm;bottom:-1mm;width:2.6mm;border:.5mm solid var(--cobalt)}
.pp .num:before{left:0;border-right:0}.pp .num:after{right:0;border-left:0}
.pp h1{font:500 28pt/1.1 "Playfair Display",serif;letter-spacing:-.02em;margin:0;max-width:122mm}
.pp .body{display:grid;grid-template-columns:54mm 1fr;gap:9mm;flex:1;min-height:0}
.pp .rail{display:flex;flex-direction:column;gap:5.5mm;min-height:0}
.pp .rail .use{font:italic 400 11.6pt/1.48 "Playfair Display",serif;padding-bottom:5mm;border-bottom:.25mm solid var(--ink)}
.pp .rail .fi{margin-top:2.4mm;padding-bottom:2.6mm;border-bottom:.25mm solid var(--hair)}
.pp .rail .fi:last-child{border-bottom:0}
.pp .rail .fi .ph{display:inline-block;font-size:8.3pt;line-height:1.4;margin-bottom:1.3mm}
.pp .rail .fi div{font-size:9pt;line-height:1.45}
.pp .rail .br{font-size:8.8pt;line-height:1.55;color:var(--soft)}
.pp .rail .tip{margin-top:auto;border-top:.5mm solid var(--cobalt);padding-top:2.8mm}
.pp .rail .tip p{margin:1.4mm 0 0;font-size:9.3pt;line-height:1.5}
.pp .main .lab{display:flex;justify-content:space-between;margin-bottom:3.4mm}

/* ---------- worked example ---------- */
.ex .ttl{font:500 44pt/1.02 "Playfair Display",serif;letter-spacing:-.03em;margin:3mm 0 6mm;white-space:nowrap}
.ex .ttl i{color:var(--cobalt);font-weight:400}
.legend{display:grid;gap:2.4mm;margin-top:4mm}
.legend div{display:grid;grid-template-columns:23mm 1fr;gap:3mm;align-items:center;font-size:8.8pt;line-height:1.4}
.fnote{position:relative;padding:5mm 7mm;margin-top:6mm;font-size:9.2pt;line-height:1.55}
.fnote:before,.fnote:after{content:"";position:absolute;top:0;bottom:0;width:3mm;border:.45mm solid var(--cobalt)}
.fnote:before{left:0;border-right:0}.fnote:after{right:0;border-left:0}
.ex .two{display:grid;grid-template-columns:1fr 1fr;gap:12mm}
.ex .strip{display:grid;grid-template-columns:1fr 1fr;gap:12mm;margin-top:auto;padding-top:5mm;border-top:.3mm solid var(--ink);align-items:start}
.ex .strip .fnote{margin-top:0}
.facts .f1{display:grid;grid-template-columns:8mm 1fr;gap:2mm;padding:2mm 0;border-top:.25mm solid var(--hair);font-size:9.3pt;line-height:1.42}
.facts .f1:first-of-type{border-top:.3mm solid var(--ink)}
.facts .f1 i{font:400 13pt/1.1 "Playfair Display",serif;font-style:normal;color:var(--cobalt);font-variant-numeric:lining-nums}
.core .c1{display:grid;grid-template-columns:1fr;gap:.8mm;padding:2mm 0;border-top:.25mm solid var(--hair);font-size:9.2pt;line-height:1.5}
.core .c1:first-of-type{border-top:.3mm solid var(--ink)}
.core .c1 .ph{font-size:7.8pt;align-self:start;justify-self:start}
.step-h{display:flex;align-items:baseline;gap:5mm;margin-bottom:5mm}
.step-h .sn{font:400 34pt/.8 "Playfair Display",serif;color:var(--cobalt);font-variant-numeric:lining-nums}
.step-h h2{margin:0;font-size:21pt;line-height:1.1}
.lane{margin-bottom:4mm;display:flex;align-items:center;gap:3mm}
.lane .ln{flex:1;border-top:.25mm solid var(--hair)}
.heros{display:grid;grid-template-columns:repeat(3,1fr);gap:5mm}
.hero{border:.3mm solid var(--ink);padding:5mm 4.6mm;display:flex;flex-direction:column;break-inside:avoid}
.hero .an{font:600 7.2pt/1.3 "Inter",sans-serif;letter-spacing:.16em;text-transform:uppercase;color:var(--cobalt);margin-bottom:4mm}
.hero .hl{font:500 15pt/1.18 "Playfair Display",serif;margin-bottom:2.6mm;letter-spacing:-.015em}
.hero .sb{font-size:8.8pt;line-height:1.5;margin-bottom:4mm}
.hero .btn{align-self:flex-start;margin-top:auto;font-size:8pt;padding:2.3mm 4mm}
.hero .rs{font-size:7.8pt;color:var(--soft);margin-top:2mm}
.recc{margin-top:6mm;display:grid;grid-template-columns:30mm 1fr;gap:5mm;border-top:.3mm solid var(--ink);padding-top:3.4mm;font-size:9.8pt;line-height:1.55}
.site{border:.3mm solid var(--ink);margin-top:2mm}
.site .bar{display:flex;justify-content:space-between;padding:2.4mm 5mm;border-bottom:.3mm solid var(--ink);font:600 7.4pt/1 "Inter",sans-serif;letter-spacing:.18em;text-transform:uppercase}
.site .in{display:grid;grid-template-columns:1fr 62mm;gap:9mm;padding:8mm 7mm}
.site h1{font-size:28pt;margin:0 0 4mm;line-height:1.08}
.site p{font-size:10pt;line-height:1.6}
.site .sd h3{font-size:11.6pt;margin:0 0 1.2mm}
.site .sd ul{list-style:none;margin-bottom:4mm}
.site .sd li{position:relative;padding-left:4.4mm;font-size:9.2pt;line-height:1.45;margin-bottom:1.2mm}
.site .sd li:before{content:"";position:absolute;left:0;top:.55em;width:1.6mm;height:1.6mm;background:var(--cobalt)}
.site .sd .st{font-size:9.2pt;line-height:1.5;margin-bottom:1.2mm}
.site .sd .st b{font:400 11pt/1 "Playfair Display",serif;color:var(--cobalt);margin-right:1.6mm;font-variant-numeric:lining-nums}
.callout{display:grid;grid-template-columns:34mm 1fr;gap:6mm;margin-top:7mm;padding:5mm 0 0;border-top:.5mm solid var(--cobalt);font-size:9.8pt;line-height:1.6}
.faqx .q{display:grid;grid-template-columns:12mm 1fr;gap:3mm;padding:3mm 0;border-top:.25mm solid var(--hair);break-inside:avoid}
.faqx .q:first-of-type{border-top:.3mm solid var(--ink)}
.faqx .q .qn{font:400 16pt/1 "Playfair Display",serif;color:var(--cobalt);font-variant-numeric:lining-nums}
.faqx .q b{display:block;font:500 12.4pt/1.3 "Playfair Display",serif;margin-bottom:1.4mm}
.faqx .q div{font-size:9.6pt;line-height:1.55}
.serp{border-top:.3mm solid var(--ink);padding:3.2mm 0 2.6mm;break-inside:avoid}
.serp .u{font-size:8pt;color:var(--soft);margin:1.4mm 0 .8mm}
.serp .tt{font:500 14pt/1.25 "Inter",sans-serif;color:var(--cobalt)}
.serp .ds{font-size:9.4pt;line-height:1.5}
.serp .cn{font-size:8pt;color:var(--soft);margin-top:1.6mm}
.led .rv{display:grid;grid-template-columns:20mm 38mm 1fr;gap:5mm;padding:3.5mm 0;border-top:.25mm solid var(--hair);font-size:9.6pt;line-height:1.5;break-inside:avoid}
.led .rv:first-of-type{border-top:.3mm solid var(--ink)}
.led .rv b{font:500 11.4pt/1.3 "Playfair Display",serif}
.pill{display:inline-block;font:700 7.2pt/1 "Inter",sans-serif;letter-spacing:.16em;text-transform:uppercase;padding:1.7mm 2.6mm;height:fit-content;text-align:center}
.pill.pass{background:var(--cobalt);color:var(--ivory)}
.pill.flag{border:.35mm solid var(--ink)}
.notice{display:grid;grid-template-columns:repeat(2,1fr);gap:6mm 10mm;margin-top:3mm}
.notice div{border-top:.3mm solid var(--ink);padding-top:3mm;font-size:10pt;line-height:1.55}
.notice div i{display:block;font:400 22pt/1 "Playfair Display",serif;font-style:normal;color:var(--cobalt);margin-bottom:2mm;font-variant-numeric:lining-nums}

/* ---------- checklist ---------- */
.chk .grid{display:grid;grid-template-columns:1fr 1fr;gap:0 12mm;align-items:start}
.chk .g{break-inside:avoid;margin-bottom:8mm}
.chk .g .gh{display:grid;grid-template-columns:11mm 1fr;align-items:baseline;border-bottom:.3mm solid var(--ink);padding-bottom:2mm;margin-bottom:1mm}
.chk .g .gh b{font:400 22pt/1 "Playfair Display",serif;color:var(--cobalt);font-variant-numeric:lining-nums}
.chk .g .gh span{font:500 13pt/1.2 "Playfair Display",serif}
.chk .it{display:grid;grid-template-columns:7mm 1fr;gap:2.4mm;padding:2.4mm 0;border-bottom:.25mm solid var(--hair);font-size:9.6pt;line-height:1.45}
.chk .it i{width:4.4mm;height:4.4mm;border:.4mm solid var(--ink);margin-top:.5mm}
.red{display:flex;flex-wrap:wrap;gap:2.4mm;margin:3mm 0}
.red span{border:.35mm solid var(--ink);padding:1.8mm 3.4mm;font:500 9.2pt/1.2 "Inter",sans-serif;border-radius:10mm}

/* ---------- closing ---------- */
.closing{background:var(--cobalt);color:var(--ivory)}
.closing .top{position:absolute;left:20mm;right:20mm;top:18mm;display:flex;justify-content:space-between;font:600 7.8pt/1 "Inter",sans-serif;letter-spacing:.24em;text-transform:uppercase}
.closing .bkL{position:absolute;left:20mm;top:46mm}
.closing .bkR{position:absolute;right:20mm;top:46mm}
.closing .mid{position:absolute;left:44mm;right:44mm;top:60mm}
.closing h1{font:500 58pt/1 "Playfair Display",serif;letter-spacing:-.03em;margin:6mm 0 6mm}
.closing .deck{color:var(--ivory);font-size:15.5pt}
.closing .nx{margin-top:12mm;border-top:.3mm solid var(--ivory)}
.closing .nx .r{display:grid;grid-template-columns:13mm 1fr;gap:3mm;padding:4.4mm 0;border-bottom:.3mm solid rgba(249,248,246,.4);font-size:10.6pt;line-height:1.5}
.closing .nx .r b{font:400 22pt/1 "Playfair Display",serif;font-variant-numeric:lining-nums}
.closing .end{position:absolute;left:20mm;right:20mm;bottom:17mm;display:flex;justify-content:space-between;align-items:flex-end}
.closing .end .q{font:italic 400 19pt/1.3 "Playfair Display",serif;max-width:112mm}
.closing .end .s{text-align:right;font:600 7.6pt/1.7 "Inter",sans-serif;letter-spacing:.2em;text-transform:uppercase}
"""


def rh(left, right=""):
    return f'<div class="rh"><span>{esc(left)}</span><span class="r">{esc(right)}</span></div>'


# ------------------------------------------------------------------- pages
def cover():
    stats = [("50", "Prompts"), ("10", "Categories"), ("1", "Client brief"), ("1", "Quality checklist")]
    st = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in stats)
    return f"""
<section class="full cover" id="cover">
  <div class="top"><span>Mahak's Studio</span><span>{esc(M.VERSION)} &nbsp;/&nbsp; {esc(M.YEAR)}</span></div>
  <div class="bkL">{bracket('l', 26, 172, 1.5)}</div>
  <div class="bkR">{bracket('r', 26, 172, 1.5)}</div>
  <div class="mid">
    <div class="kick"><span class="sq"></span>A practical prompt library</div>
    <h1 class="t">The AI<br><i>Website</i><br>Copy Kit<span class="dot"></span></h1>
    <div class="sub">{esc(M.SUBTITLE)}</div>
  </div>
  <div class="stats">{st}</div>
  <div class="aud">{esc(M.AUDIENCE_LINE)}.</div>
</section>"""


def licence():
    L = M.LICENCE
    items = "".join(f'<div class="it"><div class="n">{i:02d}</div><h3>{esc(k)}</h3><p>{md(v)}</p></div>'
                    for i, (k, v) in enumerate(L["items"], 1))
    pub = f"© {M.YEAR} {M.PUBLISHER}. All rights reserved." if M.PUBLISHER else f"© {M.YEAR}. All rights reserved."
    return f"""
<section class="pg lic" id="sec-licence">
  {rh('Before you begin', 'Licence')}
  <div class="kick"><span class="sq"></span>Please read</div>
  <h1>{esc(L['heading'])}</h1>
  <div class="grid">{items}</div>
  <div class="colophon">
    <div class="t">{esc(M.TITLE)}</div>
    <div class="s">{esc(M.VERSION)}<br>{esc(pub)}<br>Set in Playfair Display and Inter, both licensed under the SIL Open Font License.</div>
  </div>
</section>"""


def contents():
    def rail(title, key):
        return f'<a href="#{key}"><span>{esc(title)}</span><b>{pg(key)}</b></a>'
    front = [(M.LICENCE["heading"], "sec-licence"), (M.INTRO["heading"], "sec-intro"), (M.QUICKSTART["heading"], "sec-quick"),
             (M.FINDER["heading"], "sec-finder"), (M.ANATOMY["heading"], "sec-anatomy"), ("The Brief", "sec-brief")]
    back = [("Worked Example", "sec-example"), ("Quality Checklist", "sec-checklist"), (M.CLOSING["heading"], "sec-closing")]
    cats = "".join(f'<a href="#cat-{c["n"]}"><span class="n">{c["n"]:02d}</span><span class="t">{esc(c["title"])}'
                   f'<small>Prompts {c["prompts"][0]["n"]}–{c["prompts"][-1]["n"]}</small></span><span class="p">{pg("cat-%d" % c["n"])}</span></a>'
                   for c in CATEGORIES)
    return f"""
<section class="pg toc" id="sec-contents">
  {rh('Contents', 'Page')}
  <div class="kick"><span class="sq"></span>What is inside</div>
  <h1 style="margin-bottom:7mm">Contents</h1>
  <div class="layout">
    <div class="rail">
      <div class="grp"><div class="label c">Start here</div>{''.join(rail(*x) for x in front)}</div>
      <div class="grp"><div class="label c">In practice</div>{''.join(rail(*x) for x in back)}</div>
    </div>
    <div class="cats">{cats}</div>
  </div>
</section>"""


def prompt_index():
    def blk(c):
        rows = "".join(f'<a href="#p-{p["n"]}"><i>{p["n"]}</i><span>{esc(p["title"])}</span><b>{pg("p-%d" % p["n"])}</b></a>' for p in c["prompts"])
        return f'<div class="blk avoid"><div class="hd"><span class="n">{c["n"]:02d}</span><span class="t">{esc(c["title"])}</span></div>{rows}</div>'
    out = []
    for half, (a, b, sid) in enumerate([(0, 5, "sec-index"), (5, 10, "idx-2")]):
        cs = CATEGORIES[a:b]
        out.append(f"""
<section class="pg idx" id="{sid}">
  {rh('Contents', 'The 50 prompts')}
  <div class="kick"><span class="sq"></span>{'Prompts 1–25' if half == 0 else 'Prompts 26–50'}</div>
  <h1 style="margin-bottom:9mm">{'The 50 prompts, at a glance' if half == 0 else 'At a glance, continued'}</h1>
  <div class="cols">{''.join(blk(c) for c in cs)}</div>
</section>""")
    return "".join(out)


def intro():
    I = M.INTRO
    first, rest = I["lead"].split(". ", 1)
    paras = "".join(f'<p class="{"dc" if i == 0 else ""}">{md(t)}</p>' for i, t in enumerate(I["paras"]))
    who = "".join(f'<div class="w"><div class="n">{i:02d}</div><h3>{esc(a)}</h3><p>{esc(b)}</p></div>' for i, (a, b) in enumerate(I["for_items"], 1))
    rows = ""
    for i, t in enumerate(I["inside_items"], 1):
        m = re.match(r"\*\*(.+?)\*\*\s*(.*)", t)
        rows += f'<div class="row"><div class="n">{i:02d}</div><div><h3>{esc(m.group(1))}</h3><p>{esc(m.group(2))}</p></div></div>'
    return f"""
<section class="pg intro" id="sec-intro">
  {rh('Welcome', 'Introduction')}
  <div class="kick"><span class="sq"></span>{esc(I['heading'])}</div>
  <div class="hl" style="margin-top:6mm">{esc(first)}.</div>
  <div class="deck">{esc(rest)}</div>
  <div class="cols2">{paras}</div>
  <div class="label c" style="margin:11mm 0 0">{esc(I['for_heading'])}</div>
  <div class="who" style="margin-top:4mm">{who}</div>
</section>
<section class="pg inside" id="intro-2">
  {rh('Welcome', 'Introduction')}
  <div class="kick"><span class="sq"></span>{esc(I['inside_heading'])}</div>
  <h1 style="margin-bottom:8mm">Everything you need, in one place</h1>
  {rows}
  <div class="notbox"><div class="label c">{esc(I['honest_heading'])}</div><p>{esc(I['honest'])}</p></div>
</section>"""


def quickstart():
    Q = M.QUICKSTART
    steps = "".join(f"""<div class="step avoid"><div class="n">{i}</div><div><h3>{rich(t)}</h3><p>{rich_md(d)}</p></div><div class="tm">{esc(tm)}</div></div>"""
                    for i, (t, tm, d) in enumerate(Q["steps"], 1))
    say = "".join(f"<div>{esc(t)}</div>" for t in Q["followups"])
    hab = "".join(f'<div class="h"><div class="n">{i:02d}</div>{esc(t)}</div>' for i, t in enumerate(Q["habits"], 1))
    F = M.FINDER
    seq = "".join(f'<div class="s"><b>{esc(a)}</b><span>{esc(b)}</span></div>' for i, (a, b) in enumerate(F["order"], 1))
    rows = "".join(f'<div class="r"><div class="q">{esc(a)}</div><div class="nums">{"".join(f"<span>{n.strip()}</span>" for n in b.split(","))}</div></div>' for a, b in F["rows"])
    return f"""
<section class="pg qs" id="sec-quick">
  {rh('Start here', 'Quick-start')}
  <div class="kick"><span class="sq"></span>Five steps</div>
  <h1>{esc(Q['heading'])}</h1>
  <div class="deck" style="margin-bottom:8mm;font-size:13pt">{esc(Q['lead'])}</div>
  {steps}
</section>
<section class="pg qs" id="qs-2">
  {rh('Start here', 'Quick-start')}
  <div class="kick"><span class="sq"></span>{esc(Q['followups_heading'])}</div>
  <h2 style="margin:3mm 0 3mm;font-size:22pt">Keep the conversation going</h2>
  <div class="say" style="margin-bottom:7mm">{say}</div>
  <div class="label c" style="margin-bottom:3mm">{esc(Q['habits_heading'])}</div>
  <div class="hab" style="margin-bottom:7mm">{hab}</div>
  <div class="label c" style="margin-bottom:3mm">{esc(F['order_heading'])}</div>
  <div class="seq">{seq}</div>
</section>
<section class="pg find" id="sec-finder">
  {rh('Start here', 'Finder')}
  <div class="kick"><span class="sq"></span>Find your situation</div>
  <h1>{esc(F['heading'])}</h1>
  <div class="deck" style="margin-bottom:8mm;font-size:13pt">Pick the line that sounds like your problem, then jump to the prompt numbers on the right.</div>
  {rows}
</section>"""


def anatomy():
    A = M.ANATOMY
    parts = "".join(f'<div class="pt"><span class="pin">{i}</span><div><h3>{esc(a)}</h3><p>{esc(b)}</p></div></div>'
                    for i, (a, b) in enumerate(A["parts"], 1))
    marks = "".join(f'<div class="m"><span class="mk">{esc(a)}</span><br>{esc(b)}</div>' for a, b in A["markers"])
    return f"""
<section class="pg anat" id="sec-anatomy">
  {rh('Start here', 'How it works')}
  <div class="kick"><span class="sq"></span>Anatomy of a prompt page</div>
  <h1 style="margin-bottom:7mm">{esc(A['heading'])}</h1>
  <div class="top">
    <div class="mini">
      <div class="mh"><div class="a">14</div><div class="b"></div></div>
      <div class="mb">
        <div class="rl"><div class="l i"></div><div class="l"></div><div class="l" style="width:80%"></div>
          <div class="l i" style="margin-top:4mm"></div><div class="l"></div><div class="l" style="width:70%"></div>
          <div class="t"><div class="l" style="margin:0"></div></div></div>
        <div class="cd"><div class="l p"></div><div class="l"></div><div class="l" style="width:90%"></div><div class="l"></div><div class="l" style="width:76%"></div>
          <div class="l p" style="margin-top:3mm"></div><div class="l"></div><div class="l" style="width:82%"></div><div class="l"></div></div>
      </div>
      <span class="pin" style="left:-2.6mm;top:12mm">1</span>
      <span class="pin" style="left:-2.6mm;top:36mm">2</span>
      <span class="pin" style="right:-2.6mm;top:44mm">3</span>
      <span class="pin" style="left:-2.6mm;bottom:10mm">4</span>
    </div>
    <div class="parts">{parts}</div>
  </div>
  <div class="dark" style="margin-top:7mm;padding:7mm 10mm"><div class="label">{esc(A['fg_heading'])}</div>
    <p style="margin:2mm 0 4mm;font-size:9.6pt;color:rgba(249,248,246,.85)">{esc(A['fg_lead'])}</p>
    <div class="pre">{rich(straight(FACT_GUARD))}</div></div>
  <div class="label c" style="margin:6mm 0 3mm">{esc(A['markers_heading'])}</div>
  <div class="mkr">{marks}</div>
  <p class="small" style="margin:5mm 0 0">{rich(A['placeholder_note'])}</p>
</section>"""


def brief():
    B = M.BRIEF
    six = "".join(f'<div class="c"><div class="n">{i}</div><h3>{esc(humanise(n))}</h3><div class="d">{esc(d)}</div><div class="w"></div><div class="w"></div></div>'
                  for i, (n, d) in enumerate(CORE_SIX, 1))
    out = f"""
<section class="pg" id="sec-brief">
  {rh('The reusable brief', 'Part 1 of 5')}
  <div class="kick"><span class="sq"></span>Fill this in first</div>
  <h1>{esc(B['heading'])}</h1>
  <div class="deck" style="font-size:13pt;margin-bottom:3mm">{esc(B['lead'])}</div>
  <div class="label c" style="margin:6mm 0 4mm">{esc(B['core_note'])}</div>
  <div class="six">{six}</div>
</section>"""

    def sec_html(sec):
        letter, name, fields = sec
        f = "".join(f'<div class="f"><div class="q">{esc(q)}</div><div class="a"></div></div>' for q in fields)
        return f'<div class="bsec"><div class="hd"><b>{letter}</b><span>{esc(name)}</span></div>{f}</div>'
    groups = [B["sections"][0:3], B["sections"][3:6], B["sections"][6:9]]
    for i, g in enumerate(groups, 2):
        out += f"""
<section class="pg" id="brief-{i}">
  {rh('The reusable brief', f'Part {i} of 5')}
  <div class="kick"><span class="sq"></span>Detailed questions</div>
  <h2 style="margin:4mm 0 2mm;font-size:23pt">{'Sections ' + g[0][0] + '–' + g[-1][0]}</h2>
  <p class="small" style="margin-bottom:5mm">Answer in a line or two. Anything you cannot yet verify, leave blank and mark it for follow-up.</p>
  <div class="bcols" style="--lh:{['7.2mm','10.6mm','12.4mm'][i-2]}"><div>{sec_html(g[0])}</div><div>{''.join(sec_html(s) for s in g[1:])}</div></div>
</section>"""
    vals = dict(M.EX_CORE)
    vals["[KEY FACTS]"] = "the eight key facts listed in the worked example"
    filled = B["context_template"]
    for k, v in vals.items():
        filled = filled.replace(k, v)
    out += f"""
<section class="pg" id="brief-5">
  {rh('The reusable brief', 'Part 5 of 5')}
  <div class="kick"><span class="sq"></span>Paste-ready</div>
  <h1>{esc(B['context_heading'])}</h1>
  <div class="deck" style="font-size:13pt;margin-bottom:10mm">{esc(B['context_lead'])}</div>
  <div class="cardb"><div class="pre">{rich(straight(B['context_template']))}</div></div>
  <div class="label c" style="margin:9mm 0 3mm">Filled in: Saltgrain Bakehouse (fictional)</div>
  <div class="cardb ex-fill"><div class="pre">{esc(straight(filled))}</div></div>
  <div class="hab" style="margin-top:auto">
    <div class="h"><div class="n">01</div>Replace each placeholder with your answers from the Core Six.</div>
    <div class="h"><div class="n">02</div>Keep the last paragraph exactly as it is. It is the Fact Guard.</div>
  </div>
</section>"""
    return out


def divider(c):
    dk = " dk" if c["n"] % 2 == 0 else ""
    lst = "".join(f'<div class="r"><b>{p["n"]}</b><span>{esc(p["title"])}</span></div>' for p in c["prompts"])
    idxr = "".join(f'<div class="{"on" if i == c["n"] else ""}">{i:02d}</div>' for i in range(1, 11))
    return f"""
<section class="full divider{dk}" id="cat-{c['n']}">
  <div class="top"><span>Category {c['n']:02d} of 10</span><span>The AI Website Copy Kit</span></div>
  <div class="big">{c['n']:02d}</div>
  <div class="idxr">{idxr}</div>
  <div class="body">
    <h1>{esc(c['title'])}</h1>
    <p class="b">{esc(c['blurb'])}</p>
    <div class="list">{lst}</div>
  </div>
  <div class="order"><span>Suggested order</span><div>{esc(c['order'])}</div></div>
</section>"""


def prompt_page(c, p):
    fills = "".join(f'<div class="fi"><span class="ph">{esc(k)}</span><div>{esc(v)}</div></div>' for k, v in p["fill"])
    used = [humanise(x) for x in core_names if x in p["prompt"]]
    return f"""
<section class="pg pp" id="p-{p['n']}">
  {rh(f"Category {c['n']:02d}  —  {c['title']}", f"Prompt {p['n']} / 50")}
  <div class="head"><div class="num">{p['n']}</div><h1>{esc(p['title'])}</h1></div>
  <div class="body">
    <div class="rail">
      <div class="use">{esc(p['use'])}</div>
      <div><div class="label c">Fill in</div>{fills}</div>
      <div><div class="label">From your brief</div><div class="br" style="margin-top:1.6mm">{esc(', '.join(used))}.</div></div>
      <div class="tip"><div class="label c">Tip</div><p>{esc(p['tip'])}</p></div>
    </div>
    <div class="main">
      <div class="lab"><span class="label c">The prompt</span><span class="label">Copy everything between the brackets</span></div>
      <div class="cardb"><div class="pre">{rich(straight(expanded(p)))}</div></div>
    </div>
  </div>
</section>"""


def example():
    E = M
    facts = "".join(f'<div class="f1"><i>{i}</i><span>{esc(t)}</span></div>' for i, t in enumerate(E.EX_FACTS, 1))
    core = "".join(f'<div class="c1"><span class="ph">{esc(a)}</span><span>{esc(b)}</span></div>' for a, b in E.EX_CORE)
    s1 = f"""
<section class="pg ex" id="sec-example">
  {rh('Worked example', '1 of 5')}
  <div class="kick"><span class="sq"></span>A complete run, from brief to reviewed copy</div>
  <div class="ttl">Saltgrain <i>Bakehouse</i></div>
  <div class="two">
    <div>
      <div class="lane"><span class="tag in">Input</span><span class="ln"></span></div>
      <div class="label" style="margin-bottom:1mm">Step 1 &nbsp;/&nbsp; The brief: eight key facts</div>
      <div class="facts">{facts}</div>
    </div>
    <div>
      <div class="lane"><span class="tag in">Input</span><span class="ln"></span></div>
      <div class="label" style="margin-bottom:1mm">Step 2 &nbsp;/&nbsp; The Core Six, filled in</div>
      <div class="core">{core}</div>
    </div>
  </div>
  <div class="strip">
    <div>
      <div class="label c">How to read this example</div>
      <div class="legend">
        <div><span class="tag in">Input</span>What you know and supply</div>
        <div><span class="tag pr">Prompt</span>What you paste into the AI</div>
        <div><span class="tag out">Output</span>Illustrative copy that comes back</div>
      </div>
    </div>
    <div class="fnote"><strong>Please note.</strong> Saltgrain Bakehouse and the town of Eastbrook are <strong>fictional</strong>.
    Every fact was invented for this example. The sample copy was written to illustrate the prompts. It is not the output of a specific AI tool, and your own results will differ.</div>
  </div>
</section>"""
    heros = "".join(f"""<div class="hero"><div class="an">{i}. {esc(a)}</div><div class="hl">{esc(h)}</div><div class="sb">{esc(s)}</div>
      <span class="btn">{esc(b)}</span><div class="rs">{esc(r)}</div></div>""" for i, (a, h, s, b, r) in enumerate(E.EX_HERO_OUT, 1))
    s2 = f"""
<section class="pg ex" id="ex-2">
  {rh('Worked example', '2 of 5')}
  <div class="step-h"><span class="sn">3</span><h2>Run Prompt 1: the hero headline lab</h2></div>
  <div class="lane"><span class="tag pr">Prompt</span><span class="ln"></span></div>
  <div class="cardb" style="margin-bottom:6mm;padding:6mm 11mm"><div class="pre" style="font-size:9pt;line-height:1.5">{esc(straight(E.EX_HERO_FILLED))}</div></div>
  <div class="lane"><span class="tag out">Output</span><span class="ln"></span><span class="label">Illustrative</span></div>
  <div class="heros">{heros}</div>
  <div class="recc"><div class="label c" style="padding-top:.6mm">Recommendation</div><div>{esc(E.EX_HERO_REC)}</div></div>
  <p class="small" style="margin:auto 0 0">Every claim in these lines traces back to a fact in Step 1. Nothing about awards, ratings or customer numbers appears, because none was supplied.</p>
</section>"""
    S = E.EX_SERVICE
    inc = "".join(f"<li>{esc(t)}</li>" for t in S["included"])
    stp = "".join(f'<div class="st"><b>{i}</b>{esc(t)}</div>' for i, t in enumerate(S["steps"], 1))
    s3 = f"""
<section class="pg ex" id="ex-3">
  {rh('Worked example', '3 of 5')}
  <div class="step-h"><span class="sn">4</span><h2>Run Prompt {S['prompt_no']}: the service page draft</h2></div>
  <p class="small" style="margin-bottom:5mm">For the custom-cakes page. The service details came from the brief, and the placeholders were filled the same way as in Step 3.</p>
  <div class="lane"><span class="tag out">Output</span><span class="ln"></span><span class="label">Illustrative</span></div>
  <div class="site">
    <div class="bar"><span>Custom cakes page</span><span style="color:var(--cobalt)">Draft</span></div>
    <div class="in">
      <div><div class="label c" style="margin-bottom:2mm">H1</div><h1>{esc(S['h1'])}</h1><p>{esc(S['intro'])}</p>
        <h3 style="margin-top:5mm">Who this is for</h3><p>{esc(S['for'])}</p>
        <span class="btn" style="margin-top:3mm">{esc(S['cta'])}</span></div>
      <div class="sd"><h3>What is included</h3><ul>{inc}</ul>
        <h3>How it works</h3><div style="margin-bottom:4mm">{stp}</div>
        <h3>What it costs</h3><div class="st">{rich(S['cost'])}</div></div>
    </div>
  </div>
  <div class="callout"><div class="label c" style="padding-top:.6mm">The Fact Guard in action</div>
    <div>The brief said nothing about prices for larger cakes, so the draft left a marker ({rich('[NEEDS INFO: price list for larger sizes]')}) instead of inventing a number. It also kept the honest “not for” line, drawn from the fact that the bakery makes no sculpted or fondant-figure cakes.</div></div>
</section>"""
    faq = "".join(f'<div class="q"><span class="qn">Q{i}</span><div><b>{esc(q)}</b><div>{rich(a)}</div></div></div>' for i, (q, a) in enumerate(E.EX_FAQ, 1))
    meta = "".join(f"""<div class="serp"><div class="label">{esc(n)}</div><div class="u">saltgrainbakehouse.example</div><div class="tt">{esc(t)}</div>
      <div class="ds">{esc(d)}</div><div class="cn">Title {len(t)} characters &nbsp;/&nbsp; Description {len(d)} characters</div></div>""" for n, t, d in E.EX_META)
    s4 = f"""
<section class="pg ex" id="ex-4">
  {rh('Worked example', '4 of 5')}
  <div class="step-h"><span class="sn">5</span><h2>Run Prompt 24: the FAQ builder</h2></div>
  <div class="lane"><span class="tag out">Output</span><span class="ln"></span><span class="label">Shortened to four</span></div>
  <div class="faqx" style="margin-bottom:7mm">{faq}</div>
  <div class="step-h"><span class="sn">6</span><h2>Run Prompt 27: titles and descriptions</h2></div>
  <div class="lane"><span class="tag out">Output</span><span class="ln"></span><span class="label">Search-result preview</span></div>
  {meta}
  <p class="small" style="margin:auto 0 0">Character counts were measured, not estimated. Always check counts in a tool before publishing, because AI assistants count unreliably.</p>
</section>"""
    rv = "".join(f"""<div class="rv"><span class="pill {k}">{'Pass' if k == 'pass' else 'Flag'}</span><b>{esc(t)}</b><div>{esc(d)}</div></div>""" for k, t, d in E.EX_REVIEW)
    tk = "".join(f"<div><i>{i:02d}</i>{esc(t)}</div>" for i, t in enumerate(E.EX_TAKEAWAYS, 1))
    s5 = f"""
<section class="pg ex" id="ex-5">
  {rh('Worked example', '5 of 5')}
  <div class="step-h"><span class="sn">7</span><h2>Review it against the checklist</h2></div>
  <p class="small" style="margin-bottom:5mm">Before anything is published, the copy is checked against the quality checklist at the back of this kit.</p>
  <div class="led">{rv}</div>
  <div class="label c" style="margin:10mm 0 1mm">What to notice</div>
  <div class="notice">{tk}</div>
</section>"""
    return s1 + s2 + s3 + s4 + s5


def checklist():
    C = M.CHECKLIST

    def grp(name, items):
        num, title = name.split("  ", 1)
        its = "".join(f'<div class="it"><i></i><span>{rich(t)}</span></div>' for t in items)
        return f'<div class="g"><div class="gh"><b>{num}</b><span>{esc(title)}</span></div>{its}</div>'
    gs = [grp(n, i) for n, i in C["groups"]]
    red = "".join(f"<span>{esc(t)}</span>" for t in C["redflags"])
    return f"""
<section class="pg chk" id="sec-checklist">
  {rh('In practice', 'Checklist 1 of 2')}
  <div class="kick"><span class="sq"></span>Website-copy review &nbsp;/&nbsp; before it goes to the client</div>
  <h1>Quality Checklist</h1>
  <div class="deck" style="font-size:13pt;margin-bottom:7mm">{esc(C['lead'])}</div>
  <div class="grid"><div>{gs[0]}{gs[1]}</div><div>{gs[2]}{gs[3]}</div></div>
</section>
<section class="pg chk" id="checklist-2">
  {rh('In practice', 'Checklist 2 of 2')}
  <div class="kick"><span class="sq"></span>Before it goes live</div>
  <h2 style="margin:4mm 0 6mm;font-size:23pt">Checklist, continued</h2>
  <div class="grid"><div>{gs[4]}{gs[5]}</div><div>{gs[6]}{gs[7]}</div></div>
  <div style="margin-top:auto"><div class="label c">{esc(C['redflags_heading'])}</div>
  <div class="red">{red}</div><p class="small" style="margin:0">{esc(C['redflags_note'])}</p></div>
</section>"""


def closing():
    C = M.CLOSING
    nx = "".join(f'<div class="r"><b>{i}</b><div><strong>{esc(a)}</strong> {esc(b)}</div></div>' for i, (a, b) in enumerate(C["next"], 1))
    return f"""
<section class="full closing" id="sec-closing">
  <div class="top"><span>Mahak's Studio</span><span>{esc(M.VERSION)} &nbsp;/&nbsp; {esc(M.YEAR)}</span></div>
  <div class="bkL">{bracket('l', 22, 190, 1.4, 'var(--ivory)')}</div>
  <div class="bkR">{bracket('r', 22, 190, 1.4, 'var(--ivory)')}</div>
  <div class="mid">
    <div class="kick" style="color:var(--ivory)"><span class="sq" style="background:var(--ivory)"></span>The end, and the start</div>
    <h1>{esc(C['heading'])}</h1>
    <div class="deck">{esc(C['lead'])}</div>
    <div class="nx">{nx}</div>
  </div>
  <div class="end"><div class="q">{esc(C['closing_line'])}</div>
    <div class="s">{esc(M.TITLE)}<br>© {esc(M.YEAR)} {esc(M.PUBLISHER)}</div></div>
</section>"""


def build():
    parts = [cover(), licence(), contents(), prompt_index(), intro(), quickstart(), anatomy(), brief()]
    for c in CATEGORIES:
        parts.append(divider(c))
        for p in c["prompts"]:
            parts.append(prompt_page(c, p))
    parts += [example(), checklist(), closing()]
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>{esc(M.TITLE)} – {esc(M.SUBTITLE)}</title>
<meta name="author" content="{esc(M.PUBLISHER)}">
<style>{CSS}</style></head><body>{''.join(parts)}</body></html>"""


if __name__ == "__main__":
    out = os.path.join(ROOT, "_build", "kit.html")
    open(out, "w", encoding="utf-8").write(build())
    print("wrote", out)
