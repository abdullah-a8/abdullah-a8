#!/usr/bin/env python3
"""Recolour the generated README cards to Catppuccin Mocha, in place.

Usage: catppuccin.py CARDS_DIR

Exits with an error on any colour it doesn't recognise, so the workflow stops
before publishing a card that has drifted off the palette.
"""
import re
import sys
from pathlib import Path

# The card generator's dark theme with `color: purple`, mapped to Mocha.
THEME = {
    "#f0f6fc": "#bac2de",  # text -> subtext1
    "#9198a1": "#a6adc8",  # secondary -> subtext0
    "#7d8590": "#7f849c",  # muted -> overlay1
    "#3d444d": "#313244",  # border, ring track -> surface0
    "#6e7681": "#6c7086",  # neutral, "Other" -> overlay0
    "#a371f7": "#cba6f7",  # accent -> mauve
}
BASE = "#1e1e2e"
# GitHub's language colours are replaced by rank, most used first.
LANGUAGES = ["#cba6f7", "#b4befe", "#89b4fa", "#74c7ec", "#94e2d5"]
PALETTE = {BASE, *THEME.values(), *LANGUAGES}

# Six digits only: the language bar's mask uses #fff and must stay white.
HEX = re.compile(r"#[0-9a-fA-F]{6}\b")


def recolour(path: Path) -> str:
    assigned: dict[str, str] = {}

    def swap(match: re.Match[str]) -> str:
        colour = match.group().lower()
        if colour in THEME:
            return THEME[colour]
        if colour in PALETTE:
            return colour
        if colour in assigned:
            return assigned[colour]
        if path.name.startswith("languages-") and len(assigned) < len(LANGUAGES):
            assigned[colour] = LANGUAGES[len(assigned)]
            return assigned[colour]
        sys.exit(f"error: {path.name} uses {colour}, which has no Catppuccin Mocha mapping")

    return HEX.sub(swap, path.read_text(encoding="utf-8"))


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    cards = sorted(Path(sys.argv[1]).glob("*.svg"))
    if not cards:
        sys.exit(f"error: no cards in {sys.argv[1]}")
    # Recolour everything before writing, so a failure leaves no half-converted set.
    recoloured = [(card, recolour(card)) for card in cards]
    for card, svg in recoloured:
        card.write_text(svg, encoding="utf-8")
    print(f"Recoloured {len(cards)} cards to Catppuccin Mocha")


if __name__ == "__main__":
    main()
