import { visit } from 'unist-util-visit';

function text(node) {
  return node.value ?? (node.children ?? []).map(text).join('');
}

/** Turns links between the repository's files into site routes. Returns the href unchanged when it isn't one of them. */
export function repoHref(href, base) {
  const [path, hash = ''] = href.split('#');
  const anchor = hash && `#${hash}`;
  let match;
  if ((match = path.match(/(?:^|\/)(\d{4}-[\w-]+)\.md$/))) return `${base}/decisions/${match[1]}/${anchor}`;
  if ((match = path.match(/(?:^|\/)research\/([\w-]+)\.md$/))) return `${base}/research/${match[1].toLowerCase()}/${anchor}`;
  if (/(?:^|\/)PLAYBOOK\.md$/.test(path)) return `${base}/playbook/${anchor}`;
  if (/(?:^|\/)CHANGELOG\.md$/.test(path)) return `${base}/changelog/${anchor}`;
  if (/(?:^|\/)list\/[\w.-]*$/.test(path)) return `${base}/modlist/`;
  return href;
}

/** Fits the repository's Markdown into the pages: the title and a decision's status list become part of the page header. */
export default function rehypeRepoLinks({ base }) {
  return (tree) => {
    let removedTitle = false;
    tree.children = tree.children.filter((node) => {
      if (!removedTitle && node.tagName === 'h1') return !(removedTitle = true);
      return !(node.tagName === 'ul' && /^\s*Status:/.test(text(node)));
    });
    visit(tree, 'element', (node) => {
      if (node.tagName === 'table') node.properties.className = ['doc-table'];
      if (node.tagName !== 'a' || !node.properties.href) return;
      const href = repoHref(String(node.properties.href), base);
      node.properties.href = href;
      if (/^https?:/.test(href)) {
        node.properties.target = '_blank';
        node.properties.rel = 'noreferrer';
      }
    });
  };
}
