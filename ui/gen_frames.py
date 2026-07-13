#!/usr/bin/env python3
"""CornQuest UI kit — 9-slice pixel frame generator (lens-A palette discipline).

Produces honest, hard-cornered pixel frames on the token palette. These are
PLACEHOLDERS the O4 art pack upgrades later, but must look decent now.

Design: 12x12 "logical" pixel grid scaled 4x -> 48x48 device px canvas.
Border ring = 4 logical px (=16 device px) => border-image slice of 16.
The 4x4 center is TRANSPARENT so the CSS background token (--stone / material
fill) shows through even when the Frame uses `border-image ... fill`.

Ring layout (d = distance to nearest edge, 0=outermost):
  d0  outer outline (darkest)
  d1  bevel: highlight on the upper-left diagonal, shadow on lower-right
  d2  base border colour
  d3  inner outline (one step darker than fill), touches transparent centre

Light source fixed top-left 45deg (lens-A rule 6).
"""
from PIL import Image

N = 12          # logical grid
S = 4           # scale -> 48x48
SIZE = N * S

# palette: (outline, base, light, dark, inner)  RGB tuples
PALETTES = {
    "frame-parchment": {
        "outline": (74, 54, 30),
        "base":    (150, 120, 66),
        "light":   (232, 214, 150),
        "dark":    (120, 92, 48),
        "inner":   (96, 74, 40),
        "stud":    (217, 166, 59),   # harvest-gold corner accents
    },
    "frame-dark": {
        # night-purple-leaning stone (lens-A: shadows pull toward night-purple)
        "outline": (12, 10, 20),
        "base":    (58, 54, 82),
        "light":   (86, 80, 120),
        "dark":    (30, 28, 46),
        "inner":   (22, 20, 34),
        "stud":    (120, 110, 150),
    },
    "frame-gold": {
        "outline": (90, 64, 20),
        "base":    (217, 166, 59),
        "light":   (242, 202, 99),
        "dark":    (138, 101, 32),
        "inner":   (110, 80, 26),
        "stud":    (255, 240, 190),
    },
}


def build(pal):
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    px = img.load()
    for gy in range(N):
        for gx in range(N):
            d = min(gx, gy, N - 1 - gx, N - 1 - gy)
            if d >= 4:
                col = None                       # transparent centre
            elif d == 0:
                col = pal["outline"]
            elif d == 1:
                # diagonal bevel: upper-left lit, lower-right shadowed
                col = pal["light"] if (gx + gy) < (N - 1) else pal["dark"]
            elif d == 2:
                col = pal["base"]
            else:  # d == 3
                col = pal["inner"]
            # corner studs: brighten the 4 outermost corner cells
            if (gx, gy) in ((0, 0), (N - 1, 0), (0, N - 1), (N - 1, N - 1)):
                col = pal["stud"]
            if col is None:
                continue
            for oy in range(S):
                for ox in range(S):
                    px[gx * S + ox, gy * S + oy] = (col[0], col[1], col[2], 255)
    return img


if __name__ == "__main__":
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    for name, pal in PALETTES.items():
        out = os.path.join(here, name + ".png")
        build(pal).save(out)
        print("wrote", out)
