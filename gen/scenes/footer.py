"""Footer: the portfolio's CONTINUE? screen with a countdown, a coin slot and
the render stamp."""

import datetime as dt

from ..svg import GOLD2, LN, Doc, panel, rect, spans, text, tw

W, H = 1000, 176

COIN = [  # 10×10
    "...####...",
    ".##$$$$##.",
    ".#$$##$$#.",
    "#$$#$$#$$#",
    "#$$#$$$$$#",
    "#$$#$$$$$#",
    "#$$#$$#$$#",
    ".#$$##$$#.",
    ".##$$$$##.",
    "...####...",
]


def coin(x, y, s):
    cols = {"#": "#8A6A1E", "$": GOLD2}
    return "".join(rect(x + c * s, y + r * s, s, s, cols[ch])
                   for r, line in enumerate(COIN) for c, ch in enumerate(line) if ch in cols)


def render(cfg, data, path):
    now = dt.datetime.now(dt.timezone.utc)
    doc = Doc(W, H, "Obrigado pela visita", f"Rodapé: CONTINUE? com contagem regressiva. Renderizado em {now:%Y-%m-%d %H:%M} UTC.")
    doc.style(
        ".dg{animation:cd 10s steps(1,end) infinite;opacity:0}.dg9{opacity:1}"
        "@keyframes cd{0%{opacity:1}10%,100%{opacity:0}}"
        ".blink{animation:blink 1.1s steps(1,end) infinite}@keyframes blink{60%{opacity:0}}"
        ".spin{animation:spin 1.2s steps(4,end) infinite;transform-origin:905px 62px}"
        "@keyframes spin{50%{transform:scaleX(.25)}}"
    )
    doc.add(panel(0, 0, W, H))

    x, y = 40, 74
    doc.add(text(x, y, "CONTINUE?", "jp gold2", 40))
    cx = x + 40 * 0.5 * 9 + 26  # DotGothic16 Latin glyphs are half-width
    for i, d in enumerate(range(9, -1, -1)):
        cls = "dg dg9" if d == 9 else "dg"
        doc.add(f'<g class="{cls}" style="animation-delay:{i}s">{text(cx, y, str(d), "jp tx", 40)}</g>')
    thanks = cfg["footer"]["thanks"]
    doc.add(spans(x + 2, y + 34, [(thanks, "mut"), ("  ·  ", "faint"), ("thanks for visiting", "mut"), ("  ·  ", "faint")], 13),
            text(x + 2 + tw(thanks + "  ·  thanks for visiting  ·  ", 13), y + 34, "ありがとう", "jp mut", 14))

    # coin slot
    doc.add(f'<g class="spin">{coin(875, 32, 6)}</g>',
            text(905, 120, "INSIRA UMA FICHA", "jp gold blink", 16, anchor="middle"))

    # render stamp
    doc.add(f'<path d="M1 {H - 40.5}H{W - 1}" stroke="{LN}"/>')
    stamp = [("renderizado ", "faint"), (f"{now:%Y-%m-%d %H:%M} UTC", "dim"), (" · ", "faint"),
             ("atualizado todo dia via GitHub Actions", "dim"), (" · ", "faint"), ("só SVG, sem JavaScript", "dim"),
             (" · ", "faint"), (cfg["footer"]["credits"], "gold")]
    doc.add(spans(20, H - 15, stamp, 11), text(W - 20, H - 15, "↑↑↓↓←→←→BA", "faint", 11, anchor="end"))
    doc.save(path)
