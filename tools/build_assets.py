#!/usr/bin/env python3
"""
Generates every pixel-art SVG used by README.md into ../assets/.

Usage:
    python tools/build_assets.py
    python tools/build_assets.py --photo me.jpg --shot1 contenthub.png --shot2 sigmagpt.png

--photo / --shot1 / --shot2 are optional: the image is embedded (base64) inside the
retro window frame, so you get the frame + your screenshot in a single file.
"""
import argparse, base64, math, os, re

BG = "#FFF3F5"; PINK = "#F2B8CB"; PURPLE = "#42305F"; BLACK = "#111111"
LGRAY = "#E5E5E5"; GREY = "#CFCFCF"; BAR = "#BDBDBD"; OFF = "#F5F5EE"
WHITE = "#FFFFFF"; HOT = "#F06CB5"; MUTED = "#6B5B95"; K = BLACK

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")

# ---------------------------------------------------------------- 5x7 pixel font
F = {
 'A': [".###.","#...#","#...#","#####","#...#","#...#","#...#"],
 'B': ["####.","#...#","#...#","####.","#...#","#...#","####."],
 'C': [".####","#....","#....","#....","#....","#....",".####"],
 'D': ["####.","#...#","#...#","#...#","#...#","#...#","####."],
 'E': ["#####","#....","#....","####.","#....","#....","#####"],
 'F': ["#####","#....","#....","####.","#....","#....","#...."],
 'G': [".####","#....","#....","#.###","#...#","#...#",".####"],
 'H': ["#...#","#...#","#...#","#####","#...#","#...#","#...#"],
 'I': ["#####","..#..","..#..","..#..","..#..","..#..","#####"],
 'J': ["..###","...#.","...#.","...#.","...#.","#..#.",".##.."],
 'K': ["#...#","#..#.","#.#..","##...","#.#..","#..#.","#...#"],
 'L': ["#....","#....","#....","#....","#....","#....","#####"],
 'M': ["#...#","##.##","#.#.#","#.#.#","#...#","#...#","#...#"],
 'N': ["#...#","##..#","#.#.#","#..##","#...#","#...#","#...#"],
 'O': [".###.","#...#","#...#","#...#","#...#","#...#",".###."],
 'P': ["####.","#...#","#...#","####.","#....","#....","#...."],
 'Q': [".###.","#...#","#...#","#...#","#.#.#","#..#.",".##.#"],
 'R': ["####.","#...#","#...#","####.","#.#..","#..#.","#...#"],
 'S': [".####","#....","#....",".###.","....#","....#","####."],
 'T': ["#####","..#..","..#..","..#..","..#..","..#..","..#.."],
 'U': ["#...#","#...#","#...#","#...#","#...#","#...#",".###."],
 'V': ["#...#","#...#","#...#","#...#","#...#",".#.#.","..#.."],
 'W': ["#...#","#...#","#...#","#.#.#","#.#.#","##.##","#...#"],
 'X': ["#...#","#...#",".#.#.","..#..",".#.#.","#...#","#...#"],
 'Y': ["#...#","#...#",".#.#.","..#..","..#..","..#..","..#.."],
 'Z': ["#####","....#","...#.","..#..",".#...","#....","#####"],
 '0': [".###.","#...#","#..##","#.#.#","##..#","#...#",".###."],
 '1': ["..#..",".##..","..#..","..#..","..#..","..#..",".###."],
 '2': [".###.","#...#","....#","...#.","..#..",".#...","#####"],
 '3': ["####.","....#","....#",".###.","....#","....#","####."],
 '4': ["...#.","..##.",".#.#.","#..#.","#####","...#.","...#."],
 '5': ["#####","#....","####.","....#","....#","#...#",".###."],
 '6': [".###.","#....","#....","####.","#...#","#...#",".###."],
 '7': ["#####","....#","...#.","..#..",".#...",".#...",".#..."],
 '8': [".###.","#...#","#...#",".###.","#...#","#...#",".###."],
 '9': [".###.","#...#","#...#",".####","....#","....#",".###."],
 '|': ["..#..","..#..","..#..","..#..","..#..","..#..","..#.."],
 '!': ["..#..","..#..","..#..","..#..","..#..",".....","..#.."],
 "'": ["..#..","..#..",".#...",".....",".....",".....","....."],
 '-': [".....",".....",".....","#####",".....",".....","....."],
 '.': [".....",".....",".....",".....",".....",".##..",".##.."],
 '/': ["....#","....#","...#.","..#..",".#...","#....","#...."],
 '>': ["#....",".#...","..#..","...#.","..#..",".#...","#...."],
 '_': [".....",".....",".....",".....",".....",".....","#####"],
 '^': ["..#..",".#.#.","#...#",".....",".....",".....","....."],
 '*': [".....","#.#.#",".###.","#####",".###.","#.#.#","....."],
 '+': [".....","..#..","..#..","#####","..#..","..#..","....."],
}

class G:
    """Tiny pixel grid -> merged SVG rects."""
    def __init__(s): s.c = {}
    def set(s, x, y, col): s.c[(x, y)] = col
    def rect(s, x0, y0, x1, y1, col):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1): s.c[(x, y)] = col
    def ascii(s, rows, pal, ox=0, oy=0):
        for y, r in enumerate(rows):
            for x, ch in enumerate(r):
                if ch in pal: s.c[(ox + x, oy + y)] = pal[ch]
    def dims(s, px):
        return ((max(k[0] for k in s.c) + 1) * px, (max(k[1] for k in s.c) + 1) * px)
    def svg(s, px, x=0, y=0):
        rows = {}
        for (cx, cy), col in s.c.items(): rows.setdefault(cy, []).append((cx, col))
        out = []
        for cy in sorted(rows):
            r = sorted(rows[cy]); i = 0
            while i < len(r):
                j = i
                while j + 1 < len(r) and r[j+1][0] == r[j][0] + 1 and r[j+1][1] == r[i][1]: j += 1
                out.append(f'<rect x="{x+r[i][0]*px:g}" y="{y+cy*px:g}" width="{(r[j][0]-r[i][0]+1)*px:g}" height="{px:g}" fill="{r[i][1]}"/>')
                i = j + 1
        return "".join(out)

def rect(x, y, w, h, fill): return f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" fill="{fill}"/>'

def spr(g, px, x, y, rot=0):
    w, h = g.dims(px)
    inner = g.svg(px, x, y)
    return f'<g transform="rotate({rot} {x+w/2:g} {y+h/2:g})">{inner}</g>' if rot else inner

# ---------------------------------------------------------------- text
def text_grid(text, gap=1):
    g = G(); x = 0
    for ch in text.upper():
        if ch == ' ': x += 3; continue
        for y, r in enumerate(F.get(ch, F['-'])):
            for i, c in enumerate(r):
                if c == '#': g.set(x + i, y, '#')
        x += 5 + gap
    return g, max(x - gap, 1)

def text_w(text, px): return text_grid(text)[1] * px

def text(t, x, y, px, col=BLACK):
    g, w = text_grid(t)
    for k in g.c: g.c[k] = col
    return g.svg(px, x, y)

def ctext(t, cx, y, px, col=BLACK): return text(t, cx - text_w(t, px) / 2, y, px, col)

def big_dims(t, fp):
    w = text_grid(t)[1]; cell = fp / 2
    return (w * 2 + 2) * cell, 16 * cell

def big_title(t, x, y, fp, fill=PINK, edge=PURPLE):
    """Pink tiled letters with a purple pixel outline (the PDF's signature heading)."""
    g, w = text_grid(t); cell = fp / 2
    cells = set()
    for (cx, cy) in g.c:
        for dx in (0, 1):
            for dy in (0, 1): cells.add((cx * 2 + dx + 1, cy * 2 + dy + 1))
    out = set()
    for (cx, cy) in cells:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1): out.add((cx + dx, cy + dy))
    o = G()
    for k in out: o.c[k] = edge
    pink = "".join(f'M{x+cx*cell:g} {y+cy*cell:g}h{cell:g}v{cell:g}h-{cell:g}z' for (cx, cy) in sorted(cells))
    return o.svg(cell, x, y) + f'<path d="{pink}" fill="{fill}" stroke="{edge}" stroke-width="{cell*0.1:g}"/>'

def big_c(t, cx, y, fp, **k):
    w, _ = big_dims(t, fp); return big_title(t, cx - w / 2, y, fp, **k)

def fit_fp(t, maxw, top=14):
    cells = text_grid(t)[1] * 2 + 2
    fp = int(2 * maxw / cells)
    fp -= fp % 2
    return max(4, min(top, fp))

# ---------------------------------------------------------------- shapes
def stair(x, y, w, h, c, fill):
    return (rect(x + 2*c, y, w - 4*c, h, fill) + rect(x + c, y + c, w - 2*c, h - 2*c, fill)
            + rect(x, y + 2*c, w, h - 4*c, fill))

def pill(x, y, w, h, c=5, sh=7, fill=WHITE, border=PURPLE, arrow=True):
    o = [stair(x + sh, y + sh, w, h, c, border), stair(x, y, w, h, c, border),
         stair(x + c, y + c, w - 2*c, h - 2*c, c, fill)]
    if arrow:
        a = G(); a.ascii(["#####", ".###.", "..#.."], {'#': border})
        o.append(a.svg(4, x + w - c - 28, y + h - c - 22))
    return "".join(o)

def pill_text(t, cx, y, w, h, px=3, **k):
    return pill(cx - w/2, y, w, h, **k) + ctext(t, cx, y + (h - 7*px) / 2, px)

def window(x, y, w, h, title="", bar=28, sh=14, body=WHITE):
    o = [rect(x+sh, y+sh, w, h, PURPLE), rect(x, y, w, h, BLACK), rect(x+3, y+3, w-6, h-6, body),
         rect(x+3, y+3, w-6, bar, BAR), rect(x+3, y+3+bar, w-6, 3, "#8E8E8E")]
    b = bar - 12
    for i in range(3):
        bx = x + w - 12 - (i + 1) * (b + 5) + 5
        o += [rect(bx, y+9, b, b, BLACK), rect(bx+2, y+11, b-4, b-4, LGRAY)]
    if title: o.append(text(title, x + 60, y + 3 + (bar - 14) / 2, 2))
    return "".join(o), (x + 3, y + 3 + bar + 3, w - 6, h - 6 - bar - 3)

def checker(x, y, cols, rows, s, col, first=0):
    return "".join(rect(x + i*s, y + j*s, s, s, col) for j in range(rows) for i in range(cols) if (i + j + first) % 2 == 0)

def spinner(cx, cy, r, d):
    cols = ["#111111", "#333333", "#555555", "#777777", "#999999", "#BBBBBB", "#CCCCCC", "#E0E0E0"]
    cols = ["#111111", "#2B2B2B", "#444444", "#5A5A5A", "#808080", "#A0A0A0", "#C4C4C4", "#999999"]
    o = []
    for i in range(8):
        a = math.radians(-90 + i * 45)
        px_, py_ = cx + r * math.cos(a), cy + r * math.sin(a)
        o.append(rect(round(px_ - d/2), round(py_ - d/2), d, d, cols[i]))
    return "".join(o)

# ---------------------------------------------------------------- sprites
def heart(O=PURPLE, P=PINK, W=WHITE):
    g = G()
    g.ascii([".OOO.OOO.", "OWPPOPPPO", "OWPPPPPPO", "OPPPPPPPO", ".OPPPPPO.", "..OPPPO..", "...OPO...", "....O...."],
            {'O': O, 'P': P, 'W': W}); return g
def heart_solid(col=PURPLE):
    g = G(); g.ascii([".##.##.", "#######", "#######", ".#####.", "..###..", "...#..."], {'#': col}); return g
def sparkle(col=PURPLE):
    g = G(); g.ascii(["...#...", ".......", "..###..", "#.###.#", "..###..", ".......", "...#..."], {'#': col}); return g

def butterfly():
    g = G(); L = ["..O.....", "...O....", ".....O..", ".OOOO.O.", "OPPPOPPO", "OPPOPPPO", "OOPPPPPO",
                  ".OOOPPOO", "..OPPOO.", ".OPPPPO.", ".OPPPO..", "..OOO..."]
    cen = [".", ".", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]
    for y, (l, c) in enumerate(zip(L, cen)):
        for x, ch in enumerate(l):
            col = {'O': PURPLE, 'P': PINK}.get(ch)
            if col: g.set(x, y, col); g.set(16 - x, y, col)
        if c == 'O': g.set(8, y, PURPLE)
    return g

def laptop(hearts=False):
    g = G()
    g.rect(2, 0, 23, 13, K); g.rect(3, 1, 22, 12, GREY); g.rect(5, 2, 20, 10, K)
    g.rect(6, 3, 12, 3, OFF); g.rect(6, 4, 10, 4, OFF); g.rect(6, 5, 8, 5, OFF)
    if hearts:
        for hx in (6, 11, 16):
            g.ascii([".P.P.", "PPPPP", "PPPPP", ".PPP.", "..P.."], {'P': PINK}, hx, 5)
    g.rect(1, 14, 24, 14, K); g.rect(0, 15, 25, 20, K); g.rect(1, 15, 24, 19, GREY)
    g.rect(4, 16, 11, 16, OFF); g.rect(14, 16, 21, 16, OFF); g.rect(3, 18, 5, 18, OFF); g.rect(19, 18, 22, 18, OFF)
    g.rect(9, 19, 16, 21, K); g.rect(10, 18, 15, 19, GREY)
    return g

def hourglass():
    g = G(); g.rect(0, 0, 13, 2, K); g.rect(1, 1, 12, 1, GREY)
    widths = [10, 9, 8, 7, 6, 5, 4, 3, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i, w in enumerate(widths):
        y = 3 + i; s = 7 - w // 2; e = s + w - 1
        g.set(s - 1, y, K); g.set(e + 1, y, K)
        for x in range(s, e + 1): g.set(x, y, GREY if (i >= 11 or i in (8, 9, 10)) else OFF)
    g.rect(0, 21, 13, 23, K); g.rect(1, 22, 12, 22, GREY); return g

def bubble(inner="heart"):
    g = G()
    for y in range(22):
        for x in range(22):
            if 9.0 <= math.hypot(x - 10.5, y - 10.5) <= 10.9: g.set(x, y, K)
    for p in [(6, 19), (6, 20), (7, 21), (8, 22), (9, 22), (9, 20), (8, 19)]: g.set(*p, K)
    g.ascii([".OOO.OOO.", "OWPPOPPPO", "OWPPPPPPO", "OPPPPPPPO", ".OPPPPPO.", "..OPPPO..", "...OPO...", "....O...."],
            {'O': "#A63D8F", 'P': HOT, 'W': "#FFD6EC"}, 7, 7)
    return g

def pin():
    g = G()
    g.ascii([".KKKKKKK..", "KWWGGGGGK.", "KWGGGGGGK.", "KGGGGGGGK.", ".KKGGGGKK.", "..KGGGGK..", "...KKKK..."],
            {'K': K, 'W': OFF, 'G': GREY})
    for i in range(7): g.set(5 + i, 7 + i, K); g.set(6 + i, 7 + i, K)
    return g

def cursor():
    g = G()
    g.ascii(["K..........", "KK.........", "KWK........", "KWWK.......", "KWWWK......", "KWWWWK.....", "KWWWWWK....",
             "KWWWWWWK...", "KWWWWWWWK..", "KWWWWWKKKK.", "KWWKWWK....", "KWK.KWWK...", "KK..KWWK...", "K....KWWK..",
             ".....KWWK..", "......KK..."], {'K': K, 'W': WHITE}); return g

def envelope():
    g = G()
    g.ascii(["OOOOOOOOOOOOO", "OPPPPPPPPPPPO", "OOPPPPPPPPPOO", "OPOOPPPPPOOPO", "OPPPOOOOOPPPO",
             "OPPPPPPPPPPPO", "OPPPPPPPPPPPO", "OOOOOOOOOOOOO"], {'O': PURPLE, 'P': PINK}); return g

def avatar():
    g = G(); col = "#D98FAE"
    for y in range(26):
        for x in range(30):
            if math.hypot(x - 14.5, y - 9) <= 7: g.set(x, y, col)
            if y >= 17 and ((x - 14.5) / 13) ** 2 + ((y - 28) / 11) ** 2 <= 1: g.set(x, y, col)
    return g

# ---------------------------------------------------------------- svg wrapper
def doc(w, h, body, label, bg=True):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}" role="img" aria-label="{label}" shape-rendering="crispEdges">'
            f'<title>{label}</title>' + (rect(0, 0, w, h, BG) if bg else "") + body + '</svg>')

def save(name, s, sub=""):
    d = os.path.join(OUT, sub); os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, name), "w") as f: f.write(s)

def slug(t): return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')

def b64img(path):
    ext = os.path.splitext(path)[1].lower().strip('.')
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp", "gif": "gif"}.get(ext, "png")
    with open(path, "rb") as f: return f"data:image/{mime};base64," + base64.b64encode(f.read()).decode()

def embed(path, x, y, w, h, cid):
    src = b64img(path)
    return (f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath>'
            f'<image href="{src}" xlink:href="{src}" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice" clip-path="url(#{cid})"/>')

# ---------------------------------------------------------------- pages
def hero():
    W, H = 1200, 675; o = []
    o.append(spr(laptop(), 10, 42, 140, -12))
    o.append(spr(bubble(), 5, 228, 14))
    o.append(spr(sparkle(), 5, 330, 150)); o.append(spr(sparkle(), 4, 292, 190))
    for (hx, hy) in [(850, 80), (938, 108), (880, 172)]: o.append(spr(heart_solid(), 5, hx, hy))
    o.append(spr(hourglass(), 7, 1030, 40, 12))
    o.append(checker(1090, 222, 5, 7, 30, PINK))
    o.append(ctext("SOFTWARE DEVELOPER", 630, 225, 5))
    o.append(big_c("KRISHNA", 600, 292, 14))
    o.append(pill(250, 452, 700, 112, c=6))
    o.append(ctext("BACKEND DEVELOPER | MERN STACK", 600, 480, 3))
    o.append(ctext("AI ENTHUSIAST", 600, 520, 3, PURPLE))
    wsvg, _ = window(42, 420, 190, 190, "", bar=22, sh=14); o.append(wsvg)
    o.append(spr(butterfly(), 6, 61, 470)); 
    for i in range(3): o.append(spr(heart(), 3, 74 + i * 34, 570))
    o.append(spinner(1100, 520, 36, 18))
    o.append(checker(290, 600, 6, 3, 26, MUTED))
    return doc(W, H, "".join(o), "Krishna - Software Developer. Backend Developer, MERN Stack, AI Enthusiast")

def thanks():
    W, H = 1200, 675; o = []
    o.append(spr(laptop(), 10, 42, 140, -12)); o.append(spr(bubble(), 5, 228, 14))
    o.append(spr(sparkle(), 5, 330, 150)); o.append(spr(sparkle(), 4, 292, 190))
    for (hx, hy) in [(850, 80), (938, 108), (880, 172)]: o.append(spr(heart_solid(), 5, hx, hy))
    o.append(spr(hourglass(), 7, 1030, 40, 12)); o.append(checker(1090, 222, 5, 7, 30, PINK))
    o.append(big_c("THANK", 600, 120, 16)); o.append(big_c("YOU!", 600, 262, 16))
    o.append(pill_text("LET'S BUILD SOMETHING AMAZING TOGETHER.", 600, 470, 780, 100, px=3, c=6))
    wsvg, _ = window(42, 420, 190, 190, "", bar=22, sh=14); o.append(wsvg)
    o.append(spr(butterfly(), 6, 61, 470))
    for i in range(3): o.append(spr(heart(), 3, 74 + i * 34, 570))
    o.append(spinner(1100, 520, 36, 18)); o.append(checker(290, 600, 6, 3, 26, MUTED))
    return doc(W, H, "".join(o), "Thank you! Let's build something amazing together.")

def decor(kind):
    o = []
    if kind == "about":
        o += [checker(0, 0, 5, 3, 36, PINK), spr(sparkle(), 7, 1040, 50), spr(sparkle(), 6, 960, 110)]
    elif kind == "expertise":
        o += [spr(sparkle(), 7, 150, 40), spr(sparkle(), 6, 80, 100), spr(laptop(True), 5, 1020, 60),
              checker(1140, 0, 2, 3, 36, MUTED)]
    elif kind == "p1":
        o += [spr(butterfly(), 8, 80, 60), checker(960, 0, 6, 2, 40, MUTED)]
    elif kind == "p2":
        o += [spr(heart(PURPLE, PURPLE, "#8A78AD"), 5, 50, 60), spr(heart(PURPLE, PURPLE, "#8A78AD"), 5, 100, 60),
              spr(heart(PURPLE, PURPLE, "#8A78AD"), 5, 150, 60), checker(1140, 0, 2, 7, 36, PINK)]
    elif kind == "p3":
        o += [spr(sparkle(), 7, 80, 50), spr(sparkle(), 6, 140, 90), checker(960, 0, 6, 2, 40, MUTED)]
    elif kind == "current":
        o += [spr(hourglass(), 7, 110, 20, 8), checker(0, 120, 3, 4, 36, PINK), spr(heart_solid(PINK), 7, 960, 60),
              spr(heart_solid(PINK), 6, 1030, 110), spinner(1110, 60, 30, 14)]
    elif kind == "tech":
        o += [spr(bubble(), 5, 70, 30), checker(1050, 0, 4, 3, 38, MUTED)]
    elif kind == "journey":
        o += [spr(sparkle(), 7, 110, 60), spr(sparkle(), 6, 60, 120), spinner(1100, 90, 36, 16),
              spr(heart_solid(PINK), 6, 940, 60)]
    elif kind == "contact":
        o += [rect(50, 50, 230, 64, PURPLE)] + [spr(sparkle(PINK), 6, 62 + i * 74, 60) for i in range(3)]
        o += [spr(butterfly(), 8, 980, 40)]
    return "".join(o)

def header(slug_, small, big, kind):
    W, H = 1200, 250
    fp = fit_fp(big, 960)
    body = decor(kind) + ctext(small, 600, 34, 6) + big_c(big, 600, 100, fp)
    return doc(W, H, body, f"{small} {big}".strip())

def nav_pill(label):
    px = 2; w = int(text_w(label, px) + 44)
    return doc(w + 8, 44, pill_text(label, (w) / 2, 2, w, 34, px=px, c=3, sh=4, arrow=False), label)

def start_button(label="START", w=300):
    h = 64
    o = [rect(8, 8, w, h, K), rect(10, 10, w - 4, h - 4, "#FFFFFF"), rect(12, 12, w - 8, h - 8, "#808080"),
         rect(12, 12, w - 10, h - 10, "#FFFFFF"), rect(14, 14, w - 12, h - 12, "#808080"), rect(14, 14, w - 14, h - 14, BAR)]
    o.append(ctext(label, 8 + w / 2 - 2, 8 + (h - 14) / 2, 2))
    o.append(spr(cursor(), 4, w - 28, 28))
    return doc(w + 40, h + 40, "".join(o), f"{label} button")

def category(label):
    w = int(text_w(label, 3) + 60)
    return doc(w + 12, 60, pill_text(label, w / 2 + 2, 2, w, 46, px=3, c=4, sh=6, arrow=False), label)

def chip(label):
    px = 2; w = int(text_w(label, px) + 26); h = 28
    body = stair(0, 0, w, h, 2, PURPLE) + text(label, 13, 7, px, PINK)
    return doc(w, h, body, label, bg=False)

def number(n):
    fp = 12; w, h = big_dims(n, fp)
    return doc(int(w + 16), int(h + 12), big_title(n, 8, 6, fp), f"Step {n}")

def divider():
    W, H = 1200, 56; o = [checker(0, 0, 100, 2, 12, PINK), checker(0, 32, 100, 2, 12, PINK, 1)]
    o.append(rect(420, 0, 360, 56, BG))
    for i, x in enumerate((452, 556, 660)): o.append(spr(heart(), 4, x + 20 if i == 1 else x, 10))
    o.append(spr(sparkle(), 4, 520, 14)); o.append(spr(sparkle(), 4, 668, 14))
    return doc(W, H, "".join(o), "Decorative pixel divider")

def window_bar(title):
    W = 1200; inner, _ = window(6, 6, W - 28, 40, title, bar=28, sh=0, body=BG)
    return doc(W, 52, inner.replace(f'fill="{BG}"', f'fill="{BG}"'), title)

def about_photo(photo=None):
    W, H = 560, 450; sv, (cx, cy, cw, ch) = window(30, 30, 500, 390, "ABOUT_ME.EXE")
    ax, ay, aw, ah = cx + 16, cy + 10, cw - 32, ch - 26
    body = sv + rect(ax, ay, aw, ah, PINK)
    if photo: body += embed(photo, ax, ay, aw, ah, "ph")
    else:
        body += spr(avatar(), 7, ax + (aw - 210) / 2, ay + 24) + ctext("YOUR PHOTO", ax + aw / 2, ay + ah - 52, 4, PURPLE)
    body += spr(pin(), 6, 4, 2)
    return doc(W, H, body, "Profile photo in a retro computer window")

def project_window(title, shot=None, n=1):
    W, H = 680, 480; sv, (cx, cy, cw, ch) = window(34, 34, 600, 400, title)
    ax, ay, aw, ah = cx + 16, cy + 10, cw - 32, ch - 26
    body = sv + rect(ax, ay, aw, ah, PINK)
    if shot: body += embed(shot, ax, ay, aw, ah, f"s{n}")
    else:
        body += ctext("PROJECT PREVIEW", ax + aw / 2, ay + ah / 2 - 40, 5, PURPLE)
        body += ctext("REPLACE WITH A SCREENSHOT", ax + aw / 2, ay + ah / 2 + 20, 3, PURPLE)
        body += spr(sparkle(), 5, ax + 40, ay + 30) + spr(sparkle(), 5, ax + aw - 80, ay + ah - 70)
    body += spr(pin(), 6, 6, 4)
    return doc(W, H, body, f"{title} preview in a retro computer window")

def contact_button(label, icon):
    W, H = 440, 84; o = [pill(8, 6, 400, 66, c=5, sh=7, arrow=True)]
    if icon == "mail": o.append(spr(envelope(), 4, 30, 24))
    else:
        o.append(rect(30, 20, 52, 40, PURPLE))
        o.append(ctext(">_" if icon == "gh" else "IN", 56, 30, 3, PINK))
    o.append(text(label, 104, 24, 4, BLACK))
    return doc(W, H, "".join(o), label)

# ---------------------------------------------------------------- build
HEADERS = [
    ("about", "INTRODUCTION", "ABOUT ME", "about"),
    ("expertise", "CORE", "EXPERTISE", "expertise"),
    ("project-1", "FEATURED PROJECT 01", "RESUME BUDDY", "p1"),
    ("project-2", "FEATURED PROJECT 02", "CONTENTHUB", "p2"),
    ("project-3", "FEATURED PROJECT 03", "DHOON", "p3"),
    ("tech", "MY TOOLBOX /", "TECH STACK", "tech"),
    ("journey", "MY DEVELOPER", "JOURNEY", "journey"),
    ("contact", "LET'S CONNECT /", "MY CONTACT", "contact"),
]
NAV = ["ABOUT", "EXPERTISE", "PROJECTS", "TOOLBOX", "JOURNEY", "CONTACT"]
CATS = ["LANGUAGES", "FRONTEND", "BACKEND", "DATABASES", "AI / INTEGRATIONS", "TOOLS"]
CHIPS = [
    "JavaScript", "TypeScript", "Python", "C / C++", "HTML", "CSS", "React", "React.js",
    "Tailwind CSS", "Bootstrap", "Node.js", "Express.js", "FastAPI", "Flask",
    "EJS", "MongoDB", "PostgreSQL", "SQL", "Groq API", "Groq VLM", "Ollama",
    "OpenAI-compatible APIs", "Whisper", "FFmpeg", "Rasterio", "JWT", "Multer",
    "Vite", "YouTube API", "Git", "GitHub", "Docker", "Postman", "VS Code",
    "Cloudinary", "MERN Stack", "Prisma"
]

def build_about_png(photo_path):
    try:
        from PIL import Image, ImageDraw, ImageOps
        S = 2
        W, H = 560 * S, 450 * S
        img = Image.new('RGBA', (W, H), BG)
        draw = ImageDraw.Draw(img)
        x, y, w, h = 30 * S, 30 * S, 500 * S, 390 * S
        bar = 28 * S
        sh = 14 * S

        draw.rectangle([x + sh, y + sh, x + sh + w, y + sh + h], fill=PURPLE)
        draw.rectangle([x, y, x + w, y + h], fill=BLACK)
        draw.rectangle([x + 3 * S, y + 3 * S, x + w - 3 * S, y + h - 3 * S], fill=WHITE)
        draw.rectangle([x + 3 * S, y + 3 * S, x + w - 3 * S, y + 3 * S + bar], fill=BAR)
        draw.rectangle([x + 3 * S, y + 3 * S + bar, x + w - 3 * S, y + 3 * S + bar + 3 * S], fill='#8E8E8E')

        b_size = bar - 12 * S
        for i in range(3):
            bx = x + w - 12 * S - (i + 1) * (b_size + 5 * S) + 5 * S
            by = y + 9 * S
            draw.rectangle([bx, by, bx + b_size, by + b_size], fill=BLACK)
            draw.rectangle([bx + 2 * S, by + 2 * S, bx + b_size - 2 * S, by + b_size - 2 * S], fill=LGRAY)

        g, _ = text_grid('ABOUT_ME.EXE')
        t_px = 2 * S
        tx = x + 60 * S
        ty = y + 3 * S + int((bar - 14 * S) / 2)
        for (cx, cy) in g.c:
            draw.rectangle([tx + cx * t_px, ty + cy * t_px, tx + (cx + 1) * t_px, ty + (cy + 1) * t_px], fill=BLACK)

        ax = (30 + 3 + 16) * S
        ay = (30 + 3 + 28 + 3 + 10) * S
        aw = (500 - 6 - 32) * S
        ah = (390 - 6 - 28 - 3 - 26) * S

        if photo_path and os.path.exists(photo_path):
            photo = Image.open(photo_path).convert('RGB')
            photo_fit = ImageOps.fit(photo, (aw, ah), centering=(0.5, 0.4))
            img.paste(photo_fit, (ax, ay))

        pin_g = pin()
        pin_px = 6 * S
        pin_ox, pin_oy = 4 * S, 2 * S
        for (cx, cy), col in pin_g.c.items():
            draw.rectangle([pin_ox + cx * pin_px, pin_oy + cy * pin_px, pin_ox + (cx + 1) * pin_px, pin_oy + (cy + 1) * pin_px], fill=col)

        out_png = os.path.join(OUT, "about-photo.png")
        img.save(out_png, optimize=True)
    except Exception as e:
        print("Could not build PNG:", e)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--photo"); ap.add_argument("--shot1"); ap.add_argument("--shot2"); ap.add_argument("--shot3")
    a = ap.parse_args()

    default_photo = os.path.join(OUT, "krishna-photo.jpg")
    photo_file = a.photo if a.photo else (default_photo if os.path.exists(default_photo) else None)

    save("hero.svg", hero()); save("thanks.svg", thanks()); save("divider.svg", divider())
    for n, s, b, k in HEADERS: save(f"header-{n}.svg", header(n, s, b, k))
    for n in NAV: save(f"nav-{slug(n)}.svg", nav_pill(n), "nav")
    save("start.svg", start_button("START")); save("top.svg", start_button("BACK TO TOP", 380))
    for c in CATS: save(f"cat-{slug(c)}.svg", category(c), "cats")
    for c in CHIPS: save(f"chip-{slug(c)}.svg", chip(c), "chips")
    for i in range(1, 6): save(f"num-0{i}.svg", number(f"0{i}"), "nums")
    save("window-stats.svg", window_bar("GITHUB_STATS.EXE"))
    save("about-photo.svg", about_photo(photo_file))
    build_about_png(photo_file)
    save("resume-buddy-preview.svg", project_window("RESUME_BUDDY.EXE", a.shot1, 1))
    save("contenthub-preview.svg", project_window("CONTENTHUB.EXE", a.shot2, 2))
    save("dhoon-preview.svg", project_window("DHOON.EXE", a.shot3, 3))
    save("btn-github.svg", contact_button("GITHUB", "gh"), "contact")
    save("btn-linkedin.svg", contact_button("LINKEDIN", "in"), "contact")
    save("btn-email.svg", contact_button("EMAIL", "mail"), "contact")
    print("done ->", os.path.abspath(OUT))
