# Interface craft

Use the selected system's actual values. These are decision criteria, not a preset.

## Color roles

Map surfaces, content, boundaries, controls, and feedback to semantic roles.
Essential text should be strongest, descriptions quieter, and decoration less
demanding than the action. Do not make important information faint to create hierarchy.
Check alpha colors against the actual background, including images and stacked surfaces.

Reuse existing scales rather than adding a near-duplicate shade per component.
If a role is missing, define a named extension and check its real color pairs.
Decorative colors and semantic states have different jobs. An accent need not
appear on every icon, underline, selected state, and button.

Target at least 4.5:1 contrast for normal text and 3:1 for large text. Check relevant
control boundaries and focus indicators at 3:1 against adjacent colors. Numerical
checks supplement, rather than replace, inspecting the rendered interface.

## Responsive typography

Use roles for display, headings, body, descriptions, labels, and code. Apply family,
weight, size, line-height, and tracking together. Intermediate weights require a
font that supports the requested axis/range; do not globally apply 450 because
one previous product used it.

Use normal text for descriptions and examples. Reserve code pills for syntax,
token names, and precise technical values. A font size printed inside a token
table is data, not an instruction to resize that table to the displayed value.

Prefer content-driven wrapping. Use an explicit break for intentionally composed
headings, then verify narrower widths. Avoid an unbreakable heading that overflows
on phones. Keep paragraph measures comfortable on wide screens.

Do not blindly shrink every phone font. Check input zoom, browser text resizing,
long labels, and readable controls. Shorten copy or reflow before shrinking essential
text below the system's readable minimum.

## Spacing and surfaces

Define page gutters, section gaps, heading-to-content gaps, container padding, and
related-item gaps separately. A smaller card inset must not reduce the page's
section separation. Use sibling grid/flex gaps and predictable heading margins.
Inspect margin collapse, min-height, and inherited paragraph margins before
adding compensating padding.

Use shared outer containers; make a narrow FAQ or reading column an explicit
variant. Do not align sections by stretching all code panels or every card to
the largest width. Equal siblings can use grid stretch without large fixed heights.

Density follows the job. Generous section gaps can coexist with compact rows and
bullets. Shadows express elevation rather than outline every panel. Choose radii
by role; inset corners should fit their parent geometry.

## Appropriate structure

- Landing pages: offer, relevant evidence, next action. Remove repeated explanations.
- Dashboards: retain useful density, navigation, filters, comparable data, units,
  and labels. Mark sample metrics as examples, not customer results.
- Tables: keep comparisons aligned. On mobile use labeled stacked records for
  independent items, or contained scrolling for cross-column comparison. Preserve
  column relationships; never hide essential values just to prevent overflow.
- Code: separate line-number gutter from code, with enough inset at corners. Wrap
  prose-like Markdown when useful; use local scrolling when syntax needs it.
- Cards: one purpose, consistent inset, clear destination when clickable. Static
  rows do not need hover decoration. Interactive cards need keyboard focus.

## Media, icons, motion

Media should show something words cannot: a product surface, useful example, or
subject-specific story. Preserve aspect ratio, crop intent, and source treatment.
Reference imagery is not automatically licensed for reuse. Use supplied/authorized
assets or clearly framed placeholders when final assets are missing. Do not fill
space with fake screenshots full of unreadable miniature UI.

Use compatible icons with consistent optical size and stroke. Brand marks remain
distinct from interface icons. Label icon-only controls accessibly; tooltips cannot
be the only way to understand an essential action.

Animate state changes when it helps people follow them. Accordions should expand
layout smoothly without forced scrolling. Auto-playing carousels need pause and
reduced-motion behavior. Repeating tracks must cover the viewport throughout a
loop, without a blank tail. Avoid perpetual motion around body text and controls.

Polish is not a mandatory list of effects. Keep the primary task and content clear.

For icon provenance, library selection, implementation, and validation, follow
[Icon research and implementation](icons.md).
