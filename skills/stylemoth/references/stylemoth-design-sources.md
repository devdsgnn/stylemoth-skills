# Source notes and authorship

Research date: 2026-11-01. This package is independently written for StyleMoth.
It does not bundle other providers' skill files, screenshots, assets, or tool
implementations. Source links document influences, not dependencies or endorsement.
It does not claim access to private ChatGPT or Claude system instructions.

## Primary sources reviewed

| Source | Pinned file | Principle retained | Deliberate difference |
| --- | --- | --- | --- |
| Refero | [refero-design](https://github.com/referodesign/refero_skill/blob/2382e518f90096df607196b9a635da2d1bc142f9/skills/refero-design/SKILL.md) | Research before substantial visual decisions; preserve a coherent direction and role meanings. | StyleMoth retrieves complete implementation systems. It does not require another provider or several searches for a local repair. |
| Anthropic | [frontend-design](https://github.com/anthropics/skills/blob/ca45fc496a3436251f191354091d557da31c15b5/skills/frontend-design/SKILL.md) | Subject-specific choices, restraint, typography, and concise interface writing. | Existing fonts and familiar layouts remain legitimate; novelty must not override a selected system. |
| Mobbin | [redesign-screen](https://github.com/mobbin/skills/blob/06a042885d2794865e96d0e5a98cbb460fd4d0e0/skills/redesign-screen/SKILL.md) | Preserve the product's job and working behavior; connect visible changes to concrete evidence. | StyleMoth also handles new builds and file-only work. It does not halt solely because Mobbin MCP is absent. |
| OpenAI | [frontend-app-builder](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/build-web-apps/skills/frontend-app-builder/SKILL.md) | Treat the intended design as an implementation target; check the actual render, responsive layout, and interactions. | Image generation is optional when it adds value, not mandatory for token-led interfaces. QA scales to the change. |
| OpenAI | [product-design index](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/product-design/skills/index/SKILL.md) | Distinguish research, exploration, review, and implementation tasks. | One portable entrypoint routes directly to the needed reference without depending on OpenAI-specific plugins. |

Refero and Mobbin repositories report MIT licensing; Anthropic's frontend-design
folder supplies Apache-2.0 terms. OpenAI repository files were inspected as public
reference material without assuming a license for redistribution. This package
contains original instructions rather than redistributed source passages. Reassess
the applicable terms if future versions directly incorporate third-party material.

## StyleMoth-specific contribution

The central unit is a usable design system: palette primitives, semantic aliases,
responsive text styles, dimensions, elevation, component guidance, and workflows.
Selection is followed by applying those relationships to the user's product.

The MCP contract and file names were verified against the current StyleMoth backend
and all three local exports. Coverage statements are dated; discovery and retrieved
metadata take precedence over remembered catalog details.

The product's repeated real problems informed the craft guidance: section gaps
and internal insets are different controls; technical-value pills are different
from descriptions; a viewer's appearance is different from its exported product
system; compact content can coexist with generous section spacing. These are
decision criteria, not universal instructions to make every site white, use Inter,
set regular weight to 450, add a typewriter hero, or hide mobile downloads.

## Maintenance checks

Before changing the access reference, compare against the actual server's tool
names, schemas, bundle files, theme coverage, and alias structure. Before adding
a global design rule, test whether it would break a legitimate brief or existing
system. Keep conditional guidance in its supporting file and the entrypoint short.
