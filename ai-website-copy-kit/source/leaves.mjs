import { createRequire } from 'module';
const require = createRequire('/opt/node22/lib/node_modules/');
const { chromium } = require('playwright');
import path from 'path'; import fs from 'fs';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const pg = await b.newPage();
await pg.goto('file://' + path.resolve(process.argv[2]), { waitUntil: 'load' });
const data = await pg.evaluate(() => [...document.querySelectorAll('section.pg, section.full')].map((s, i) => ({
  i: i + 1, id: s.id,
  leaves: [...s.querySelectorAll('*')].filter(e => e.children.length === 0 && e.tagName !== 'svg' && e.tagName !== 'path' && e.textContent.trim().length > 1).map(e => e.textContent)
})));
fs.writeFileSync(process.argv[3], JSON.stringify(data)); await b.close();
