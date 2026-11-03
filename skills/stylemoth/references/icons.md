# Icon research and implementation

Run this as part of reference research and implementation, without a separate
user request. User-specified libraries override the default selection order.

## Identify the reference's library

Inspect bundle documentation, dependency manifests, imports, and asset credits.
When live inspection is available, look for library-specific markup, SVG metadata,
asset URLs, and the website's official source repository. Record the evidence
that identifies the family and its variant: outline, solid, duotone, or another
documented treatment. Visual resemblance alone does not establish provenance.

Check the library's official license and the particular icon set/version. Free to
view or download does not necessarily mean permitted for commercial reuse. Retain
required notices and attribution. Do not extract proprietary icons from a website
or use a paid set without an appropriate license.

For screenshots or inaccessible sources, note that provenance is unverified.
After a focused check, proceed with the fallback rather than stalling the build
or claiming the reference uses a library you could not identify.

## Selection order

1. The reference website's verified icon library, when its license permits the
   intended reuse and it can be used in the project's stack.
2. Lucide, using its official framework package or distributed SVG assets.
3. Heroicons if Lucide is unavailable or cannot supply a suitable icon/variant.
4. Another maintained, reuse-permitted library if neither fits; record why.

Verify the chosen package and license from official sources during implementation.
Use one coherent family for interface icons. Resolve a missing symbol with a
semantic alternative from that family before mixing sets. Match the reference's
optical weight, stroke, size, fill, and color roles using supported properties.
Do not add decorative icons where the reference calls for text or open space.

## Implement from the library

Use official components and named imports for the actual framework; import only
the icons needed. In a plain HTML project, use official distributed SVGs with the
required notices. Library SVG markup is allowed; hand-authored or redrawn paths,
AI-generated UI icons, CSS-drawn icon substitutes, emoji, and Unicode stand-ins
are not the default. Never recreate a library icon from a screenshot.

Centralize shared icon size/stroke/color rules. Keep icon-only controls accessible
with a meaningful name and an adequate hit area; hide decorative icons from
assistive technology. Do not use a tooltip as the only accessible label.

Brand logos and product illustrations are separate assets, not interface icons.
Preserve authorized authentic logos; do not replace them with generic library
symbols or redraw them under this policy.

## Review and handoff

Keep a compact implementation note: reference evidence or unknown provenance,
chosen library/package, official license source, variant, and any fallback reason.
Check that every added interface icon comes from the selected library, renders
correctly at its intended size, and stays consistent across sections and states.
Do not claim the source library was matched when a fallback was used.
