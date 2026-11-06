# AI / Teammate onboarding

Read in this order:
1. `STATUS.md`: current work and unresolved decisions.
2. `docs/WORLD_RULES.md`: canonical facts, implementation defaults and open questions.
3. `docs/BRIEF_AND_FEEDBACK.md`: distinguish assignment requirements, user-summarised teacher feedback and assistant proposals.
4. `docs/HISTORY.md` and `docs/NARRATIVE.md`: why alternatives changed or were rejected.
5. Your workstream document: `PHYSICAL.md`, `ADVERTISEMENT.md`, or `prototype/README.md`.
6. `AGENTS.md`, `CONTRIBUTING.md`, and recent `WORK_LOG.md` entries before editing.

## User-provided live prototypes

- HUSH home page: https://banner-dish-90173388.figma.site
- Phone simulation: https://feed-test-35321007.figma.site
- Both URLs returned HTTP 200 on 2026-11-06; screen content and full interactive flows were not audited in this update. Do not assume the two sites are technically integrated.

## Critical context

- Read `docs/PRIOR_HUSH_CONTEXT.md` for the earlier HUSH master summary: group UNLIMITED, HUSH does not listen to rooms, and session-pattern metadata is an open question.
- The project's centre is **running out of privacy**, and the resulting everyday budgeting behaviour. Product feature growth is not the goal.
- Product direction changed from wall-mounted Nest-like hub to a **screen-equipped Wi-Fi router**.
- Household allowance in the current Home story is **20 shared hours**. A separate Home Plus tier of 80 shared hours was proposed in the prior summary and could coexist; its inclusion, name and recurring price are NOT settled. $3.99 buys an additional 60 minutes.
- A final student-relevant story and its immediate consequence are NOT chosen.
- Search → automatic parent/roommate notification was challenged by the user and withdrawn for lacking a credible information-sharing mechanism. Do not bring it back as an accepted rule.
- Profile updates alone may still be too weak for the teacher's request for an immediate life consequence.
- A physical student model uses a white picture frame + iPad + coloured dough. Ads may depict a fully manufactured future product instead.
- The user explicitly selected https://banner-dish-90173388.figma.site as the FINAL prototype and rejected the earlier green prototype. The final homepage was observed; other screens and editable source have not yet been verified. The repository `prototype/` and its screenshots are historical only. Do not rebuild or promote them as the final version.
- Never claim the prototype performs real payments, network protection, or profile deletion.
- AI-generated visuals are concepts; they are not proof of a manufactured product or completed physical build.

## Portable context message

“Please read START_HERE.md, STATUS.md, docs/WORLD_RULES.md and AGENTS.md in this repository before doing work. Check latest main and issues. Explain which task you are taking, preserve confirmed world rules, and update progress documents in the same commit. Treat proposals as proposals and do not overwrite another teammate's changes.”
