# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

## Repository Overview

Safeword is a bilingual (English/French) Hugo site deployed on Netlify. The project now uses first-party local templates and assets (no vendored external theme).

## Development Commands

### Local Development

```bash
hugo server -D
```

### Production Build

```bash
hugo --gc --minify
```

## Deployment

Deployment is configured in `netlify.toml`.

- Build command: `hugo --gc --minify`
- Hugo version: `0.155.3`
- Node version: `25`

## Structure

- `content/`: Markdown content (`*.md` and `*.fr.md`)
- `layouts/`: first-party Hugo templates and partials
- `assets/`: Hugo pipeline assets (CSS/JS)
- `static/`: static images/files
- `i18n/`: translation strings
- `hugo.toml`: site config

## Multilingual Rules

For each page, keep language parity:
- English: `content/section/page.md`
- French: `content/section/page.fr.md`

## Content Front Matter

Use YAML front matter:

```yaml
---
title: "Page Title"
date: 2023-01-01
draft: false
---
```
