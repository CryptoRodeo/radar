---
title:      "Shared-Brain"
ring:       trial
segment:    techniques
tags:       [knowledge-management]
featured:   true
internal:   true
---

A collaborative knowledge management technique using [Logseq](https://logseq.com/)
with a "private by default" workflow. Shared-Brain enables teams to maintain a
collaborative graph of interconnected notes while keeping personal drafts private
until explicitly shared.

## Core Principles:

1. **Private by Default**: Everything you create—pages, notes, assets—is ignored
   by Git and stays local. Nothing is shared accidentally.

2. **Share by Renaming**: To publish a page, simply rename it to start with the
   `Shared-Brain/` prefix. Logseq automatically renames the file, making it
   visible to Git.

3. **Text-Only**: Markdown text only for compatibility with text-based tools
   like `repomix`. Assets (images, PDFs), whiteboards, and draws are not shared.

## How It Works:

* Clone the shared repository as your Logseq graph folder
* Create pages normally—they remain 100% private and local
* When ready to share, rename the page: `[[My Notes]]` → `[[Shared-Brain/Notes]]`
* Use standard Git commands to commit and push shared pages
* Manual Git control (no auto-sync) ensures clear commit messages and proper review

## Benefits:

* **Privacy-first**: Accidental sharing is prevented by design
* **Simple publishing**: One rename action to share content
* **Collaboration**: Build a shared knowledge graph across teams
* **Version control**: Full Git history of shared knowledge
* **Web access**: GitLab Pages provides web view without requiring Logseq installation

## Considerations:

* Requires manual Git operations (pull, commit, push)
* Team coordination needed for major changes (via Slack)
* Text-only limitation may not suit all use cases
* Learning curve for users new to Logseq or Git

See the [Shared-Brain repository](https://gitlab.cee.redhat.com/twaugh/Shared-Brain)
and [web view](https://twaugh.pages.redhat.com/Shared-Brain/#/graph) for more details.

---

## Contact

- **Ralph Bean** — [rbean@redhat.com](mailto:rbean@redhat.com) — (Portfolio & Delivery)

**Date added**: 2025-12-16 | **Last updated**: 2025-12-16
