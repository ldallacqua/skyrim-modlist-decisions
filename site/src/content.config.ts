import { glob } from 'astro/loaders';
import { defineCollection, z } from 'astro:content';

// The repository's Markdown is the source of truth, so these read it where it lives instead of copying it into the site
const fileId = ({ entry }: { entry: string }) => entry.replace(/\.md$/, '').toLowerCase();
const schema = z.object({}).passthrough();

export const collections = {
  decisions: defineCollection({ loader: glob({ pattern: ['[0-9]*.md', '!0000-*'], base: '../decisions', generateId: fileId }), schema }),
  research: defineCollection({ loader: glob({ pattern: '*.md', base: '../research', generateId: fileId }), schema }),
  docs: defineCollection({ loader: glob({ pattern: ['PLAYBOOK.md', 'CHANGELOG.md'], base: '..', generateId: fileId }), schema }),
};
