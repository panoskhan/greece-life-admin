from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
from urllib.request import Request, urlopen
import re
import sys
import time

ROOT = Path(__file__).resolve().parents[1]

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("href", "src"):
            value = attrs.get(key)
            if value:
                self.urls.append((tag, key, value))

html_files = list(ROOT.rglob("*.html"))
js_files = list(ROOT.rglob("*.js"))
urls = []
for path in html_files:
    parser = LinkParser()
    parser.feed(path.read_text(encoding="utf-8"))
    urls.extend((path, *item) for item in parser.urls)

for path in js_files:
    text = path.read_text(encoding="utf-8")
    for url in re.findall(r'https?://[^\"\'`\s)]+', text):
        urls.append((path, "js", url))

errors = []
external = []
for path, tag, kind, value in urls:
    if value.startswith(("#", "mailto:", "tel:", "javascript:")):
        continue
    parsed = urlparse(value)
    if parsed.scheme in ("http", "https"):
        external.append((path, value))
        continue
    target = (path.parent / value.split("#", 1)[0].split("?", 1)[0]).resolve()
    if not target.exists():
        errors.append(f"Missing local target: {path.relative_to(ROOT)} -> {value}")

# Check external URLs referenced by the app. Network failures are reported as failures
# so broken official links cannot silently enter the release.
for path, url in external:
    try:
        req = Request(url, method="HEAD", headers={"User-Agent": "Greece-Life-Admin-Link-Checker/1.0"})
        with urlopen(req, timeout=15) as response:
            if response.status >= 400:
                raise RuntimeError(f"HTTP {response.status}")
    except Exception:
        try:
            req = Request(url, method="GET", headers={"User-Agent": "Greece-Life-Admin-Link-Checker/1.0"})
            with urlopen(req, timeout=20) as response:
                if response.status >= 400:
                    raise RuntimeError(f"HTTP {response.status}")
        except Exception as exc:
            errors.append(f"External link failed: {path.relative_to(ROOT)} -> {url} ({exc})")
    time.sleep(0.05)

print(f"Checked {len(html_files)} HTML files, {len(js_files)} JS files, {len(urls)} references.")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print("All local references and external URLs passed.")
