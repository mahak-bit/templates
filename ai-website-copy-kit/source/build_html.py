# -*- coding: utf-8 -*-
"""Generate the print-ready HTML for The AI Website Copy Kit.

Usage: build_html.py [pages.json]   (pages.json maps anchor id -> page number; optional)
"""
import html, json, os, re, sys
from prompts import CATEGORIES, CORE_SIX, FACT_GUARD, expanded, all_prompts
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


def rich(s):
    """Escape + highlight placeholders (cobalt) and AI markers."""
    out = []
    for part in PH_RE.split(s):
        if not part:
            continue
        if PH_RE.fullmatch(part):
            cls = "mk" if MK_RE.match(part) else "ph"
            out.append(f'<span class="{cls}">{esc(part)}</span>')
        else:
            out.append(esc(part))
    return "".join(out)


def rich_md(s):
    """Like md() but also highlights placeholders."""
    pieces = PH_RE.split(s)
    out = []
    for part in pieces:
        if not part:
            continue
        if PH_RE.fullmatch(part):
            cls = "mk" if MK_RE.match(part) else "ph"
            out.append(f'<span class="{cls}">{esc(part)}</span>')
        else:
            out.append(md(part))
    return "".join(out)


def straight(t):
    """Straight quotes in copyable prompt text: Inter's curly closing quote extracts as a lookalike character."""
    return t.replace('\u201c','"').replace('\u201d','"').replace('\u2018',"'").replace('\u2019',"'")


def pg(key):
    return PAGES.get(key, "–")


CSS = r"""
@font-face{font-family:"Playfair Display";font-style:normal;font-weight:400 900;src:url("../fonts/PlayfairDisplay-normal.woff2") format("woff2");}
@font-face{font-family:"Playfair Display";font-style:italic;font-weight:400 900;src:url("../fonts/PlayfairDisplay-italic.woff2") format("woff2");}
:root{--ivory:#F9F8F6;--ink:#161616;--cobalt:#002FA7;--rule:rgba(22,22,22,.16);--tint:rgba(22,22,22,.045);--ctint:rgba(0,47,167,.06);--mute:rgba(22,22,22,.68);}
@page{size:A4;margin:20mm 18mm 22mm 18mm;background:#F9F8F6;
  @bottom-left{content:"The AI Website Copy Kit";font:500 6.8pt/1 "Inter",sans-serif;letter-spacing:.14em;text-transform:uppercase;color:rgba(22,22,22,.62);vertical-align:top;padding-top:7mm;}
  @bottom-right{content:counter(page);font:500 8pt/1 "Inter",sans-serif;color:#002FA7;vertical-align:top;padding-top:6.8mm;}
}
@page full{margin:0;@bottom-left{content:none}@bottom-right{content:none}}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;font-feature-settings:"calt" 0,"case" 0 !important;font-variant-ligatures:none !important}
html{background:var(--ivory)}
body{background:var(--ivory);color:var(--ink);font:400 9.6pt/1.58 "Inter",sans-serif;font-feature-settings:"calt" 0,"case" 0,"ss03" 0;font-variant-ligatures:none;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
h1,h2,h3,.serif{font-family:"Playfair Display",Georgia,serif;font-weight:600;letter-spacing:-.01em}
a{color:inherit;text-decoration:none}
strong{font-weight:600}
.sec{break-before:page}
.full{page:full;height:296.6mm;width:210mm;position:relative;overflow:hidden;break-before:page;break-after:avoid}
.first{break-before:auto}
.kick{font:600 7pt/1.2 "Inter",sans-serif;letter-spacing:.2em;text-transform:uppercase;color:var(--cobalt)}
.kick.dim{color:var(--mute)}
h1{font-size:31pt;line-height:1.08;margin:3mm 0 4.5mm}
h2{font-size:17pt;line-height:1.2;margin:7mm 0 3mm}
h3{font-size:11.5pt;line-height:1.25;margin:0 0 1.5mm}
.lead{font:italic 400 13pt/1.45 "Playfair Display",Georgia,serif;color:var(--ink);max-width:150mm;margin-bottom:6mm}
p{margin-bottom:3mm;max-width:155mm}
.rule{height:.35mm;background:var(--ink);width:100%;margin:5mm 0}
.rule.c{background:var(--cobalt);width:18mm;height:.8mm}
.label{font:600 6.8pt/1.2 "Inter",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:var(--mute);margin:0 0 2mm}
.ph{color:var(--cobalt);font-weight:600}
.mk{font-weight:600;color:var(--ink);background:rgba(0,47,167,.10);padding:0 .8mm;border-radius:.6mm}
ul.dot{list-style:none}
ul.dot li{position:relative;padding-left:5mm;margin-bottom:1.8mm}
ul.dot li:before{content:"";position:absolute;left:0;top:.62em;width:1.6mm;height:1.6mm;background:var(--cobalt)}
.box{background:var(--tint);border-left:.9mm solid var(--cobalt);padding:5mm 6mm;border-radius:0 .8mm .8mm 0}
.box.plain{border-left:0;background:var(--ctint)}
.pre{white-space:pre-wrap;font:400 9.1pt/1.58 "Inter",sans-serif}
.small{font-size:8.2pt;color:var(--mute);line-height:1.5}
table{border-collapse:collapse;width:100%}
td,th{vertical-align:top;text-align:left}
.avoid{break-inside:avoid}

/* ---------- cover ---------- */
.cover{background:var(--ivory)}
.cover .panel{position:absolute;right:0;top:0;bottom:0;width:66mm;background:var(--cobalt);color:var(--ivory)}
.cover .panel .n{position:absolute;left:8mm;bottom:56mm;font:600 140pt/0.8 "Playfair Display",serif;letter-spacing:-.04em}
.cover .panel .w{position:absolute;left:9mm;bottom:41mm;font:600 8pt/1.4 "Inter",sans-serif;letter-spacing:.3em;text-transform:uppercase}
.cover .panel .s{position:absolute;left:9mm;bottom:24mm;width:46mm;font:400 8.4pt/1.5 "Inter",sans-serif;opacity:.92}
.cover .main{position:absolute;left:20mm;top:28mm;width:118mm}
.cover .main .kick{margin-bottom:62mm}
.cover h1.t{font-size:60pt;line-height:.98;margin:0 0 10mm;letter-spacing:-.025em}
.cover h1.t i{color:var(--cobalt);font-weight:500}
.cover .sub{font:400 13.5pt/1.4 "Inter",sans-serif;width:96mm;margin-bottom:9mm}
.cover .foot{position:absolute;left:20mm;bottom:22mm;width:118mm}
.cover .foot .aud{font:500 8pt/1.5 "Inter",sans-serif;max-width:92mm}
.cover .foot .ed{font:600 6.8pt/1 "Inter",sans-serif;letter-spacing:.2em;text-transform:uppercase;color:var(--cobalt);margin-top:5mm}

/* ---------- divider ---------- */
.divider{background:var(--cobalt);color:var(--ivory)}
.divider .num{position:absolute;left:20mm;top:20mm;font:600 168pt/.9 "Playfair Display",serif;letter-spacing:-.05em;opacity:1}
.divider .kick{color:var(--ivory);position:absolute;left:20mm;top:20mm;opacity:.9}
.divider .body{position:absolute;left:20mm;right:20mm;top:104mm}
.divider h1{font-size:36pt;line-height:1.08;margin:0 0 6mm;max-width:150mm}
.divider p.b{font:400 11.2pt/1.55 "Inter",sans-serif;max-width:142mm;margin-bottom:9mm;color:var(--ivory)}
.divider .list{border-top:.3mm solid rgba(249,248,246,.55);max-width:170mm}
.divider .list .r{display:flex;gap:6mm;padding:3.1mm 0;border-bottom:.3mm solid rgba(249,248,246,.35);font:500 10.5pt/1.3 "Inter",sans-serif}
.divider .list .r b{font:600 10pt/1.3 "Playfair Display",serif;width:10mm;flex:none}
.divider .order{position:absolute;left:20mm;right:20mm;bottom:22mm;font:400 9pt/1.5 "Inter",sans-serif;max-width:140mm}
.divider .order span{display:block;font:600 6.8pt/1.2 "Inter",sans-serif;letter-spacing:.2em;text-transform:uppercase;margin-bottom:2mm}

/* ---------- contents ---------- */
.toc .grp{margin:7mm 0 1mm}
.toc .row{display:flex;align-items:baseline;gap:3mm;padding:1.75mm 0;border-bottom:.25mm solid var(--rule);font-size:10pt}
.toc .row .nn{width:8mm;flex:none;font:600 9pt/1 "Playfair Display",serif;color:var(--cobalt)}
.toc .row .tt{flex:1}
.toc .row .ss{font-size:8pt;color:var(--mute);margin-right:2mm}
.toc .row .pp{width:8mm;text-align:right;font-weight:600;color:var(--cobalt)}
.idx{columns:2;column-gap:12mm}
.idx .cat{break-after:avoid;margin:4.5mm 0 1mm;font:600 7pt/1.3 "Inter",sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--cobalt)}
.idx .cat:first-child{margin-top:0}
.idx .row{display:flex;gap:2.5mm;padding:1.25mm 0;border-bottom:.25mm solid var(--rule);font-size:8.6pt;line-height:1.3;break-inside:avoid}
.idx .row .nn{width:6mm;flex:none;font:600 8.6pt/1.3 "Playfair Display",serif;color:var(--cobalt)}
.idx .row .tt{flex:1}
.idx .row .pp{font-weight:600;color:var(--cobalt)}

/* ---------- licence / intro ---------- */
.two{display:grid;grid-template-columns:1fr 1fr;gap:10mm}
.defs .d{display:grid;grid-template-columns:38mm 1fr;gap:6mm;padding:3.4mm 0;border-top:.25mm solid var(--rule)}
.defs .d .k{font:600 10pt/1.3 "Playfair Display",serif}
.defs .d .v{font-size:9.2pt}
.card{padding:5mm 0;border-top:.35mm solid var(--ink)}
.card .nm{font:600 20pt/1 "Playfair Display",serif;color:var(--cobalt);margin-bottom:2mm}

/* ---------- quick start ---------- */
.step{display:grid;grid-template-columns:13mm 1fr 30mm;gap:4mm;padding:3.2mm 0;border-top:.25mm solid var(--rule)}
.step .no{font:600 21pt/1 "Playfair Display",serif;color:var(--cobalt)}
.step .tm{font:600 7pt/1.4 "Inter",sans-serif;letter-spacing:.12em;text-transform:uppercase;color:var(--mute);text-align:right;padding-top:1.6mm}
.step p{margin:0;font-size:8.9pt;line-height:1.5}
.qs ul.dot li{font-size:8.7pt;margin-bottom:1.3mm}
.find td{padding:2.5mm 0;border-top:.25mm solid var(--rule);font-size:9.4pt}
.find td.n{width:36mm;text-align:right;font:600 10pt/1.4 "Playfair Display",serif;color:var(--cobalt)}
.seq{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}
.seq .s{border-top:.35mm solid var(--cobalt);padding-top:2.2mm;font-size:8.6pt;line-height:1.4}
.seq .s b{display:block;font:600 11pt/1.2 "Playfair Display",serif;color:var(--cobalt);margin-bottom:.8mm}

/* ---------- brief ---------- */
.six{display:grid;grid-template-columns:1fr 1fr;gap:5mm 8mm}
.six .c{border-top:.5mm solid var(--cobalt);padding-top:2.2mm;min-height:50mm}
.six .c .h{font:600 11.5pt/1.2 "Playfair Display",serif;margin-bottom:.8mm}
.six .c .h span{color:var(--cobalt);margin-right:2mm}
.six .c .d{font-size:8pt;color:var(--mute);line-height:1.4}
.f{margin-bottom:2.6mm;break-inside:avoid}
.f .q{font-size:8.6pt;margin-bottom:.4mm}
.f .a{height:8mm;border-bottom:.3mm solid rgba(22,22,22,.32)}
.bsec{margin-bottom:6mm;break-inside:avoid}
.bsec .hd{display:flex;gap:3mm;align-items:baseline;border-bottom:.35mm solid var(--ink);padding-bottom:1.4mm;margin-bottom:3mm;break-after:avoid}
.bsec .hd b{font:600 15pt/1 "Playfair Display",serif;color:var(--cobalt)}
.bsec .hd span{font:600 7.2pt/1 "Inter",sans-serif;letter-spacing:.16em;text-transform:uppercase}
.cols2{columns:2;column-gap:10mm}
.bcols{columns:2;column-gap:10mm}
.bcols .f .q{font-size:8.3pt;line-height:1.35}

/* ---------- prompt page ---------- */
.pp-top{display:flex;justify-content:space-between;align-items:baseline;border-bottom:.35mm solid var(--ink);padding-bottom:2.2mm}
.pp-top .r{font:600 7.4pt/1 "Inter",sans-serif;letter-spacing:.2em;text-transform:uppercase;color:var(--cobalt)}
.pp h1{font-size:28pt;margin:6mm 0 2.5mm;max-width:160mm}
.pp .use{font:italic 400 12pt/1.45 "Playfair Display",Georgia,serif;max-width:150mm;margin-bottom:6.5mm}
.fill td{padding:2.1mm 0;border-top:.25mm solid var(--rule);font-size:8.8pt}
.fill tr:last-child td{border-bottom:.25mm solid var(--rule)}
.fill td.k{width:62mm;padding-right:5mm}
.fill td.k .ph{font-size:8.4pt}
.pp .promptbox{margin-top:5mm}
.pp .promptbox .box{padding:6mm 7mm}
.pp .tip{margin-top:5mm;display:grid;grid-template-columns:18mm 1fr;gap:3mm;font-size:9pt}
.pp .tip .label{margin:.4mm 0 0;color:var(--cobalt)}
.chips{margin-top:3.5mm;font-size:7.6pt;color:var(--mute)}
.chips .ph{font-weight:500;margin-right:2.5mm;white-space:nowrap}

/* ---------- worked example ---------- */
.ex-note{font-size:8.2pt;color:var(--mute);border-top:.25mm solid var(--rule);padding-top:2mm;margin-top:4mm}
.angle{break-inside:avoid;border-top:.35mm solid var(--ink);padding:3.5mm 0 3.5mm;display:grid;grid-template-columns:30mm 1fr;gap:5mm}
.angle .t{font:600 6.8pt/1.3 "Inter",sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--cobalt);padding-top:1.4mm}
.angle .hl{font:600 15pt/1.2 "Playfair Display",serif;margin-bottom:1.5mm}
.angle .sb{font-size:9.2pt;margin-bottom:1.8mm}
.angle .bt{display:inline-block;background:var(--cobalt);color:var(--ivory);font:600 8pt/1 "Inter",sans-serif;padding:2.2mm 4mm;border-radius:.6mm}
.angle .rs{font-size:8pt;color:var(--mute);margin-left:3mm}
.snap{display:grid;grid-template-columns:1fr 1fr;gap:6mm}
.fact{counter-increment:f}
.fact li{margin-bottom:1.5mm}
.faq .qa{padding:3mm 0;border-top:.25mm solid var(--rule);break-inside:avoid}
.faq .qa b{display:block;font:600 10.5pt/1.3 "Playfair Display",serif;margin-bottom:.8mm}
.meta{break-inside:avoid;border-top:.35mm solid var(--ink);padding:3mm 0}
.meta .ttl{font:400 11.5pt/1.3 "Inter",sans-serif;color:var(--cobalt);font-weight:500}
.meta .dsc{font-size:9pt;margin-top:.8mm}
.meta .cnt{font-size:7.6pt;color:var(--mute);margin-top:1.2mm}
.rv{display:grid;grid-template-columns:18mm 44mm 1fr;gap:4mm;padding:2.6mm 0;border-top:.25mm solid var(--rule);font-size:9pt;break-inside:avoid}
.rv .st{font:600 7pt/1.5 "Inter",sans-serif;letter-spacing:.12em;text-transform:uppercase}
.rv .st.pass{color:var(--cobalt)}
.rv .st.flag{color:var(--ink)}
.rv .st.flag:before{content:"\25B2 "}
.rv .st.pass:before{content:"\2713 "}
.rv b{font-weight:600}

/* ---------- checklist ---------- */
.chk .g{break-inside:avoid;margin-bottom:5.2mm}
.chk .g h3{font-size:12pt;border-bottom:.35mm solid var(--ink);padding-bottom:1.2mm;margin-bottom:1.5mm}
.chk .it{display:flex;gap:3mm;padding:1.25mm 0;font-size:8.7pt;line-height:1.38}
.chk .it i{flex:none;width:3.6mm;height:3.6mm;border:.35mm solid var(--ink);margin-top:.5mm}
.red{display:flex;flex-wrap:wrap;gap:2mm;margin:2mm 0 3mm}
.red span{border:.3mm solid var(--ink);padding:1mm 2.6mm;font:500 8pt/1.2 "Inter",sans-serif;border-radius:10mm}

/* ---------- closing ---------- */
.closing{background:var(--cobalt);color:var(--ivory)}
.closing .in{position:absolute;left:20mm;right:20mm;top:34mm}
.closing h1{font-size:46pt;margin:4mm 0 5mm}
.closing .lead{color:var(--ivory);max-width:140mm}
.closing .kick{color:var(--ivory)}
.closing .steps{margin-top:8mm;max-width:165mm;border-top:.3mm solid rgba(249,248,246,.55)}
.closing .steps .r{display:grid;grid-template-columns:12mm 1fr;gap:3mm;padding:4mm 0;border-bottom:.3mm solid rgba(249,248,246,.35);font-size:10.4pt}
.closing .steps .r b.n{font:600 17pt/1 "Playfair Display",serif}
.closing .end{position:absolute;left:20mm;right:20mm;bottom:24mm}
.closing .end .q{font:italic 500 17pt/1.35 "Playfair Display",serif;max-width:130mm;margin-bottom:6mm}
.closing .end .t{font:600 7pt/1.5 "Inter",sans-serif;letter-spacing:.2em;text-transform:uppercase;opacity:.95}
"""


def anchor_link(key, inner):
    return f'<a href="#{key}">{inner}</a>'


def cover():
    return f"""
<section class="full cover first" id="cover">
  <div class="main">
    <div class="kick">A practical prompt library</div>
    <h1 class="t">The AI<br><i>Website</i><br>Copy Kit</h1>
    <div class="rule c"></div>
    <div class="sub">{esc(M.SUBTITLE)}</div>
  </div>
  <div class="foot">
    <div class="aud">{esc(M.AUDIENCE_LINE)}</div>
    <div class="ed">{esc(M.VERSION)} · {esc(M.YEAR)}</div>
  </div>
  <div class="panel">
    <div class="n">50</div>
    <div class="w">Prompts</div>
    <div class="s">10 categories. A reusable brief, a worked example and a quality checklist.</div>
  </div>
</section>"""


def licence():
    L = M.LICENCE
    pub = f"© {M.YEAR} {M.PUBLISHER}. All rights reserved." if M.PUBLISHER else f"© {M.YEAR}. All rights reserved."
    rows = "".join(f'<div class="d"><div class="k">{esc(k)}</div><div class="v">{md(v)}</div></div>' for k, v in L["items"])
    return f"""
<section class="sec" id="sec-licence">
  <div class="kick">Before you begin</div>
  <h1>{esc(L['heading'])}</h1>
  <div class="rule c"></div>
  <div class="defs" style="margin-top:6mm">{rows}</div>
  <p class="small" style="margin-top:8mm">{esc(M.TITLE)} · {esc(M.VERSION)}<br>{esc(pub)}<br>
  Set in Playfair Display and Inter (both licensed under the SIL Open Font License).</p>
</section>"""


def contents():
    def row(nn, title, key, sub=""):
        s = f'<span class="ss">{esc(sub)}</span>' if sub else ""
        return (f'<a class="row" href="#{key}"><span class="nn">{nn}</span><span class="tt">{esc(title)}</span>{s}'
                f'<span class="pp">{pg(key)}</span></a>')
    front = [("", M.LICENCE["heading"], "sec-licence"),
             ("", M.INTRO["heading"], "sec-intro"),
             ("", M.QUICKSTART["heading"], "sec-quick"),
             ("", M.FINDER["heading"], "sec-finder"),
             ("", M.ANATOMY["heading"], "sec-anatomy"),
             ("", M.BRIEF["heading"], "sec-brief")]
    cats = "".join(row(f"{c['n']:02d}", c["title"], f"cat-{c['n']}",
                       f"Prompts {c['prompts'][0]['n']}–{c['prompts'][-1]['n']}") for c in CATEGORIES)
    back = [("", "Worked Example: Saltgrain Bakehouse", "sec-example"),
            ("", M.CHECKLIST["heading"], "sec-checklist"),
            ("", M.CLOSING["heading"], "sec-closing")]
    return f"""
<section class="sec toc" id="sec-contents">
  <div class="kick">Contents</div>
  <h1>What is inside</h1>
  <div class="rule c"></div>
  <div class="grp label">Start here</div>
  {''.join(row(*r) for r in front)}
  <div class="grp label">The 50 prompts</div>
  {cats}
  <div class="grp label">Put it into practice</div>
  {''.join(row(*r) for r in back)}
  <p class="small" style="margin-top:6mm">Page numbers are clickable in the PDF. A full list of all 50 prompts follows.</p>
</section>"""


def prompt_index():
    out = []
    for c in CATEGORIES:
        out.append(f'<div class="cat">{c["n"]:02d} · {esc(c["title"])}</div>')
        for p in c["prompts"]:
            out.append(f'<a class="row" href="#p-{p["n"]}"><span class="nn">{p["n"]}</span>'
                       f'<span class="tt">{esc(p["title"])}</span><span class="pp">{pg("p-%d" % p["n"])}</span></a>')
    return f"""
<section class="sec" id="sec-index">
  <div class="kick">Contents</div>
  <h1>All 50 prompts</h1>
  <div class="rule c"></div>
  <div class="idx">{''.join(out)}</div>
</section>"""


def intro():
    I = M.INTRO
    paras = "".join(f"<p>{md(t)}</p>" for t in I["paras"])
    who = "".join(f'<li><strong>{esc(a)}</strong> {esc(b)}</li>' for a, b in I["for_items"])
    inside = "".join(f"<li>{md(t)}</li>" for t in I["inside_items"])
    return f"""
<section class="sec" id="sec-intro">
  <div class="kick">Welcome</div>
  <h1>{esc(I['heading'])}</h1>
  <p class="lead">{esc(I['lead'])}</p>
  {paras}
  <div class="two" style="margin-top:7mm">
    <div><div class="label">{esc(I['for_heading'])}</div><ul class="dot">{who}</ul></div>
    <div><div class="label">{esc(I['inside_heading'])}</div><ul class="dot">{inside}</ul></div>
  </div>
  <div class="box avoid" style="margin-top:8mm"><div class="label" style="color:var(--cobalt)">{esc(I['honest_heading'])}</div>
  <p style="margin:0">{esc(I['honest'])}</p></div>
</section>"""


def quickstart():
    Q = M.QUICKSTART
    steps = "".join(f"""<div class="step avoid"><div class="no">{i}</div><div><h3>{rich(t)}</h3><p>{rich_md(d)}</p></div>
      <div class="tm">{esc(tm)}</div></div>""" for i, (t, tm, d) in enumerate(Q["steps"], 1))
    fu = "".join(f"<li>{esc(t)}</li>" for t in Q["followups"])
    hb = "".join(f"<li>{esc(t)}</li>" for t in Q["habits"])
    return f"""
<section class="sec qs" id="sec-quick">
  <div class="kick">Start here</div>
  <h1>{esc(Q['heading'])}</h1>
  <p class="lead" style="margin-bottom:4mm">{esc(Q['lead'])}</p>
  {steps}
  <div class="two" style="margin-top:6mm">
    <div><div class="label">{esc(Q['followups_heading'])}</div><ul class="dot">{fu}</ul></div>
    <div><div class="label">{esc(Q['habits_heading'])}</div><ul class="dot">{hb}</ul></div>
  </div>
</section>"""


def finder():
    F = M.FINDER
    rows = "".join(f'<tr><td>{esc(a)}</td><td class="n">{esc(b)}</td></tr>' for a, b in F["rows"])
    seq = "".join(f'<div class="s"><b>{esc(a)}</b>{esc(b)}</div>' for a, b in F["order"])
    return f"""
<section class="sec" id="sec-finder">
  <div class="kick">Start here</div>
  <h1>{esc(F['heading'])}</h1>
  <p class="lead" style="margin-bottom:3mm">Find your situation, then jump to the prompt numbers on the right.</p>
  <table class="find" style="margin-bottom:8mm">{rows}</table>
  <div class="label">{esc(F['order_heading'])}</div>
  <div class="seq">{seq}</div>
</section>"""


def anatomy():
    A = M.ANATOMY
    parts = "".join(f'<div class="d"><div class="k">{esc(a)}</div><div class="v">{esc(b)}</div></div>' for a, b in A["parts"])
    marks = "".join(f'<div class="d"><div class="k"><span class="mk">{esc(a)}</span></div><div class="v">{esc(b)}</div></div>' for a, b in A["markers"])
    return f"""
<section class="sec" id="sec-anatomy">
  <div class="kick">Start here</div>
  <h1>{esc(A['heading'])}</h1>
  <p class="lead" style="margin-bottom:3mm">{esc(A['lead'])}</p>
  <div class="defs">{parts}</div>
  <h2>{esc(A['fg_heading'])}</h2>
  <p>{esc(A['fg_lead'])}</p>
  <div class="box"><div class="pre">{rich(straight(FACT_GUARD))}</div></div>
  <h2>{esc(A['markers_heading'])}</h2>
  <div class="defs">{marks}</div>
  <p class="small" style="margin-top:5mm">{rich(A['placeholder_note'])}</p>
</section>"""


def brief():
    B = M.BRIEF
    six = "".join(f'<div class="c"><div class="h"><span>{i}</span>{esc(' '.join(w if w=='of' else w.capitalize() for w in n.strip('[]').lower().split()))}</div><div class="d">{esc(d)}</div></div>'
                  for i, (n, d) in enumerate(CORE_SIX, 1))
    p1 = f"""
<section class="sec" id="sec-brief">
  <div class="kick">The reusable brief · Part 1</div>
  <h1>{esc(B['heading'])}</h1>
  <p class="lead" style="margin-bottom:3mm">{esc(B['lead'])}</p>
  <div class="label" style="margin-top:5mm">{esc(B['core_note'])}</div>
  <div class="six">{six}</div>
</section>"""

    def sec_html(sec):
        letter, name, fields = sec
        f = "".join(f'<div class="f"><div class="q">{esc(q)}</div><div class="a"></div></div>' for q in fields)
        return f'<div class="bsec"><div class="hd"><b>{letter}</b><span>{esc(name)}</span></div>{f}</div>'
    secs = B["sections"]
    half = [secs[0:4], secs[4:9]]
    p2 = f"""
<section class="sec" id="brief-2">
  <div class="kick">The reusable brief · Part 2</div>
  <h2 style="margin-top:2mm">Detailed questions</h2>
  <p class="small" style="margin-bottom:4mm">Answer in a line or two. Anything you cannot yet verify, leave blank and mark it for follow-up.</p>
  <div class="bcols">{''.join(sec_html(s) for s in half[0])}</div>
</section>
<section class="sec" id="brief-3">
  <div class="kick">The reusable brief · Part 3</div>
  <h2 style="margin-top:2mm">Detailed questions, continued</h2>
  <div class="bcols">{''.join(sec_html(s) for s in half[1])}</div>
</section>
<section class="sec" id="brief-4">
  <div class="kick">The reusable brief · Part 4</div>
  <h1>{esc(B['context_heading'])}</h1>
  <p class="lead" style="margin-bottom:5mm">{esc(B['context_lead'])}</p>
  <div class="box"><div class="pre">{rich(straight(B['context_template']))}</div></div>
  <p class="small" style="margin-top:6mm">Replace each placeholder with your answers from the Core Six. Keep the last paragraph exactly as it is.</p>
</section>"""
    return p1 + p2


def divider(c):
    lst = "".join(f'<div class="r"><b>{p["n"]}</b><span>{esc(p["title"])}</span></div>' for p in c["prompts"])
    return f"""
<section class="full divider" id="cat-{c['n']}">
  <div class="kick">Category {c['n']:02d} / 10</div>
  <div class="num" style="top:30mm">{c['n']:02d}</div>
  <div class="body">
    <h1>{esc(c['title'])}</h1>
    <p class="b">{esc(c['blurb'])}</p>
    <div class="list">{lst}</div>
  </div>
  <div class="order"><span>Suggested order</span>{esc(c['order'])}</div>
</section>"""


def prompt_page(c, p):
    rows = "".join(f'<tr><td class="k"><span class="ph">{esc(k)}</span></td><td>{esc(v)}</td></tr>' for k, v in p["fill"])
    used = [x for x in core_names if x in p["prompt"]]
    chips = "".join(f'<span class="ph">{esc(x)}</span>' for x in used)
    return f"""
<section class="sec pp" id="p-{p['n']}">
  <div class="pp-top"><span class="kick dim">Category {c['n']:02d} · {esc(c['title'])}</span><span class="r">Prompt {p['n']} / 50</span></div>
  <h1>{esc(p['title'])}</h1>
  <div class="use">{esc(p['use'])}</div>
  <div class="label">Fill in</div>
  <table class="fill">{rows}</table>
  <div class="chips">Also uses from your brief: {chips}</div>
  <div class="promptbox"><div class="label">The prompt — copy everything in the box</div>
    <div class="box"><div class="pre">{rich(straight(expanded(p)))}</div></div></div>
  <div class="tip"><div class="label">Tip</div><div>{esc(p['tip'])}</div></div>
</section>"""


def example():
    E = M
    facts = "".join(f"<li>{esc(t)}</li>" for t in E.EX_FACTS)
    core = "".join(f'<tr><td class="k"><span class="ph">{esc(a)}</span></td><td>{esc(b)}</td></tr>' for a, b in E.EX_CORE)
    s1 = f"""
<section class="sec" id="sec-example">
  <div class="kick">Worked example · 1 of 5</div>
  <h1>Saltgrain Bakehouse</h1>
  <p class="lead" style="margin-bottom:3mm">A complete run through the kit, from brief to reviewed copy.</p>
  <div class="box plain avoid"><strong>Please note:</strong> Saltgrain Bakehouse and the town of Eastbrook are <strong>fictional</strong>.
  Every fact below was invented for this example. The sample copy that follows was written to illustrate how
  the prompts work; it is not the output of a specific AI tool, and your own results will differ.</div>
  <h2>Step 1 — The brief: key facts</h2>
  <p>These eight facts are everything the AI is allowed to use.</p>
  <ul class="dot">{facts}</ul>
  <h2>Step 2 — The Core Six, filled in</h2>
  <table class="fill">{core}</table>
</section>"""
    angles = "".join(f"""<div class="angle"><div class="t">{i}. {esc(a)}</div><div>
      <div class="hl">{esc(h)}</div><div class="sb">{esc(s)}</div>
      <span class="bt">{esc(b)}</span><span class="rs">{esc(r)}</span></div></div>""" for i, (a, h, s, b, r) in enumerate(E.EX_HERO_OUT, 1))
    s2 = f"""
<section class="sec" id="ex-2">
  <div class="kick">Worked example · 2 of 5</div>
  <h2 style="margin-top:2mm">Step 3 — Run Prompt 1 (Hero Headline Lab)</h2>
  <p>The placeholders from the brief go straight into the prompt:</p>
  <div class="box"><div class="pre" style="font-size:8.2pt">{esc(E.EX_HERO_FILLED)}</div></div>
  <h2>Illustrative output</h2>
  {angles}
  <div class="box plain avoid" style="margin-top:3mm"><strong>Recommendation:</strong> {esc(E.EX_HERO_REC)}</div>
  <p class="ex-note">Every claim in these lines traces back to a fact in Step 1. Nothing about awards, ratings or customer numbers appears because none was supplied.</p>
</section>"""
    S = E.EX_SERVICE
    inc = "".join(f"<li>{esc(t)}</li>" for t in S["included"])
    stp = "".join(f"<div style=\"margin-bottom:1mm\">{i}.&nbsp; {esc(t)}</div>" for i, t in enumerate(S["steps"], 1))
    s3 = f"""
<section class="sec" id="ex-3">
  <div class="kick">Worked example · 3 of 5</div>
  <h2 style="margin-top:2mm">Step 4 — Run Prompt {S['prompt_no']} (Service Page Draft)</h2>
  <p>For the custom cakes page. Service details came from the brief; the placeholders were filled the same way as in Step 3.</p>
  <div class="label" style="margin-top:4mm">Illustrative output</div>
  <div class="box" style="padding:7mm 8mm">
    <div class="label" style="color:var(--cobalt)">H1</div>
    <h1 style="font-size:23pt;margin:0 0 3mm">{esc(S['h1'])}</h1>
    <p>{esc(S['intro'])}</p>
    <h3 style="margin-top:4mm">Who this is for</h3><p>{esc(S['for'])}</p>
    <h3 style="margin-top:3mm">What is included</h3><ul class="dot">{inc}</ul>
    <h3 style="margin-top:3mm">How it works</h3><div style="margin-bottom:3mm">{stp}</div>
    <h3>What it costs</h3><p>{rich(S['cost'])}</p>
    <span class="bt" style="display:inline-block;background:var(--cobalt);color:var(--ivory);font:600 8pt/1 Inter;padding:2.4mm 4.5mm">{esc(S['cta'])}</span>
  </div>
  <div class="box plain avoid" style="margin-top:5mm"><strong>The Fact Guard in action.</strong> The brief said nothing about prices for larger cakes, so the draft left a marker
  ({rich('[NEEDS INFO: price list for larger sizes]')}) instead of inventing a number. It also kept the honest “not for” line, drawn from the fact that the bakery makes no sculpted or fondant-figure cakes.</div>
</section>"""
    faq = "".join(f'<div class="qa"><b>{esc(q)}</b>{rich(a)}</div>' for q, a in E.EX_FAQ)
    meta = "".join(f"""<div class="meta"><div class="label">{esc(n)}</div><div class="ttl">{esc(t)}</div>
      <div class="dsc">{esc(d)}</div><div class="cnt">Title {len(t)} characters · Description {len(d)} characters</div></div>""" for n, t, d in E.EX_META)
    s4 = f"""
<section class="sec" id="ex-4">
  <div class="kick">Worked example · 4 of 5</div>
  <h2 style="margin-top:2mm">Step 5 — Run Prompt 24 (FAQ Builder), shortened here to four</h2>
  <div class="faq">{faq}</div>
  <h2>Step 6 — Run Prompt 27 (Title Tags & Meta Descriptions)</h2>
  {meta}
  <p class="ex-note">Character counts were measured, not estimated. Always check counts in a tool before publishing, because AI assistants count unreliably.</p>
</section>"""
    rv = "".join(f"""<div class="rv"><div class="st {k}">{'Pass' if k=='pass' else 'Flag'}</div><div><b>{esc(t)}</b></div><div>{esc(d)}</div></div>""" for k, t, d in E.EX_REVIEW)
    tk = "".join(f"<li>{esc(t)}</li>" for t in E.EX_TAKEAWAYS)
    s5 = f"""
<section class="sec" id="ex-5">
  <div class="kick">Worked example · 5 of 5</div>
  <h2 style="margin-top:2mm">Step 7 — Review with the checklist</h2>
  <p>Before anything is published, the copy is checked against the quality checklist at the back of this kit.</p>
  <div style="margin-top:3mm">{rv}</div>
  <h2>What to notice</h2>
  <ul class="dot">{tk}</ul>
</section>"""
    return s1 + s2 + s3 + s4 + s5


def checklist():
    C = M.CHECKLIST
    gs = []
    for name, items in C["groups"]:
        its = "".join(f'<div class="it"><i></i><span>{rich(t)}</span></div>' for t in items)
        gs.append(f'<div class="g"><h3>{esc(name)}</h3>{its}</div>')
    red = "".join(f"<span>{esc(t)}</span>" for t in C["redflags"])
    return f"""
<section class="sec chk" id="sec-checklist">
  <div class="kick">Put it into practice</div>
  <h1>{esc(C['heading'])}</h1>
  <p class="lead" style="margin-bottom:4mm">{esc(C['lead'])}</p>
  <div class="cols2">{''.join(gs[:4])}</div>
</section>
<section class="sec chk" id="checklist-2">
  <div class="kick">Put it into practice</div>
  <h2 style="margin-top:2mm">Checklist, continued</h2>
  <div class="cols2">{''.join(gs[4:])}</div>
  <div class="label" style="margin-top:6mm">{esc(C['redflags_heading'])}</div>
  <div class="red">{red}</div>
  <p class="small">{esc(C['redflags_note'])}</p>
</section>"""


def closing():
    C = M.CLOSING
    nx = "".join(f'<div class="r"><b class="n">{i}</b><div><strong>{esc(a)}</strong> {esc(b)}</div></div>' for i, (a, b) in enumerate(C["next"], 1))
    return f"""
<section class="full closing" id="sec-closing">
  <div class="in">
    <div class="kick">The end, and the start</div>
    <h1>{esc(C['heading'])}</h1>
    <p class="lead">{esc(C['lead'])}</p>
    <div class="label" style="color:var(--ivory);margin-top:10mm">{esc(C['next_heading'])}</div>
    <div class="steps">{nx}</div>
  </div>
  <div class="end">
    <div class="q">{esc(C['closing_line'])}</div>
    <div class="t">{esc(M.TITLE)} · {esc(M.VERSION)}</div>
  </div>
</section>"""


def build():
    parts = [cover(), licence(), contents(), prompt_index(), intro(), quickstart(), finder(), anatomy(), brief()]
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
