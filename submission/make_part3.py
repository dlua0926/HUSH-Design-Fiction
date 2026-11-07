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
    ("P7", "Catalogue insert v2", AD / "HUSH-Magazine-Insert-v2-Prompt.txt"),
    ("P8", "Catalogue insert v3 (new layout)", AD / "HUSH-Magazine-Insert-v3-Prompt.txt"),
    ("P9", "Catalogue insert v4 (How It Works in 3D)", AD / "HUSH-Magazine-Insert-v4-Prompt.txt"),
    ("P10", "Catalogue insert v5 (type, copy, fine print)", AD / "HUSH-Magazine-Insert-v5-Prompt.txt"),
    ("P11", "Catalogue insert v5b (remaining italics)", AD / "HUSH-Magazine-Insert-v5b-Prompt.txt"),
    ("P12", "Catalogue insert v5c (back view, final)", AD / "HUSH-Magazine-Insert-v5c-Prompt.txt"),
    ("P13", "Quick-start guide illustrations, set 1", REPO / "ai/prompts/HUSH-Instructions-Illustrations-1-Prompt.txt"),
    ("P14", "Quick-start guide illustrations, set 2", REPO / "ai/prompts/HUSH-Instructions-Illustrations-2-Prompt.txt"),
    ("P15", "Catalogue insert, final: separate product elements", REPO / "ai/prompts/HUSH-Catalogue-Insert-v6-Elements-Prompt.txt"),
    ("P16", "Catalogue insert, final: front-facing laptop", REPO / "ai/prompts/HUSH-Catalogue-Insert-Laptop-Prompt.txt"),
    ("P17", "Catalogue insert, final: angled 3D hero", REPO / "ai/prompts/HUSH-Catalogue-Insert-v8-angled-Prompt.txt"),
    ("P18", "Catalogue insert, final: angled hero on green screen", REPO / "ai/prompts/HUSH-Catalogue-Insert-v9-green-Prompt.txt"),
]


# Key text prompts given to Claude (Claude Code) by Jinge, verbatim, with English translation.
# "[…]" marks where the original message continued and is not reproduced here.
TEXT_PROMPTS = [
    ("T1", "Instruction set rules",
     "关于说明书的问题：先订阅套餐，我们有20小时，80小时plan这些，付款了之后才可以点击开启使用 还有个问题是 一关闭就是关闭整个家庭了，但是如果其中一个人相关另外人不想关怎么办 改改",
     "About the guide: you subscribe to a plan first (we have 20-hour, 80-hour plans and so on); only after paying can you press start. Another problem: pausing turns it off for the whole household, so what if one person wants to and the others don't? Fix it.",
     "Our two new rules written into the guide: subscribe first; household pause (Keep me private, Step out)."),
    ("T2", "Share the guide",
     "组员要用他的ai改，你同步在github上，记得放上工程文件",
     "A teammate wants to edit it with his AI. Sync it to GitHub, and remember to include the project files.",
     "Guide files shared on GitHub for teammates to edit."),
    ("T3", "Catalogue insert layout",
     "按这个排版改，然后左下角画风改改，改得更精致简约，未来风符合 […]",
     "Follow this layout, and change the art style at the bottom left: more refined, minimal and futuristic […]",
     "Prompt P8 (catalogue insert v3)."),
    ("T4", "Catalogue insert style",
     "左下角还是不行，不要手绘风",
     "The bottom left still doesn't work. No hand-drawn style.",
     "Prompt P9 (v4, How It Works in 3D)."),
    ("T5", "Catalogue insert type",
     "你还有什么建议吗。斜体你觉得要换吗 / 出 v5",
     "Any other suggestions? Do you think the italics should change? / Make v5.",
     "Prompts P10–P11 (upright type, fine print)."),
    ("T6", "Catalogue insert back view",
     "那个back view 改改，挡住了",
     "Fix that back view, it's blocked.",
     "Prompt P12 (v5c, final)."),
    ("T7", "Compile the submission",
     "现在一次性生成剩下的，先不推到仓库",
     "Now generate everything that's left in one go. Don't push it to the repository yet.",
     "Our material assembled into one PDF and the English polished."),
    ("T8", "Consequence",
     "等等，按 招聘平台的\"跳槽意向\"信号被卖给雇主。用 GPT 建议的那句通知：\"Employment Profile Updated…\"，后果是现在的公司把 J 标成可能离职，第二天 J 就被调离一个重要项目。[…] 来",
     "Wait. Go with: the job platform's \"intent to change jobs\" signal is sold to employers. Use the notice GPT suggested, \"Employment Profile Updated…\"; the consequence is that J.'s current company flags J. as likely to leave, and J. is moved off an important project the next day. […] Do it.",
     "Our chosen consequence written up as scenario screens and two world rules."),
    ("T9", "Review round",
     "那就按你的意见来 […] 这个先不管",
     "Go with your suggestions then […] leave that one for now (the Figma button label).",
     "Our review decisions applied: page tags, shorter text, APA references, naming."),
    ("T10", "Final fixes",
     "这个界面应该是手机竖屏不是横屏 封面变形了像个床头表一样 去除红框里面图的白边 封面prototype没有展示完整 […] 好糊 logo文字统一，按这个图片来",
     "This interface should be a portrait phone screen, not landscape. The cover device is distorted and looks like a bedside clock. Remove the white borders on the boxed images. The prototype isn't fully shown on the cover. […] It's blurry. Make the logo text consistent, following this image.",
     "Our visual corrections applied: portrait phone, cover, logo, sharper images."),
    ("T11", "Recent signals, sharp poster",
     "趋势要是近期的趋势 不是10年前的 FAINT SIGNALS用2026年近期几个月的，最大一两年的 […] 这些东西放说明书很枯燥  海报包浆了，能不能清晰化，比如让gpt吧每个图片单独生成 iteration选几个改动大的重点就好了，不用放这么多小变化版本",
     "The trends must be recent, not from ten years ago. Use faint signals from the last few months of 2026, at most a year or two old. […] This is dull in the guide. The poster looks over-compressed; can it be made sharp, for example by having GPT generate each image separately? For the iterations, pick a few with big changes; no need for so many small variations.",
     "Recent sources found for our signals; small-print page and poster images redone (P15)."),
    ("T12", "Follow the team layout",
     "根据这个pdf文件修改海报，更换为高清图",
     "Revise the poster according to this PDF (a teammate's red-and-white vector version), and replace the images with high-resolution ones.",
     "Poster updated to our teammate's layout with high-resolution images (P16)."),
    ("T13", "Angled hero",
     "海报的那个主视觉图换成倾斜的那个3d风",
     "Change the poster's main visual to the angled 3D style.",
     "Hero image regenerated in the angled style we chose (P17–P18)."),
]

ROWS = [
    ("Concept and world",
     "The what-if, faint signals, archetype, the Private Hours model, all prices and hours, household rules, the job-search scenario and the employer consequence. Rejected several AI-suggested story ideas.",
     "Discussion partner only: questioned whether the story's cause and effect held up.",
     "—"),
    ("Physical model",
     "Designed and built by hand: frame, card mat, stand, iPad running our prototype. Photographed for this document.",
     "Early concept sketches of frame and colour options, used only to compare directions.",
     "P1"),
    ("Interactive prototypes",
     "Designed and built in Figma: the HUSH Home interface and the phone simulation.",
     "None recorded by the team. Screens in this document are screenshots of our prototypes.",
     "—"),
    ("Quick-start guide",
     "Content and rules: setup order, subscribe before use, household pause rules, what happens at 00:00, troubleshooting cases, fine print.",
     "Wrote our rules up as polished English copy and laid out the pages; generated 9 text-free line illustrations.",
     "P13–P14, T1–T2"),
    ("Advertisement",
     "Layout sketched by Jinge, then a red-and-white version by a teammate; headline, offer, fine print and every number; feedback on each round.",
     "Generated the product images to our layout and feedback; set our copy in type.",
     "P2–P12, P15–P18, T3–T6, T12–T13"),
    ("Scenario props",
     "The story and the consequence (J. pauses, searches, is moved off a project).",
     "Polished the wording of the three mock-up screens and built them as images.",
     "T8"),
    ("Process pages and sources",
     "Structure, arguments, critical questions, choice of signals; a teammate reviewed the draft with ChatGPT.",
     "Polished our English and layout; searched for recent news sources, which we checked before use.",
     "T7, T9–T11"),
    ("Week 11 slides",
     "Original group presentation, included unchanged.",
     "Not covered by this record.",
     "—"),
]
def esc(s): return html.escape(s)

rows = "\n".join(
    f"<tr><td><b>{esc(a)}</b></td><td>{esc(b)}</td><td class='ai'>{esc(c)}</td><td class='p'>{esc(e)}</td></tr>"
    for a, b, c, e in ROWS)

blocks = []
for pid, title, path in PROMPTS:
    text = path.read_text(encoding="utf-8").strip()
    paras = "".join(f"<p>{esc(line)}</p>" if line.strip() else "<p class='gap'></p>" for line in text.splitlines())
    blocks.append(f"<div class='pr'><div class='ph'><span>{pid}</span> {esc(title)} <em>{esc(path.name)}</em></div>{paras}</div>")


trows = "\n".join(
    f"<tr><td class='p'>{pid}</td><td><b>{esc(t)}</b></td><td class='zh'>{esc(zh)}</td><td>{esc(en)}</td><td>{esc(out)}</td></tr>"
    for pid, t, zh, en, out in TEXT_PROMPTS)

doc = f"""<!doctype html><html><head><meta charset="utf-8"><title>HUSH — AI record</title>
<link rel="stylesheet" href="style.css">
<style>
@page {{ size: 297mm 210mm; margin: 12mm 15mm 12mm; }}
html, body {{ background: #fff; }}
.rec h1 {{ font-size: 20pt; }}
.rec table {{ font-size: 7.3pt; }} .rec td {{ padding: 1.1mm 2.2mm 1.1mm 0; }} .rec h1 {{ margin-bottom: 2mm; }}
.rec td.p {{ color: var(--alert); font-weight: 600; font-size: 6.8pt; }} .rec td.ai {{ color: var(--soft); }}
.app {{ column-count: 3; column-gap: 7mm; font-size: 6.9pt; line-height: 1.38; }}
.app .pr {{ margin-bottom: 4mm; }}
.app .ph {{ font-size: 7.6pt; font-weight: 700; border-top: .5mm solid var(--ink); padding-top: 1.2mm; margin-bottom: 1.2mm; break-after: avoid; }}
.app .ph span {{ color: var(--alert); }}
.app .ph em {{ font-style: normal; font-weight: 400; color: var(--soft); font-size: 6.6pt; display:block; }}
.app p {{ margin: 0; }}
.app p.gap {{ height: 1.2mm; }}
.tp {{ font-size: 7pt; }} .tp td {{ padding: 1.2mm 2.4mm 1.2mm 0; }} .tp td.zh {{ font-family: 'Microsoft YaHei', 'PingFang SC', sans-serif; }} .tp td.p {{ color: var(--alert); font-weight: 700; }}
</style></head><body>
<section class="rec" style="page-break-after: always">
  <div class="kicker"><span class="ptag">PROCESS · 2026</span>11 · Generative AI usage record</div>
  <h1>Our project, with AI as a tool.</h1>
  <p style="max-width:235mm; margin-bottom:3mm">HUSH is our group's idea, world and story. We used AI for two things: <b>generating images</b> (product renders, concept sketches, guide illustrations) and <b>polishing copy</b> (turning our notes and decisions into clean English, and setting it on the page). Every decision about the world is ours: the what-if, the scenario, the plans, prices, hours, household rules and fine print. The physical model and the Figma prototypes are our own work.</p>
  <p class="small" style="max-width:235mm; margin-bottom:4mm">Tools: Codex (OpenAI) for image generation, Claude (Anthropic) for copy and layout, ChatGPT (OpenAI) for one review of the draft. Appendix A gives the image prompts in full (P1–P18). Appendix B gives the instructions we gave the AI, verbatim (T1–T13). Full chat transcripts are kept by Jinge and can be provided on request.</p>
  <table>
    <tr><th style="width:15%">Part</th><th style="width:44%">Our work</th><th style="width:30%">What AI was used for</th><th>Prompts</th></tr>
    {rows}
  </table>
</section>
<section style="page-break-after: always; height: 180mm; display:flex; flex-direction:column; justify-content:flex-end">
  <div class="kicker">Appendices A and B · not part of the design fiction</div>
  <h1 style="font-size:40pt; font-weight:500; margin:3mm 0 4mm">Prompts, in full</h1>
  <p style="max-width:170mm">A: the exact prompts used for AI image generation (P1–P18). B: the instructions we gave the AI, verbatim in Chinese with English translations (T1–T13). Both are referenced in the usage record above.</p>
</section>
<section>
  <div class="kicker" style="margin-bottom:3mm">Appendix A · Prompts used, in full</div>
  <div class="app">{''.join(blocks)}</div>
</section>
<section style="page-break-before: always">
  <div class="kicker" style="margin-bottom:3mm">Appendix B · Our instructions to the AI, verbatim (Chinese) with English translation</div>
  <table class="tp">
    <tr><th style="width:5%">ID</th><th style="width:11%">Task</th><th style="width:27%">Original (verbatim)</th><th style="width:32%">English translation</th><th>Result</th></tr>
    {trows}
  </table>
  <p class="small" style="margin-top:4mm">"[…]" marks where a message continued with screenshots or other details not reproduced here. These show how we directed the work: each instruction sets what to change and why. AI replies are not reproduced; every text and image was reviewed by the team before use.</p>
</section>
</body></html>"""
(HERE / "part3.html").write_text(doc, encoding="utf-8")
print("part3.html written,", len(PROMPTS), "prompts")
