# Focused card grid replaces the icon wall and 3D graph

Supersedes the About, Stack and Card layout in ADR 0001. The nine-category icon wall took more of the Profile than it earned now that tools change quickly and agents do much of the typing. The isometric graph and the profile-details chart repeated the contribution calendar GitHub already shows on the page.

Below Connect, the Profile is five Cards: About and Core stack, languages and summary, then the streak as a full-width strip. About is the animated card from `github-cool-readme`. Core stack lists twelve tools taken from what recent repositories actually use. Everything uses muted Catppuccin Mocha, including the language colours, which are assigned by rank.

**Considered Options**: trimmed skillicons rows; keeping the 3D graph; GitHub's Primer colours with light and dark variants; a weekly-rhythm Card; a notable-contributions Card, which had one entry.

**Consequences**: The generator has no Catppuccin theme, so `scripts/catppuccin.py` recolours its output and stops the workflow on any unmapped colour. Core stack is a static SVG in `assets/`, edited by hand when the regular tools change. Summary, languages and About come from the `Update README cards` workflow and need the `CARDS_TOKEN` secret, and About's copy lives in `cool-readme.yml`. The streak stays on its existing deployment. The wide strip scales down on phones.
