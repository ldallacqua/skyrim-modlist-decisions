// Publishes dist/ to the gh-pages branch. This avoids GitHub Actions, which needs a token with the workflow scope.
import { execFileSync } from 'node:child_process';
import { cpSync, mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';

const REMOTE = 'https://github.com/ldallacqua/skyrim-modlist-decisions.git';
const identity = (key) => execFileSync('git', ['config', key], { encoding: 'utf-8' }).trim();
const folder = mkdtempSync(path.join(tmpdir(), 'site-deploy-'));
const git = (...args) => execFileSync('git', args, { cwd: folder, stdio: 'inherit' });

try {
  cpSync('dist', folder, { recursive: true });
  writeFileSync(path.join(folder, '.nojekyll'), ''); // Otherwise GitHub Pages ignores the _astro folder
  git('init', '-q', '-b', 'gh-pages');
  git('add', '-A');
  git('-c', `user.name=${identity('user.name')}`, '-c', `user.email=${identity('user.email')}`, 'commit', '-q', '-m', 'Deploy the site');
  git('-c', 'credential.helper=', '-c', 'credential.helper=!gh auth git-credential', 'push', '-q', '-f', REMOTE, 'gh-pages');
  console.log('Deployed to gh-pages.');
} finally {
  rmSync(folder, { recursive: true, force: true });
}
