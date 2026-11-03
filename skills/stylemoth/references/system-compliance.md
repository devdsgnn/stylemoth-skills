# Selected-system compliance

Use this alongside reference-build for builds, sections, restyles and refinements
with a selected system. For a small correction, apply only the affected rules.
This is a working implementation contract, not additional copy in the product UI.

## Establish authority before composing

The user's explicit request controls scope and overrides. Within that scope,
explicit bundle usage rules control implementation; source-site inspection fills
missing visual detail. General design advice and other websites do not override
either. If a live source differs from the exported version, keep the bundle's
explicit rules and note the difference. If bundle files contradict one another,
record the conflict and choose the most specific applicable component/state rule;
ask only when the conflict prevents a meaningful implementation.

A requested red-to-blue substitution changes brand roles and their related alpha
variants, not neutral surfaces, spacing, typography, density or component structure.
A requested new hero background permits research for that background, not a new
visual language for every feature card. Track each override with its scope.

## Extract usage, not just values

Before composing a substantial selected-system UI, create a compact working rule
map from DESIGN.md, tokens.json and the CSS entry point. Read token descriptions,
usage groups, aliases, responsive variants and source conditions, not just $value.
Include applicable space/layout, radiusUsage, shadowUsage, type, colors and motion.
Do not assume every bundle uses the same schema or token names.

| Role / component | Source path + usage instruction | Wide / narrow value | Implementation binding | Verification |
| --- | --- | --- | --- | --- |
| Actual role | Exact file and token/rule; preserve qualifications | Resolved values and conditions | Shared variable, selector or component prop | Measured or unverified |

Map page maximum width, outer gutters, section separation, heading-to-content gap,
card insets, grid/row gaps, control insets, type roles and content measure where
specified. An allowed value is not interchangeable with another allowed value:
using a grid-gap token for panel padding is a failure even if both are on the scale.
Respect terms such as “only”, “occasional”, “compact” and mobile exceptions.
For example, if a bundle says panel inset 24px / mobile 16px and story gap 96px /
mobile 48px, implement those roles exactly; those numbers are not universal defaults.
If a breakpoint or role is absent, make a minimal documented inference using the
existing project/source pattern. Do not invent a retrieved rule or silently replace
an explicit rule with a framework default, convenient utility or optical adjustment.

## Match the reference's composition and content

Inspect the selected source's relevant feature sections, not only its hero. For
each distinct section/card family, record the closest source section and its:
- title, description and action placement;
- text measure, line count/density and relative type hierarchy;
- media-to-copy proportion, icon size/style, crop and alignment;
- surface layers, borders, transparency, lighting and motion, including absences.

Use these as a blueprint for original product content and functional UI. Do not
substitute a generic icon/title/body card for a source's rich product demonstration,
or import another website's card because it looks attractive. Additional sources
may verify product facts or fill a genuinely missing pattern; document the gap and
translate that pattern into the selected system. Do not create a visual collage.
If source inspection is blocked, use available bundle/screenshots and identify the
unverified card details; do not claim fidelity to unseen elements.

For a minimal source, preserve low information density, few visual layers, quiet
surfaces and restrained actions. Empty space is intentional; do not fill it with
badges, nested panels, labels or decoration. For a content-led source, preserve its
reading order, paragraph/list hierarchy, useful detail and readable line length;
do not compress it into decorative microcopy. Follow explicit content guidance
before inferred word/line budgets. Adapt copy to the product without invented
metrics, testimonials or claims. Preserve user-supplied content unless editing it
is authorized. Use layout and hierarchy, not smaller type, to resolve crowding.

## Verify before repeating the pattern

Implement one representative feature card/section first. Compare its actual render
with the source and rule map at wide and narrow widths before propagating it.
Inspect computed styles for padding on each side, gaps, max-width, actual font
family/weight/line-height, radius and surface/alpha roles. Check effective distances:
stacked margins, parent padding and child gaps can double spacing even when each
individual declaration uses a valid token. Check font loading and CSS cascade.

Correct mismatches in shared primitives and recheck affected variants. Explicit
numeric role rules must match the resolved values at their stated conditions;
allow only browser rounding, a recorded user override, or a necessary documented
accessibility/responsive exception. Do not hide a mismatch behind “looks close”.
Visual judgment remains necessary for composition, density and source character.

Before handoff, audit every distinct section family, repeated components and
changed responsive states against the map. Record expected versus observed values
and screenshot/source evidence for material checks. Mark each rule verified,
exception (with reason), or unverified. Do not call the result system-compliant
while unexplained deviations remain. If browser tools are unavailable, inspect
source/CSS and explicitly report that rendered compliance remains unverified.
A build passing, a valid token file, or a source list alone is not this check.
