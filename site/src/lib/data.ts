import fs from 'node:fs';
import path from 'node:path';
import { parse } from 'csv-parse/sync';
import type { CollectionEntry } from 'astro:content';
import checks from '../data/checks.json';

const REPO = path.resolve(process.cwd(), '..');
const NEXUS = 'https://www.nexusmods.com/skyrimspecialedition/mods/';

function readRepo(file: string) {
  return fs.readFileSync(path.join(REPO, file), 'utf-8');
}

function readCsv(file: string): Record<string, string>[] {
  return parse(readRepo(file), { columns: true, skip_empty_lines: true });
}

export interface Mod {
  name: string;
  version: string;
  enabled: boolean;
  url: string | null;
  official: boolean;
  required: boolean;
}

export interface Section {
  name: string;
  slug: string;
  zone: string;
  decisions: string[];
  mods: Mod[];
}

export interface Plugin {
  name: string;
  type: string;
  itm: number;
  udr: number;
  navmeshes: number;
  cleaned: boolean;
}

export type Status = 'accepted' | 'proposed' | 'superseded';

export interface Decision {
  id: string;
  number: string;
  title: string;
  status: Status;
  afterTheFact: boolean;
  date: string;
  summary: string;
}

// The zones from decision 0003, with the separators where they are today
const ZONES: Record<string, string> = {
  'DLC & CC': 'Top', 'SKSE & Frameworks': 'Top', Fixes: 'Top',
  'UI & Camera': 'Upper',
  Shaders: 'Middle', 'Skeleton & Physics': 'Middle', Body: 'Middle', 'Head & Face': 'Middle', Skin: 'Middle',
  Presets: 'Middle', Hair: 'Middle', Animation: 'Middle', Armor: 'Middle', Gameplay: 'Middle',
  Tools: 'End', 'Recently Added': 'End', Outputs: 'End',
};

const SECTION_DECISIONS: Record<string, string[]> = {
  'DLC & CC': ['0001', '0011'], 'SKSE & Frameworks': ['0001'], Shaders: ['0006', '0014'], 'Skeleton & Physics': ['0004'],
  Body: ['0004'], 'Head & Face': ['0004'], Skin: ['0004'], Presets: ['0004'], Animation: ['0005'], Armor: ['0004'],
  Tools: ['0005', '0008'], 'Recently Added': ['0012'], Outputs: ['0007', '0008'],
};

export function slugify(name: string) {
  return name.toLowerCase().replace(/&/g, 'and').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

function cleanVersion(version: string) {
  // MO2 prefixes the versions it can't parse with f or d, and pads the rest to four numbers
  return version.replace(/^[fd](?=\d)/, '').replace(/\.0(?=$|-|[a-z])/, '').replace(/-$/, '');
}

export function getSections(): Section[] {
  const required = new Set<string>(JSON.parse(readRepo('rules/rules.json')).required_mods);
  const sections: Section[] = [];
  for (const row of readCsv('list/mods.csv')) {
    if (row.type === 'separator') {
      sections.push({ name: row.name, slug: slugify(row.name), zone: ZONES[row.name] ?? 'Middle', decisions: SECTION_DECISIONS[row.name] ?? [], mods: [] });
      continue;
    }
    sections.at(-1)?.mods.push({
      name: row.type === 'unmanaged' ? row.name.replace(/^[\w ]+:\s*/, '') : row.name,
      version: cleanVersion(row.version),
      enabled: row.enabled === 'yes',
      url: row.nexus_id ? NEXUS + row.nexus_id : null,
      official: row.type === 'unmanaged',
      required: required.has(row.name),
    });
  }
  return sections;
}

export function getPlugins(): Plugin[] {
  const cleaning = new Map(readCsv('list/cleaning.csv').map((row) => [row.plugin, row]));
  return readRepo('list/loadorder.txt')
    .split(/\r?\n/)
    .filter((line) => line.trim() && !line.startsWith('#'))
    .map((name) => {
      const row = cleaning.get(name);
      const [itm, udr, navmeshes] = [row?.itm, row?.udr, row?.deleted_navmeshes].map(Number).map((n) => n || 0);
      return { name, type: name.split('.').pop()!.toUpperCase(), itm, udr, navmeshes, cleaned: itm + udr > 0 };
    });
}

export function toDecision(entry: CollectionEntry<'decisions'>): Decision {
  const body = entry.body ?? '';
  const heading = body.match(/^# (\d{4})\. (.+)$/m);
  const status = body.match(/\*\*Status:\*\* (.+)$/m)?.[1] ?? '';
  return {
    id: entry.id,
    number: heading?.[1] ?? '',
    title: heading?.[2] ?? entry.id,
    status: status.split(' ')[0] as Status,
    afterTheFact: status.includes('after the fact'),
    date: body.match(/\*\*Date:\*\* (.+)$/m)?.[1] ?? '',
    summary: body.match(/\*\*Summary:\*\* (.+)$/m)?.[1]?.replace(/\[([^\]]+)\]\([^)]*\)/g, '$1') ?? '',
  };
}

export function byNumber(a: Decision, b: Decision) {
  return a.number.localeCompare(b.number);
}

export type Check = { title: string; decision: string; status: string | null; result: 'ok' | 'warn' | 'fail'; problems: string[] };
export const getChecks = () => checks as Check[];
