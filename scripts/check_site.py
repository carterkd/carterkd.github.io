#!/usr/bin/env python3
"""Dependency-free structural checks for the static website."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(ROOT.glob("*.html"))


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.links: list[str] = []
        self.images: list[tuple[str, str | None]] = []
        self.has_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if identifier := values.get("id"):
            self.ids.append(identifier)
        if tag == "a" and (href := values.get("href")):
            self.links.append(href)
        if tag == "img" and (src := values.get("src")):
            self.images.append((src, values.get("alt")))
        if tag == "title":
            self.has_title = True


def local_target(page: Path, raw_url: str) -> Path | None:
    parsed = urlsplit(raw_url)
    if parsed.scheme or parsed.netloc or raw_url.startswith(("mailto:", "tel:", "#")):
        return None
    path = unquote(parsed.path)
    if not path:
        return None
    target = (page.parent / path).resolve()
    if path.endswith("/"):
        target /= "index.html"
    return target


def main() -> int:
    errors: list[str] = []
    if not HTML_FILES:
        errors.append("No HTML pages found")

    for page in HTML_FILES:
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))

        if not parser.has_title:
            errors.append(f"{page.name}: missing <title>")

        duplicate_ids = sorted({value for value in parser.ids if parser.ids.count(value) > 1})
        for identifier in duplicate_ids:
            errors.append(f"{page.name}: duplicate id #{identifier}")

        for src, alt in parser.images:
            if alt is None:
                errors.append(f"{page.name}: image {src!r} is missing alt text")
            target = local_target(page, src)
            if target is not None and not target.exists():
                errors.append(f"{page.name}: missing image {src!r}")

        for href in parser.links:
            target = local_target(page, href)
            if target is not None and not target.exists():
                errors.append(f"{page.name}: broken local link {href!r}")

    if errors:
        print("Site checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Site checks passed: {len(HTML_FILES)} HTML pages validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
