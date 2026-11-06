# Instruction set: HUSH Home Quick Start Guide

This is the in-world quick-start booklet for Assessment 4. It has 8 A5 pages (148 × 210 mm), so it prints as one folded booklet.

- **Deliverable:** [HUSH_Quick_Start_Guide.pdf](HUSH_Quick_Start_Guide.pdf)
- **Overview of all pages:** [preview/all-pages.png](preview/all-pages.png)

## Files

| File | What it is |
|---|---|
| `guide.html` | **Source file. Edit this one.** It holds all text, layout and styles: one `<section class="page">` per page, with page comments `<!-- 1. COVER -->` to `<!-- 8. BACK COVER -->`. |
| `render.ps1` / `render.sh` | Rebuild the PDF from `guide.html` with headless Edge/Chrome (Windows / macOS). |
| `img/*.png` | Line illustrations, AI-generated with Codex image generation. Prompts are in `ai/prompts/HUSH-Instructions-Illustrations-*-Prompt.txt`. |
| `ref/screen-home.jpg` | Screenshot of the final Figma home screen, used for the "Meet your screen" diagram on page 2. |
| `ref/device-reference.png` | Crop of the real physical model, used as the style reference for the illustrations. |

## How to edit

1. Change text in `guide.html`. Plain HTML, so any editor or AI can work on it.
2. Rebuild the PDF:
   - Windows: `powershell -ExecutionPolicy Bypass -File instructions/render.ps1`
   - macOS: `sh instructions/render.sh`
   - With no script: open `guide.html` in Chrome, then Print. Set paper size to A5, margins to None, and tick **Background graphics**.
3. Open the PDF and check that every page still fits. Each page is a fixed A5 box, so text that is too long gets cut off at the bottom rather than flowing onto the next page.

Each page uses a CSS class for its layout. To add an illustration, copy an existing `.step` block. To keep the look consistent, generate new illustrations with the same prompt style: white background, black single-weight line, dark green `#2E4238` accent, no text.

## Page plan

| Page | Content |
|---|---|
| 1 | Cover |
| 2 | In the box, plus a numbered "Meet your screen" diagram (uses the real Figma screen) |
| 3 | Set up: 01 Connect, 02 Join HUSH Wi-Fi, 03 Choose a plan (must subscribe and pay before protection can start), plus a plan comparison table |
| 4 | Use: 04 Start, 05 Pause, 06 Monthly report, plus "Is this worth an hour?" |
| 5 | Sharing with your household: A pause requests, B Keep me private, C Step out, D member limits |
| 6 | When your hours run out, plus troubleshooting (malfunction scenarios) |
| 7 | The small print, plus specifications |
| 8 | Back cover |

## World rules used, and the open decision

The guide follows the final Figma prototype (https://banner-dish-90173388.figma.site).

**Taken from the prototype**

| Rule | Value |
|---|---|
| Plans | Personal 10 h, Home 20 h, Home+ 40 h |
| Plan prices | $9.99 / $19.99 / $29.99 per month |
| Devices covered | 10 / 20 / 40 |
| Extra hour | $3.99 for 60 minutes, whole home |
| Pausing | Pause and resume are supported |
| Existing data | Previously collected data is not removed |
| Room listening | HUSH does not listen to the room |

**Added by the guide.** These are written in Jinge's session and are not yet confirmed by the team:

| Rule | Detail |
|---|---|
| Subscribe first | The start button stays locked until a plan is paid for. Requested by Jinge. |
| Household pause | Pause requests time out after 30 s. Any member can choose "Keep me private" or "Step out". The account holder can set per-member limits. Requested by Jinge: what happens when one person wants to stop and others don't. |
| Unused hours | Expire at renewal. |
| Session times | Start and end times are kept "for billing and service improvement". This is a deliberate fine-print twist. |
| Emergency access | Emergency services may access the connection. |
| Display sync | Phone and router displays sync every few minutes. This explains why the exhibition photo shows different remaining times on the two screens. |
| Hardware | Model H-20, 10.9" display, Wi-Fi 9. Invented specs. |

**Open decision: plan tiers.** Jinge mentioned an **80-hour** plan, but the Figma plan page shows **10 / 20 / 40**. The guide follows Figma for consistency. If the team switches to 80 h, update the Figma "Change plan" page and the table on page 3 and the fine print on page 7 together.
