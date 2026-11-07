"""Warp a flat screen UI (el/screen-*.png) onto the blank screen of an angled render.

usage: python warp_screen.py <render.png> <screen.png> <out.png>
Finds the flat screen region by colour, fits its four edges, warps the UI with a
perspective transform, and keeps it inside the detected screen mask.
"""
import sys
import numpy as np
from PIL import Image, ImageFilter

render_p, screen_p, out_p = sys.argv[1:4]
R = Image.open(render_p).convert("RGB")
A = np.asarray(R).astype(int)
H, W, _ = A.shape

# screen colour = most common light colour near the centre
cy, cx = H // 2, W // 2
patch = A[cy - 40:cy + 40, cx - 40:cx + 40].reshape(-1, 3)
col = np.median(patch, axis=0)
dist = np.abs(A - col).sum(axis=2)
mask = dist < 9

# keep the connected region that contains the centre (simple flood fill)
from collections import deque
seen = np.zeros_like(mask)
q = deque([(cy, cx)]); seen[cy, cx] = True
while q:
    y, x = q.popleft()
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <= nx < W and mask[ny, nx] and not seen[ny, nx]:
            seen[ny, nx] = True; q.append((ny, nx))
m = seen
ys, xs = np.nonzero(m)
print("screen pixels", len(xs), "bbox", xs.min(), ys.min(), xs.max(), ys.max())

# edge points: for each row the leftmost/rightmost; for each column top/bottom
rows = np.unique(ys)
left = np.array([(xs[ys == r].min(), r) for r in rows])
right = np.array([(xs[ys == r].max(), r) for r in rows])
cols = np.unique(xs)
top = np.array([(c, ys[xs == c].min()) for c in cols])
bot = np.array([(c, ys[xs == c].max()) for c in cols])

def trim(pts, frac=0.25):
    n = len(pts); a = int(n * frac); return pts[a:n - a]  # drop rounded corners

def fit_xy(pts):   # x = a*y + b  (near-vertical edges)
    a, b = np.polyfit(pts[:, 1], pts[:, 0], 1); return ("v", a, b)
def fit_yx(pts):   # y = a*x + b  (near-horizontal edges)
    a, b = np.polyfit(pts[:, 0], pts[:, 1], 1); return ("h", a, b)

L, Rr, T, B = fit_xy(trim(left)), fit_xy(trim(right)), fit_yx(trim(top)), fit_yx(trim(bot))

def inter(v, h):
    _, a1, b1 = v; _, a2, b2 = h          # x = a1*y + b1 ; y = a2*x + b2
    y = (a2 * b1 + b2) / (1 - a2 * a1); x = a1 * y + b1; return (x, y)

tl, tr, br, bl = inter(L, T), inter(Rr, T), inter(Rr, B), inter(L, B)
print("corners", [tuple(round(v) for v in p) for p in (tl, tr, br, bl)])
# inset the quad slightly so the UI sits fully inside the glass (rounded corners, lip)
INSET = float(sys.argv[4]) if len(sys.argv) > 4 else 0.025
cxq = sum(p[0] for p in (tl, tr, br, bl)) / 4; cyq = sum(p[1] for p in (tl, tr, br, bl)) / 4
tl, tr, br, bl = [(cxq + (x - cxq) * (1 - INSET), cyq + (y - cyq) * (1 - INSET)) for x, y in (tl, tr, br, bl)]

S = Image.open(screen_p).convert("RGB")
sw, sh = S.size
# perspective coefficients: map output (render) coords -> input (screen) coords
def coeffs(dst, src):
    M = []; v = []
    for (x, y), (u, w) in zip(dst, src):
        M.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); v.append(u)
        M.append([0, 0, 0, x, y, 1, -w * x, -w * y]); v.append(w)
    return np.linalg.solve(np.array(M, float), np.array(v, float)).tolist()
c = coeffs([tl, tr, br, bl], [(0, 0), (sw, 0), (sw, sh), (0, sh)])
warped = S.transform((W, H), Image.PERSPECTIVE, c, Image.BICUBIC)

# mask = detected screen region, slightly grown to cover anti-aliased edge, softened
mk = Image.fromarray((m * 255).astype("uint8")).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(1.2))
quad = Image.new("L", (W, H), 0)
from PIL import ImageDraw
ImageDraw.Draw(quad).polygon([tl, tr, br, bl], fill=255)
quad = quad.filter(ImageFilter.GaussianBlur(0.8))
out = R.copy()
out.paste(Image.new("RGB", (W, H), (241, 238, 232)), (0, 0), mk)
from PIL import ImageChops
out.paste(warped, (0, 0), ImageChops.multiply(quad, mk))
out.save(out_p)
print("wrote", out_p)
