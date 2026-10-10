// Measure every fixed page: does its content fit its frame? Report fill ratio per page type.
import { createRequire } from 'module';
const require = createRequire('/opt/node22/lib/node_modules/');
const { chromium } = require('playwright');
import path from 'path';
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const page = await browser.newPage({ viewport: { width: 643, height: 1000 } });
await page.goto('file://' + path.resolve(process.argv[2]), { waitUntil: 'load' });
await page.evaluate(() => document.fonts.ready);
await page.emulateMedia({ media: 'print' });
const res = await page.evaluate(() => {
  const out = [];
  document.querySelectorAll('section.pg, section.full').forEach((s, i) => {
    const over = s.scrollHeight - s.clientHeight;
    // lowest descendant bottom relative to section top
    let low = 0; const top = s.getBoundingClientRect().top;
    s.querySelectorAll('*').forEach(e => { const b = e.getBoundingClientRect().bottom - top; if (b > low && e.getBoundingClientRect().height > 0) low = b; });
    const wide = [...s.querySelectorAll('*')].filter(e => e.scrollWidth > e.clientWidth + 2 && getComputedStyle(e).overflow === 'visible' && e.clientWidth > 0 && e.tagName !== 'svg' && !e.closest('svg')).length;
    out.push({ i: i + 1, id: s.id, over: Math.round(over), fill: +(low / s.clientHeight).toFixed(2), h: Math.round(s.clientHeight) });
  });
  return out;
});
const bad = res.filter(r => r.over > 1);
console.log('sections:', res.length, '| overflowing:', bad.length);
bad.forEach(r => console.log('  OVERFLOW', r.id, '+' + r.over + 'px'));
const pp = res.filter(r => r.id.startsWith('p-'));
console.log('prompt pages fill min/max:', Math.min(...pp.map(r => r.fill)), Math.max(...pp.map(r => r.fill)));
res.filter(r => r.fill < 0.55 && !r.id.startsWith('cat-') && r.id !== 'cover' && r.id !== 'sec-closing').forEach(r => console.log('  LOW FILL', r.id, r.fill));
await browser.close();
