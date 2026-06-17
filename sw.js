/* Logos — service worker (offline shell + cached logos) */
const CACHE = "logos-v1";
const SHELL = ["/", "/index.html", "/docs.html", "/updates.html", "/assets/favicon.svg", "/assets/logos.json"];

self.addEventListener("install", (e) => {
  e.waitUntil(
    caches.open(CACHE).then((c) => c.addAll(SHELL).catch(() => {})).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return; // only same-origin

  // network-first for documents + JSON (keep content fresh, fall back offline)
  if (req.destination === "document" || url.pathname.endsWith(".json")) {
    e.respondWith(
      fetch(req)
        .then((r) => { const c = r.clone(); caches.open(CACHE).then((ca) => ca.put(req, c)); return r; })
        .catch(() => caches.match(req).then((m) => m || caches.match("/")))
    );
    return;
  }

  // cache-first for everything else (logos, icons, css)
  e.respondWith(
    caches.match(req).then((m) => m || fetch(req).then((r) => {
      const c = r.clone();
      caches.open(CACHE).then((ca) => ca.put(req, c));
      return r;
    }).catch(() => m))
  );
});
