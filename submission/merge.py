"""Merge: part1 + guide (A5 pages 2-up on A4 landscape) + part2 + W11 slides (fit to A4) + part3."""
import sys, pathlib
from pypdf import PdfReader, PdfWriter, PageObject, Transformation
from pypdf.generic import RectangleObject

d = pathlib.Path(sys.argv[1]); guide = sys.argv[2]; slides = sys.argv[3]
OUT = sys.argv[4] if len(sys.argv) > 4 else "HUSH_A4_Submission_DRAFT.pdf"
W, H = 841.89, 595.28                      # A4 landscape, points
PAPER = (0xF4/255, 0xF2/255, 0xED/255)

def blank(color=PAPER):
    pg = PageObject.create_blank_page(width=W, height=H)
    if color:
        from pypdf.generic import DecodedStreamObject, NameObject, ArrayObject
        s = DecodedStreamObject(); s.set_data(f"{color[0]:.4f} {color[1]:.4f} {color[2]:.4f} rg 0 0 {W} {H} re f".encode())
        pg[NameObject("/Contents")] = w._add_object(s)
    return pg

w = PdfWriter()
for p in PdfReader(d / "out/part1.pdf").pages: w.add_page(p)

g = PdfReader(guide).pages
for i in range(0, len(g), 2):
    pg = blank()
    for j, src in enumerate(g[i:i+2]):
        sw, sh = float(src.mediabox.width), float(src.mediabox.height)
        s = min((W/2)/sw, H/sh)
        tx = j*W/2 + (W/2 - sw*s)/2; ty = (H - sh*s)/2
        pg.merge_transformed_page(src, Transformation().scale(s).translate(tx, ty))
    w.add_page(pg)

for p in PdfReader(d / "out/part2.pdf").pages: w.add_page(p)

for src in PdfReader(slides).pages:
    sw, sh = float(src.mediabox.width), float(src.mediabox.height)
    m = 18; s = min((W-2*m)/sw, (H-2*m)/sh)
    pg = blank((0.118, 0.141, 0.129))
    x0, y0 = float(src.mediabox.left), float(src.mediabox.bottom)   # slide 1 has a non-zero origin
    pg.merge_transformed_page(src, Transformation().translate(-x0, -y0).scale(s).translate((W-sw*s)/2, (H-sh*s)/2))
    w.add_page(pg)

for p in PdfReader(d / "out/part3.pdf").pages: w.add_page(p)

w.add_metadata({"/Title": "HUSH — Assessment 4 Design Fiction Prototype (Group UNLIMITED)", "/Author": "Group UNLIMITED: Jinge Gao, Jing Wang, Di Luan, Yini Chen"})
w.compress_identical_objects()
out = d / OUT
with open(out, "wb") as f: w.write(f)
print("wrote", out, len(w.pages), "pages")
