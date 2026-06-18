# Brands Logo — Playground & how-to

This is the copy + steps for the **Figma Community playground file** (the file people
open to try the plugin), plus where the marketing assets go when you publish.

---

## 🎮 Playground file copy

Paste these as text frames in the community file. Keep one section per area of the
canvas, with empty frames/rectangles people can target.

### Welcome

> **Brands Logo — try it right here.**
> 15,000+ brand logos & icons, inside Figma. Run the plugin from
> **Plugins → Brands Logo**, then follow the steps below. Nothing here is destructive —
> insert, replace and resize as much as you like.

### 1 · Insert

> **Search & drop a logo in.**
> Type a brand (e.g. `stripe`), make sure the mode is **Insert**, and click it.
> It lands on the canvas inside a tidy square frame, scaled to fit.

### 2 · Replace in place

> **Swap a logo without breaking your layout.**
> Select the logo frame below, switch to **Replace**, and click a different brand.
> The frame keeps its exact size — the logo never stretches.
> *(Try it on this frame ⬇️)* — leave a 160×160 logo frame here.

### 3 · Auto size — fill any shape

> **Drop a logo into a frame you already have.**
> Select the rectangle below, set the size dropdown to **Auto size**, switch to
> **Replace**, and click a logo. It fills the exact bounds, centered, no distortion.
> *(Try it on this rectangle ⬇️)* — leave a 480×200 rectangle here.

### 4 · Resize

> **Pick a size, or resize after.**
> Choose a preset / **Custom…** size before inserting, or select any logo frame and
> edit **W × H** in the plugin (Shift + ↑/↓ nudges by 4).

### 5 · Two libraries

> **Brands Logo + svgl.**
> Use the tabs at the top to switch between this repo's 15,000+ logos and svgl's
> curated brand icons.

### Footer

> Free & open source · brandslogo.vercel.app · made by @rakibulism

---

## 🚀 Publishing checklist (Figma Community)

When you publish the plugin (**Plugins → Development → Brands Logo → Publish…**):

| Field | File | Size |
|-------|------|------|
| Icon | `marketing/plugin-icon-124.png` (flat, no corner radius) | 124 × 124 |
| **Cover / thumbnail** | `marketing/thumbnail.png` | 1920 × 1080 |
| **Carousel** (up to 9) | `marketing/carousel-1…9.png` | 1920 × 1080 each |
| **Video** | `marketing/walkthrough.mp4` (H.264, ~15s) | 1920 × 1080 |
| Playground file | a Figma file using the copy above | — |

**Carousel order** (already built):

1. `carousel-1.png` — cover / what it is
2. `carousel-2.png` — search & insert
3. `carousel-3.png` — replace in place (no distortion)
4. `carousel-4.png` — auto size (fill any frame)
5. `carousel-5.png` — sizes (auto / presets / custom)
6. `carousel-6.png` — two libraries (Brands Logo + svgl)
7. `carousel-7.png` — clean, named, non-destructive frames
8. `carousel-8.png` — light / dark / device themes
9. `carousel-9.png` — call to action

After publishing, replace the placeholder Community URL
(`…/plugin/0000000000/brands-logo`) in `scripts/site_template.html`, `docs.html`,
`updates.html` with the real link, then run `python3 scripts/gen_site.py`.

---

## Regenerating the images

```bash
python3 scripts/gen_plugin_assets.py     # thumbnail, carousel, og, icons (Pillow-only)
python3 scripts/gen_video.py             # walkthrough.mp4 (needs: pip install --user imageio-ffmpeg)
```

Real logos come from the pre-rasterized tiles in `marketing/tiles/`. The MP4 uses the
ffmpeg binary bundled by `imageio-ffmpeg` — no system ffmpeg required.
