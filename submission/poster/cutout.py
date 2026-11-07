"""Cut a light product render out of its warm off-white background.
usage: python cutout.py in.png out.png [tolerance]
Background = pixels reachable from the border that are not brighter than the
background and within `tolerance` of it (so soft shadows go, bright bezel highlights stay)."""
import sys, numpy as np
from collections import deque
from PIL import Image, ImageFilter
src, dst = sys.argv[1], sys.argv[2]; T = int(sys.argv[3]) if len(sys.argv) > 3 else 45
im = Image.open(src).convert("RGB"); A = np.asarray(im).astype(int); H, W, _ = A.shape
bg = np.median(np.concatenate([A[:10].reshape(-1, 3), A[-10:].reshape(-1, 3)]), axis=0)
diff = np.abs(A - bg).sum(axis=2); bright = A.sum(axis=2) > bg.sum() + 6
okbg = (diff <= T) & (~bright)
seen = np.zeros((H, W), bool); q = deque()
for x in range(W):
    for y in (0, H - 1):
        if okbg[y, x]: seen[y, x] = True; q.append((y, x))
for y in range(H):
    for x in (0, W - 1):
        if okbg[y, x] and not seen[y, x]: seen[y, x] = True; q.append((y, x))
while q:
    y, x = q.popleft()
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <= nx < W and okbg[ny, nx] and not seen[ny, nx]:
            seen[ny, nx] = True; q.append((ny, nx))
alpha = Image.fromarray(((~seen) * 255).astype("uint8"))
alpha = alpha.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
out = im.copy(); out.putalpha(alpha)
bb = alpha.point(lambda v: 255 if v > 128 else 0).getbbox()
out = out.crop((max(0, bb[0] - 12), max(0, bb[1] - 12), min(W, bb[2] + 12), min(H, bb[3] + 12)))
out.save(dst); print("bg", bg, "bbox", bb, "->", out.size)
