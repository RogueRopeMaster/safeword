#!/usr/bin/env python3
import argparse
from datetime import datetime, date
from pathlib import Path

WEEKDAYS_EN = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MONTHS_EN = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]

WEEKDAYS_FR = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]
MONTHS_FR = [
    "janvier", "f\u00e9vrier", "mars", "avril", "mai", "juin",
    "juillet", "ao\u00fbt", "septembre", "octobre", "novembre", "d\u00e9cembre",
]

EM_DASH = "\u2014"


def parse_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise SystemExit(f"Invalid date '{value}'. Use YYYY-MM-DD.") from exc


def parse_datetime(value: str) -> datetime:
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        try:
            return datetime.strptime(value, "%Y-%m-%d %H:%M")
        except ValueError as exc:
            raise SystemExit(
                f"Invalid datetime '{value}'. Use YYYY-MM-DD HH:MM or ISO format."
            ) from exc


def format_en_date(dt: datetime) -> str:
    weekday = WEEKDAYS_EN[dt.weekday()]
    month = MONTHS_EN[dt.month - 1]
    return f"{weekday}, {month} {dt.day}, {dt.year}"


def format_en_time(dt: datetime) -> str:
    hour = dt.hour
    minute = dt.minute
    ampm = "AM" if hour < 12 else "PM"
    hour12 = hour % 12
    if hour12 == 0:
        hour12 = 12
    return f"{hour12}:{minute:02d} {ampm}"


def format_fr_date(dt: datetime) -> str:
    weekday = WEEKDAYS_FR[dt.weekday()]
    month = MONTHS_FR[dt.month - 1]
    return f"{weekday}, {dt.day} {month} {dt.year}"


def format_fr_time(dt: datetime) -> str:
    return f"{dt.hour:02d}:{dt.minute:02d}"


def build_frontmatter(title: str, date_str: str, tags, categories, image_path: str | None) -> str:
    lines = ["---", f"title: \"{title}\"", f"date: {date_str}", "draft: false"]
    lines.append(f"tags: {tags}")
    lines.append(f"categories: {categories}")
    if image_path:
        lines.append(f"image: \"{image_path}\"")
    lines.append("---")
    return "\n".join(lines)


def build_body_en(description: str, start_dt: datetime, end_dt: datetime, image_path: str | None, link: str | None, quote: str | None) -> str:
    lines = []
    if image_path:
        lines.append(f"![Event Flyer]({image_path})")
        lines.append("")
    lines.append(description)
    lines.append("")
    lines.append("**When**  ")
    lines.append(f"{format_en_date(start_dt)} {EM_DASH} {format_en_time(start_dt)}  ")
    lines.append(f"Until: {format_en_date(end_dt)} {EM_DASH} {format_en_time(end_dt)}")
    if link:
        lines.append("")
        if quote:
            lines.append(f"> \"{quote}\" - {link}")
        else:
            lines.append(f"> {link}")
    return "\n".join(lines)


def build_body_fr(description: str, start_dt: datetime, end_dt: datetime, image_path: str | None, link: str | None, quote: str | None) -> str:
    lines = []
    if image_path:
        lines.append(f"![Flyer de l'\u00e9v\u00e9nement]({image_path})")
        lines.append("")
    lines.append(description)
    lines.append("")
    lines.append("**Quand**  ")
    lines.append(f"{format_fr_date(start_dt)} {EM_DASH} {format_fr_time(start_dt)}  ")
    lines.append(f"Jusqu'au : {format_fr_date(end_dt)} {EM_DASH} {format_fr_time(end_dt)}")
    if link:
        lines.append("")
        if quote:
            lines.append(f"> \"{quote}\" - {link}")
        else:
            lines.append(f"> {link}")
    return "\n".join(lines)


def normalize_image(image: str | None) -> str | None:
    if not image:
        return None
    if image.startswith("/images/"):
        return image
    filename = Path(image).name
    return f"/images/{filename}"


def resolve_root(root_arg: str | None) -> Path:
    root = Path(root_arg) if root_arg else Path.cwd()
    if (root / "content" / "events").is_dir():
        return root
    raise SystemExit("Could not find content/events. Use --root to point at the Hugo repo root.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create bilingual Safeword event pages.")
    parser.add_argument("--root", help="Path to Hugo repo root (must contain content/events)")
    parser.add_argument("--date", help="Frontmatter date YYYY-MM-DD (defaults to start date)")
    parser.add_argument("--start", required=True, help="Start datetime YYYY-MM-DD HH:MM")
    parser.add_argument("--end", required=True, help="End datetime YYYY-MM-DD HH:MM")
    parser.add_argument("--title-en", required=True, help="English title")
    parser.add_argument("--title-fr", help="French title")
    parser.add_argument("--desc-en", help="English description")
    parser.add_argument("--desc-fr", help="French description")
    parser.add_argument("--image", help="Image filename or /images/ path")
    parser.add_argument("--link", help="Optional event link")
    parser.add_argument("--quote", help="Optional quote for the link line")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")

    args = parser.parse_args()

    start_dt = parse_datetime(args.start)
    end_dt = parse_datetime(args.end)
    frontmatter_date = parse_date(args.date) if args.date else start_dt.date()
    date_str = frontmatter_date.isoformat()

    title_fr = args.title_fr or args.title_en
    desc_en = args.desc_en or "TODO: Add description."
    desc_fr = args.desc_fr or "TODO: Ajouter la description."
    image_path = normalize_image(args.image)

    root = resolve_root(args.root)
    events_dir = root / "content" / "events"
    en_path = events_dir / f"event-{date_str}.md"
    fr_path = events_dir / f"event-{date_str}.fr.md"

    if not args.force:
        for path in (en_path, fr_path):
            if path.exists():
                raise SystemExit(f"Refusing to overwrite existing file: {path}")

    frontmatter_en = build_frontmatter(
        title=args.title_en,
        date_str=date_str,
        tags='["event"]',
        categories='["events"]',
        image_path=image_path,
    )
    frontmatter_fr = build_frontmatter(
        title=title_fr,
        date_str=date_str,
        tags='["\u00e9v\u00e9nement"]',
        categories='["\u00e9v\u00e9nements"]',
        image_path=image_path,
    )

    body_en = build_body_en(desc_en, start_dt, end_dt, image_path, args.link, args.quote)
    body_fr = build_body_fr(desc_fr, start_dt, end_dt, image_path, args.link, args.quote)

    en_path.write_text(frontmatter_en + "\n" + body_en + "\n", encoding="utf-8")
    fr_path.write_text(frontmatter_fr + "\n" + body_fr + "\n", encoding="utf-8")

    print(f"Created {en_path}")
    print(f"Created {fr_path}")
    if args.title_fr is None:
        print("Note: French title copied from English. Provide --title-fr to override.")
    if args.desc_fr is None:
        print("Note: French description placeholder used. Provide --desc-fr to override.")


if __name__ == "__main__":
    main()
