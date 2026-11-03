// Writes the checker's results for the site to read. A failing check still produces results, and the site shows them.
import { spawnSync } from 'node:child_process';
import { mkdirSync, writeFileSync } from 'node:fs';

for (const [command, ...prefix] of [['python'], ['python3'], ['py', '-3']]) {
  const run = spawnSync(command, [...prefix, '../tools/check.py', '--json'], { encoding: 'utf-8' });
  if (run.error || !run.stdout?.trimStart().startsWith('[')) continue;
  mkdirSync('src/data', { recursive: true });
  writeFileSync('src/data/checks.json', run.stdout);
  process.exit(0);
}
console.error('Could not run tools/check.py: Python was not found.');
process.exit(1);
