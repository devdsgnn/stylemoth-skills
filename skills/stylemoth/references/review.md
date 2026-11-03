# Review the delivered interface

Use for substantial UI changes. These are comparison questions, not a requirement
for lengthy reports or unrelated tests.

For a selected system, use [System compliance](system-compliance.md). Compare
expected role values with computed styles and effective spacing; compare feature
compositions and content density with the selected source, not unrelated examples.

## Follow the main task

Walk from entry to completion. Does each changed control do what its label promises?
Is necessary information beside the decision? Are failures recoverable? Compare
restyles against the baseline for lost content, routes, actions, and data.

## Inspect the real render

Inspect the requested surface, not just the hero. Compare:

1. Hierarchy: intended focal point and understandable next action.
2. System: semantic colors, type, spacing, radius, elevation, icon family.
3. Rhythm: aligned gutters, deliberate heading gaps, repeatable insets.
4. Content: real copy fits; descriptions read well; no invented proof.
5. Media: assets load, crop correctly, and do not obscure UI.
6. Responsive layout: no page-wide overflow or clipped/squeezed controls.
7. Behavior: keyboard focus, selection, disclosure, pending and error feedback.

For new pages inspect representative desktop, laptop, and phone layouts. Check
around a breakpoint if needed. Include long content or zoom where it could expose
a real issue. If both themes are supplied, inspect both; do not claim unsupported
themes were verified.

Use actual browser screenshots for material visual comparisons when available.
A generated concept is not proof of a running implementation. If browser access
is unavailable, state which aspects remain unverified.

## Fix causes

For spacing drift, inspect computed styles, component variants, shared containers,
and inherited margins. For typography, check font loading before altering sizes.
For layout jumps, inspect layout and scroll anchoring before adding easing.
Keep fixes in the responsible rule rather than stacking unrelated overrides.

Run relevant project checks. Repeat because a change/failure warrants it, not on
every tiny style edit. A local correction needs the affected component and likely
shared-style impact checked, not a new full-site audit. Do not change production
data just to prove a visual adjustment.

## Handoff

State the result and reason, summarize actual visual/functional checks, link the
deliverable, and disclose meaningful gaps. Keep detailed research available without
dumping it into the reply. Describe observed improvements such as readable labels
or an aligned action, not unmeasured conversion gains or exhaustive accessibility.
Finish when the authorized scope is complete; do not reopen the design direction
during handoff.

For icon provenance, library selection, implementation, and validation, follow
[Icon research and implementation](icons.md).
