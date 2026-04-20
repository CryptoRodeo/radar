---
title:      "Context Mode"
ring:       assess
segment:    tools
tags:       [code-assistance, mcp]
featured:   true
internal:   true
---

MCP server plugin for Claude Code that acts as a compression layer between
Claude Code and MCP tool outputs. When AI coding tools call external tools
(browser snapshots, GitHub API, log files, test output), the raw data floods
the AI's limited 200K-token context window. Context Mode intercepts these
outputs, runs processing code in an isolated sandbox, and only lets a small
summary back into the conversation — the raw data never enters context.

## How it works:

Two core mechanisms:

* **Sandbox execution** — each tool output is processed in an isolated
  subprocess. You write small scripts (in 10 supported languages) to extract
  what you need. Only stdout from those scripts enters the context window.
  Authenticated CLIs (gh, aws, kubectl, docker) work via credential
  passthrough.
* **Knowledge base** — content is chunked, stored in a local SQLite FTS5
  full-text search index, and queried on demand. URLs can be fetched,
  converted to markdown, and indexed without the raw HTML ever entering
  context.

## Real-world numbers:

* Playwright browser snapshot: 56 KB → 299 bytes
* 20 GitHub issues: 59 KB → 1.1 KB
* 500-line access log: 45 KB → 155 bytes
* 500-row CSV: 85 KB → 222 bytes
* Full session: 315 KB → 5.4 KB (98% reduction)
* Session time before context slowdown: ~30 min → ~3 hours

## Status:

* **Author**: mksglu (open source)
* **License**: Elastic License v2 (ELv2)
* **GitHub**: 2,500+ stars, 131 forks
* **Install**: `claude mcp add context-mode -- npx -y context-mode`
  or via Claude Code plugin marketplace

## Security note:

The sandbox is a context-saving mechanism, not a security boundary.
Authenticated CLIs (gh, aws, kubectl, docker) work via credential
passthrough, so subprocess-isolated code has the same access as your
main session. Because the processing scripts are LLM-generated, prompt
injection in tool output could lead to arbitrary code execution with
your credentials — the same risk profile as Claude Code itself.

## Recommendation:

Worth exploring for people that are heavily using Claude Code with multiple MCP tools.
The context savings are significant for long coding sessions. Evaluate
whether the summarization approach fits your workflow,  you trade raw detail
for dramatically longer effective sessions.

---

## Contact

- **Chmouel Boudjnah** — [chmouel@redhat.com](mailto:chmouel@redhat.com)

**Date added**: 2026-03-06 | **Last updated**: 2026-03-06
