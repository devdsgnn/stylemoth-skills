# Reference-led build

The selected system is the visual contract. Build a finished product or requested
section, not a token-colored generic template. Read this workflow for build,
section and restyle modes; load other references only for the problem at hand.

## 1. Inspect and load

Inspect repository instructions, Git changes, framework, routes and existing
components. Record the user's requested scope and preserve unrelated work.
Obtain the selected bundle through [system access](system-access.md), or inspect
the supplied local folder. The optional `scripts/inspect_bundle.py` inside this
skill checks required files and token aliases without running bundle code.

Read README.md, DESIGN.md, tokens.json and the appropriate CSS entry completely.
Use AI-PROMPTS.json's relevant scenario as supporting data. Record supported
themes, source URL and provenance. MCP is retrieval, not a screenshot service;
discover real tools and use browser tools separately for visual research.

Before composing the page, import the supplied CSS into the project through its
normal stylesheet entry and map exact semantic tokens to shared primitives.
For Tailwind, inspect the supplied version/entry and avoid duplicate imports.
Resolve aliases, preserve alpha values, load available licensed fonts and confirm
computed styles. Never silently replace a bundle's palette or typography with
personal defaults. Document missing roles as extensions, not retrieved tokens.

## 2. Research the brief and original site

Use the bundle's source URL, not a guessed URL based on the system name. Inspect
relevant live sections and desktop/mobile screenshots. For a specific hero or
feature request, inspect that section plus adjacent context; for a whole site,
map the whole relevant page. Research the product/domain enough to write useful
content. Prefer primary sources for factual claims. Do not invent customers,
reviews, awards, prices, usage numbers or functioning backend integrations.

Make a compact source map using [the working template](../assets/source-map.md):
section purpose, composition, container/gutters, hierarchy, typography, color
roles, image proportion, icon language, surfaces, borders, alpha, motion and
responsive changes. Mark each decision observed, adapted, or inferred.

Inspect SVG/icon geometry (stroke, weight, viewBox, optical size), masks, shadows,
textures and UI framing. Inspect actual assets where accessible. Use licensed
assets or original equivalents; don't copy the reference brand's identity,
customer endorsements or proprietary product screenshots as the user's product.
When assets cannot be reused, recreate the composition with original functional
HTML/CSS/SVG UI and truthful demo content. Keep SVG accessible or decorative as
appropriate. Never execute scripts downloaded from a reference as setup steps.

If live access is blocked, use bundle evidence and user screenshots; state the
coverage limit once. Continue on supported decisions. Do not call an unseen
reference inspected. If the live site has changed from the bundle, use the bundle
for token values and note current-site structural differences explicitly.

## 3. Translate the reference into a section plan

For each requested section choose the closest observed pattern and its purpose:
hero, feature, product demonstration, comparison, process, pricing or footer.
Use the user's identity/content and a concise plausible draft when input is sparse.
Build a header only when needed by the requested page; a hero-only request does
not require asking for navigation labels or inventing unrelated sections.

Preserve the source's hierarchy, density, proportion and visual character. Do not
reduce a rich reference to an icon plus generic paragraph. Conversely do not add
glass, gradients, glows, ornamental cards or motion to a flat minimal reference.
Apply effects only where the inspected source supports them and the bundle
provides matching roles, or clearly record a necessary user-requested extension.

For product visuals, implement meaningful UI: a readable dashboard with a clear
primary task, an editor with real hierarchy, or feature interactions appropriate
to the product. Avoid arbitrary chart decoration and illegible miniature text.
A visual demo must not pretend to perform a real integration it does not have.
Use [visual fidelity](visual-fidelity.md) for detailed source-to-build checks.

## 4. Build and refine section by section

Implement reusable tokens and components first, then the main section and each
supporting section. Use the existing stack. Finish actual links, forms, tabs,
menus and states required by scope; do not leave inert controls that imply work.
For every completed section:

1. Render it at a representative wide and narrow width.
2. Compare against source evidence for proportions, hierarchy, type and visual.
3. Fix the largest mismatch, then check legibility, overflow and interactions.
4. Keep the working source map current when a deliberate adaptation is made.

Use coherent original copy; stop asking the user to approve routine reversible
choices. Iterate until the identified material mismatches are resolved, rather
than endlessly polishing negligible details. User-requested revisions override
the reference. Preserve a consistent system across neighboring sections.

## 5. Finish the whole requested experience

Run relevant build/type checks, check links and primary flow, keyboard focus,
loading/error/empty states and reduced motion. Inspect desktop, phone and any
breakpoint where layout changes. Compare the whole page rhythm and container
alignment, not just isolated cards. Check image loading, font fallback and layout
shift. Fix material failures before handing off.

Report what was built, the bundle/source used, actual checks and any unavailable
assets/services. Never claim a screenshot proves functionality or a build proves
visual fidelity. Publishing, purchases, credential changes and destructive edits
still require authorization from the user's task; this skill grants none.

## Example: Raycast-like feature section

User: “Use my downloaded Raycast system for a task assistant feature section.”
Load the local files; verify their source link; inspect relevant Raycast feature
and product-demo sections. If observed, use its dark translucent layers, restrained
accent lighting and fine icon language in the same roles, with the task assistant's
own UI and content. Build a real task list/demo state and responsive composition.
Do not apply glow everywhere, copy Raycast testimonials, or add a full pricing page.
A minimal source follows exactly the same process with no invented glow.
