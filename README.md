# parkland.consulting

The website for Parkland Consulting Group. Plain HTML and CSS, no build step, hosted on Cloudflare Pages.

## Pages

| URL | File |
| --- | --- |
| `/` | `index.html` |
| `/services/` | `services/index.html` |
| `/services/pattern-audit/` | `services/pattern-audit/index.html` |
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
