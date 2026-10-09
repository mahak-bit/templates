#!/usr/bin/env bash
# Rebuild everything. Requires: python3 (pypdf, python-docx), node + playwright, Chromium, Inter font installed.
set -euo pipefail
cd "$(dirname "$0")"
python3 source/validate_prompts.py
python3 source/build_html.py                       && node source/render.mjs _build/kit.html _build/pass1.pdf
python3 source/pagemap.py _build/pass1.pdf _build/pages1.json
python3 source/build_html.py _build/pages1.json    && node source/render.mjs _build/kit.html _build/pass2.pdf
python3 source/pagemap.py _build/pass2.pdf _build/pages3.json
cmp <(python3 -c "import json;print(json.load(open('_build/pages1.json')))") <(python3 -c "import json;print(json.load(open('_build/pages3.json')))")
cp _build/pass2.pdf dist/The-AI-Website-Copy-Kit.pdf
python3 source/build_docx.py && python3 source/build_txt.py && python3 source/build_canva.py
