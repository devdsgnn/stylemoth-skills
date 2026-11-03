# StyleMoth Studio

Design the product around its subject and the person's task. Research should make
the decisions more specific; implementation should preserve those decisions.
This is a general design method, not a mandatory StyleMoth look or MCP dependency.

## Choose the right depth

| Request | Work to do |
| --- | --- |
| New website or interface | Establish the job, inspect relevant references, choose a direction, compose and build. |
| Explore options | Develop distinct directions with comparable content and scope; let the user choose when requested. |
| Improve an existing screen | Inspect the baseline, identify the requested problems, preserve the rest. |
| Multi-step flow | Map entry, decisions, system responses, failure recovery, and completion. |
| Review or compare | Inspect evidence and explain concrete tradeoffs; do not edit unless asked. |
| Small style repair | Inspect the component and cascade; fix locally without a new design process. |

Read the source before asking questions. Infer routine choices and proceed within
the request. Ask when the missing audience, task, source, or constraint would change
the design substantially. Do not turn optional concept exploration into an approval
gate for an already authorized build.

If the user selects a StyleMoth system, its bundle governs its colors, type, and
component roles. Use the apply-system.md workflow for retrieval and token application. Studio can inform structure, content, and flows, but must not
silently replace the selected system. Neither skill needs the other to operate.

## 1. Understand the job and preserve the baseline

Write a short internal brief: product, audience, task, completion, platform, content,
and constraints. For existing work, record the working routes, data, controls,
identity, and regions outside scope. Follow the current main path when accessible.
Do not infer the entire product from one screenshot.

Translate vague complaints into inspectable problems: a title collides with a
control, comparison data is too far from the choice, or related content has three
different insets. Prioritize the user's complaint and changes that affect the main
task. Aesthetic preference can justify a change; label it as judgment rather than
pretending it is a measured usability result.

## 2. Research decisions, not decoration

Use the researcher workflow in
[references/design-researcher.md](design-researcher.md) to find sources
through StyleMoth when connected, inspect their original websites when useful,
and record what each source actually supports. Studio can research a StyleMoth
system without adopting its theme. The researcher is a workflow role, not a
mandatory subagent or a claim that a new search service exists.

For substantial work read [references/research.md](research.md).
Use sources already provided first. Connected Refero or Mobbin tools can supply
styles, screens, sections, or flows if available; discover real tool schemas and
respect access limits. Public websites, Figma, screenshots, project files, and a
user's existing system also provide evidence. No single provider is required.

Look separately for visual language, the specific UI problem, and journey behavior.
Use a few relevant sources deeply rather than collecting many thumbnails. Inspect
the actual image or rendered page before citing visual details. Search snippets
and page titles are not evidence of layout or behavior.

Choose one visual foundation. Other sources can contribute a bounded decision,
such as an error pattern or responsive table. Do not combine several unrelated
palettes and component styles into an average. Preserve the user's own identity
when research concerns interaction structure rather than a requested rebrand.

Stop searching when the necessary decisions have evidence. For a local repair,
the existing source and user instruction can be sufficient. If access is blocked,
state the limitation and use available material. Never imply that the skill includes
a reference corpus or access to services the user has not connected.

## 3. Form a product-specific direction

For new visual direction read [references/art-direction.md](art-direction.md).
Set a concrete direction before writing extensive UI: canvas, typography, accent
roles, density, composition, surface boundaries, media, and motion. Tie a memorable
choice to the product, not to a fashionable aesthetic preset.

Keep a compact decision note for substantial work:

```text
Job and audience:
Must preserve:
Primary visual foundation and its defining traits:
Specific pattern/flow references and what each contributes:
Page or screen structure, with a purpose for each region:
Type, color roles, spacing, surface, and media commitments:
Original decisions or necessary extensions:
Main interaction and responsive checks:
```

When several sources or decisions need comparison, use the researcher's source
table and decision table instead of a long prose dump. A flow can use a compact
state matrix. Keep these as working notes and show only what helps the user
choose or assess the result. Tables are optional for a local repair and do not
prescribe table-heavy product layouts.

Use a wireframe, small style specimen, or mockup if it resolves real uncertainty.
Image generation is useful for bitmap concepts or assets when available, but is
not mandatory for a table, form, token-led screen, or a local CSS edit. Requested
options should differ in structure or visual language, not just accent color.

## 4. Compose the complete requested experience

Read [references/product-patterns.md](product-patterns.md) when deciding
screen anatomy or flow behavior. Design enough downstream structure to support
the main task; a full-page request is not complete after the hero.

Use content to determine hierarchy. Establish the offer or task, required context,
and action. Give each section a different job rather than repeating the same claim
in a sequence of card grids. Keep functional interfaces dense enough to work.

Choose a card, list, table, open section, drawer, or full-width band because the
information needs that structure. Do not wrap every region in another rounded
panel. A consistent system can contain different compositions.

Write short, specific interface copy. Preserve supplied claims and data. Label
examples, simulated product behavior, and missing assets honestly. No invented
customer quotes, popularity counts, certifications, or performance claims.

## 5. Build through a coherent system

Use the existing stack and component conventions. Reuse tokens and primitives;
define missing roles deliberately. Avoid hand-tuning every similar component
independently. Set controls' typography explicitly, load fonts, and check the
actual weight range. A familiar typeface is acceptable when chosen for the brief.

For spacing, typography, media, icons, and motion use
[references/interface-craft.md](interface-craft.md). For input, async,
and control states use [references/states-and-validation.md](states-and-validation.md).
Apply only the guidance relevant to the changed surface.

Retain the intended container model, information hierarchy, palette temperature,
and media treatment during implementation. Do not casually replace a white canvas
with cream, a real table with cards, or required product evidence with decorative
graphics. Use native text and real controls, not a screenshot as the interface.

Extend layouts intentionally for smaller screens. Preserve task-critical data and
actions, sensible reading order, keyboard focus, and usable touch targets. Use
supplied theme variants where present; a newly requested theme needs deliberate
semantic mapping rather than automatic color inversion.

## 6. Critique the real outcome

Read [references/review.md](review.md) for substantial builds and redesigns.
Compare the actual render to the chosen direction and the baseline, including
the whole requested surface, core interaction, phone layout, and applicable themes.
Correct concrete drift instead of repeatedly changing the design's premise.

Check both visual and functional quality. Appropriate builds and tests cannot
replace inspecting the layout, and a beautiful screenshot cannot prove controls
work. For local edits keep verification local unless shared rules create risk.
Do not repeat full-page QA after every small adjustment.

Finish with the result, actual checks, preview when useful, and remaining gaps.
Research and design judgment can explain a decision; they cannot establish a
conversion lift or user preference without testing. Do not claim this skill is
better than another from instruction length or a subjective score.

## Maintenance

Read [references/source-notes.md](stylemoth-studio-sources.md) for research influences.

