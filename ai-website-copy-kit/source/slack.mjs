import { createRequire } from 'module';
const require = createRequire('/opt/node22/lib/node_modules/');
const { chromium } = require('playwright');
import path from 'path';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const pg = await b.newPage({ viewport: { width: 643, height: 1000 } });
await pg.goto('file://' + path.resolve(process.argv[2]), { waitUntil: 'load' });
await pg.evaluate(() => document.fonts.ready); await pg.emulateMedia({ media: 'print' });
const r = await pg.evaluate(() => [...document.querySelectorAll('section.pp')].map(s => {
  const top = s.getBoundingClientRect(); const card = s.querySelector('.cardb').getBoundingClientRect();
  const rail = s.querySelector('.rail'); const kids = [...rail.children]; const last = kids[kids.length - 1];
  // natural rail height = sum of children heights + gaps (tip has margin-top:auto so measure without it)
  const used = kids.slice(0, -1).reduce((a, k) => a + k.getBoundingClientRect().height, 0) + (kids.length - 1) * 5.5 * 3.78 + last.getBoundingClientRect().height;
  return { id: s.id, cardSlackMm: +((top.bottom - card.bottom) / 3.78).toFixed(1), railSlackMm: +((rail.clientHeight - used) / 3.78).toFixed(1) };
}));
r.sort((a, b) => Math.min(a.cardSlackMm, a.railSlackMm) - Math.min(b.cardSlackMm, b.railSlackMm));
console.log('tightest 6 prompt pages (mm of free space; card slack / rail slack):');
r.slice(0, 6).forEach(x => console.log(' ', x.id, x.cardSlackMm, x.railSlackMm));
console.log('min card slack', Math.min(...r.map(x => x.cardSlackMm)), '| min rail slack', Math.min(...r.map(x => x.railSlackMm)));
await b.close();
