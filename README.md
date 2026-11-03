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
