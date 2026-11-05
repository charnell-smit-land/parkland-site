#!/usr/bin/env python3
"""Build the Insights index and article pages from tools/insights_content.py.
Run from the repo root: python3 tools/build_insights.py
It also refreshes the Insights entries in sitemap.xml."""
import datetime, html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from insights_content import ARTICLES  # noqa: E402

SITE = "https://parkland.consulting"
TEMPLATE_SRC = os.path.join(ROOT, "about", "index.html")

FIGURES = {
"leak": '''<svg viewBox="0 0 440 300" role="img" aria-labelledby="fig-t" xmlns="http://www.w3.org/2000/svg">
<title id="fig-t">Traffic rises over time while sales stay flat, leaving a gap labeled the leak</title>
<g stroke="#E4E6E8" stroke-width="1"><line x1="12" y1="50" x2="428" y2="50"/><line x1="12" y1="120" x2="428" y2="120"/><line x1="12" y1="190" x2="428" y2="190"/><line x1="12" y1="250" x2="428" y2="250"/></g>
<path d="M12 222 C110 212 170 180 230 146 S350 76 420 56 L420 214 C350 215 280 217 230 218 S110 220 12 222 Z" fill="#C8F04B" fill-opacity="0.45"/>
<path d="M12 222 C110 212 170 180 230 146 S350 76 420 56" fill="none" stroke="#121417" stroke-width="4" stroke-linecap="round"/>
<path d="M12 222 C110 220 230 218 280 217 S350 215 420 214" fill="none" stroke="#0B5D5B" stroke-width="4" stroke-linecap="round"/>
<circle cx="420" cy="56" r="6" fill="#121417"/><circle cx="420" cy="214" r="6" fill="#0B5D5B"/>
<text x="406" y="36" text-anchor="end" font-family="IBM Plex Mono, monospace" font-size="16" fill="#121417">TRAFFIC</text>
<text x="406" y="244" text-anchor="end" font-family="IBM Plex Mono, monospace" font-size="16" fill="#0B5D5B">SALES</text>
<text x="320" y="166" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="700" font-size="30" fill="#121417">The leak</text>
<text x="12" y="284" font-family="IBM Plex Mono, monospace" font-size="15" fill="#5A6068">TIME →</text>
</svg>''',
"customers": '''<svg viewBox="0 0 440 262" role="img" aria-labelledby="fig-t" xmlns="http://www.w3.org/2000/svg">
<title id="fig-t">Illustration: core customers are a small share of all customers but a large share of repeat business</title>
<text x="0" y="22" font-family="IBM Plex Mono, monospace" font-size="15" fill="#5A6068">SHARE OF CUSTOMERS</text>
<rect x="0" y="34" width="440" height="56" rx="12" fill="#E4E6E8"/>
<rect x="0" y="34" width="96" height="56" rx="12" fill="#C8F04B"/>
<text x="14" y="69" font-family="IBM Plex Sans, sans-serif" font-weight="600" font-size="18" fill="#121417">Core</text>
<text x="0" y="142" font-family="IBM Plex Mono, monospace" font-size="15" fill="#5A6068">SHARE OF REPEAT BUSINESS</text>
<rect x="0" y="154" width="440" height="56" rx="12" fill="#E4E6E8"/>
<rect x="0" y="154" width="290" height="56" rx="12" fill="#C8F04B"/>
<text x="14" y="189" font-family="IBM Plex Sans, sans-serif" font-weight="600" font-size="18" fill="#121417">Core customers</text>
<text x="0" y="250" font-family="IBM Plex Mono, monospace" font-size="14" fill="#5A6068">ILLUSTRATION</text>
</svg>''',
"grid": '''<svg viewBox="0 0 440 440" role="img" aria-labelledby="fig-t" xmlns="http://www.w3.org/2000/svg">
<title id="fig-t">A two by two grid. Problems that happen often and that customers feel are labeled Fix First</title>
<rect x="36" y="0" width="198" height="190" rx="14" fill="#F2F4F4"/>
<rect x="242" y="0" width="198" height="190" rx="14" fill="#C8F04B"/>
<rect x="36" y="198" width="198" height="190" rx="14" fill="#F2F4F4"/>
<rect x="242" y="198" width="198" height="190" rx="14" fill="#F2F4F4"/>
<text x="135" y="92" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="700" font-size="28" fill="#121417">Schedule</text>
<text x="135" y="120" text-anchor="middle" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#3F454C">Often, behind</text>
<text x="135" y="140" text-anchor="middle" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#3F454C">the scenes</text>
<text x="341" y="92" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="700" font-size="30" fill="#121417">Fix First</text>
<text x="341" y="120" text-anchor="middle" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#121417">Often, and</text>
<text x="341" y="140" text-anchor="middle" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#121417">customers feel it</text>
<text x="135" y="290" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="700" font-size="28" fill="#121417">Let Go</text>
<text x="135" y="318" text-anchor="middle" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#3F454C">Rare, behind</text>
<text x="135" y="338" text-anchor="middle" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#3F454C">the scenes</text>
<text x="341" y="290" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="700" font-size="28" fill="#121417">Watch</text>
<text x="341" y="318" text-anchor="middle" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#3F454C">Rare, and</text>
<text x="341" y="338" text-anchor="middle" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#3F454C">customers feel it</text>
<text x="238" y="428" text-anchor="middle" font-family="IBM Plex Mono, monospace" font-size="14" fill="#5A6068">CUSTOMERS FEEL IT →</text>
<text x="0" y="0" transform="translate(18 194) rotate(-90)" text-anchor="middle" font-family="IBM Plex Mono, monospace" font-size="14" fill="#5A6068">HAPPENS OFTEN →</text>
</svg>''',
}

def esc(s):
    return html.escape(s, quote=True)

def fmt_date(d):
    dt = datetime.date.fromisoformat(d)
    return dt.strftime("%B %-d, %Y")

def words(a):
    t = a["answer"] + " " + " ".join(
        b[1] if b[0] in ("p", "h2", "example") else " ".join(x + " " + y for x, y in b[1]) if b[0] == "steps" else b[2]
        for b in a["body"])
    return len(t.split())

def page_shell():
    src = open(TEMPLATE_SRC).read()
    head_end = src.index("</head>")
    body_start = src.index("<body>")
    main_start = src.index('<main id="main">')
    main_end = src.index("</main>") + len("</main>")
    header = src[body_start:main_start]
    footer = src[main_end:]
    header = header.replace('<a href="/about/" aria-current="page">About</a>', '<a href="/about/">About</a>')
    header = header.replace('<a href="/insights/">Insights</a>', '<a href="/insights/" aria-current="page">Insights</a>')
    css = re.search(r'<link rel="stylesheet" href="/assets/styles\.css\?v=[0-9a-f]+">', src).group(0)
    return header, footer, css

def head(title, desc, url, css, ogtype, schema):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="Parkland Consulting Group">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/logo.png">
<meta name="twitter:card" content="summary">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" title="Parkland Insights" href="/insights/feed.xml">
<link rel="preload" href="/assets/fonts/bricolage-grotesque.woff" as="font" type="font/woff" crossorigin>
<link rel="preload" href="/assets/fonts/ibm-plex-sans.woff" as="font" type="font/woff" crossorigin>
{css}
{"".join('<script type="application/ld+json">' + json.dumps(s) + '</script>' for s in schema)}
</head>
'''

def body_html(a):
    out = []
    for b in a["body"]:
        k = b[0]
        if k == "p":
            out.append(f"<p>{esc(b[1])}</p>")
        elif k == "h2":
            out.append(f'<h2 class="h3">{esc(b[1])}</h2>')
        elif k == "example":
            out.append(f'<div class="example"><span>For example</span>{esc(b[1])}</div>')
        elif k == "figure":
            out.append(f'<figure class="art-figure">{FIGURES[b[1]]}<figcaption>{esc(b[2])}</figcaption></figure>')
        elif k == "steps":
            items = "".join(f'<li><strong>{esc(t)}</strong><span>{esc(d)}</span></li>' for t, d in b[1])
            out.append(f'<ol class="art-steps">{items}</ol>')
    return "\n".join(out)

def build():
    header, footer, css = page_shell()
    org = {"@type": "Organization", "name": "Parkland Consulting Group", "url": SITE + "/", "logo": SITE + "/assets/logo.png"}
    author = {"@type": "Person", "@id": SITE + "/about/#charnell", "name": "Charnell Smith-Landry", "url": SITE + "/about/"}
    for a in ARTICLES:
        url = f"{SITE}/insights/{a['slug']}/"
        mins = max(3, round(words(a) / 220))
        schema = [
            {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["description"],
             "datePublished": a["date"], "dateModified": a.get("updated", a["date"]), "mainEntityOfPage": url,
             "author": author, "publisher": org, "image": SITE + "/assets/logo.png", "articleSection": a["tag"]},
            {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": a["title"],
             "acceptedAnswer": {"@type": "Answer", "text": a["answer"]}}]},
        ]
        checks = "".join(f"<li>{esc(c)}</li>" for c in a["check"])
        page = head(f"{a['title']} | Parkland Insights", a["description"], url, css, "article", schema) + header + f'''<main id="main">
<article class="wrap article">
<header class="art-head">
<a class="text-link" href="/insights/" style="align-self:flex-start;font-size:15px">All Insights</a>
<p class="eyebrow">Insights · {esc(a["tag"])}</p>
<h1 class="h1 sm">{esc(a["title"])}</h1>
<p class="art-meta">By <a href="/about/">Charnell Smith-Landry</a>, Founder · <time datetime="{a["date"]}">{fmt_date(a["date"])}</time> · {mins} min read</p>
</header>
<div class="answer"><span>The short answer</span><p>{esc(a["answer"])}</p></div>
<div class="art-body">
{body_html(a)}
</div>
<aside class="pattern-check" aria-label="Pattern Check">
<p class="eyebrow">Pattern Check</p>
<ul>{checks}</ul>
<p class="note">{esc(a["check_note"])}</p>
</aside>
<aside class="pattern-card" aria-label="Pattern Card">
<div class="pc-top"><svg width="38" height="20" viewBox="0 0 44 24" aria-hidden="true"><circle cx="10" cy="12" r="9" fill="#FFFFFF" fill-opacity="0.18"/><circle cx="22" cy="12" r="9" fill="#FFFFFF" fill-opacity="0.42"/><circle cx="34" cy="12" r="9" fill="#C8F04B"/><circle cx="34" cy="12" r="3" fill="#111416"/></svg><span>Pattern Card</span></div>
<div class="pc-row"><span>The question</span><p class="q">{esc(a["title"])}</p></div>
<div class="pc-row"><span>The pattern</span><p>{esc(a["pattern"])}</p></div>
<div class="pc-row"><span>The move</span><p>{esc(a["move"])}</p></div>
<p class="pc-foot">parkland.consulting · Grow on Patterns, Not Hunches.</p>
</aside>
</article>

<section class="wrap cta-wrap">
<div class="cta">
<div class="main">
<h2>Want Us to Find Your Patterns?</h2>
<p>A Pattern Audit reads your customers, operations and numbers and gives you a ranked, 90-day plan. Investment starting from $3,000.</p>
</div>
<div class="btn-row"><a class="btn btn-dark" href="/services/pattern-audit/">See the Pattern Audit</a><a class="btn btn-ghost" href="/book/">Book a Call</a></div>
</div>
</section>
</main>''' + footer
        os.makedirs(os.path.join(ROOT, "insights", a["slug"]), exist_ok=True)
        open(os.path.join(ROOT, "insights", a["slug"], "index.html"), "w").write(page)

    # Index page
    cards = "\n".join(f'''<article class="ins-card">
<p class="tag">{esc(a["tag"])} · <time datetime="{a["date"]}">{fmt_date(a["date"])}</time></p>
<h2 class="h3"><a href="/insights/{a["slug"]}/">{esc(a["title"])}</a></h2>
<p>{esc(a["description"])}</p>
<a class="text-link" href="/insights/{a["slug"]}/" aria-hidden="true" tabindex="-1">Read the Insight</a>
</article>''' for a in ARTICLES)
    url = SITE + "/insights/"
    schema = [{"@context": "https://schema.org", "@type": "Blog", "name": "Parkland Insights", "url": url,
               "description": "Short, practical answers to the questions small business owners ask, built on the patterns behind growth.",
               "publisher": org,
               "blogPost": [{"@type": "BlogPosting", "headline": a["title"], "url": f"{SITE}/insights/{a['slug']}/", "datePublished": a["date"]} for a in ARTICLES]}]
    page = head("Insights | Parkland Consulting Group",
                "Short, practical answers to the questions small business owners ask, built on the patterns behind growth.",
                url, css, "website", schema) + header + f'''<main id="main">
<section class="wrap page-hero stack-lg" style="padding-bottom:48px">
<p class="eyebrow">Insights</p>
<h1 class="h1 sm">Patterns Worth Knowing.</h1>
<p class="lede">Short, practical answers to the questions business owners ask most. Each one names the pattern behind the problem and the move that fixes it.</p>
<div class="ins-format"><span><b>The question</b> you're asking</span><span><b>The pattern</b> behind it</span><span><b>The move</b> to make</span></div>
</section>
<section class="wrap section tight-top">
<div class="ins-list">
{cards}
</div>
</section>
<section class="wrap cta-wrap">
<div class="cta">
<div class="main">
<h2>Have a Question We Haven't Answered?</h2>
<p>Book a free 30-minute call and bring the problem you keep running into.</p>
</div>
<a class="btn btn-dark" href="/book/">Book a Call</a>
</div>
</section>
</main>''' + footer
    os.makedirs(os.path.join(ROOT, "insights"), exist_ok=True)
    open(os.path.join(ROOT, "insights", "index.html"), "w").write(page)

    # RSS feed
    items = "".join(f'''<item><title>{esc(a["title"])}</title><link>{SITE}/insights/{a["slug"]}/</link><guid>{SITE}/insights/{a["slug"]}/</guid><pubDate>{datetime.datetime.fromisoformat(a["date"]).strftime("%a, %d %b %Y 12:00:00 +0000")}</pubDate><description>{esc(a["answer"])}</description></item>''' for a in ARTICLES)
    open(os.path.join(ROOT, "insights", "feed.xml"), "w").write(f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel><title>Parkland Insights</title><link>{SITE}/insights/</link><description>Patterns worth knowing for small and growing businesses.</description><language>en-us</language>{items}</channel></rss>
''')

    # Sitemap
    sm_path = os.path.join(ROOT, "sitemap.xml")
    sm = open(sm_path).read()
    sm = re.sub(r"\s*<url><loc>https://parkland\.consulting/insights/[^<]*</loc><lastmod>[^<]*</lastmod></url>", "", sm)
    newest = max(a.get("updated", a["date"]) for a in ARTICLES)
    entries = f'\n  <url><loc>{SITE}/insights/</loc><lastmod>{newest}</lastmod></url>' + "".join(
        f'\n  <url><loc>{SITE}/insights/{a["slug"]}/</loc><lastmod>{a.get("updated", a["date"])}</lastmod></url>' for a in ARTICLES)
    sm = sm.replace("\n</urlset>", entries + "\n</urlset>")
    open(sm_path, "w").write(sm)
    print(f"Built {len(ARTICLES)} articles, index, feed and sitemap")

if __name__ == "__main__":
    build()
