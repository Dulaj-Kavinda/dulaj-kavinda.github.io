# Dulaj Dasanayake — Portfolio

Static site for GitHub Pages. HTML pages are generated from `src/` (Python 3 stdlib only, no installs).

```
src/content.py   all text, links, images (edit this to change content)
src/build.py     layout + reusable components (header, footer, cards) + dev server
css/             base · layout · components · home   (+ vendored bootstrap.min.css grid)
js/              main.js (mobile nav) · typewriter.js
```

```bash
python3 src/build.py            # regenerate *.html
python3 src/build.py --serve    # rebuild on change + serve at http://localhost:8000
```

The root `*.html` files are build output — commit them, but edit `src/` instead.
