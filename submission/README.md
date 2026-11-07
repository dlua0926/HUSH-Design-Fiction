# Final submission PDF: ROUGH FIRST DRAFT

> **This is a quick first pass, not the final submission.** Jinge's AI put it together in one go on 2026-11-07 to have something complete to react to. Wording, page order, image choices and the AI record all still need the team's review. Change anything you like.

- **Draft PDF:** [HUSH_A4_Submission_DRAFT.pdf](HUSH_A4_Submission_DRAFT.pdf). 34 pages, A4 landscape, about 17 MB.
- Assessment 4 asks for all deliverables compiled into one PDF, due 8 Nov 2026, 11:59 pm.

## Page order

| Pages | Content | Source |
|---|---|---|
| 1–2 | Cover, overview and contents | `part1.html` |
| 3–4 | Faint signals (APA citations), speculative path to 2046, what-if, archetype | `part1.html` |
| 5 | World rules, including paused data and derived data | `part1.html` |
| 6 | Design development | `part1.html` |
| 7 | In-world: physical model (two labelled states) | `part1.html` |
| 8–9 | In-world: Figma interface | `part1.html` + `shots/` |
| 10–11 | In-world: scenario, Sat 15 to Mon 17 Sept 2046 | `part1.html` + `shots/` + `props/` |
| 12–16 | Instruction set divider and guide, 2 pages per sheet | `../instructions/` |
| 17–18 | Catalogue insert ad, plus variants and iterations | `part2.html` |
| 19–20 | Critical questions; References (APA 7) | `part2.html` |
| 21–26 | W11 divider and the 5 slides, unchanged, each with an "ARCHIVED" banner | `part2.html`, `slides/`, `merge.py` |
| 27 | AI usage record | `make_part3.py` |
| 28–34 | Appendix A: 15 image prompts. Appendix B: 11 key text prompts to Claude, verbatim and translated | `make_part3.py` |

Phone screens (`shots/m*.png`) are captured at 390×844 and 3× scale, with the status text replaced to "Protection Paused · Tracking active" during capture. Figma still shows the old text.

Pages are tagged **IN-WORLD ARTEFACT · 2046** or **PROCESS · 2026**.

The catalogue insert is `poster/poster.html`, which uses Codex renders in `poster/el/`. To re-render it, capture the page at 794×1123 and 4× scale, then export `img/poster-v6.jpg`.

Props 06–08 are HTML files in `props/src/`. To change their wording, edit the HTML, re-capture the PNG at 1440×900 with 2× scale, then re-crop. Crop boxes, in pixels of the 2880×1800 PNG:
- `notice` (640, 244, 2240, 1310)
- `insight` (0, 0, 2290, 1396)
- `monday` (480, 0, 2550, 1380)
- `shots/p3-linkedin` → `p3-crop` (0, 173, 1152, 943)

## How to edit and rebuild

1. Edit the text in `part1.html` or `part2.html`. Each page is one `<section class="page">`. Shared styles are in `style.css`.
   - To change the AI record table or the prompt list, edit `make_part3.py`. Do not edit `part3.html`: the build regenerates it.
2. Rebuild:
   - **Windows:** run `powershell -ExecutionPolicy Bypass -File submission/build.ps1`. This needs Edge or Chrome, and Python with `pypdf`.
   - **Without the script:** print each `part*.html` from Chrome to PDF (A4 landscape, margins None, Background graphics on). Then run `python submission/merge.py submission instructions/HUSH_Quick_Start_Guide.pdf submission/slides/W11-presentation.pdf`.
3. Pages are fixed-size boxes. Text that is too long is cut off at the bottom, so check every page after a rebuild.

## Image sources

- `shots/`: screenshots of the two live Figma prototypes, taken with a headless browser. These are real captures, not AI images.
- `img/exhibition.jpg` and `img/front.jpg`: real photos of the physical model.
- `img/c-*.jpg`, `img/ad-*.jpg`, `img/poster.jpg` and `img/pv-*.jpg`: AI-generated concepts and advertisements. Their prompts are in `ai/prompts/`.
- `img/w11-hub.jpg`: one slide from the W11 deck.

## Known gaps: team to check before submitting

- **AI usage record (pages 24–28).** It only covers what is recorded in this repo and in Jinge's sessions. Add anything else:
  - whether the Figma prototypes used Figma AI features;
  - any AI images used in the W11 deck;
  - who made `07-magazine-full-page.jpg`;
  - each member's own AI use.
- **Plan tiers.** The draft follows Figma (10 / 20 / 40 h). The 80 h idea is not used.
- **Scenario wording.** The scenario (J. pauses to save hours, then searches for jobs) is a draft reading of the existing prototypes and still needs team agreement.
- **Process pages.** Faint signals, the 2026 to 2046 path and the critical questions were drafted by AI from the repo docs. Rewrite them in the team's own words where needed.
