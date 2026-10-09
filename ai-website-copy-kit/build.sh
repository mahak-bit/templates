#!/usr/bin/env bash
# Rebuild the PDF + companion files. Requires: python3 (pypdf, python-docx), node + playwright, Chromium, Inter font installed.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p _build dist
python3 source/validate_prompts.py
python3 source/build_html.py                    && node source/render.mjs _build/kit.html _build/pass1.pdf
python3 source/pagemap.py _build/pass1.pdf _build/pages1.json
python3 source/build_html.py _build/pages1.json && node source/render.mjs _build/kit.html _build/pass2.pdf
python3 source/pagemap.py _build/pass2.pdf _build/pages3.json
node source/qa.mjs _build/kit.html                       # fixed-page overflow at print width
node source/leaves.mjs _build/kit.html _build/leaves.json
python3 source/pdfcheck.py _build/leaves.json _build/pass2.pdf   # every fragment on its own PDF page
cp _build/pass2.pdf dist/The-AI-Website-Copy-Kit.pdf
python3 source/build_docx.py && python3 source/build_txt.py
