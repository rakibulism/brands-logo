// ES module entry for the brands-logo npm package.
import { createRequire } from "node:module";

const lib = createRequire(import.meta.url)("./index.cjs");

export const { version, count, categories, logos, url, has } = lib;
export default lib;
