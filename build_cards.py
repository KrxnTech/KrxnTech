#!/usr/bin/env python3
"""Render the profile README cards into cards/ as self-contained animated SVGs.

Everything here has to survive being shown through an <img> tag, so each card only uses:
  * one inline <style> block (CSS keyframes, @font-face with base64 WOFF2 data URIs)
  * SMIL <animate> (only for the little "live" dot, with a static twin for reduced motion)
  * no scripts, no external requests

Usage:
  python build_cards.py            # animated cards
  STATIC=1 python build_cards.py   # final frame only (no animation), for screenshots

Fonts are subset per card with pyftsubset (fontTools.subset) to just the glyphs that card uses.
"""
import base64
import html
import json
import math
import os
import subprocess
import sys
import tempfile
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent
STATIC = os.environ.get("STATIC") == "1"
OUT = ROOT / os.environ.get("CARDS_DIR", "cards")
DATA = ROOT / os.environ.get("CONTRIB_JSON", "data/contributions.json")

# --------------------------------------------------------------------------- config
LOGIN = "KrxnTech"
NAME = ("Krishna", "Sharma")  # first line upright, second line italic
EYEBROW = "BACKEND ENGINEER"
TAGLINE = "I build backends and MERN apps, then ship them with DevOps and cloud."
LINKEDIN = "https://www.linkedin.com/in/krishna-sharma-10b5ab359/"
HANDLE = f"github.com/{LOGIN}"

# optional portrait: PORTRAIT=path, or drop assets/portrait.(png|jpg|webp) in the repo
_portrait_candidates = [os.environ.get("PORTRAIT", "")] + [str(ROOT / f"assets/portrait.{e}") for e in ("png", "jpg", "jpeg", "webp")]
PORTRAIT = next((Path(p) for p in _portrait_candidates if p and Path(p).is_file()), None)

# colours sampled from the reference screenshots (warm paper, ink, blue/red/yellow tiles)
BG, LINE, INK, MUTED = "#F3F3F1", "#DEDED9", "#141414", "#6E6E69"
BRAND, RED, YELLOW, WHITE = "#2F55FF", "#F03C2E", "#FFC81E", "#FFFFFF"
GRAPH = ["#E3E3DF", "#CAD3FF", "#93A8FF", "#5B79FF", "#2A4BEE"]  # contribution graph, in the brand colour

TILES = [  # label, upright, italic, text, fill, ink, link, file
    ("BUILD", "2", "AI apps", "Resume Buddy and ContentHub: MERN apps where AI does the heavy part.",
     BRAND, WHITE, f"https://github.com/{LOGIN}?tab=repositories", "tile-build"),
    ("SHIP", "Docker", "& cloud", "Containers, pipelines and deploys for the things I build.",
     RED, WHITE, f"https://github.com/{LOGIN}/Resume-Buddy", "tile-ship"),
    ("TALK", "Say", "hi", "Backend, DevOps or MERN work? Find me on LinkedIn.",
     YELLOW, INK, LINKEDIN, "tile-talk"),
]

# (monogram, label): the hanging stack, based on the LinkedIn bio. Edit freely.
STACK = [("TS", "TypeScript"), ("Nd", "Node.js"), ("Ex", "Express"), ("Re", "React"), ("Mo", "MongoDB"),
         ("Dk", "Docker"), ("Lx", "Linux"), ("CI", "Actions"), ("AW", "AWS"), ("Gt", "Git")]

REPOS = [  # name, description, in_progress
    ("Resume-Buddy", "AI-powered MERN app that checks a resume against a job description, finds skill gaps and suggests how to fix them.", False),
    ("ContentHub", "AI web platform that turns 4 to 5 minute videos into several short clips automatically.", True),
]

LANG_COLOURS = {"JavaScript": "#F1E05A", "TypeScript": "#3178C6", "Python": "#3572A5", "HTML": "#E34C26",
                "CSS": "#563D7C", "Dockerfile": "#384D54", "Shell": "#89E051"}

FONT_DIR = ROOT / "fonts"
FONTS = {  # key: (family, style, weight, file)
    "serif": ("KSerif", "normal", 400, "instrument-serif-latin-400-normal.woff2"),
    "serifi": ("KSerif", "italic", 400, "instrument-serif-latin-400-italic.woff2"),
    "sans": ("KSans", "normal", 400, "instrument-sans-latin-400-normal.woff2"),
    "sansm": ("KSans", "normal", 500, "instrument-sans-latin-500-normal.woff2"),
    "mono": ("KMono", "normal", 400, "jetbrains-mono-latin-400-normal.woff2"),
}

# --------------------------------------------------------------------------- helpers
esc = lambda s: html.escape(str(s), quote=False)  # noqa: E731
f1 = lambda x: f"{x:.1f}".rstrip("0").rstrip(".")  # noqa: E731


class Metric:
    """Measures text with the real font so wrapping and fitting are exact."""

    def __init__(self, path):
        font = TTFont(path)
        self.cmap, self.hmtx, self.upm = font.getBestCmap(), font["hmtx"], font["head"].unitsPerEm

    def w(self, text, size, ls=0.0):
        total = 0
        for ch in text:
            g = self.cmap.get(ord(ch))
            total += self.hmtx[g][0] if g else self.upm * 0.5
        return total / self.upm * size + ls * len(text)


METRICS = {k: Metric(FONT_DIR / v[3]) for k, v in FONTS.items()}
_subset_cache = {}


def subset_font(key, chars):
    chars = "".join(sorted(set(chars) | {" "}))
    if (key, chars) in _subset_cache:
        return _subset_cache[(key, chars)]
    with tempfile.TemporaryDirectory() as tmp:
        txt, out = Path(tmp, "t.txt"), Path(tmp, "o.woff2")
        txt.write_text(chars, encoding="utf-8")
        cmd = [sys.executable, "-m", "fontTools.subset", str(FONT_DIR / FONTS[key][3]), f"--text-file={txt}",
               "--flavor=woff2", "--layout-features=kern,liga", "--no-hinting", f"--output-file={out}"]
        subprocess.run(cmd, check=True, capture_output=True)  # same tool as the pyftsubset command
        b64 = base64.b64encode(out.read_bytes()).decode()
    _subset_cache[(key, chars)] = b64
    return b64


def wrap(text, font, size, max_w, ls=0.0):
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if cur and METRICS[font].w(trial, size, ls) > max_w:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    return lines + [cur] if cur else lines


def arrow(x, y, s, colour, sw=1.7):
    return (f'<path d="M{f1(x)} {f1(y + s)}L{f1(x + s)} {f1(y)}M{f1(x + s * .12)} {f1(y)}H{f1(x + s)}V{f1(y + s * .88)}" '
            f'fill="none" stroke="{colour}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>')


def star(cx, cy, r, colour):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * .42
        pts.append(f"{f1(cx + rr * math.cos(a))},{f1(cy + rr * math.sin(a))}")
    return f'<polygon points="{" ".join(pts)}" fill="{colour}"/>'


def fork(x, y, colour):
    return (f'<g fill="none" stroke="{colour}" stroke-width="1.5" stroke-linecap="round">'
            f'<circle cx="{x + 2.5}" cy="{y + 2.5}" r="2"/><circle cx="{x + 11.5}" cy="{y + 2.5}" r="2"/>'
            f'<circle cx="{x + 7}" cy="{y + 13}" r="2"/>'
            f'<path d="M{x + 2.5} {y + 4.5}V{y + 6.5}Q{x + 2.5} {y + 8.5} {x + 4.5} {y + 8.5}H{x + 9.5}'
            f'Q{x + 11.5} {y + 8.5} {x + 11.5} {y + 6.5}V{y + 4.5}M{x + 7} {y + 8.5}V{y + 11}"/></g>')


# --------------------------------------------------------------------------- card base
CSS_BASE = """
.f-serif,.f-serifi{font-family:KSerif,"Instrument Serif",Georgia,serif;font-weight:400}
.f-serifi{font-style:italic}
.f-sans,.f-sansm{font-family:KSans,"Instrument Sans",system-ui,-apple-system,"Segoe UI",sans-serif}
.f-sans{font-weight:400}.f-sansm{font-weight:500}
.f-mono{font-family:KMono,"JetBrains Mono",ui-monospace,Menlo,monospace;font-weight:400}
.bar{transform-box:fill-box;transform-origin:50% 100%}
"""
CSS_MOTION = """
@keyframes rise{from{opacity:0;transform:translateY(16px)}}
@keyframes fade{from{opacity:0}}
@keyframes grow{from{transform:scaleY(0)}}
@keyframes pop{from{opacity:0;transform:scale(.55)}}
@keyframes drop{from{opacity:0;transform:translateY(-70px)}}
@keyframes swing{0%,100%{transform:rotate(0)}25%{transform:rotate(var(--a))}75%{transform:rotate(var(--b))}}
.rise{animation:rise .8s cubic-bezier(.2,.7,.2,1) both}
.fade{animation:fade .9s ease-out both}
.grow{animation:grow .9s cubic-bezier(.2,.8,.2,1) both}
.pop{animation:pop .45s cubic-bezier(.2,.9,.3,1.3) both;transform-box:fill-box;transform-origin:center}
.drop{animation:drop .9s cubic-bezier(.3,1.3,.5,1) both}
.swing{animation:swing var(--t,4s) ease-in-out infinite;animation-delay:var(--s,0s)}
.rise,.fade,.grow,.pop,.drop{animation-delay:var(--d,0s)}
.still{display:none}
@media (prefers-reduced-motion:reduce){*{animation:none!important}.smil{display:none}.still{display:inline}}
"""


class Card:
    def __init__(self, name, w, h, title, desc, delay):
        self.name, self.w, self.h, self.title, self.desc, self.t0 = name, w, h, title, desc, delay
        self.body, self.used = [], defaultdict(set)

    # -- primitives
    def add(self, markup):
        self.body.append(markup)

    def frame(self, fill=BG, stroke=LINE, rx=32):
        self.add(f'<rect x=".5" y=".5" width="{self.w - 1}" height="{self.h - 1}" rx="{rx}" fill="{fill}"'
                 + (f' stroke="{stroke}"' if stroke else "") + "/>")

    def g(self, inner, anim="rise", d=0.0, extra=""):
        if STATIC:
            return f"<g{extra}>{inner}</g>"
        return f'<g class="{anim}" style="--d:{self.t0 + d:.2f}s"{extra}>{inner}</g>'

    def t(self, x, y, text, font, size, fill, anchor="start", ls=0.0):
        self.used[font].update(text)
        a = "" if anchor == "start" else f' text-anchor="{anchor}"'
        s = f' letter-spacing="{ls}"' if ls else ""
        return f'<text x="{f1(x)}" y="{f1(y)}" class="f-{font}" font-size="{f1(size)}" fill="{fill}"{a}{s}>{esc(text)}</text>'

    def rich(self, x, y, runs, size, anchor="start"):
        """runs: [(font, text, fill)] set as tspans in one text element; returns (markup, width)."""
        spans, width = [], 0
        for font, text, fill in runs:
            self.used[font].update(text)
            width += METRICS[font].w(text, size)
            spans.append(f'<tspan class="f-{font}" fill="{fill}" xml:space="preserve">{esc(text)}</tspan>')
        a = "" if anchor == "start" else f' text-anchor="{anchor}"'
        return f'<text x="{f1(x)}" y="{f1(y)}" font-size="{f1(size)}"{a}>{"".join(spans)}</text>', width

    def dot(self, x, y, s, fill, rx=2.5):
        """Pulsing marker: SMIL animation plus a static twin that reduced motion falls back to."""
        rect = f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{rx}" fill="{fill}"'
        if STATIC:
            return rect + "/>"
        return (f'{rect} class="smil"><animate attributeName="opacity" values="1;.25;1" dur="2.6s" '
                f'begin="{self.t0 + .8:.2f}s" repeatCount="indefinite"/></rect>{rect} class="still"/>')

    # -- output
    def svg(self):
        faces = []
        for key, chars in self.used.items():
            fam, style, weight, _ = FONTS[key]
            faces.append(f'@font-face{{font-family:{fam};font-style:{style};font-weight:{weight};'
                         f'src:url(data:font/woff2;base64,{subset_font(key, chars)}) format("woff2")}}')
        css = "".join(faces) + CSS_BASE + ("" if STATIC else CSS_MOTION)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}" '
                f'role="img" aria-labelledby="t d"><title id="t">{esc(self.title)}</title><desc id="d">{esc(self.desc)}</desc>'
                f"<style>{css}</style>{''.join(self.body)}</svg>\n")

    def write(self):
        OUT.mkdir(parents=True, exist_ok=True)
        data = self.svg()
        (OUT / f"{self.name}.svg").write_text(data, encoding="utf-8")
        print(f"  cards/{self.name}.svg  {len(data) / 1024:.1f} KB")


# --------------------------------------------------------------------------- data
def load_data():
    d = json.loads(DATA.read_text())
    d["days"] = sorted(d["days"], key=lambda x: x["date"])
    return d


def month_window(days):
    end = date.fromisoformat(days[-1]["date"])
    months = []
    y, m = end.year, end.month
    for _ in range(12):
        months.append((y, m))
        m -= 1
        if m == 0:
            y, m = y - 1, 12
    months.reverse()
    sums = {k: 0 for k in months}
    window = []
    for d in days:
        dt = date.fromisoformat(d["date"])
        if (dt.year, dt.month) in sums:
            sums[(dt.year, dt.month)] += d["count"]
            window.append((dt, d["count"]))
    return months, sums, window


def streaks(days):
    counts = [d["count"] for d in days]
    longest = run = 0
    for c in counts:
        run = run + 1 if c > 0 else 0
        longest = max(longest, run)
    cur, i = 0, len(counts) - 1
    if i >= 0 and counts[i] == 0:  # today may simply not be over yet
        i -= 1
    while i >= 0 and counts[i] > 0:
        cur += 1
        i -= 1
    return cur, longest


# --------------------------------------------------------------------------- cards
def hero(t0):
    W, H = 900, 500
    c = Card("hero", W, H, f"{NAME[0]} {NAME[1]}", f"{EYEBROW}. {TAGLINE}", t0)
    c.frame()
    avail = 470 if PORTRAIT else 790
    size = min(156, avail / max(METRICS["serif"].w(NAME[0], 1), METRICS["serifi"].w(NAME[1], 1)))
    b1, b2 = 88 + size * .8, 88 + size * .8 + size * .86
    c.add(c.dot(58, 49, 10, BRAND))
    c.add(c.g(c.t(80, 59, EYEBROW, "mono", 13, INK, ls=1.8), "fade"))
    m, _ = c.rich(56, b1, [("serif", NAME[0], INK)], size)
    c.add(c.g(m, "rise", .15))
    m, _ = c.rich(56, b2, [("serifi", NAME[1], INK)], size)
    c.add(c.g(m, "rise", .3))
    y = b2 + 58
    lines = wrap(TAGLINE, "sans", 21, min(avail, 520))
    c.add(c.g("".join(c.t(58, y + i * 30, ln, "sans", 21, INK) for i, ln in enumerate(lines)), "rise", .5))
    y += len(lines) * 30 + 14
    hw = METRICS["mono"].w(HANDLE, 15)
    c.add(c.g(c.t(58, y, HANDLE, "mono", 15, INK) + arrow(58 + hw + 8, y - 11, 9, BRAND), "rise", .65))
    if PORTRAIT:
        mime = {"png": "png", "jpg": "jpeg", "jpeg": "jpeg", "webp": "webp"}[PORTRAIT.suffix[1:].lower()]
        uri = f"data:image/{mime};base64," + base64.b64encode(PORTRAIT.read_bytes()).decode()
        c.add('<clipPath id="pc"><rect x="574" y="64" width="270" height="372" rx="26"/></clipPath>')
        c.add(c.g(f'<image href="{uri}" x="574" y="64" width="270" height="372" preserveAspectRatio="xMidYMid slice" clip-path="url(#pc)"/>', "fade", .35))
    c.write()


def tile(spec, idx, t0):
    label, big_a, big_b, text, fill, ink, _link, fname = spec
    W, H = 292, 244
    c = Card(fname, W, H, f"{label}: {big_a} {big_b}", text, t0 + idx * .15)
    c.add(f'<rect width="{W}" height="{H}" rx="26" fill="{fill}"/>')
    c.add(c.g(c.t(26, 42, label, "mono", 12, ink, ls=1.8) + arrow(W - 42, 28, 12, ink), "fade"))
    full = METRICS["serif"].w(big_a + " ", 1) + METRICS["serifi"].w(big_b, 1)
    size = max(34, min(54, (W - 52) / full))
    m, _ = c.rich(26, 128, [("serif", big_a + " ", ink), ("serifi", big_b, ink)], size)
    c.add(c.g(m, "rise", .15))
    lines = wrap(text, "sans", 15.5, W - 56)
    c.add(c.g("".join(c.t(26, 166 + i * 22, ln, "sans", 15.5, ink) for i, ln in enumerate(lines)), "rise", .3))
    c.write()


def stack(t0):
    W, H, rail = 900, 372, 36
    c = Card("stack", W, H, "Tech stack", "Tools I work with: " + ", ".join(n for _, n in STACK), t0)
    c.frame()
    c.add(c.g(f'<rect x="48" y="{rail - 6}" width="{W - 96}" height="12" rx="6" fill="{INK}"/>', "fade"))
    pal = [(BRAND, WHITE), (INK, WHITE), (YELLOW, INK), (RED, WHITE), (WHITE, INK)]
    lengths = [86, 124, 70, 108, 94, 132, 78, 116, 90, 104]
    span = (W - 140) / (len(STACK) - 1)
    for i, (mark, name) in enumerate(STACK):
        cx, L = 70 + i * span, lengths[i % len(lengths)]
        fill, ink = pal[i % len(pal)]
        tw, th = 68, 92
        a = 5 + (i * 7) % 5 * .8
        sign = 1 if i % 2 == 0 else -1
        t = 3.4 + (i * 37) % 9 * .22
        d = i * .12
        msize = min(34, 44 / max(METRICS["serif"].w(mark, 1), .1))
        tile_svg = (
            f'<line x1="0" y1="0" x2="0" y2="{L}" stroke="{INK}" stroke-width="1.6"/>'
            f'<circle cx="0" cy="{L}" r="4.5" fill="{BG}" stroke="{INK}" stroke-width="1.6"/>'
            f'<rect x="{-tw / 2}" y="{L}" width="{tw}" height="{th}" rx="14" fill="{fill}"'
            + (f' stroke="{LINE}"' if fill == WHITE else "") + "/>"
            + c.t(0, L + 52, mark, "serif", msize, ink, anchor="middle")
            + c.t(0, L + 78, name, "mono", 10, ink, anchor="middle")
        )
        swing = tile_svg if STATIC else (
            f'<g class="swing" style="--a:{sign * a:.1f}deg;--b:{-sign * a:.1f}deg;--t:{t:.2f}s;--s:{t0 + 1.0 + d:.2f}s">{tile_svg}</g>')
        pin = c.g(f'<circle cx="0" cy="0" r="5" fill="{INK}"/>', "fade")
        inner = swing if STATIC else f'<g class="drop" style="--d:{t0 + .25 + d:.2f}s">{swing}</g>'
        c.add(f'<g transform="translate({f1(cx)} {rail})">{inner}{pin}</g>')
    m, _ = c.rich(56, H - 30, [("serif", "The stack, ", INK), ("serifi", "hanging by a thread", INK)], 38)
    c.add(c.g(m, "rise", .9))
    c.write()


def contributions_card(data, t0):
    days = data["days"]
    months, sums, window = month_window(days)
    total = sum(sums.values())
    cur, longest = streaks(days)
    active = sum(1 for _, n in window if n > 0)
    best_day, best = max(window, key=lambda x: x[1])
    W, H = 900, 404
    c = Card("contributions", W, H, f"{total:,} contributions in the last 12 months",
             f"{cur} day current streak, {active} of {len(window)} days active, busiest day {best}", t0)
    c.frame()
    c.add(c.g(c.t(56, 64, "THE LAST 12 MONTHS ON GITHUB", "mono", 12, MUTED, ls=1.6), "fade"))
    m, _ = c.rich(56, 140, [("serif", f"{total:,} ", INK), ("serifi", "contributions", INK)], 70)
    c.add(c.g(m, "rise", .1))
    # bars
    x0, slot, base, top = 56, 45.5, 332, 190
    complete = [sums[k] for k in months[:-1]]
    peak = max(complete) if complete and max(complete) > 0 else 1
    scale = (base - top) / max(max(sums.values()), 1)
    names = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
    for i, k in enumerate(months):
        h = max(10, sums[k] * scale)
        x, last = x0 + i * slot, i == len(months) - 1
        fill = "#C8C8C1" if last else (BRAND if sums[k] == peak and sums[k] > 0 else INK)
        d = .25 + i * .06
        rect = f'x="{f1(x)}" y="{f1(base - h)}" width="39" height="{f1(h)}" rx="7" fill="{fill}"/>'
        c.add(f"<rect {rect}" if STATIC else f'<rect class="bar grow" style="--d:{t0 + d:.2f}s" {rect}')
        c.add(c.g(c.t(x + 19.5, base + 27, names[k[1] - 1], "mono", 11, MUTED, anchor="middle"), "fade", d))
        if fill == BRAND:
            c.add(c.g(c.t(x + 19.5, base - h - 10, f"{sums[k]:,}", "mono", 12, BRAND, anchor="middle"), "fade", d + .5))
    # right-hand stats
    rx_, rw = 650, 200
    stats = [
        ([("serif", f"{cur} ", INK), ("serifi", "days", INK)], f"current streak, longest {longest}"),
        ([("serif", f"{active} ", INK), ("serif", f"/ {len(window)}", "#9A9A94")], "days with a contribution"),
        ([("serif", f"{best}", INK)], f"on the busiest day, {best_day.strftime('%b')} {best_day.day}"),
    ]
    for i, (runs, cap) in enumerate(stats):
        y = 108 + i * 102
        m, _ = c.rich(rx_, y, runs, 52)
        c.add(c.g(m + c.t(rx_, y + 26, cap, "sans", 14.5, MUTED), "rise", .5 + i * .15))
        if i < 2:
            c.add(c.g(f'<line x1="{rx_}" x2="{rx_ + rw}" y1="{y + 46}" y2="{y + 46}" stroke="{LINE}"/>', "fade", .6 + i * .15))
    c.write()


def repo_card(name, desc, wip, data, idx, t0):
    W, H = 900, 252
    info = data.get("repos", {}).get(name, {})
    c = Card(f"repo-{name.lower()}", W, H, name, desc, t0)
    c.frame()
    c.add(c.dot(58, 49, 10, YELLOW if wip else BRAND))
    c.add(c.g(c.t(80, 59, "IN PROGRESS" if wip else "FEATURED PROJECT", "mono", 12, INK, ls=1.8), "fade"))
    m, _ = c.rich(56, 126, [("serif", name, INK)], 60)
    c.add(c.g(m, "rise", .15))
    lines = wrap(desc, "sans", 17, 620)[:3]
    c.add(c.g("".join(c.t(58, 160 + i * 25, ln, "sans", 17, INK) for i, ln in enumerate(lines)), "rise", .3))
    # meta row: language, stars, forks, updated (only what the data has)
    x, y, meta = 58, 224, []
    langs = info.get("languages") or ([info["language"]] if info.get("language") else [])
    for lang in langs[:3]:
        meta.append(f'<circle cx="{x + 5}" cy="{y - 5}" r="5" fill="{LANG_COLOURS.get(lang, INK)}"/>' + c.t(x + 16, y, lang, "mono", 12.5, MUTED))
        x += 16 + METRICS["mono"].w(lang, 12.5) + 20
    if "stars" in info:
        meta.append(star(x + 7, y - 6, 7, MUTED) + c.t(x + 20, y, str(info["stars"]), "mono", 12.5, MUTED))
        x += 20 + METRICS["mono"].w(str(info["stars"]), 12.5) + 20
        meta.append(fork(x, y - 14, MUTED) + c.t(x + 20, y, str(info.get("forks", 0)), "mono", 12.5, MUTED))
        x += 20 + METRICS["mono"].w(str(info.get("forks", 0)), 12.5) + 20
    if info.get("pushed_at"):
        when = datetime.fromisoformat(info["pushed_at"].replace("Z", "+00:00")).strftime("%b %Y")
        meta.append(c.t(x, y, f"Updated {when}", "mono", 12.5, MUTED))
    if not meta:
        meta.append(c.t(x, y, f"{HANDLE}/{name}", "mono", 12.5, MUTED))
    c.add(c.g("".join(meta), "fade", .5))
    c.add(c.g(f'<circle cx="806" cy="124" r="36" fill="{BRAND}"/>' + arrow(794, 112, 24, WHITE, 2.2), "pop", .45))
    c.write()


def graph_card(data, t0):
    days = data["days"]
    W, H = 900, 332
    c = Card("graph", W, H, "Contribution graph in blue", "One year of daily contributions, darker blue is more", t0)
    c.frame()
    m, _ = c.rich(56, 86, [("serif", "One year, ", INK), ("serifi", "in blue", BRAND)], 46)
    c.add(c.g(m, "rise", .05))
    c.add(c.dot(W - 56 - 10 - METRICS["mono"].w("REFRESHED DAILY", 12, 1.6) - 14, 66, 10, BRAND))
    c.add(c.g(c.t(W - 56, 76, "REFRESHED DAILY", "mono", 12, MUTED, anchor="end", ls=1.6), "fade"))
    first = date.fromisoformat(days[0]["date"])
    pad = (first.weekday() + 1) % 7  # weeks start on Sunday
    cells = [None] * pad + days
    weeks = math.ceil(len(cells) / 7)
    pitch = (W - 112) / weeks
    cell = pitch * .78
    gy, labels = 122, []
    prev_x = -99
    names = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
    for w in range(weeks):
        col = []
        for r in range(7):
            item = cells[w * 7 + r] if w * 7 + r < len(cells) else None
            if not item:
                continue
            col.append(f'<rect x="{f1(56 + w * pitch)}" y="{f1(gy + r * pitch)}" width="{f1(cell)}" height="{f1(cell)}" '
                       f'rx="{f1(cell * .26)}" fill="{GRAPH[min(item["level"], 4)]}"/>')
            if item["date"].endswith("-01") and 56 + w * pitch - prev_x > 44:
                labels.append(c.t(56 + w * pitch, gy + 7 * pitch + 22, names[int(item["date"][5:7]) - 1], "mono", 11, MUTED))
                prev_x = 56 + w * pitch
        c.add(c.g("".join(col), "fade", .2 + w * .014))
    c.add(c.g("".join(labels), "fade", .9))
    lx = W - 56
    legend = [c.t(lx, gy + 7 * pitch + 58, "more", "mono", 11, MUTED, anchor="end")]
    lx -= METRICS["mono"].w("more", 11) + 10
    for lvl in range(4, -1, -1):
        lx -= cell
        legend.append(f'<rect x="{f1(lx)}" y="{f1(gy + 7 * pitch + 48)}" width="{f1(cell)}" height="{f1(cell)}" rx="{f1(cell * .26)}" fill="{GRAPH[lvl]}"/>')
        lx -= 4
    legend.append(c.t(lx - 6, gy + 7 * pitch + 58, "less", "mono", 11, MUTED, anchor="end"))
    c.add(c.g("".join(legend), "fade", 1.0))
    c.write()


def main():
    data = load_data()
    print(("STATIC (final frame)" if STATIC else "animated") + f" cards -> {OUT}")
    # delays step down the page so it plays top to bottom: hero, tiles, stack, chart, repos, graph
    hero(0.0)
    for i, spec in enumerate(TILES):
        tile(spec, i, 0.55)
    stack(1.15)
    contributions_card(data, 1.85)
    for i, (name, desc, wip) in enumerate(REPOS):
        repo_card(name, desc, wip, data, i, 2.55 + i * .4)
    graph_card(data, 3.5)


if __name__ == "__main__":
    main()
