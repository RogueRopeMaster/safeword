# Safeword Hugo Website

Bilingual (English/French) Hugo website for Safeword events, docs, and posts.

## Stack

- Hugo `v0.155.3+extended` (Netlify target)
- First-party local templates in `layouts/` (no external theme dependency)
- Local styles in `assets/css/site.css` and `assets/css/docs.css`

## Structure

- `content/`: Markdown content (paired EN/FR files)
- `layouts/`: Site templates and partials
- `assets/`: Hugo Pipe assets (CSS/JS)
- `static/`: Static files and images
- `i18n/`: Translation keys
- `hugo.toml`: Site configuration

## Local Development

```bash
hugo server -D
```

The site runs at `http://localhost:1313`.

## Build

```bash
hugo --gc --minify
```

The generated output is written to `public/`.

## Content Workflow

1. Add/update markdown in the relevant section under `content/`.
2. Keep bilingual parity (`page.md` and `page.fr.md`).
3. Build locally and verify EN/FR rendering before publishing.
