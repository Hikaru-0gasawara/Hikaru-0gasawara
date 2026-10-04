"""Contribution streaks: total, current (with a pixel flame) and longest."""

import math

from ..svg import GOLD, GOLD2, LN, PN, PN2, RED, Doc, date_pt, label, num, panel, rect, text

W, H = 495, 250

FLAME = [  # 9×11 pixel flame: 1 outer, 2 inner, 3 core
    "....1....",
    "...11....",
    "...121...",
    "..1221...",
    ".112221..",
    ".1223211.",
    "11233321.",
    "12333321.",
    "12333221.",
    ".122221..",
    "..1111...",
]


def span(a, b, today):
    if not a:
        return "—"
    if b == today:
        return f"{date_pt(a, a.year != today.year)} – hoje"
    same = a.year == b.year
    return f"{date_pt(a, not same)} – {date_pt(b)}"


def flame(x, y, s):
    cols = {"1": RED, "2": GOLD, "3": GOLD2}
    return "".join(rect(x + c * s, y + r * s, s, s, cols[ch])
                   for r, line in enumerate(FLAME) for c, ch in enumerate(line) if ch in cols)


def render(cfg, data, path):
    today = data["today"]
    cur, best = data["streak_cur"], data["streak_best"]
    doc = Doc(W, H, "GitHub — sequência de contribuições",
              f"Total {num(data['contrib_total'])}; sequência atual {cur} dias; maior sequência {best} dias.")
    doc.style(".ring{animation:ring 1.2s cubic-bezier(.2,.8,.2,1) .3s backwards}"
              "@keyframes fl{50%{transform:scaleY(1.08)}}")
    doc.add(panel(0, 0, W, H, "Sequência", f"desde {date_pt(data['first_contrib'])}"))

    cols = [W / 6, W / 2, W * 5 / 6]
    doc.add(f'<path d="M{W / 3:.1f} 58V{H - 22}M{2 * W / 3:.1f} 58V{H - 22}" stroke="{LN}"/>')

    # total
    x = cols[0]
    doc.add(text(x, 140, num(data["contrib_total"]), "tx b", 30, anchor="middle"),
            label(x, 168, "contribuições", anchor="middle"),
            text(x, 190, span(data["first_contrib"], today, today), "dim", 11, anchor="middle"))

    # current, inside a ring that fills by day of week (a week = full ring)
    x, cy, r = cols[1], 136, 44
    circ = 2 * math.pi * r
    frac = min(cur / 7, 1)
    fy = cy - r - 20
    doc.style(f"@keyframes ring{{from{{stroke-dashoffset:{circ:.1f}}}}}"
              f".fl{{animation:fl 1.6s steps(2,end) infinite;transform-origin:{x:.1f}px {fy + 33}px}}")
    doc.add(f'<circle cx="{x}" cy="{cy}" r="{r}" fill="{PN2}" stroke="rgba(232,228,212,.08)" stroke-width="6"/>',
            f'<circle class="ring" cx="{x}" cy="{cy}" r="{r}" fill="none" stroke="{GOLD2}" stroke-width="6" '
            f'stroke-dasharray="{circ:.1f}" stroke-dashoffset="{circ * (1 - frac):.1f}" transform="rotate(-90 {x} {cy})"/>',
            f'<rect x="{x - 20}" y="{cy - r - 18}" width="40" height="30" fill="{PN}"/>',
            f'<g class="fl">{flame(x - 13.5, fy, 3)}</g>',
            text(x, cy + 11, str(cur), "gold2 b", 32, anchor="middle"),
            label(x, cy + r + 30, "sequência atual", "gold", anchor="middle"),
            text(x, cy + r + 52, span(*data["streak_cur_range"], today) if cur else "começa no próximo commit",
                 "dim", 11, anchor="middle"))

    # longest
    x = cols[2]
    a, b = data["streak_best_range"]
    doc.add(text(x, 140, num(best), "tx b", 30, anchor="middle"),
            label(x, 168, "maior sequência", anchor="middle"),
            text(x, 190, span(a, b, today), "dim", 11, anchor="middle"))
    doc.save(path)
