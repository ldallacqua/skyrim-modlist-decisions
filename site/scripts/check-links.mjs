// Fails if any internal link or asset in dist/ points to a file that doesn't exist.
import { existsSync, readdirSync, readFileSync } from 'node:fs';
import path from 'node:path';

const BASE = '/skyrim-modlist-decisions';
const pages = readdirSync('dist', { recursive: true }).filter((file) => String(file).endsWith('.html')).map(String);
const broken = new Set();
let checked = 0;

for (const page of pages) {
  const html = readFileSync(path.join('dist', page), 'utf-8');
  for (const [, url] of html.matchAll(/\s(?:href|src)="([^"]+)"/g)) {
    if (/^(https?:|mailto:|#|data:)/.test(url)) continue;
    const clean = url.split('#')[0].split('?')[0];
    checked++;
    const target = clean.startsWith(BASE) ? clean.slice(BASE.length) : clean.startsWith('/') ? null : path.posix.join('/', path.posix.dirname(page.replaceAll('\\', '/')), clean);
    const file = target && path.join('dist', decodeURI(target));
    if (!file || !(existsSync(path.join(file, 'index.html')) || (existsSync(file) && !file.endsWith(path.sep)))) broken.add(`${page}: ${url}`);
  }
}

console.log(`${pages.length} pages, ${checked} internal links checked, ${broken.size} broken`);
for (const item of broken) console.log(`  ${item}`);
process.exit(broken.size ? 1 : 0);
