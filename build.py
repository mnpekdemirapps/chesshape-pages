#!/usr/bin/env python3
"""Builds the privacy policy and terms of use in every language the app ships.

Chesshape's UI is translated into eleven languages, so its legal pages have to
be too — a store listing in German that links an English-only policy is a
listing that fails review in some markets. Writing eleven pairs of pages by hand
guarantees they drift; the ones that matter are the facts about data handling,
and those must say the same thing everywhere.

So: one HTML shell, one content table (content.py), and this script to emit
them. Every page carries the same language switcher and the same contact
address, and English keeps its original filenames so links already published in
the store listing keep working.

    python3 build.py
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from content import CONTACT, EFFECTIVE, LANGS, PLATFORM  # noqa: E402

# English keeps the bare filenames it was first published under.
def filename(doc, code):
    return f"{doc}.html" if code == "en" else f"{doc}-{code}.html"


def switcher(doc, current):
    links = []
    for code, lang in LANGS.items():
        label = f"{lang['flag']} {lang['name']}"
        if code == current:
            links.append(f'<strong class="here">{label}</strong>')
        else:
            links.append(f'<a href="{filename(doc, code)}" lang="{code}">{label}</a>')
    return '<nav class="langs" aria-label="Language">' + "".join(links) + "</nav>"


def render(doc, code):
    lang = LANGS[code]
    page = lang[doc]
    other = "terms" if doc == "privacy" else "privacy"

    sections = "\n\n".join(
        f"  <h2>{heading}</h2>\n  {body}" for heading, body in page["sections"]
    )

    return f"""<!doctype html>
<html lang="{code}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page['title']} — Chesshape</title>
<meta name="description" content="{page['summary']}">
<link rel="icon" sizes="32x32" href="assets/favicon-32.png">
<link rel="icon" sizes="192x192" href="assets/favicon-192.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="doc">
  <nav class="site">
    <a href="index.html"><img src="assets/favicon-192.png" alt="Chesshape"></a>
    <span class="brand">CHESSHAPE</span>
    <span class="links"><a href="index.html">{lang['nav_home']}</a><a href="{filename(other, code)}">{lang[other]['title']}</a></span>
  </nav>

  <header>
    <h1>{page['title']}</h1>
    <p class="meta">{lang['effective_label']}: {EFFECTIVE} · {lang['app_label']}: <strong>Chesshape</strong> ({PLATFORM})</p>
  </header>

  {switcher(doc, code)}

  {page['intro']}

{sections}

  <div class="contact-box">
    <strong>{lang['contact_label']}</strong><br>
    {page['contact_line']}<br>
    📧 <a href="mailto:{CONTACT}">{CONTACT}</a>
  </div>

  <footer class="site">
    <span>© 2026 Chesshape</span>
    <span class="spacer"></span>
    <a href="index.html">{lang['nav_home']}</a>
    <a href="{filename(other, code)}">{lang[other]['title']}</a>
  </footer>
</div>
</body>
</html>
"""


def main():
    written = 0
    for doc in ("privacy", "terms"):
        for code in LANGS:
            path = HERE / filename(doc, code)
            path.write_text(render(doc, code), encoding="utf-8")
            written += 1
    print(f"wrote {written} pages in {len(LANGS)} languages")

    missing = [code for code, lang in LANGS.items()
               if CONTACT not in render("privacy", code)]
    if missing:
        print("MISSING CONTACT:", missing)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
