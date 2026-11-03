# StyleMoth skill

One coding-agent skill for visual research, design systems, building, and refinement.
Includes system application through StyleMoth MCP or exported files, original UI design,
layout, typography, colors, interaction states, and review guidance.

## Install

Download the ZIP at https://stylemoth.com/downloads/stylemoth-skill.zip and extract it.
Move the entire `stylemoth` folder into your project's skill directory:

| Agent | Location |
| --- | --- |
| Codex | `.agents/skills/stylemoth/` |
| Cursor | `.cursor/skills/stylemoth/` |
| Claude Code | `.claude/skills/stylemoth/` |

`SKILL.md` must be directly inside that folder. Keep `references/` and `agents/` alongside it.
Start a new agent session if necessary. For another agent, follow its Agent Skills support.
Back up local changes before replacing an existing installation. Remove the folder to uninstall.

Alternatively, ask your agent:

> Install the StyleMoth skill from https://github.com/devdsgnn/stylemoth-skills into this project.
> Read the README and inspect skills/stylemoth first. Copy the entire stylemoth folder into the
> skill directory supported by this agent. Preserve any existing customizations; ask before
> overwriting them. Confirm the installed path and how to invoke it. Do not change MCP credentials.

## Use

Codex: `Use $stylemoth to refine my project while preserving working features.`
Claude Code: `/stylemoth Refine my project while preserving working features.`
Cursor: ask Agent to use the StyleMoth skill for your task.

For a chosen system: ask StyleMoth to read its design guide and tokens before implementation.
For original work: provide the brief, content, and any references.

## Access

This package includes instructions only. It does not include paid design systems, API keys,
or access to external services. Connect MCP separately at https://stylemoth.com/mcp;
protected library access follows your plan. Exported files can be used without MCP.

## Agent documentation

- https://learn.chatgpt.com/docs/build-skills
- https://cursor.com/help/customization/skills
- https://code.claude.com/docs/en/skills

Version 1.0.0. Combines the independently written StyleMoth Design and Studio workflows.
Source notes are included in references/. No third-party skill files or website assets are bundled.

## Reference-led workflow (v1.1.1)

Use `build`, `section`, `restyle`, `research`, `refine`, or `review` after invoking
StyleMoth. These are modes inside one skill. The main workflow reads your bundle,
imports its CSS/tokens, researches the original site and your brief, builds real
section visuals, and reviews each section at desktop and mobile sizes.

Example: `Use $stylemoth build a task-assistant website using the Raycast bundle
in ./design-system. Follow its visual hierarchy and refine the finished result.`

See [prompt examples](examples/prompts.md), [client/MCP setup](docs/integrations.md),
and [behavioral evaluation cases](docs/evaluation.md).

### Package structure

- `skills/stylemoth/`: one skill, focused references, source-map template, bundle inspector.
- `.claude-plugin/`, `.cursor-plugin/`, `.codex-plugin/`: client distribution metadata.
- `gemini-extension.json`, `GEMINI.md`: Gemini context adapter.
- `integrations/`: optional MCP templates; no credentials or automatic setup.
- `scripts/`: package validation, inspector tests and deterministic ZIP creation.
- `docs/ci/check.yml`: ready-to-enable GitHub Actions validation (copy to `.github/workflows/check.yml` with a workflow-authorized credential).

### Maintain and extend

Run `python3 scripts/check_release.py`, `python3 scripts/test_bundle.py`, then
`python3 scripts/package.py`. The ZIP contains the portable skill and README;
plugin metadata stays in the repository/source archive. Inspect an export with
`python3 skills/stylemoth/scripts/inspect_bundle.py /path/to/bundle`.

Add new workflow guidance as focused references, route it from SKILL.md and add
behavioral cases. Keep one skill and no empty integration folders. Update VERSION,
SKILL metadata and all client manifest versions together. Test generated ZIP
contents before release. Behavioral cases need actual agent/browser runs; structural
checks do not establish design quality or universal client compatibility.

Selected-system builds now require a usage-role map and rendered compliance review.
Spacing descriptions and responsive exceptions are applied by role; feature-card
composition and content density stay tied to the selected source. Outside research
is limited to missing patterns or explicit user overrides. See
[system compliance](skills/stylemoth/references/system-compliance.md).
