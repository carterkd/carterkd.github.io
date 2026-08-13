# Carter Davis — academic website

Static personal academic site for [Carter Davis](https://fisher.osu.edu/people/davis.4983), designed to publish at [carterkd.github.io](https://carterkd.github.io/).

## Pages

- `index.html` — bio, research areas, selected publications, and teaching
- `research.html` — publications, working papers, abstracts, and project links
- `contact.html` — institutional email, office, and profiles
- `assets/files/carter-davis-cv.pdf` — downloadable CV

Shared styling is in `styles.css`; the small-screen navigation is in `script.js`.

## Preview locally

From this directory:

```bash
python -m http.server 8000
```

Then open <http://localhost:8000>.

Run the structural checks before publishing:

```bash
python scripts/check_site.py
```

## Publish

GitHub Pages is configured to deploy the repository root from `main`. Every push to `main` republishes the site automatically. The setting is visible under **Settings → Pages → Build and deployment → Source → Deploy from a branch**.

## Common updates

- Add or revise papers directly in `research.html`.
- Keep the two selected publications on `index.html` in sync with the research page.
- Replace `assets/files/carter-davis-cv.pdf` when the CV changes; keep the filename unchanged so links do not break.
- Replace `assets/images/carter-davis.jpg` when the headshot changes; use a square image if possible.
- Navigation and footer markup is repeated across the three pages, so update all three when adding a page.

## Migration sources

The initial content was migrated on August 12, 2026 from:

- <https://sites.google.com/site/carterkentdavis/>
- <https://fisher.osu.edu/people/davis.4983>

The institutional profile supplied the previously missing contact information and the current professional headshot. The initial CV came from the public Fisher profile and matches the Google Drive version linked by the original site.
