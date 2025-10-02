const html = (s) => new Response(s, {headers:{'Content-Type':'text/html; charset=utf-8'}});
const rnd = (n) => Math.floor(Math.random()*n);
const QUOTES = [
  'Simplicity is the soul of efficiency. — Austin Freeman',
  'Programs must be written for people to read. — Harold Abelson',
  'Small steps lead to big results.',
  'Progress over perfection.',
  'Ship early, learn fast.'
];

self.addEventListener('install', e => self.skipWaiting());
self.addEventListener('activate', e => self.clients.claim());

self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);
  if (url.pathname === '/api/suggest') {
    event.respondWith(handleSuggest(url));
  } else if (url.pathname === '/api/filter') {
    event.respondWith(handleFilter(event.request));
  } else if (url.pathname === '/api/price') {
    event.respondWith(handlePrice(url));
  } else if (url.pathname === '/api/quote') {
    event.respondWith(handleQuote());
  }
});

async function handleSuggest(url) {
  const q = url.searchParams.get('q')?.trim() ?? '';
  const limit = parseInt(url.searchParams.get('limit') || '5', 10);
  if (!q) return html('<em>Type to see suggestions…</em>');
  const base = ['htmx','hyperscript','django','flask','alpine','tailwind','dom','events','triggers','swap','target','include','ajax','json','partial'];
  const filtered = base.filter(x => x.includes(q.toLowerCase())).slice(0, limit);
  const list = filtered.length ? filtered.map(s => `<li>${s}</li>`).join('') : '<li><em>No matches</em></li>';
  return html(`<strong>Suggestions for "${q}"</strong><ul>${list}</ul>`);
}

async function handleFilter(req) {
  const body = await req.formData();
  const tags = (body.get('tags') || '').split(',').filter(Boolean);
  const items = [
    {name:'Build a Nav Bar', tag:'frontend'},
    {name:'REST Endpoint', tag:'backend'},
    {name:'SQL Basics', tag:'data'},
    {name:'Pipelines 101', tag:'devops'},
    {name:'HTMX Partials', tag:'frontend'},
    {name:'ORM Patterns', tag:'backend'},
    {name:'Pandas Intro', tag:'data'},
    {name:'Containerize App', tag:'devops'}
  ];
  const filtered = tags.length ? items.filter(i => tags.includes(i.tag)) : items;
  const htmlStr = filtered.map(i => `<div>• ${i.name} <span class="tag">${i.tag}</span></div>`).join('') || '<em>No items match</em>';
  return html(htmlStr);
}

async function handlePrice(url) {
  const value = parseInt(url.searchParams.get('value') || url.searchParams.get('price') || '50', 10);
  const init = url.searchParams.get('init') === 'true';
  const total = Math.round(value * 15);
  const msg = init ? '(initialized) ' : '';
  return html(`Current value: ${value} → ${msg}total = R ${total}`);
}

async function handleQuote() {
  const q = QUOTES[rnd(QUOTES.length)];
  return html(`<div>📝 ${q}</div>`);
}