import { Check, ChevronRight, ExternalLink, Search, X } from 'lucide-react';
import { useDeferredValue, useEffect, useMemo, useState } from 'react';
import type { Plugin, Section } from '../lib/data';

interface Props {
  sections: Section[];
  plugins: Plugin[];
  base: string;
  decisionIds: Record<string, string>;
}

const COLLAPSED_BY_DEFAULT = new Set(['dlc-and-cc']);

function Row({ mod }: { mod: Section['mods'][number] }) {
  return (
    <li className="flex items-center gap-3 border-t border-line-subtle/70 py-1.5 pr-3 pl-4 text-sm transition-colors hover:bg-bg-3/50">
      <span
        aria-label={mod.enabled ? 'Enabled' : 'Disabled'}
        role="img"
        className={`grid size-3.5 shrink-0 place-items-center rounded-[3px] ${mod.enabled ? 'bg-accent text-bg-0' : 'border border-line-strong'}`}
      >
        {mod.enabled && <Check size={11} strokeWidth={3.5} />}
      </span>
      <span className={`min-w-0 flex-1 truncate ${mod.enabled ? '' : 'text-inactive'}`} title={mod.name}>
        {mod.name}
      </span>
      {mod.required && <span className="hidden rounded border border-line px-1.5 text-[11px] text-secondary sm:inline">required</span>}
      {mod.official && <span className="hidden text-xs text-inactive sm:inline">game content</span>}
      {mod.version && <span className="hidden shrink-0 font-mono text-xs text-inactive sm:inline">{mod.version}</span>}
      {mod.url ? (
        <a href={mod.url} target="_blank" rel="noreferrer" aria-label={`${mod.name} on Nexus Mods`} className="shrink-0 rounded p-1 text-inactive hover:text-accent-text">
          <ExternalLink size={14} />
        </a>
      ) : (
        <span className="w-[22px] shrink-0" />
      )}
    </li>
  );
}

export default function ModList({ sections, plugins, base, decisionIds }: Props) {
  const [tab, setTab] = useState<'mods' | 'plugins'>('mods');
  const [query, setQuery] = useState('');
  const [cleanedOnly, setCleanedOnly] = useState(false);
  const [closed, setClosed] = useState<Set<string>>(COLLAPSED_BY_DEFAULT);
  const deferred = useDeferredValue(query.trim().toLowerCase());

  // A link from another page opens the section it points to
  useEffect(() => {
    const open = () => {
      const slug = decodeURIComponent(location.hash.slice(1));
      if (!slug) return;
      setTab('mods');
      setClosed((previous) => {
        const next = new Set(previous);
        next.delete(slug);
        return next;
      });
      requestAnimationFrame(() => document.getElementById(slug)?.scrollIntoView());
    };
    open();
    window.addEventListener('hashchange', open);
    return () => window.removeEventListener('hashchange', open);
  }, []);

  const visible = useMemo(
    () => sections.map((section) => ({ ...section, mods: section.mods.filter((mod) => mod.name.toLowerCase().includes(deferred)) })).filter((section) => !deferred || section.mods.length),
    [sections, deferred],
  );
  const matches = visible.reduce((total, section) => total + section.mods.length, 0);
  const shownPlugins = useMemo(
    () => plugins.map((plugin, index) => ({ ...plugin, index })).filter((plugin) => plugin.name.toLowerCase().includes(deferred) && (!cleanedOnly || plugin.cleaned || plugin.navmeshes)),
    [plugins, deferred, cleanedOnly],
  );
  const allClosed = closed.size === sections.length;

  function toggle(slug: string) {
    setClosed((previous) => {
      const next = new Set(previous);
      if (next.has(slug)) next.delete(slug);
      else next.add(slug);
      return next;
    });
  }

  return (
    <div>
      <div className="sticky top-14 z-30 -mx-4 flex flex-wrap items-center gap-2 border-b border-line-subtle bg-bg-0/90 px-4 py-3 backdrop-blur-md sm:-mx-6 sm:px-6">
        <div role="tablist" aria-label="View" className="flex rounded-md border border-line bg-bg-1 p-0.5">
          {(['mods', 'plugins'] as const).map((name) => (
            <button
              key={name}
              role="tab"
              aria-selected={tab === name}
              onClick={() => setTab(name)}
              className={`rounded px-3 py-1 text-sm capitalize transition-colors ${tab === name ? 'bg-bg-3 text-strong' : 'text-secondary hover:text-strong'}`}
            >
              {name}
            </button>
          ))}
        </div>
        <label className="relative min-w-40 flex-1 sm:max-w-xs">
          <span className="sr-only">Filter by name</span>
          <Search size={15} className="pointer-events-none absolute top-1/2 left-2.5 -translate-y-1/2 text-inactive" />
          <input
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder={`Filter ${tab}`}
            className="w-full rounded-md border border-line bg-bg-1 py-1.5 pr-8 pl-8 text-sm text-strong placeholder:text-inactive focus:border-accent focus:outline-none"
          />
          {query && (
            <button aria-label="Clear filter" onClick={() => setQuery('')} className="absolute top-1/2 right-2 -translate-y-1/2 text-inactive hover:text-strong">
              <X size={15} />
            </button>
          )}
        </label>
        <div className="ml-auto flex items-center gap-3 text-sm text-secondary">
          {tab === 'mods' ? (
            <>
              <span aria-live="polite">{matches} entries</span>
              <button className="rounded px-2 py-1 hover:bg-bg-2 hover:text-strong" onClick={() => setClosed(allClosed ? new Set() : new Set(sections.map((section) => section.slug)))}>
                {allClosed ? 'Expand all' : 'Collapse all'}
              </button>
            </>
          ) : (
            <>
              <span aria-live="polite">{shownPlugins.length} plugins</span>
              <label className="flex items-center gap-2">
                <input type="checkbox" checked={cleanedOnly} onChange={(event) => setCleanedOnly(event.target.checked)} className="accent-accent" />
                Cleaning results only
              </label>
            </>
          )}
        </div>
      </div>

      {tab === 'mods' ? (
        <div className="mt-4 overflow-hidden rounded-md border border-line">
          {visible.map((section) => {
            const open = deferred ? true : !closed.has(section.slug);
            return (
              <section key={section.slug} id={section.slug} aria-label={section.name} className="scroll-mt-32">
                <div className="flex items-center gap-2 border-t border-line bg-separator pr-3 first:border-t-0">
                  <button aria-expanded={open} onClick={() => toggle(section.slug)} className="flex min-w-0 flex-1 items-center gap-2 py-2 pl-3 text-left text-sm font-semibold text-strong">
                    <ChevronRight size={15} className={`shrink-0 text-accent-text transition-transform ${open ? 'rotate-90' : ''}`} />
                    <span className="truncate">{section.name}</span>
                    <span className="font-mono text-xs font-normal text-secondary">{section.mods.length}</span>
                  </button>
                  {section.decisions.map((number) => (
                    <a key={number} href={`${base}/decisions/${decisionIds[number]}/`} title={`Decision ${number}`} className="shrink-0 rounded border border-line-strong px-1.5 py-0.5 font-mono text-[11px] text-secondary hover:border-accent hover:text-accent-text">
                      {number}
                    </a>
                  ))}
                </div>
                {open && (
                  <ul className="bg-bg-2">
                    {section.mods.map((mod) => (
                      <Row key={mod.name} mod={mod} />
                    ))}
                    {!section.mods.length && <li className="py-2 pl-4 text-sm text-inactive">Empty</li>}
                  </ul>
                )}
              </section>
            );
          })}
          {!visible.length && <p className="p-6 text-sm text-secondary">Nothing matches that name.</p>}
        </div>
      ) : (
        <div className="mt-4 overflow-x-auto rounded-md border border-line">
          <table className="w-full bg-bg-2 text-sm">
            <thead>
              <tr className="bg-bg-1 text-left text-xs text-secondary">
                <th className="px-3 py-2 font-semibold">Order</th>
                <th className="px-3 py-2 font-semibold">Plugin</th>
                <th className="px-3 py-2 font-semibold">Type</th>
                <th className="px-3 py-2 text-right font-semibold whitespace-nowrap">ITMs removed</th>
                <th className="px-3 py-2 text-right font-semibold whitespace-nowrap">UDRs undeleted</th>
                <th className="px-3 py-2 text-right font-semibold whitespace-nowrap">Deleted navmeshes</th>
              </tr>
            </thead>
            <tbody className="font-mono text-xs">
              {shownPlugins.map((plugin) => (
                <tr key={plugin.name} className="border-t border-line-subtle/70 hover:bg-bg-3/50">
                  <td className="px-3 py-1.5 text-inactive">{plugin.index}</td>
                  <td className="px-3 py-1.5 font-sans text-sm whitespace-nowrap">{plugin.name}</td>
                  <td className="px-3 py-1.5 text-secondary">{plugin.type}</td>
                  <td className="px-3 py-1.5 text-right">{plugin.itm || <span className="text-line-strong">·</span>}</td>
                  <td className="px-3 py-1.5 text-right">{plugin.udr || <span className="text-line-strong">·</span>}</td>
                  <td className={`px-3 py-1.5 text-right ${plugin.navmeshes ? 'text-amber' : ''}`}>{plugin.navmeshes || <span className="text-line-strong">·</span>}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
