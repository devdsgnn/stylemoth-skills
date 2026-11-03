# StyleMoth system access

Use when selecting/loading a system. Checked against `server/mcp.mjs` and exported
bundles on 2026-11-01. Discover current tools rather than assuming a client's
namespace or a permanent catalog.

## Connection and secrets

Endpoint: `https://stylemoth.com/api/mcp`.

The service uses Streamable HTTP with a bearer access key. Users sign in on
StyleMoth to create/revoke their own keys. Store keys in the client's secret store
or environment, never in this skill, generated source, screenshots, chat, or Git.
This skill does not create keys or modify MCP configuration automatically.
A website login does not automatically authenticate an MCP client.

Treat authentication failure as an access problem, not an empty catalog. Do not
retry indefinitely or bypass it. Continue with supplied files when possible.
Explain missing access without asking the user to paste a secret into chat.

## Verified tools

| Logical name | Arguments | Result |
| --- | --- | --- |
| `search_design_systems` | `query`: string; `theme`: `all`, `light`, `dark` | `systems` with IDs, descriptions, URLs, themes. Empty query lists catalog. |
| `get_design_system` | `system`: returned ID | Complete bundle; `files` keyed by filename, theme, URL, read order. |
| `get_design_tokens` | `system`; optional `group` | Exact tokens or top-level group. Unknown group returns available groups. |
| `get_design_file` | `system`; `file`: allowed filename | One complete file. Arbitrary paths are not supported. |
| `get_build_guide` | `system`; `workflow`: `start`, `content`, `restyle` | Guide, shared prompt, scenario-specific prompt. |

Use the actual namespace exposed by the client. Inspect `isError` before consuming
a result. Results currently contain text blocks: JSON-decode JSON payloads, but
preserve CSS and Markdown as text. An error is not an empty valid system.

Example for a dark developer-tool landing page:

```text
search_design_systems({"query":"developer productivity", "theme":"dark"})
get_design_system({"system":"raycast"})
get_build_guide({"system":"raycast", "workflow":"start"})
```

The example ID is valid at inspection, not a mandatory default. If search returns
no results, list the catalog before concluding nothing fits. Stop broadening once
available choices are clear. Never invent tools for screenshots, Figma export,
semantic similarity, or product flows that the server does not expose.

## Downloaded files

Use the user's supplied folder. StyleMoth's own canonical exports live at
`public/references/<system>/`; another project may use a different path.

| File | Purpose |
| --- | --- |
| `README.md` | Setup, fonts, scope, supported theme. |
| `DESIGN.md` | Intent and practical build guidance. |
| `tokens.json` | Palettes, aliases, type, dimensions, usage. |
| `reference.css` | Plain CSS variables and starter recipes. |
| `reference.tailwind.css` | Tailwind v4 entry importing sibling `reference.css`. |
| `AI-PROMPTS.json` | Shared prompt and distinct scenarios. |
| `CODEX-PROMPT.txt` | Starter workflow; plain instructions usable in any agent. |

The guide tool maps workflow `start` to scenario ID `scratch`; the other IDs are
`content` and `restyle`. Read the relevant scenario, not the same prompt for all.
For Tailwind v4 use its entry and resolve sibling imports once. Otherwise use plain
CSS. Do not change frameworks just to use an optional export.

## Tokens

Inspect the actual groups rather than assuming a schema:

- `palette`: families, numbered shades, and alpha values where supplied.
- `semanticColor`: roles that resolve to palette entries.
- `font`, `typography`, `typographyMobile`: families and responsive text styles.
- `space`, `layout`: dimensions and layout guidance.
- `radius`, `radiusUsage`: values and component assignments.
- `shadow`, `shadowUsage`: elevation and usage.
- `interaction`: control height, focus, disabled, motion, and state guidance.
- `reference`, `$extensions`: provenance and sampled coverage.

Resolve aliases such as `{palette.neutral.0}` through their actual JSON paths to
`$value`. Follow recursively; report missing paths or cycles. Preserve alpha.
For structured sRGB values, use the supplied hex extension when consistent with
the numeric value, or convert components without discarding alpha. Inspect the
exported CSS name before inventing a variable name.

Raycast also retains historical `color`/`semantic` groups. For new work use the
current `palette`/`semanticColor` layer consistently. Historical source hex values
are provenance, not interchangeable live values.

At inspection Raycast supplies dark; Duna and ElevenLabs supply light. A deliberate
dark section does not establish a complete dark theme. A requested extra theme
requires new semantic mapping and contrast checks. Current retrieved coverage is
authoritative. Dashboard systems must be found in the catalog or user files;
do not infer availability from a marketing preview.

The systems are independent website-inspired interpretations, not official brand
source code or brand-asset licenses. Use the customer's identity/content. Do not
carry StyleMoth viewer tabs, downloads, logo, or cursor effects into their product
unless requested.
