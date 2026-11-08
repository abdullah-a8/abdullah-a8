# GitHub Profile

The public README at `abdullah-a8/abdullah-a8`. It is the eight-second scan surface for hiring managers and engineers; `abdullahamin.dev` is the long read.

## Language

**Profile**:
The GitHub README. Hiring-manager scan lives in the Hero, Connect, and About. Engineer depth lives in the Stack and Cards.
_Avoid_: portfolio, site, resume

**Hero**:
The top of the Profile. The typing SVG greeting is the only hero; there is no name heading. Lines are `Hi, I'm Abdullah` and `I love building software`, centered, JetBrains Mono at size 35, no emojis.
_Avoid_: banner, identity rotator, name H1, title case on line 2

**Connect**:
The contact row directly under the Hero, with no section heading. Two-tone for-the-badge shields in muted Catppuccin Mocha: surface1 label with a mauve icon, surface0 value. Email, LinkedIn, and Portfolio, each showing the destination.
_Avoid_: skillicons, custom email SVG, Material Blue, a Connect heading, solid single-color shields, bright teal or mauve fills

**About**:
The animated About Card. A headline from the site copy, lines that scroll, and facts that take turns with current focus: retrieval and RAG, LLM pipelines, computer vision, systems programming. Durable copy with no employer and no job title. The headline does not repeat the Hero's greeting.
_Avoid_: a Markdown About section, two-column table, process essay, Qult, current role, `Hi, I'm Abdullah` as the headline

**Stack**:
The Core stack Card: twelve regularly used tools in a four-by-three box, taken from recent repositories. A static SVG at `assets/stack.svg`.
_Avoid_: the nine-category icon wall, skillicons, listing everything ever used

**Card**:
A widget on the Profile. The set is About, Core stack, languages, and summary in two rows at 400×195, with the streak as a full-width strip beneath them. Every Card uses muted Catppuccin Mocha on a base panel with no border: subtext for text, surface for lines, mauve as the accent. The same Cards show on light and dark pages. `scripts/catppuccin.py` recolours the generated ones.
_Avoid_: isometric contribution graph, profile-details, trophy, GitHub Trophy, productive-time, most-commit-language, GitHub language colours, tokyonight, radical
