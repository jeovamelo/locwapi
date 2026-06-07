import os
import re

js_path = "/root/whatsapp-api/custom/index-CO3NSIFj.js"
with open(js_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find occurrences of 'GitHub'
for match in re.finditer(r'GitHub', content):
    start = max(0, match.start() - 150)
    end = min(len(content), match.end() + 150)
    print(f"--- Occurrence of GitHub at index {match.start()} ---")
    print(content[start:end])
    print()

# Find occurrences of 'Welcome'
for match in re.finditer(r'Welcome', content):
    start = max(0, match.start() - 150)
    end = min(len(content), match.end() + 150)
    print(f"--- Occurrence of Welcome at index {match.start()} ---")
    print(content[start:end])
    print()
