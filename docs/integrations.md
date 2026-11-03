# Clients and optional MCP

The portable install is the complete `skills/stylemoth/` folder. See the README
for project paths. One skill includes all workflow modes and supporting resources.

The repository also includes Claude Code, Cursor and Codex plugin manifests and
a Gemini CLI extension context entry. They reference the same source skill.
These are distribution metadata, not claims of approval in any marketplace.
Plugin loading differs by client version; direct folder installation remains the
fallback. End-to-end installation in every client has not been tested.

For Claude Code's local plugin development, use `claude --plugin-dir /path/to/stylemoth-skills`.
Gemini's extension entry loads GEMINI.md, which routes design requests to the same
skill. Do not install both the extension/plugin and a duplicate folder in one client.

## MCP is optional

The files in `integrations/` are opt-in setup templates, not auto-loaded root
configuration. This keeps file-only workflows functional without credentials.
Merge the relevant server entry into existing client configuration; do not replace
other servers. Set STYLEMOTH_API_KEY privately in the client's environment first.
Restart/reconnect, verify tool discovery, then search and retrieve a real bundle.
Get and manage your own key at https://stylemoth.com/mcp. Paid access rules apply.
Never paste a key into the skill, source code, screenshots, installation prompt or Git.

- Codex: `integrations/codex.toml`, into the existing Codex config.
- Claude Code: `integrations/claude.mcp.json`, into project `.mcp.json` when authorized.
- Cursor: `integrations/cursor.mcp.json`, into project `.cursor/mcp.json` when authorized.
- Other clients: configure Streamable HTTP at `https://stylemoth.com/api/mcp`
  with a Bearer Authorization header through that client's secret mechanism.

Auth failures are not empty catalogs. A local downloaded bundle works independently.
No registry publication workflow is included: publishing a remote server listing
requires its own ownership/metadata verification and is separate from a skill release.

## Sources checked

- https://github.com/referodesign/refero_skill — package organization reference;
  StyleMoth workflow text and scripts are independently authored.
- https://code.claude.com/docs/en/plugins-reference
- https://code.claude.com/docs/en/mcp
- https://cursor.com/docs/reference/plugins
- https://cursor.com/docs/mcp
- https://geminicli.com/docs/extensions/reference/
- StyleMoth's deployed MCP implementation and app configuration examples.
