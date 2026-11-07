# AI usage record

AI assistance in the source chat included concept critique, narrative brainstorming, prototype coding, physical mockups, advertising copy and image generation. This file is a starting record, not proof the university's full documentation requirements are complete.

## Provenance
- Built-in image generation was used for physical concepts and advertisements. Selected exact prompts that were saved at generation time are retained in `ai/prompts/`.
- Some intermediate prompts were visible in the original conversation but not saved as separate files. Their operations are summarised below rather than fabricating exact originals.
- Source chat retains the user's initial long prototype prompt. The condensed rules are in docs/WORLD_RULES.md and initial design in docs/HISTORY.md; these are not verbatim substitutes.
- The latest lifestyle request used a user-supplied nighttime HUSH poster as style reference and a generated manufactured-router poster as device reference. The source reference poster is not republished here; team should retain it privately and verify its origin/usage rights.

## Operations
| Output | Type | Inputs / role | Review status |
|---|---|---|---|
| Physical concept01 | Generation | User materials description: white frame/iPad/dough | Superseded |
| Physical02 | Edit | Prior concept + user-selected screen | Superseded; gap solution retained |
| Physical03 | Edit | Prior concept + user clay-colour photograph | Superseded; available colours retained |
| Physical04 | Edit | Prior concept + clay photo; user wants colourful frame | Current proposed construction reference |
| Ad01 | Generation from reference | Colourful physical concept + agreed draft advertising language | Superseded by user request for finished future product |
| Ad02 | Edit | Ad01; replace craft model with manufactured router | Earlier poster, superseded style |
| Ad04 lifestyle | Generation with references | User's lifestyle poster + Ad02 device | Latest draft, not approved |
| Web app | Coding | User project brief and authorisation | Functional snapshot, earlier visual style |
| Instruction set text + layout | Claude (Anthropic) drafting, HTML layout | Final Figma prototype, world rules, Jinge's requests (subscribe first, household pause) | Draft, Jinge reviewed; team review pending |
| Instruction illustrations (9) | Codex image generation | Prompts in ai/prompts/HUSH-Instructions-Illustrations-*; real model photo crop as reference | Used in guide; no text in images |

Before submission, record team edits, final exports, the actual final prompt history and any AI assistance by other teammates. Label reconstructed notes honestly. Generated text/UI should be checked and preferably redrawn in an editable tool for final typography control.

## 2026-11-06 — Magazine full-page preview
Built-in image generation, with the earlier white antenna-free campaign image as style reference and a prior captured final Figma home screen as UI reference. Exact prompt: prompts/HUSH-Magazine-Advertisement-Prompt.txt. Output: assets/advertisements/07-magazine-full-page.jpg. Generated appearance/copy visually inspected; editable type and production export remain future work. No new world rule or monthly price was introduced.

## 2026-11-07 — Magazine insert v2–v5c and rough final PDF (Jinge)
- **Magazine insert (poster v5c).** Codex (OpenAI) image generation, run from Claude Code (Anthropic).
  - Jinge supplied the layout sketch and gave feedback each round: silhouette steps; minimal 3D instead of hand-drawn; no italics; step 1 renamed "Choose a Plan"; fine print added; back view must not hide the ports.
  - The exact prompts are in `prompts/HUSH-Magazine-Insert-v2…v5c-Prompt.txt`.
  - All in-image text was checked word by word.
- **Draft submission PDF.** Claude (Anthropic) drafted the process text (faint signals, path to 2046, what-if, world rules, scenario, critical questions) and the layout, and generated the AI record table.
  - These are rough and unreviewed. The team should rewrite them in its own words where needed.
  - The prototype screenshots are automated browser captures, not AI images.

## 2026-11-07 — Review and revision
- **Draft review.** A teammate used ChatGPT to review the draft PDF; that checklist was not committed.
- **Revision.** Claude Code did the follow-up work, with subagents:
  - Researched and cross-checked the faint-signal sources.
  - Critiqued the causal chain of the new consequence and suggested the prop copy, which Jinge chose and which was edited.
  - Built props 06–08 as HTML mock-ups. They are not AI images: the text is typed, not generated.

## 2026-11-07 — Text prompts and logo
- Added Appendix B to the PDF: key text prompts to Claude, verbatim with translations (T1–T10). Full session transcripts are kept by Jinge.
- The HUSH logo SVG was drawn by Claude as vector paths, matching the logo in the AI-generated magazine ad.

## 2026-11-07 — Final catalogue insert (v6)
- **Codex image generation.** Produced 8 separate product renders with no text (P15).
- **Claude Code.** Composed them in HTML with live type, the HUSH wordmark and the real screen UI.
- **Research.** Faint-signal sources were found and cross-checked by Claude research subagents.
