"use strict";
// CommonJS entry for the brands-logo npm package.
const data = require("../assets/logos.json");
const { version } = require("../package.json");

const CDN = `https://cdn.jsdelivr.net/npm/brands-logo@${version}/logos/`;
const names = new Set(data.logos.map((l) => l.n));

/** Versioned jsDelivr URL for a logo slug, e.g. url("github"). Throws on unknown slugs. */
function url(name) {
  if (!names.has(name)) throw new Error(`brands-logo: unknown logo "${name}"`);
  return `${CDN}${name}.svg`;
}

/** True when a logo with this slug exists. */
function has(name) {
  return names.has(name);
}

module.exports = {
  version,
  count: data.count,
  categories: data.categories,
  logos: data.logos,
  url,
  has,
};
