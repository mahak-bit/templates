import { createRequire } from 'module';
const require = createRequire('/opt/node22/lib/node_modules/');
const { chromium } = require('playwright');
import path from 'path';
const [,, htmlPath, pdfPath] = process.argv;
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const page = await browser.newPage();
await page.goto('file://' + path.resolve(htmlPath), { waitUntil: 'load' });
await page.evaluate(() => document.fonts.ready);
const fams = await page.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.style));
console.log('webfonts loaded:', fams.join(', '));
await page.pdf({ path: pdfPath, format: 'A4', printBackground: true, preferCSSPageSize: true, outline: true, tagged: true,
  displayHeaderFooter: false });
await browser.close();
console.log('wrote', pdfPath);
