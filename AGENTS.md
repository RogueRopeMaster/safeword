# Repository Guidelines

## Project Structure & Module Organization
- `content/` holds site content in Markdown (`events/`, `docs/`, `posts/`, etc.).
- `layouts/` contains first-party Hugo templates (partials, section templates, single/list views, base layout).
- `assets/css/site.css` and `assets/css/docs.css` contain custom styling; `assets/js/site.js` contains local behavior.
- `i18n/` contains translation strings; `hugo.toml` defines menus, languages, and site params.
- `public/` is generated build output; do not hand-edit it.

## Build, Test, and Development Commands
- `hugo server -D`: run the local dev server with drafts at `http://localhost:1313`.
- `hugo`: generate a production build into `public/`.
- `hugo --gc --minify`: optional pre-release check to garbage-collect and minify output.
- `hugo --gc --minify`: Netlify build command (deploy parity).

## Coding Style & Naming Conventions
- Use Markdown with YAML front matter (`---` blocks) for content files.
- Keep file names lowercase and kebab-case (`event-2025-11-08.md`).
- Maintain bilingual parity: each English page should have a paired French file (`page.md` and `page.fr.md`) in the same directory.
- Event content follows `content/events/event-YYYY-MM-DD(.fr).md`.
- Match existing formatting in templates/CSS (2-space indentation is the repo norm).

## Testing Guidelines
- No automated test framework is configured; `hugo` build success is the baseline validation.
- Before opening a PR:
  - Run `hugo` and resolve warnings/errors.
  - Run `hugo server -D` and manually verify EN/FR pages, event pages, docs navigation, and external links.
  - Confirm images resolve from `static/images/` and include meaningful alt text.

## Commit & Pull Request Guidelines
- History is mixed, but clear imperative subjects are preferred (`Add ...`, `Fix ...`, `Refine ...`); optional Conventional Commit prefixes like `feat:` are acceptable.
- Keep commits focused to one logical change area (content, templates, styling, or config).
- PRs should include a short summary, affected paths, linked issue/task (if any), and screenshots for UI/layout changes.
- Explicitly note bilingual updates (or intentional exceptions) in the PR description.
