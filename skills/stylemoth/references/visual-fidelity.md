# Visual fidelity checklist

Compare the render with the actual reference, not memory. Record only findings
that affect the requested task; no numeric similarity claims without measurement.

- Composition: same dominant visual, alignment, column balance, negative space,
  content density and section rhythm. Adapt to user content rather than force copy.
- Typography: family or documented fallback, weight, size, line height, tracking,
  text width, line breaks and contrast. Match the hierarchy, not only the heading.
- Color: exact semantic roles, neutral temperature and accent frequency. Keep
  transparent surfaces transparent; inspect them against their actual background.
- Surfaces: radius, border opacity, elevation and nested-layer depth. No effects
  that the source does not support. Shadows and glow are distinct treatments.
- Visuals: correct screenshot aspect ratio, meaningful original UI, SVG stroke
  style, icon scale, masking and image fit. No stretching or unlicensed branding.
- Motion: observe trigger, duration, easing, direction and resting state. Do not
  infer motion from a static screenshot. Preserve reduced-motion alternatives.
- Responsive: reflow, crop and text scale based on observed mobile evidence; do
  not merely shrink desktop. No essential content hidden to suppress overflow.
- Interaction: keyboard, focus, active/hover/disabled states, errors and completion.

Fix composition and type before small decorative details. For conflicting source
versions, record the chosen version and apply it consistently.
