import { createRequire } from 'module';
const require = createRequire('/opt/node22/lib/node_modules/');
const { chromium } = require('playwright');
import path from 'path'; import fs from 'fs';
const dir = process.argv[2], out = process.argv[3];
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.html'))) {
  const m = fs.readFileSync(path.join(dir, f), 'utf8').match(/width:(\d+)px;height:(\d+)px;position:relative/);
  const pg = await b.newPage({ viewport: { width: +m[1], height: +m[2] }, deviceScaleFactor: 2 });
  await pg.goto('file://' + path.resolve(dir, f), { waitUntil: 'load' }); await pg.evaluate(() => document.fonts.ready);
  const name = f.replace('.html', '.png'); await pg.screenshot({ path: path.join(out, name) });
  console.log(name, m[1] + 'x' + m[2]); await pg.close();
}
await b.close();
