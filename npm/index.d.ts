export interface Logo {
  /** File slug: logos/{n}.svg */
  n: string;
  /** Category key, matches Category.key */
  c: string;
  /** true for a wordmark (icon + name), false for an icon only */
  w: boolean;
}

export interface Category {
  key: string;
  name: string;
  icon: string;
  count: number;
}

export declare const version: string;
export declare const count: number;
export declare const categories: Category[];
export declare const logos: Logo[];
/** Versioned jsDelivr URL for a logo slug. Throws on unknown slugs. */
export declare function url(name: string): string;
/** True when a logo with this slug exists. */
export declare function has(name: string): boolean;

declare const lib: {
  version: string;
  count: number;
  categories: Category[];
  logos: Logo[];
  url: typeof url;
  has: typeof has;
};
export default lib;
