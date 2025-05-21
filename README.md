# Safeword Hugo Website

This is a bilingual (English/French) website built with [Hugo](https://gohugo.io/) using the [Hugo-Coder](https://github.com/luizdepra/hugo-coder) theme.

## Structure

The site follows the standard Hugo structure:

- `content/`: Contains all the content files in Markdown format
  - English content: `*.md`
  - French content: `*.fr.md`
- `static/`: Contains static assets like images
- `themes/`: Contains the Hugo-Coder theme as a git submodule
- `hugo.toml`: Main configuration file

## Content Sections

- Home: Main landing page
- About: Information about the organization
- Blog: Blog posts and updates
- Projects: Project showcase
- Contact: Contact information

## Development

To run the site locally:

```bash
# Start the Hugo development server
hugo server -D
```

This will start a local development server at http://localhost:1313/

## Building

To build the site for production:

```bash
# Build the site
hugo
```

This will generate the static site in the `public/` directory.

## Adding Content

To add new content:

1. Create a new Markdown file in the appropriate content directory
2. Add front matter at the top of the file
3. Add your content in Markdown format
4. Create a corresponding `.fr.md` file for the French version

## Multilingual Support

The site supports English and French. To add content in both languages:

- English: `content/section/page.md`
- French: `content/section/page.fr.md`

The language switcher in the theme will automatically detect and display the available languages.