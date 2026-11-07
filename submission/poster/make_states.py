"""Make hero-active.html and hero-paused.html from hero-ui.html (the 00:00 state)."""
import pathlib
d = pathlib.Path(__file__).parent
base = (d / "hero-ui.html").read_text(encoding="utf-8")

extra_css = """
.pp{width:150px;height:150px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#F0414B,#C8102E 70%);box-shadow:0 0 0 8px rgba(200,16,46,.12),0 6px 18px rgba(200,16,46,.35);display:flex;align-items:center;justify-content:center;gap:16px}
.pp i{display:block;width:16px;height:58px;background:#fff;border-radius:3px}
.dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:10px;vertical-align:1px}
</style>"""

def make(name, label, dotcol, ring, band_title, cats):
    s = base.replace("</style>", extra_css, 1)
    s = s.replace('<div class="k">PRIVATE HOURS</div><div class="n">00:00</div><div class="r">remaining</div>',
                  f'<div class="k"><span class="dot" style="background:{dotcol}"></span>{label}</div><div class="n">59:59</div><div class="r">remaining</div>')
    s = s.replace('<div class="ring"><b>0</b><span>HRS</span></div>', ring)
    s = s.replace('<span><i></i>PROTECTION INACTIVE</span>', f'<span><i style="background:{dotcol}"></i>{band_title}</span>')
    old_cats = '<div>App Tracking<b>Active</b></div><div>Browser Profiling<b>Active</b></div><div>Device Data Sharing<b>Active</b></div><div>Ad Personalisation<b>Active</b></div>'
    s = s.replace(old_cats, "".join(f"<div>{k}<b>{v}</b></div>" for k, v in cats))
    (d / name).write_text(s, encoding="utf-8")

make("hero-active.html", "PROTECTION ACTIVE", "#5E9B6E",
     '<div class="pp"><i></i><i></i></div>', "11 DEVICES PROTECTED",
     [("App Tracking", "Blocked"), ("Browser Profiling", "Blocked"), ("Device Data Sharing", "Protected"), ("Ad Personalisation", "Blocked")])
make("hero-paused.html", "PROTECTION PAUSED", "#E0392B",
     '<div class="ring"><b>1</b><span>HRS</span></div>', "PROTECTION PAUSED · TIME SAVED",
     [("App Tracking", "Active"), ("Browser Profiling", "Active"), ("Device Data Sharing", "Active"), ("Ad Personalisation", "Active")])
print("ok")
