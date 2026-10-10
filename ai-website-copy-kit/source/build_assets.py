# -*- coding: utf-8 -*-
"""Marketing images for the Gumroad listing and social posts. Real PDF pages are used as previews."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_html import bracket
import prompts as P
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, '_build', 'assets')
PG = lambda k: f'pages/{k}.png'

BASE = """
@font-face{font-family:"Playfair Display";font-style:normal;font-weight:400 900;src:url("../../fonts/PlayfairDisplay-normal.woff2") format("woff2");}
@font-face{font-family:"Playfair Display";font-style:italic;font-weight:400 900;src:url("../../fonts/PlayfairDisplay-italic.woff2") format("woff2");}
:root{--ivory:#F9F8F6;--ink:#161616;--cobalt:#002FA7}
*{box-sizing:border-box;margin:0;padding:0;font-feature-settings:"calt" 0,"case" 0 !important;font-variant-ligatures:none !important}
html,body{background:var(--ivory);color:var(--ink);font-family:"Inter",sans-serif;-webkit-print-color-adjust:exact}
.serif{font-family:"Playfair Display",serif;font-variant-numeric:lining-nums}
.kick{font:600 13px/1.2 Inter;letter-spacing:.22em;text-transform:uppercase;color:var(--cobalt)}
.sq{display:inline-block;width:9px;height:9px;background:var(--cobalt);margin-right:10px;vertical-align:1px}
.pagei{position:absolute;box-shadow:0 18px 40px rgba(22,22,22,.18),0 2px 6px rgba(22,22,22,.12);background:#fff}
.pagei img{display:block;width:100%;height:100%}
.ph{color:var(--cobalt);font-weight:600;background:rgba(0,47,167,.08);padding:0 6px;border-radius:3px}
svg.bk{display:block;position:absolute}
"""
def page(name, w, h, css, body):
    html = f'<!doctype html><meta charset="utf-8"><style>{BASE}body{{width:{w}px;height:{h}px;position:relative;overflow:hidden}}{css}</style><body>{body}</body>'
    open(os.path.join(A, name + '.html'), 'w', encoding='utf-8').write(html)

def pxb(side, w, h, sw, color='#002FA7', x=0, y=0):
    # bracket() works in mm; draw in px via a custom svg
    k = sw / 2
    d = f"M{w},{k} H{k} V{h-k} H{w}" if side == 'l' else f"M0,{k} H{w-k} V{h-k} H0"
    return (f'<svg class="bk" style="left:{x}px;top:{y}px" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="square"/></svg>')

# ---------- Gumroad cover 1280x720
page('cover-1280x720', 1280, 720, """
.t{position:absolute;left:96px;top:150px;font:500 78px/.98 "Playfair Display",serif;letter-spacing:-.035em;font-variant-numeric:lining-nums}
.t i{color:var(--cobalt);font-weight:400}.t .dot{display:inline-block;width:.15em;height:.15em;background:var(--cobalt);margin-left:.06em}
.sub{position:absolute;left:96px;top:420px;width:470px;font:italic 400 24px/1.35 "Playfair Display",serif}
.k{position:absolute;left:96px;top:96px}
.stats{position:absolute;left:96px;top:560px;width:520px;display:grid;grid-template-columns:repeat(4,1fr);border-top:1.5px solid var(--ink);padding-top:16px}
.stats b{display:block;font:400 40px/1 "Playfair Display",serif;color:var(--cobalt);font-variant-numeric:lining-nums}
.stats span{font:600 10.5px/1.4 Inter;letter-spacing:.16em;text-transform:uppercase}
""", f"""
{pxb('l',40,520,3,x=56,y=100)}
<div class="k kick"><span class="sq"></span>A practical prompt library</div>
<div class="t">The AI<br><i>Website</i><br>Copy Kit<span class="dot"></span></div>
<div class="sub">50 Ready-to-Use AI Prompts for Better Website Content</div>
<div class="stats"><div><b>50</b><span>Prompts</span></div><div><b>10</b><span>Categories</span></div><div><b>1</b><span>Client brief</span></div><div><b>1</b><span>Checklist</span></div></div>
<div class="pagei" style="left:790px;top:118px;width:340px;height:481px;transform:rotate(0deg)"><img src="{PG('p1')}"></div>
<div class="pagei" style="left:690px;top:70px;width:340px;height:481px"><img src="{PG('cover')}"></div>
""")

# ---------- square thumbnail 1000x1000
page('thumbnail-1000x1000', 1000, 1000, """
.t{position:absolute;left:0;right:0;top:300px;text-align:center;font:500 112px/.98 "Playfair Display",serif;letter-spacing:-.035em}
.t i{color:var(--cobalt);font-weight:400}
.sub{position:absolute;left:0;right:0;top:700px;text-align:center;font:italic 30px/1.35 "Playfair Display",serif;padding:0 200px}
.k{position:absolute;left:0;right:0;top:230px;text-align:center}
.n{position:absolute;left:0;right:0;bottom:92px;text-align:center;font:600 15px/1 Inter;letter-spacing:.24em;text-transform:uppercase}
""", f"""
{pxb('l',60,760,4,x=96,y=120)}{pxb('r',60,760,4,x=844,y=120)}
<div class="k kick"><span class="sq"></span>Prompt library</div>
<div class="t">The AI<br><i>Website</i><br>Copy Kit</div>
<div class="sub">50 ready-to-use prompts for better website content</div>
<div class="n">PDF &nbsp;/&nbsp; Mahak's Studio</div>
""")

# ---------- previews 1280x720: caption left, two real pages right
def preview(name, kick, head, text, left, right):
    page(name, 1280, 720, """
.k{position:absolute;left:80px;top:150px}
.h{position:absolute;left:80px;top:190px;width:340px;font:500 46px/1.08 "Playfair Display",serif;letter-spacing:-.025em}
.p{position:absolute;left:80px;top:430px;width:330px;font:400 18px/1.55 Inter}
.bar{position:absolute;left:80px;top:395px;width:56px;height:3px;background:var(--cobalt)}
""", f"""
{pxb('l',24,420,2.4,x=44,y=150)}
<div class="k kick"><span class="sq"></span>{kick}</div><div class="h">{head}</div><div class="bar"></div><div class="p">{text}</div>
<div class="pagei" style="left:470px;top:70px;width:366px;height:518px"><img src="{PG(left)}"></div>
<div class="pagei" style="left:860px;top:110px;width:366px;height:518px"><img src="{PG(right)}"></div>
""")
preview('preview-1-contents', 'Inside the kit', '50 prompts in 10 categories', 'From the hero headline to the client revision policy. Every prompt has placeholders, instructions and a tip.', 'contents', 'index')
preview('preview-2-prompt', 'Every prompt', 'Copy. Fill the brackets. Paste.', 'Each prompt page tells you when to use it, what to fill in, and gives you the full prompt to paste into your AI chat.', 'div1', 'p1')
preview('preview-3-example', 'Worked example', 'See the whole process end to end', 'A fictional bakery, from brief to reviewed copy. Inputs, prompts and outputs are clearly separated.', 'ex1', 'ex2')
preview('preview-4-brief', 'Brief + checklist', 'Start with facts. Finish with a check.', 'A reusable client and business brief feeds every prompt. A quality checklist catches weak or unsupported copy.', 'brief', 'chk')

# ---------- Instagram 1080x1350
SOCIAL = """
.k{position:absolute;left:120px;top:110px}
.f{position:absolute;left:120px;right:120px;bottom:96px;display:flex;justify-content:space-between;align-items:flex-end;border-top:2px solid var(--ink);padding-top:26px;font:600 15px/1.5 Inter;letter-spacing:.2em;text-transform:uppercase}
.f span:last-child{color:var(--cobalt)}
"""
page('post-1-hook', 1080, 1350, SOCIAL + """
.h{position:absolute;left:120px;right:120px;top:300px;font:500 112px/1.02 "Playfair Display",serif;letter-spacing:-.035em}
.h i{color:var(--cobalt);font-weight:400}
.s{position:absolute;left:120px;width:700px;top:700px;font:italic 36px/1.4 "Playfair Display",serif}
""", f"""{pxb('l',60,980,4,x=60,y=170)}{pxb('r',60,980,4,x=960,y=170)}
<div class="k kick"><span class="sq"></span>Website copy, sorted</div>
<div class="h">Stuck at <i>&ldquo;Lorem ipsum&rdquo;?</i></div>
<div class="s">50 prompts that turn real business facts into website copy you can check and edit.</div>
<div class="f"><span>The AI Website Copy Kit</span><span>Link in bio</span></div>""")

page('post-2-habits', 1080, 1350, SOCIAL + """
.h{position:absolute;left:120px;right:120px;top:260px;font:500 84px/1.05 "Playfair Display",serif;letter-spacing:-.03em}
.r{position:absolute;left:120px;right:120px;display:grid;grid-template-columns:110px 1fr;border-top:2px solid var(--ink);padding-top:26px}
.r b{font:400 72px/1 "Playfair Display",serif;color:var(--cobalt);font-variant-numeric:lining-nums}
.r div{font:500 38px/1.25 "Playfair Display",serif}.r small{display:block;font:400 22px/1.5 Inter;margin-top:8px}
""", """<div class="k kick"><span class="sq"></span>The three habits</div>
<div class="h">Write from facts.<br><i style="color:#002FA7;font-weight:400">Edit</i> like a human.<br>Check before you publish.</div>
<div class="r" style="top:660px"><b>1</b><div>Give the AI real facts<small>Use only what you can verify.</small></div></div>
<div class="r" style="top:830px"><b>2</b><div>Read every draft aloud<small>Cut anything untrue or unhelpful.</small></div></div>
<div class="r" style="top:1000px"><b>3</b><div>Run the checklist<small>Numbers, names, claims, links.</small></div></div>
<div class="f"><span>The AI Website Copy Kit</span><span>Link in bio</span></div>""")

pr = P.CATEGORIES[0]['prompts'][0]
page('post-3-prompt', 1080, 1350, SOCIAL + """
.h{position:absolute;left:120px;right:120px;top:250px;font:500 78px/1.05 "Playfair Display",serif;letter-spacing:-.03em}
.card{position:absolute;left:150px;right:150px;top:520px;padding:56px 70px;font:400 27px/1.6 Inter}
.card:before,.card:after{content:"";position:absolute;top:0;bottom:0;width:30px;border:4px solid var(--cobalt)}
.card:before{left:0;border-right:0}.card:after{right:0;border-left:0}
.fg{position:absolute;left:120px;right:120px;top:960px;background:var(--ink);color:var(--ivory);padding:34px 44px;font:400 23px/1.5 Inter}
.fg b{display:block;font:600 14px/1 Inter;letter-spacing:.22em;text-transform:uppercase;margin-bottom:14px;color:rgba(249,248,246,.75)}
""", """<div class="k kick"><span class="sq"></span>Prompt 1 of 50</div>
<div class="h">Fill the <i style="color:#002FA7;font-weight:400">[brackets]</i>.<br>Paste. Done.</div>
<div class="card">Write hero-section copy for the homepage of <span class="ph">[BUSINESS NAME]</span>.<br><br>About the business: <span class="ph">[BUSINESS DESCRIPTION]</span><br>Who it is for: <span class="ph">[TARGET AUDIENCE]</span><br>Facts you may use: <span class="ph">[KEY FACTS]</span></div>
<div class="fg"><b>The Fact Guard, in every prompt</b>Use only the facts I have given you. If a detail is missing, flag it instead of guessing.</div>
<div class="f"><span>The AI Website Copy Kit</span><span>Link in bio</span></div>""")
print('assets html written')
