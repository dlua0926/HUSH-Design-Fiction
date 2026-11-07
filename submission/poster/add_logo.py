"""Warp the HUSH wordmark onto the bottom bezel, using the screen quad found by warp_screen.py.
usage: python add_logo.py render_ui.png logo.png out.png tlx tly trx try brx bry blx bly sw sh"""
import sys, numpy as np
from PIL import Image, ImageOps
src, logo_p, out_p = sys.argv[1:4]
q = list(map(float, sys.argv[4:12])); sw, sh = map(float, sys.argv[12:14])
quad = [(q[0], q[1]), (q[2], q[3]), (q[4], q[5]), (q[6], q[7])]
R = Image.open(src).convert("RGB"); W, H = R.size
L = Image.open(logo_p).convert("L"); alpha = ImageOps.invert(L)
# place the logo in "screen space" below the screen: centred, 9% of screen width, at y = 1.075*sh
lw = sw * 0.11; lh = lw * L.size[1] / L.size[0]
canvas_a = Image.new("L", (int(sw), int(sh * 1.2)), 0)
la = alpha.resize((int(lw), int(lh)), Image.LANCZOS)
canvas_a.paste(la, (int((sw - lw) / 2), int(sh * 1.075 - lh / 2)))
def coeffs(dst, srcpts):
    M = []; v = []
    for (x, y), (u, w) in zip(dst, srcpts):
        M.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); v.append(u)
        M.append([0, 0, 0, x, y, 1, -w * x, -w * y]); v.append(w)
    return np.linalg.solve(np.array(M, float), np.array(v, float)).tolist()
c = coeffs(quad, [(0, 0), (sw, 0), (sw, sh), (0, sh)])
wa = canvas_a.transform((W, H), Image.PERSPECTIVE, c, Image.BICUBIC)
out = R.copy(); out.paste(Image.new("RGB", (W, H), (40, 44, 42)), (0, 0), wa); out.save(out_p); print("ok")
