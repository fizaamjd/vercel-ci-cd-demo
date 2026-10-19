from html.parser import HTMLParser
from pathlib import Path
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.tags=[]
    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
p=Path(__file__).resolve().parents[1]/"index.html"
s=p.read_text(); page=Page(); page.feed(s)
assert all(t in page.tags for t in ["html","head","title","body","main","h1"])
assert "require(" not in s and "process.env" not in s and "MY_SECRET_KEY" not in s
print("Static document structure and browser configuration checks passed")
