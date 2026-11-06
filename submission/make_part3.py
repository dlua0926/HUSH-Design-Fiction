"""Build part3.html: AI usage record + full prompt appendix (flowing pages)."""
import html, pathlib, sys

HERE = pathlib.Path(__file__).parent
REPO = pathlib.Path(sys.argv[1])          # HUSH-Design-Fiction checkout
AD = REPO / "ai/prompts"

PROMPTS = [
    ("P1", "Physical prototype concept sketches", REPO / "ai/prompts/HUSH-Physical-Prototype-Prompt.txt"),
    ("P2", "Advertisement draft: poster", REPO / "ai/prompts/HUSH-Advertisement-Poster-Prompt.txt"),
    ("P3", "Advertisement draft: future product", REPO / "ai/prompts/HUSH-Advertisement-Future-Product-Prompt.txt"),
    ("P4", "Advertisement: lifestyle (exhibition poster)", REPO / "ai/prompts/HUSH-Advertisement-Lifestyle-Prompt.txt"),
    ("P5", "Advertisement: white, no antennas", REPO / "ai/prompts/HUSH-Advertisement-White-No-Antennas-Prompt.txt"),
    ("P6", "Advertisement: lifestyle magazine page", REPO / "ai/prompts/HUSH-Magazine-Advertisement-Prompt.txt"),
    ("P7", "Magazine insert v2", AD / "HUSH-Magazine-Insert-v2-Prompt.txt"),
    ("P8", "Magazine insert v3 (new layout)", AD / "HUSH-Magazine-Insert-v3-Prompt.txt"),
    ("P9", "Magazine insert v4 (How It Works in 3D)", AD / "HUSH-Magazine-Insert-v4-Prompt.txt"),
    ("P10", "Magazine insert v5 (type, copy, fine print)", AD / "HUSH-Magazine-Insert-v5-Prompt.txt"),
    ("P11", "Magazine insert v5b (remaining italics)", AD / "HUSH-Magazine-Insert-v5b-Prompt.txt"),
    ("P12", "Magazine insert v5c (back view, final)", AD / "HUSH-Magazine-Insert-v5c-Prompt.txt"),
    ("P13", "Quick-start guide illustrations, set 1", REPO / "ai/prompts/HUSH-Instructions-Illustrations-1-Prompt.txt"),
    ("P14", "Quick-start guide illustrations, set 2", REPO / "ai/prompts/HUSH-Instructions-Illustrations-2-Prompt.txt"),
]

ROWS = [
    ("Concept, scenario critique and world-rule notes",
     "AI chat assistants used by team members during development; summaries kept in the project repository",
     "Brainstormed scenarios, questioned causal logic, drafted working documentation",
     "Chose the what-if and the job-search scenario; rejected AI-proposed scenarios (automatic parent, roommate and employer alerts); set every price, hour and rule",
     "—"),
    ("Physical concept sketches (design development page)",
     "AI image generation",
     "Concept renders of frame, mat and colour options",
     "Built the real model by hand (frame, card mat, stand, iPad). Only the photographs show the artefact",
     "P1"),
    ("Earlier advertisement drafts and exhibition poster",
     "AI image generation",
     "Generated imagery and in-image type",
     "Wrote the copy lines and numbers; selected, printed and exhibited the lifestyle poster",
     "P2–P6"),
    ("Final magazine insert (v2 to v5c)",
     "Codex (OpenAI) image generation, run from Claude Code (Anthropic)",
     "Generated and edited the poster images from Jinge's layout sketch; Claude wrote each prompt from her feedback",
     "Jinge drew the layout and gave feedback each round (silhouette steps, no hand-drawn style, no italics, fine print, back view). All in-image text was checked word by word",
     "P7–P12"),
    ("Quick-start guide: text and layout",
     "Claude (Anthropic) in Claude Code",
     "Drafted the booklet text and HTML layout from the Figma prototype and world rules",
     "Jinge set the new rules (subscribe before use; what happens when one member wants to pause and others don't) and reviewed the draft",
     "Requests in chat"),
    ("Quick-start guide: illustrations (9)",
     "Codex (OpenAI) image generation",
     "Line illustrations with no text, using a photo of the real model as reference",
     "Selected and placed the images",
     "P13–P14"),
    ("This compiled document",
     "Claude (Anthropic) in Claude Code",
     "Drafted the process text and layout; captured the prototype screens automatically from the live Figma sites",
     "Jinge directed structure and content; the team reviewed before submission",
     "Requests in chat"),
]

def esc(s): return html.escape(s)

rows = "\n".join(
    f"<tr><td><b>{esc(a)}</b></td><td>{esc(b)}</td><td>{esc(c)}</td><td>{esc(d)}</td><td class='p'>{esc(e)}</td></tr>"
    for a, b, c, d, e in ROWS)

blocks = []
for pid, title, path in PROMPTS:
    text = path.read_text(encoding="utf-8").strip()
    paras = "".join(f"<p>{esc(line)}</p>" if line.strip() else "<p class='gap'></p>" for line in text.splitlines())
    blocks.append(f"<div class='pr'><div class='ph'><span>{pid}</span> {esc(title)} <em>{esc(path.name)}</em></div>{paras}</div>")

doc = f"""<!doctype html><html><head><meta charset="utf-8"><title>HUSH — AI record</title>
<link rel="stylesheet" href="style.css">
<style>
@page {{ size: 297mm 210mm; margin: 12mm 15mm 12mm; }}
html, body {{ background: #fff; }}
.rec h1 {{ font-size: 20pt; }}
.rec table {{ font-size: 7.9pt; }}
.rec td.p {{ white-space: nowrap; color: var(--alert); font-weight: 600; }}
.app {{ column-count: 3; column-gap: 7mm; font-size: 6.9pt; line-height: 1.38; }}
.app .pr {{ margin-bottom: 4mm; }}
.app .ph {{ font-size: 7.6pt; font-weight: 700; border-top: .5mm solid var(--ink); padding-top: 1.2mm; margin-bottom: 1.2mm; break-after: avoid; }}
.app .ph span {{ color: var(--alert); }}
.app .ph em {{ font-style: normal; font-weight: 400; color: var(--soft); font-size: 6.6pt; display:block; }}
.app p {{ margin: 0; }}
.app p.gap {{ height: 1.2mm; }}
</style></head><body>
<section class="rec" style="page-break-after: always">
  <div class="kicker">11 · Generative AI usage record</div>
  <h1>How AI was used, and what we decided.</h1>
  <p style="max-width:230mm; margin-bottom:5mm">AI was used as a sketching, drafting and image-production tool. The team made every decision about the world: the what-if, the scenario, the plans, prices, hours, household rules and fine print. The physical model and its photographs are our own work. All text that appears inside AI-generated images was checked against the world rules, and images were regenerated until the wording was correct. The full prompts follow (P1–P14). The project repository keeps the working history.</p>
  <table>
    <tr><th style="width:19%">Output</th><th style="width:17%">Tool</th><th style="width:24%">What the AI did</th><th style="width:32%">What the team did</th><th>Prompt</th></tr>
    {rows}
  </table>
</section>
<section>
  <div class="kicker" style="margin-bottom:3mm">11 · Appendix · Prompts used, in full</div>
  <div class="app">{''.join(blocks)}</div>
</section>
</body></html>"""
(HERE / "part3.html").write_text(doc, encoding="utf-8")
print("part3.html written,", len(PROMPTS), "prompts")
