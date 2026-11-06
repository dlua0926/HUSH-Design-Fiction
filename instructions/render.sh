#!/bin/sh
# macOS / Linux: rebuild HUSH_Quick_Start_Guide.pdf from guide.html with headless Chrome.
cd "$(dirname "$0")" || exit 1
for b in "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
         "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" \
         google-chrome chromium chromium-browser; do
  if command -v "$b" >/dev/null 2>&1 || [ -x "$b" ]; then BROWSER="$b"; break; fi
done
[ -z "$BROWSER" ] && { echo "Chrome not found. Open guide.html in Chrome and Print > Save as PDF instead."; exit 1; }
"$BROWSER" --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$PWD/HUSH_Quick_Start_Guide.pdf" "file://$PWD/guide.html"
echo "Wrote $PWD/HUSH_Quick_Start_Guide.pdf"
