# AIDA Consulting Solutions website

Static site for https://www.aidaconsulting.ca/ — plain HTML and CSS, no build step.

- `index.html` — the whole page (content lives here)
- `styles.css` — styling, light and dark themes
- `assets/` — favicon and social share image
- `CNAME` — custom domain for GitHub Pages

## Preview locally

    python3 -m http.server 8000

Then open http://localhost:8000.

## Deploy

Hosted on GitHub Pages from the `main` branch (Settings → Pages → Deploy from a branch → `main` / root). Every push to `main` publishes.
