#!/usr/bin/env python3
import sys, os, subprocess, markdown, html

CSS = """
@page { size: A4; margin: 22mm 18mm; }
* { box-sizing: border-box; }
body { font-family: 'Inter','Helvetica Neue',Arial,sans-serif; color:#0B1020;
  font-size: 10.5pt; line-height: 1.55; }
h1,h2,h3,h4 { color:#0B1020; line-height:1.25; font-weight:700; }
h1 { font-size: 22pt; border-bottom:3px solid #2F5FD6; padding-bottom:6px; margin-top:0; }
h2 { font-size: 15pt; border-left:5px solid #2F5FD6; padding-left:10px; margin-top:26px; }
h3 { font-size: 12.5pt; color:#2F5FD6; margin-top:18px; }
h4 { font-size: 11pt; }
a { color:#2F5FD6; text-decoration:none; }
p { margin: 8px 0; }
code { font-family:'JetBrains Mono','SF Mono',Consolas,monospace; font-size:9pt;
  background:#F4F6FB; padding:1px 5px; border-radius:4px; color:#1e293b; }
pre { background:#0E1424; color:#e6edf7; padding:12px 14px; border-radius:8px;
  overflow-x:auto; font-size:8.5pt; line-height:1.45; }
pre code { background:transparent; color:#e6edf7; padding:0; }
table { border-collapse:collapse; width:100%; margin:12px 0; font-size:9pt; }
th { background:#2F5FD6; color:#fff; text-align:left; padding:7px 9px; }
td { border:1px solid #E2E8F0; padding:6px 9px; vertical-align:top; }
tr:nth-child(even) td { background:#F8FAFD; }
blockquote { border-left:4px solid #2F5FD6; background:#F4F6FB; margin:12px 0;
  padding:8px 14px; color:#334155; }
hr { border:none; border-top:1px solid #E2E8F0; margin:20px 0; }
ul,ol { margin:8px 0 8px 22px; }
li { margin:3px 0; }
strong { color:#0B1020; }
"""

def convert(md_path, pdf_path):
    text = open(md_path, encoding="utf-8").read()
    body = markdown.markdown(text, extensions=["tables","fenced_code","toc","sane_lists","attr_list"])
    full = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"
    htmlf = pdf_path.replace(".pdf", ".tmp.html")
    open(htmlf, "w", encoding="utf-8").write(full)
    subprocess.run([
        "google-chrome","--headless","--no-sandbox","--disable-gpu",
        f"--print-to-pdf={pdf_path}","--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw","--virtual-time-budget=10000",
        f"file://{os.path.abspath(htmlf)}"
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.remove(htmlf)
    print("PDF:", pdf_path)

if __name__ == "__main__":
    for md in sys.argv[1:]:
        convert(md, md.rsplit(".",1)[0] + ".pdf")
