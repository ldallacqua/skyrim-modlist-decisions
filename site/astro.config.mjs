import react from '@astrojs/react';
import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'astro/config';
import rehypeRepoLinks from './src/lib/rehype-repo-links.mjs';

export const BASE = '/skyrim-modlist-decisions';

export default defineConfig({
  site: 'https://ldallacqua.github.io',
  base: BASE,
  trailingSlash: 'always',
  integrations: [react()],
  vite: { plugins: [tailwindcss()] },
  markdown: {
    rehypePlugins: [[rehypeRepoLinks, { base: BASE }]],
    shikiConfig: { theme: 'github-dark-dimmed' },
  },
});
