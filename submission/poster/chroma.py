"""Green-screen key: python chroma.py in_green.png ui_warped_rgb.png out_rgba.png
Alpha comes from in_green.png; colour comes from ui_warped_rgb.png (same size) with green spill removed."""
import sys, numpy as np
from PIL import Image, ImageFilter
g_in, rgb_in, out = sys.argv[1:4]
G = np.asarray(Image.open(g_in).convert("RGB")).astype(float)
C = np.asarray(Image.open(rgb_in).convert("RGB")).astype(float)
r, g, b = G[..., 0], G[..., 1], G[..., 2]
greenness = g - np.maximum(r, b)              # ~255 on pure green, ~0 on the white device
alpha = np.clip(1 - (greenness - 25) / 110, 0, 1)
a = Image.fromarray((alpha * 255).astype("uint8")).filter(ImageFilter.GaussianBlur(0.8))
alpha = np.asarray(a).astype(float) / 255
# despill: limit green channel on semi-transparent / edge pixels
cr, cg, cb = C[..., 0], C[..., 1], C[..., 2]
cg = np.minimum(cg, np.maximum(cr, cb) + 4)
C = np.stack([cr, cg, cb], axis=-1)
rgba = np.dstack([C, alpha * 255]).astype("uint8")
im = Image.fromarray(rgba, "RGBA")
bb = a.point(lambda v: 255 if v > 128 else 0).getbbox()
im = im.crop((max(0, bb[0] - 10), max(0, bb[1] - 10), bb[2] + 10, bb[3] + 10))
im.save(out); print("bbox", bb, im.size)
