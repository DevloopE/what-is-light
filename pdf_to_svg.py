"""Convert a single-page PDF (from TikZ/standalone) to an SVG string.

Uses PyMuPDF. Writes `<pdf>.svg` next to the input PDF.
"""
import sys
import fitz  # PyMuPDF

def pdf_to_svg(pdf_path: str, out_path: str) -> None:
    doc = fitz.open(pdf_path)
    page = doc[0]
    svg = page.get_svg_image(text_as_path=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    doc.close()
    print(f"wrote {out_path}")


if __name__ == "__main__":
    pdf_to_svg(sys.argv[1], sys.argv[2])
