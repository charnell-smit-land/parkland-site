# parkland.consulting

The website for Parkland Consulting Group. Plain HTML and CSS, no build step, hosted on Cloudflare Pages.

## Pages

| URL | File |
| --- | --- |
| `/` | `index.html` |
| `/services/` | `services/index.html` |
| `/services/pattern-audit/` | `services/pattern-audit/index.html` |
| `/services/growth-strategy/` | `services/growth-strategy/index.html` |
| `/services/scale-strategy/` | `services/scale-strategy/index.html` |
| `/services/communication-strategy/` | `services/communication-strategy/index.html` |
| `/about/` | `about/index.html` |
| `/book/` | `book/index.html` |

Shared styles live in `assets/styles.css`. Old WordPress URLs are redirected in `_redirects`.

## Cloudflare Pages settings

- Framework preset: None
- Build command: leave empty
- Build output directory: `/`

## Common edits

- **Booking link:** change `CAL_LINK` near the bottom of `book/index.html`, plus the fallback link above it.
- **Prices:** search the files for `[PRICE]`, `[MONTHLY RATE]` and `[X WEEKS]`.
- **Accent color:** change `--accent` at the top of `assets/styles.css` (the logo and favicon also use `#C8F04B`).

## Preview locally

```
python3 -m http.server 8000
```

Then open http://localhost:8000.

## After editing styles

Pages load `assets/styles.css?v=...`. When `styles.css` changes, update the `v=` value on every page (the first 8 characters of `sha1sum assets/styles.css`) so browsers fetch the new file.

## Responsive check (run before every publish)

Serve the site locally with `python3 -m http.server 8765`, then run `node checks/responsive.js`.
It loads every page at 320, 360, 390, 430, 768, 1024, 1280, 1440 and 1920 pixels wide and fails if
anything scrolls sideways or sticks out past the edge of the screen. Add new pages to the list in the script.
