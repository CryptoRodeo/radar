---
title:      "Ralph Wiggum (Iterative, Spec-Driven LLM Development)"
ring:       assess
segment:    techniques
tags:       [workflow, prompting]
featured:   true
internal:   true
---

# Ralph Wiggum
The Ralph Wiggum technique (also called the "Ralph Loop") is a spec-driven,
AI-assisted development methodology where an LLM implements software
incrementally under strict constraints.

Instead of allowing an AI agent to freely generate code, developers define
explicit specifications and guardrails. The LLM executes a single, tightly
scoped feature per iteration, updates persistent artifacts that act as memory,
and then stops for human review.

In its purest form, it's a simple while loop that repeatedly feeds an AI agent a prompt until completion.
Named after The Simpsons character, it embodies the philosophy of persistent iteration despite setbacks.

## Core concepts:

* Specs and memory live in files, not in the LLM context
* One feature per run, enforced by an execution contract
* Human-in-the-loop between iterations
* Deterministic, auditable progress

## Typical file layout:

**prd.json**: Machine-readable product requirements document

  * Lists features, steps, and completion status
  * Easy for LLMs to scan and update with minimal tokens

**progress.txt**: Append-only memory and audit log

  * Records decisions, changes, and validation results
  * Replaces conversational memory and reduces hallucinations

**ralph-once.sh** / **ralph.sh**: Execution wrapper

  * Enforces strict rules on what the LLM may and may not do
  * Ensures the loop stops after one feature (or after N iterations)

### File examples (prd.json, progress.txt):
These files were used to implement a small feature. What you see is what the LLM read, updated and outputted.

- [prd.json](https://raw.githubusercontent.com/CryptoRodeo/ralph/refs/heads/main/examples/prd.json):
- [progress.txt](https://raw.githubusercontent.com/CryptoRodeo/ralph/refs/heads/main/examples/progress.txt)

**Things to keep in mind**:

  * **"passes"** in **prd.json** should be set to **"false"** when creating a new feature spec.

    * The LLM will update it to **true** once it determines it the feature is implemented.
    * You can set it back to `false` and update the spec if you need more changes.

  * The feature specs in **prd.json** **do not have to be in order**. The LLM will decide which feature to prioritize first.

### Script examples:

- [ralph-once.sh](https://raw.githubusercontent.com/CryptoRodeo/ralph/refs/heads/main/ralph-once.sh)
- [ralph.sh](https://raw.githubusercontent.com/CryptoRodeo/ralph/refs/heads/main/ralph.sh)

## Workflow:

* Run the Ralph script
* The LLM reads **prd.json** and selects exactly one unfinished feature
* The LLM plans and implements only that feature
* Validation is performed (tests, types, builds, etc.)
* Decisions and results are appended to **progress.txt**
* The completed feature is marked done in `prd.json`
* The loop stops and waits for human review

## Proven use cases:

* Automating small scripts and tooling tasks
* Refactoring with strong guardrails
* Incremental feature development

## Benefits:

* Strong guardrails prevent scope creep
* Reduced hallucinations due to file-based memory
* Low token usage from small, focused prompts
* Fully auditable change history
* Clear separation of responsibilities:

  * Humans write specs and tests
  * LLMs perform mechanical implementation

## Lessons learned:

* JSON specs work better than Markdown for LLM scanning and updates
* Ambiguous specs surface quickly and force clarification
* Writing the spec is often the hardest and most valuable part
* The technique works best for incremental, well-bounded changes
* Human approval between loops is critical for safety and correctness

## References:

**Introductory video**: https://www.youtube.com/watch?v=Jr2auYrBDA4

**Workflow walkthrough**: https://www.youtube.com/watch?v=_IK18goX4X8

**Spec-driven development article**:
https://developers.redhat.com/articles/2025/10/22/how-spec-driven-development-improves-ai-coding-quality

**Ralph Wiggum resources**:

  * https://ghuntley.com/ralph/
  * https://www.aihero.dev/getting-started-with-ralph
  * https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum
  * https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents

## Addendum:

There is an official claude code plugin for this:
https://github.com/anthropics/claude-code/blob/main/plugins/ralph-wiggum/README.md
but we keep seeing "don't use the ralph claude plugin!!!" videos and posts like
this: https://www.aihero.dev/why-the-anthropic-ralph-plugin-sucks TLDR: Instead
of multiple sessions the plugin creates one big loop session without actually
exiting, creating a bigger context each loop. Bigger context -> worse output.

---

## Contact

- **Bryan Ramos** — [bramos@redhat.com](mailto:bramos@redhat.com) — (Trusted Software Delivery)

**Date added**: 2026-01-21 | **Last updated**: 2026-01-21
