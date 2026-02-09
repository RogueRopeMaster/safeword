---
name: safeword-event-pages
description: Create or update Safeword Hugo event pages in `content/events/` for new or upcoming events, including bilingual English/French Markdown, frontmatter, schedule formatting, and local flyer images in `static/images/`. Use when asked to add an event, post an upcoming event, attach a flyer, or update event details.
---

# Safeword Event Pages

## Overview

Create bilingual event pages for the Safeword Hugo site. This workflow standardizes filenames, frontmatter, schedule formatting, and local image handling for event flyers.

## Workflow

Inputs
- Event title and short label (English and French if provided)
- Description or tagline text (English and French if provided)
- Start date and time, end date and time, timezone if relevant
- Flyer image URL or local image file path
- Optional link (Fetlife, tickets, or other)

Steps
1. Choose filenames based on the event start date: `content/events/event-YYYY-MM-DD.md` and `content/events/event-YYYY-MM-DD.fr.md`

2. Create or update frontmatter. English frontmatter template:

```yaml
---
title: "EVENT TITLE"
date: 2025-08-23
draft: false
tags: ["event"]
categories: ["events"]
image: "/images/IMAGE-FILENAME.jpg"
---
```

French frontmatter template:

```yaml
---
title: "TITRE DE L'EVENEMENT"
date: 2025-08-23
draft: false
tags: ["événement"]
categories: ["événements"]
image: "/images/IMAGE-FILENAME.jpg"
---
```

3. Add the body content. English body pattern:

```md
![Event Flyer](/images/IMAGE-FILENAME.jpg)

DESCRIPTION TEXT

**When**  
Sat, Aug 23, 2025 — 9:00 PM  
Until: Sun, Aug 24, 2025 — 3:00 AM
```

French body pattern:

```md
![Flyer de l'événement](/images/IMAGE-FILENAME.jpg)

DESCRIPTION TEXT

**Quand**  
Sam, 23 août 2025 — 21:00  
Jusqu'au : dim, 24 août 2025 — 03:00
```

4. Handle the image. Prefer local images in `static/images/` to avoid hotlinking. If given a URL, download it and rename to a short, lowercase filename tied to the event (example: `ouak10-min.jpg`), then set `image` to `/images/<filename>`. If download fails due to hotlink protection, ask the user for a rehosted URL or a local file.

5. Add optional link. If a link is provided, add a final line as a blockquote, for example:

```md
> "Short quote or tagline" - https://example.com
```

6. Language handling. If only English copy is provided, create a best-effort French translation and flag it to the user for confirmation.

## Scripted Scaffold

Use the helper script to generate both event files:

```bash
python3 .claude/skills/safeword-event-pages/scripts/create_event_pages.py \\
  --root . \\
  --start \"2025-08-23 21:00\" \\
  --end \"2025-08-24 03:00\" \\
  --title-en \"OUAK10 : A grand occasion awaits; try the slipper and let the story unfold.\" \\
  --title-fr \"OUAK10 : Une grande occasion vous attend ; essayez la pantoufle et laissez l'histoire se derouler.\" \\
  --desc-en \"A grand occasion awaits; try the slipper and let the story unfold.\" \\
  --desc-fr \"Une grande occasion vous attend ; essayez la pantoufle et laissez l'histoire se derouler.\" \\
  --image \"ouak10-min.jpg\"
```

Notes
- `--date` is optional. If omitted, the frontmatter date uses the start date.
- `--image` accepts either `/images/filename.jpg` or a bare filename.
- Use `--force` to overwrite existing files.
