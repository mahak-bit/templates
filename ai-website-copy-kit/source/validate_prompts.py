import re, itertools, sys
from prompts import CATEGORIES, CORE_SIX, all_prompts, expanded, FACT_GUARD
PH = re.compile(r"\[[A-Z][A-Z0-9 &/'’,\-\.\(\)]*\]")
core = {c[0] for c in CORE_SIX}
errs, warns = [], []
ap = all_prompts()
nums = [p["n"] for _, p in ap]
if nums != list(range(1, 51)): errs.append(f"numbering wrong: {nums}")
if len(CATEGORIES) != 10: errs.append("need 10 categories")
for c in CATEGORIES:
    if len(c["prompts"]) != 5: errs.append(f"category {c['n']} has {len(c['prompts'])} prompts")
titles = [p["title"].lower() for _, p in ap]
if len(set(titles)) != len(titles): errs.append("duplicate titles")
for c, p in ap:
    used = set(PH.findall(p["prompt"]))
    fill = {f[0] for f in p["fill"]}
    unexplained = used - core - fill
    unused_fill = fill - used
    if unexplained: errs.append(f"P{p['n']} unexplained placeholders: {sorted(unexplained)}")
    if unused_fill: errs.append(f"P{p['n']} fill not used in prompt: {sorted(unused_fill)}")
    if "{FG}" not in p["prompt"]: errs.append(f"P{p['n']} missing Fact Guard")
    for k in ("use", "tip", "title"):
        if not p.get(k): errs.append(f"P{p['n']} missing {k}")
    # stray braces / brackets
    txt = expanded(p)
    if "{" in txt or "}" in txt: errs.append(f"P{p['n']} stray brace")
    for b in re.findall(r"\[[^\]]*\]", txt):
        if not PH.fullmatch(b) and ":" not in b: warns.append(f"P{p['n']} odd bracket: {b}")
# near-duplicate check on prompt bodies (excluding fact guard + shared context lines)
def toks(p):
    t = p["prompt"].replace("{FG}", "")
    return set(re.findall(r"[a-z']+", t.lower()))
for (c1,p1),(c2,p2) in itertools.combinations(ap,2):
    a,b = toks(p1),toks(p2)
    j = len(a&b)/len(a|b)
    if j > 0.5: warns.append(f"P{p1['n']} vs P{p2['n']} similarity {j:.2f}")
wc = [len(expanded(p).split()) for _,p in ap]
print("prompts:", len(ap), "| words per prompt min/avg/max:", min(wc), sum(wc)//len(wc), max(wc), "| total", sum(wc))
print("ERRORS:", *errs, sep="\n  ") if errs else print("ERRORS: none")
print("WARNINGS:", *warns, sep="\n  ") if warns else print("WARNINGS: none")
sys.exit(1 if errs else 0)
