#!/usr/bin/env python3
"""Static site generator for the portfolio (Python standard library only).

    python3 src/build.py            # regenerate the HTML pages in the project root
    python3 src/build.py --serve    # rebuild on every change and serve on http://localhost:8000
"""
import functools
import http.server
import json
import os
import sys
import threading
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import content as c  # noqa: E402
from content import SITE  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


# ------------------------------------------------------------------ helpers
def indent(html, spaces):
    pad = " " * spaces
    return "\n".join(pad + line if line.strip() else line for line in html.strip("\n").splitlines())


def join(items, sep="\n"):
    return sep.join(i for i in items if i)


def link(url, label, cls="pill-link"):
    return f'<a href="{url}" target="_blank" class="{cls}">{label}</a>'


# --------------------------------------------------------------- components
def social_link(kind, url, icon, label, cls=""):
    inner = (f'<i class="fa {icon}" aria-hidden="true"></i>' if kind == "fa"
             else f'<img src="images/icons/{icon}.svg" alt="{label}">')
    attrs = f' class="{cls}"' if cls else ""
    return f'<a href="{url}" target="_blank"{attrs} aria-label="{label}">{inner}</a>'


def nav(active, show_cv):
    items = [
        f'<li class="nav-item"><a class="nav-link{" active" if key == active else ""}" href="{href}">{label}</a></li>'
        for key, label, href in c.NAV
    ]
    if show_cv:
        items.append(
            f'<li class="nav-item cv-nav-item">{link(SITE["cv_url"], "<span>Download CV</span>", "cv-button")}</li>')
    return f"""
<div class="container">
   <nav class="navbar navbar-expand-lg">
      <div class="logo"><a href="index.html">{SITE["first"]} <span>{SITE["last"]}</span></a></div>
      <button class="navbar-toggler" type="button" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
         <i class="fa fa-bars"></i>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
         <ul class="navbar-nav ml-auto">
{indent(join(items), 12)}
         </ul>
      </div>
   </nav>
</div>"""


def footer():
    socials = join(social_link(*s, cls="social_circle") for s in c.FOOTER_SOCIALS)
    return f"""
<footer class="site_footer_dark">
   <div class="container text-center">
      <div class="footer_item">
         <i class="fa fa-envelope fa-2x"></i>
         <h4 class="footer_label">Email</h4>
         <p class="footer_text">{SITE["email"]}</p>
      </div>
      <div class="footer_item">
         <i class="fa fa-map-marker fa-2x"></i>
         <h4 class="footer_label">Address</h4>
         <p class="footer_text">{SITE["address"]}</p>
      </div>
      <div class="social_icons">
{indent(socials, 9)}
      </div>
      <div class="footer_item footer_item--legal">
         <p class="copyright_text">© {SITE["year"]} {SITE["name"]}. All Rights Reserved.</p>
         <p class="footer_credits">Design Inspired by ThemeWagon</p>
      </div>
   </div>
</footer>"""


def page_section(title_plain, title_accent, intro, cards):
    return f"""
<section class="page-section">
   <div class="container">
      <h1 class="page-title">{title_plain} <span>{title_accent}</span></h1>
      <p class="page-intro">{intro}</p>
   </div>
   <div class="container">
      <div class="page-list">
{indent(join(cards, chr(10) * 2), 9)}
      </div>
   </div>
</section>"""


def timeline_card(e):
    """Education / career entry: logo, headings, dated paragraphs, optional tech stack, org badge."""
    sub = f'\n<h3 class="edu-title">{e["subheading"]}</h3>' if e.get("subheading") else ""
    entries = join(
        f'<p class="edu-duration"><strong>{d}</strong></p>\n<p class="edu-description">{t}</p>'
        for d, t in e["entries"])
    tech = f'\n<div class="tech-stack"><strong>Tech Stack:</strong> {e["tech"]}</div>' if e.get("tech") else ""
    url, label = e["badge"]
    return f"""<div class="edu-card">
   <img src="images/{e["logo"]}" alt="{e["alt"]}" class="edu-logo">
   <div class="edu-content">
      <h4 class="edu-title">{e["heading"]}</h4>{indent(sub, 6) if sub else ""}
      <hr class="edu-divider">
{indent(entries, 6)}{indent(tech, 6) if tech else ""}
      {link(url, label)}
   </div>
</div>"""


def figure(src, alt, caption):
    return f"""<div class="panel__figure">
   <img src="images/research/{src}" alt="{alt}" class="img-fluid">
   <small class="panel__caption">{caption}</small>
</div>"""


def research_card(r):
    points = join(f"<li>{p}</li>" for p in r["points"])
    links = join(link(u, l) for u, l in r.get("links", []))
    pub = ""
    if r.get("publication"):
        pub_links = join(link(u, l) for u, l in r.get("publication_links", []))
        pub_fig = ""
        if r.get("publication_figure"):
            src, alt, cap = r["publication_figure"]
            pub_fig = f"""<div class="panel__images panel__images--single">
   <img src="images/research/{src}" alt="{alt}" class="img-fluid">
</div>
<small class="panel__caption">{cap}</small>"""
        pub = f"""<div class="panel__publication">
   <h3 class="panel__subtitle">📄 Publication</h3>
   <p class="panel__text">
      {r["publication"]}
   </p>
{indent(join([pub_links, pub_fig]), 3)}
</div>"""
    return f"""<div class="panel">
   <h2 class="panel__title">{r["title"]}</h2>
   <p class="panel__role">{r["role"]}</p>
   <hr class="panel__divider">
   <p class="panel__text">
      {r["description"]}
   </p>
   <ul class="panel__list">
{indent(points, 6)}
   </ul>
{indent(join([figure(*r["figure"]) if r.get("figure") else "", links, pub]), 3)}
</div>"""


def award_card(a):
    logos = join(f'<img src="images/{src}" alt="{alt}">' for src, alt in a["logos"])
    text = (f"<b>{a['highlight']}</b><br>\n" if a.get("highlight") else "") + a["description"]
    images = ""
    if a.get("images"):
        imgs = join(f'<img src="images/{s}" alt="{al}" class="img-fluid">' for s, al in a["images"])
        pair = " panel__images--pair" if len(a["images"]) > 1 else ""
        images = f'<div class="panel__images{pair}">\n{indent(imgs, 3)}\n</div>'
    note = f'<p class="panel__note">{a["note"]}</p>' if a.get("note") else ""
    return f"""<div class="panel panel--award">
   <div class="panel__logos">
{indent(logos, 6)}
   </div>
   <div class="panel__body">
      <h2 class="panel__title">{a["title"]}</h2>
      <p class="panel__date"><strong>{a["date"]}</strong></p>
      <p class="panel__text">{text}</p>
{indent(join([images, note]), 6)}
   </div>
</div>"""


def nav_card(href, image, title, text):
    return f"""<div class="col-md-4 mb-4">
   <a href="{href}" class="nav-card-link">
      <div class="nav-card" style="background-image: url('images/{image}');">
         <div class="nav-card-content">
            <h5>{title}</h5>
            <p>{text}</p>
         </div>
      </div>
   </a>
</div>"""


def blog_card(p):
    button = link(p["url"] or "#", "Read More", "readmore_button") if p["url"] else \
        '<a href="#" class="readmore_button">Read More</a>'
    return f"""<div class="col-md-4 d-flex mb-4">
   <div class="blog_box">
      <div>
         <div class="blog_img" style="background-image: url('images/{p["image"]}');">
            <h4 class="date_text">{p["date"]}</h4>
            <h4 class="prep_text">{p["title"]}</h4>
         </div>
         <p class="lorem_text">{p["text"]}</p>
      </div>
      <div class="readmore_bt_1">
         {button}
      </div>
   </div>
</div>"""


# ------------------------------------------------------------------- layout
def document(title, active, body, hero="", home=False):
    header_cls = "header_section header_section_home" if home else "header_section header_bg"
    hero_markup = f'\n   <div class="header-bg-image"></div>' if home else ""
    return f"""<!DOCTYPE html>
<!-- GENERATED by src/build.py — edit src/content.py or src/build.py, not this file. -->
<html lang="en">
<head>
   <meta charset="utf-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>{title}</title>
   <meta name="description" content="Portfolio of {SITE["name"]} — software engineer and researcher in machine learning and healthcare informatics.">
   <meta name="author" content="{SITE["name"]}">
   <link rel="preconnect" href="https://fonts.googleapis.com">
   <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
   <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap">
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
   <link rel="stylesheet" href="css/bootstrap.min.css">
   <link rel="stylesheet" href="css/base.css">
   <link rel="stylesheet" href="css/layout.css">
   <link rel="stylesheet" href="css/components.css">
   <link rel="stylesheet" href="css/home.css">
</head>
<body>
<header class="{header_cls}">{hero_markup}
{indent(nav(active, show_cv=home), 3)}
{indent(hero, 3) if hero else ""}
</header>
{body}
{footer()}
<script src="js/main.js"></script>{'''
<script src="js/typewriter.js"></script>''' if home else ""}
</body>
</html>
"""


# -------------------------------------------------------------------- pages
def home_hero():
    socials = join(f"<li>{social_link(*s)}</li>" for s in c.HERO_SOCIALS)
    return f"""<div class="banner_section">
   <div class="container-fluid">
   <div class="container-fluid">
      <div class="row">
         <div class="col-md-6">
            <div class="banner_title_main">
               <h3 class="banner_text">Hello I'm <br>{SITE["full_name"]}</h3>
               <h1 class="banner_title"><span id="typewriter-text" data-roles='{json.dumps(c.TYPEWRITER_ROLES)}'></span><span class="cursor">|</span></h1>
            </div>
         </div>
         <div class="col-md-6">
            <div class="social_icon">
               <ul>
{indent(socials, 16)}
               </ul>
            </div>
         </div>
      </div>
   </div>
   </div>
</div>"""


def home_body():
    cards = join(nav_card(*x) for x in c.HOME_CARDS)
    posts = join(blog_card(p) for p in c.BLOG_POSTS)
    return f"""
<section class="quick_nav_section">
   <div class="container">
      <div class="row justify-content-center">
{indent(cards, 9)}
      </div>
   </div>
</section>

<section class="blog_section">
   <div class="container text-center">
      <h1 class="blog_title">My <span>Blog</span></h1>
      <p class="blog_text">Read my reflections on research, engineering, and ideas that inspire innovation.</p>
   </div>
</section>

<section class="blog_content_wrapper">
   <div class="container">
      <div class="row justify-content-center">
{indent(posts, 9)}
      </div>
   </div>
</section>"""


PAGES = {
    "index.html": lambda: document(SITE["name"], "home", home_body(), hero=home_hero(), home=True),
    "education.html": lambda: document(SITE["name"], "education", page_section(
        "My", "Education",
        "My path in technology began with a strong interest in understanding how systems work. Over time, this curiosity "
        "evolved into a solid grounding in computer science, shaped by both structured learning and self-driven exploration.",
        [timeline_card(e) for e in c.EDUCATION])),
    "career.html": lambda: document(SITE["name"], "career", page_section(
        "My", "Professional Career",
        "Through hands-on roles in software engineering, I’ve focused on building reliable, scalable solutions that solve "
        "real-world problems. Every step has been about growing technically while contributing meaningfully to the teams I’ve been part of.",
        [timeline_card(e) for e in c.CAREER])),
    "research.html": lambda: document(SITE["name"], "research", page_section(
        "My", "Research Projects",
        "I have actively pursued research in applied machine learning and healthcare informatics, driven by the goal of building "
        "intelligent, interpretable systems. Here are some of the notable research contributions I have made.",
        [research_card(r) for r in c.RESEARCH])),
    "awards.html": lambda: document(SITE["name"], "awards", page_section(
        "My", "Achievements",
        "These milestones reflect my drive to learn, lead, and create meaningful impact.",
        [award_card(a) for a in c.AWARDS])),
}


def build():
    for name, render in PAGES.items():
        (ROOT / name).write_text(render(), encoding="utf-8")
    print(f"built {len(PAGES)} pages")


def sources_mtime():
    return max(p.stat().st_mtime for p in (ROOT / "src").glob("*.py"))


def serve(port=8000):
    build()
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
    server = http.server.ThreadingHTTPServer(("", port), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    print(f"serving http://localhost:{port}  (Ctrl+C to stop)")
    seen = sources_mtime()
    try:
        while True:
            time.sleep(0.5)
            if (now := sources_mtime()) != seen:
                seen = now
                os.execv(sys.executable, [sys.executable, *sys.argv])  # reload content modules
    except KeyboardInterrupt:
        server.shutdown()


if __name__ == "__main__":
    serve() if "--serve" in sys.argv else build()
