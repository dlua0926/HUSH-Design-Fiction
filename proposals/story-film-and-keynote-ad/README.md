# Proposal: presentation story prototype + keynote-style ad

**Status: PROPOSAL, not approved.** Nothing here replaces the final Figma prototype (https://banner-dish-90173388.figma.site) or any accepted world rule. Added 2026-11-02 (Australia/Sydney) by Jinge Gao with Claude (Anthropic) assistance.

## What is in this folder

| File | What it is | How to open |
|---|---|---|
| `story-prototype.html` | Clickable multi-device story for the live presentation (projector), complementing the Figma prototype that runs on the physical unit. Hub screens copy the Figma cream/black UI and the white-frame / sage-base / two-antenna router form. | Open in a browser. `→` next, `←` back, `R` restart, `M` Guided/Demo mode, `P` monthly report. |
| `keynote-ad.html` | About 1-minute "launch event" style advertisement (16:9), 11 chapters. | Open in a browser, press Play film, or `←` `→` / space. |
| `flow-wireframe.html` | Low-fidelity flow used to agree the story order (notes in Chinese). | Open in a browser. |

All three are self-contained HTML (only Google Fonts load from the network). No real payment, network protection, tracking or profile change happens; everything is simulated.

## Story covered by `story-prototype.html`

Mon 10 Sep 2046, 8:42 PM. Private Hours 00:00, 20 / 20 used, renewal in 3 days, 11 devices.
1. Hub at 00:00 → Privacy status (Buy 1 Private Hour · $3.99 / Wait 3 days).
2. Laptop: resident searches "changing jobs without employer knowing"; HUSH prompt offers one hour.
3. **Paid branch:** purchase sheet with the history-limitation fine print → protection ACTIVE 59:59 (live) → search, nothing else happens.
4. **Unpaid branch:** results → phone notification "Employment Profile Updated" (ProfileLink) → shared living-room TV recommendations → next-day work calendar "Retention check-in · Suggested by Workforce Insights" → buys an hour later; screen says "Earlier activity remains in connected profiles."
5. Ending (Thu 18 Oct 2046): 02:00 left, phone shows test results ready, "Is this worth one Private Hour?"
6. iPad monthly report: 1,284 requests = 438 + 327 + 291 + 155 + 73; 63 advertising profile updates.

## Needs team decision before any of this is used

1. **Shared-TV scene may conflict with a withdrawn rule.** WORLD_RULES / START_HERE record that automatic family/roommate disclosure was withdrawn for lacking a credible mechanism. In this proposal a partner sees career recommendations on the household TV. Collector, recipient, mechanism and incentive are NOT yet specified. Keep, rework or remove.
2. **Workplace consequence mechanism is not specified.** "Workforce Insights" suggesting a retention check-in needs a stated collector, recipient, mechanism and incentive, or should be replaced by the team's chosen immediate consequence (issue #1).
3. **Plan wording** now follows the repo: Home plan, 20 shared hours, recurring price unsettled. The ad's "Spend them on what matters" hour amounts (banking 0.5 h, test results 1 h, job search 1 h, messages 2 h) and the legal line "Hours renew monthly" are proposals.
4. **Ad direction:** the repo's current ad direction is a warm nighttime lifestyle poster (issue #4). This keynote film is an alternative / supplement, not a replacement.

## AI use

Built with Claude (Anthropic): story spec, HTML/CSS/JS, copy drafts and visual layout. Fictional brand names (Lumen, Hearth TV, NextHorizon Careers, ProfileLink, Workforce Insights, Northside Pathology, Cardinal, Adwell, Polaris Social, Basket, Clipstream, Tuneloop) were invented for this proposal. No AI image generation was used; all visuals are CSS/SVG. Verification: script syntax checked with `node --check`; both paths and the report were clicked through in a desktop browser at 1280×800. Phone-width layout was not separately verified.
