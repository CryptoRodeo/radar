---
name: contribute-radar-entry
description: Walk a user through contributing a new technology blip to the radar. Gathers quadrant, ring, name, description, and contact info interactively, then generates the Markdown radar entry, validates it, commits, and creates a GitLab MR.
user_invocable: true
---

# Contribute Radar Entry

Guide the user through adding a new technology blip to the radar. The radar is built with the AOEpeople techradar framework. Contributors create Markdown files with YAML frontmatter directly in `radar/<quadrant>/`.

Follow every step below in order. Use `AskUserQuestion` for each input-gathering step.

## Step 1: Quadrant and Ring

Use `AskUserQuestion` to ask the user to select a **quadrant** (called "segment" in the AOEpeople framework):

- **Header**: "Quadrant"
- **Options** (single-select):
  - `tools` — Development and operational tools (GitLab CI, Prometheus, Claude Code...)
  - `techniques` — Development and process techniques (TDD, pair programming...)
  - `platforms` — Infrastructure, deployment, cloud platforms (Kubernetes, OpenShift...)
  - `tips` — Tips and recommendations (using LLMs to understand codebases...)

Then use `AskUserQuestion` to ask the user to select a **ring**:

- **Header**: "Ring"
- **Options** (single-select):
  - `adopt` — Proven in production, high confidence, actively using
  - `trial` — Worth pursuing in projects that can handle risk
  - `assess` — Worth exploring to understand potential
  - `hold` — Proceed with caution or avoid

Then use `AskUserQuestion` to ask whether this is a **new entry**:

- **Header**: "New entry?"
- **Options** (single-select):
  - `Yes` — First time on the radar
  - `No` — Updating an existing assessment

## Step 2: Technology Name and URL

Use `AskUserQuestion` to ask for the **technology name**:

- **Header**: "Technology name"
- **Question**: "What is the technology name? Use title case (e.g. 'Claude Code', 'GitLab CI', 'Trunk Based Development')."
- Provide a few example names as options to show naming conventions, plus an "Other" option for free-text entry.

Use `AskUserQuestion` to ask for a **URL**:

- **Header**: "Reference URL"
- **Question**: "Do you have a URL with more information about this technology? (project homepage, docs, blog post)"
- **Options**: `No URL` / use "Other" for the user to paste a URL.

If a URL is provided, use `mcp__plugin_context-mode_context-mode__ctx_fetch_and_index` to fetch and index it. Use the fetched content to help draft the description in the next step.

## Step 3: Draft the Description

Using the information gathered (quadrant, ring, name, URL content if available), draft a description following the project's best practices. Structure the description with these sections where applicable:

- **Context**: What problem does it solve?
- **How it works**: Key mechanisms explained simply
- **Experience**: Provide stories or numbers about actual usage in Portfolio & Development
- **Status**: Author/vendor, license, GitHub stats, install method
- **Security notes**: If applicable
- **Recommendation**: Who should use it and when

Use markdown formatting within the description (## headers, bullet lists).

Present the draft description to the user using `AskUserQuestion`:

- **Header**: "Description review"
- **Question**: Show the full drafted description and ask: "Here is the drafted description. Would you like to approve it, or provide edits?"
- **Options**: `Approve as-is` / `Edit` (use "Other" for the user to provide revision instructions)

If the user wants edits, revise accordingly and present again until approved.

## Step 4: Contact Information

Use `AskUserQuestion` to ask for **contact method**:

- **Header**: "Contact method"
- **Options** (single-select):
  - `Email` — Email address
  - `Slack` — Slack channel URL
  - `Both` — Email and Slack

Then use `AskUserQuestion` to gather the contact details:

- **Header**: "Contact details"
- **Question**: Based on the selected method, ask for: full name, email address, and/or Slack channel URL, and team name (optional).

## Step 5: Generate Markdown Entry, Validate, Commit, and Create MR

### 5a. Generate the Markdown file

Derive the filename using kebab-case from the technology name. Write the file to:

```
radar/<quadrant>/<kebab-case-name>.md
```

Use this exact structure:

```markdown
---
title:      "<Technology Name>"
ring:       <ring>
segment:    <quadrant>
tags:       [<relevant-tag>]
featured:   <true if new, false otherwise>
---

<description content here>

---

## Contact

- **<Contact Name>** — [<email>](mailto:<email>)

**Date added**: <today YYYY-MM-DD> | **Last updated**: <today YYYY-MM-DD>
```

Only include email, Slack, and team fields that were actually provided.

### 5b. Validate

Run `make validate` from the repository root to check the Markdown entry is valid.

If validation fails, read the error output, fix the Markdown file, and retry. Repeat until validation passes.

### 5c. Confirm before committing

Show the user the final Markdown entry content. Use `AskUserQuestion` to confirm:

- **Header**: "Ready to commit?"
- **Question**: "The radar entry has been created and validated. Ready to commit and create an MR?"
- **Options**: `Yes, commit and create MR` / `No, I want to make changes`

If the user wants changes, go back and make them, then re-run `make validate`.

### 5d. Create branch, commit, push, and MR

1. Create branch from main: `git checkout -b add-<kebab-case-name>-blip main`
2. Stage the file: `git add radar/<quadrant>/<kebab-case-name>.md`
3. Commit: `git commit -m "Add <Name> blip to <quadrant> quadrant"`
4. Push: `git push -u origin add-<kebab-case-name>-blip`
5. Create MR: `glab mr create --title "Add <Name> blip to <quadrant> quadrant" --description "<summary of the blip>"`
6. Return the MR URL to the user.

**Important**: Always ask the user for confirmation before pushing and creating the MR.
