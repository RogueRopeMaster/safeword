# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains a bilingual (English/French) website for Safeword, built with [Hugo](https://gohugo.io/) using the [Hugo-Coder](https://github.com/luizdepra/hugo-coder) theme. The site is deployed using Netlify.

## Development Commands

### Local Development

To run the site locally for development:

```bash
# Start the Hugo development server with draft content enabled
hugo server -D
```

This will start a local development server at http://localhost:1313/

### Building for Production

To build the site for production:

```bash
# Build the site
hugo
```

This will generate the static site in the `public/` directory.

## Deployment

The site is deployed to Netlify. The deployment configuration is in `netlify.toml`. When code is pushed to the repository, Netlify automatically builds and deploys the site using Hugo version 0.142.0.

## Site Architecture

### Directory Structure

- `content/`: Contains all the content files in Markdown format
  - English content: `*.md`
  - French content: `*.fr.md`
- `static/`: Contains static assets like images
- `themes/`: Contains the Hugo-Coder theme as a git submodule
- `hugo.toml`: Main configuration file

### Multilingual Support

The site supports English and French. For each content file, there are two versions:
- English: `content/section/page.md`
- French: `content/section/page.fr.md`

The language configuration is managed in `hugo.toml` with separate menu structures for each language.

### Content Sections

The main content sections are:
- Home: Main landing page
- About: Information about the organization
- Events: List of past and upcoming events
- Volunteers: Information about volunteers
- Contact: Contact information

### Content Format

Content files use Markdown with YAML front matter. The front matter includes metadata like title, date, tags, categories, and draft status.

### Theme Customization

The site uses the Hugo-Coder theme with dark color scheme. Theme customization settings are defined in `hugo.toml`.

## Adding New Content

To add new content:

1. Create a new Markdown file in the appropriate content directory
2. Add front matter at the top of the file
3. Add content in Markdown format
4. Create a corresponding `.fr.md` file for the French version

Example front matter:

```yaml
---
title: "Page Title"
date: 2023-01-01
draft: false
tags: ["tag1", "tag2"]
categories: ["category"]
---
```