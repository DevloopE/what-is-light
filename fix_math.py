"""Replace bare <, >, <=, >= inside $...$ and $$...$$ with LaTeX commands.

The HTML parser was eating `<T_c$ ...` as a malformed tag. Replacing with
\lt / \gt / \le / \ge is purely a LaTeX-side change; MathJax renders identically.
"""
import re
import sys
from pathlib import Path

def fix_math_text(text: str) -> str:
    text = text.replace('<<', r'\ll ')
    text = text.replace('>>', r'\gg ')
    text = text.replace('<=', r'\le ')
    text = text.replace('>=', r'\ge ')
    text = re.sub(r'(?<!\\)<', r'\\lt ', text)
    text = re.sub(r'(?<!\\)>', r'\\gt ', text)
    return text

def fix(content: str) -> str:
    content = re.sub(r'\$\$(.+?)\$\$',
                     lambda m: '$$' + fix_math_text(m.group(1)) + '$$',
                     content, flags=re.DOTALL)
    content = re.sub(r'\$([^$\n]+?)\$',
                     lambda m: '$' + fix_math_text(m.group(1)) + '$',
                     content)
    return content

if __name__ == "__main__":
    roots = [Path(p) for p in sys.argv[1:]]
    fixed_count = 0
    for root in roots:
        for path in sorted(root.glob("*.html")):
            if path.name == "index.html":
                continue
            original = path.read_text(encoding="utf-8")
            new = fix(original)
            if new != original:
                path.write_text(new, encoding="utf-8")
                fixed_count += 1
                print(f"fixed {path.name}")
    print(f"--- {fixed_count} files modified ---")
