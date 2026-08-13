# Website maintenance instructions

This repository is Carter Davis's public academic website. Prefer focused, factual edits and preserve the site's restrained editorial design.

## Content rules

- Do not invent paper statuses, coauthors, venues, presentations, contact details, or biographical claims.
- Treat Carter's direct instructions as authoritative. For externally sourced updates, prefer his Fisher profile, journal pages, SSRN records, and the current CV.
- Keep publication titles, author names, and outbound links exact.
- If a paper's status is uncertain, leave the existing status unchanged and flag the uncertainty.
- Use first person for biographical copy and research descriptions.

## Implementation rules

- Keep the site dependency-free: semantic HTML, `styles.css`, and minimal vanilla JavaScript.
- Maintain keyboard navigation, visible focus states, descriptive link text, image alternatives, and responsive layouts.
- Update repeated navigation/footer markup in `index.html`, `research.html`, and `contact.html` together.
- Keep canonical URLs, the sitemap, and Open Graph URLs aligned with the production domain.
- Do not rename the CV or headshot without updating every reference.

## Verification

Run:

```bash
python scripts/check_site.py
```

For layout changes, serve the directory locally and inspect desktop and mobile widths in a browser.
