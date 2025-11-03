#!/usr/bin/env python3
import re, sys, pathlib

if len(sys.argv) < 2:
    sys.exit("Usage: extract_frontmatter.py <path-to-file>")

path = pathlib.Path(sys.argv[1])
if not path.exists():
    sys.exit(0)

text = path.read_text(encoding="utf-8")

# 匹配 front matter 块
m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
if m:
    print(m.group(1))
