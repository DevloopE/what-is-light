"""Add LaTeX macros to MathJax config in all HTML articles.

Adds: \slashed, \slash (Feynman slash), \bra, \ket (Dirac notation), \abs, \norm, \Tr.
"""
from pathlib import Path

OLD = "window.MathJax = { tex: {inlineMath:[['$','$']], displayMath:[['$$','$$']], tags:'ams'}, svg: {fontCache:'global'} };"

# In the JS string the macros use \\ to escape \ for JS literals.
# In the Python source we need \\\\ to write \\ to file.
NEW = (
    "window.MathJax = { tex: { inlineMath:[['$','$']], "
    "displayMath:[['$$','$$']], tags:'ams', "
    "macros: { "
    "slashed: ['{\\\\not{#1}}', 1], "
    "slash: ['{\\\\not{#1}}', 1], "
    "bra: ['\\\\langle{#1}|', 1], "
    "ket: ['|{#1}\\\\rangle', 1], "
    "braket: ['\\\\langle{#1}|{#2}\\\\rangle', 2], "
    "abs: ['\\\\left|{#1}\\\\right|', 1], "
    "norm: ['\\\\left\\\\|{#1}\\\\right\\\\|', 1], "
    "Tr: ['\\\\operatorname{Tr}', 0], "
    "Im: ['\\\\operatorname{Im}', 0], "
    "Re: ['\\\\operatorname{Re}', 0] "
    "} }, svg: {fontCache:'global'} };"
)

root = Path("C:/Users/Devlo/Desktop/book/light-book")
fixed = 0
for path in root.rglob("*.html"):
    text = path.read_text(encoding="utf-8")
    if OLD in text:
        path.write_text(text.replace(OLD, NEW), encoding="utf-8")
        fixed += 1
        print(f"updated {path.relative_to(root)}")
print(f"--- {fixed} files updated ---")
