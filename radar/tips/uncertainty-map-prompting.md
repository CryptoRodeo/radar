---
title:      "Uncertainty Map Prompting"
ring:       assess
segment:    tips
tags:       [prompting]
featured:   true
internal:   true
---

A prompting technique to help identify when LLMs are hallucinating or providing
plausible but inaccurate answers. The approach involves adding this instruction
to your prompts:

> Add a section at the end of your responses labeled "Uncertainty Map," where you
> describe what you're least confident about, what you may be oversimplifying,
> and what questions or followups would change your opinion.

## Benefits:

* **Hallucination detection**: Helps identify when the LLM is fabricating information
  rather than admitting uncertainty
* **Confidence calibration**: Makes the LLM assess and communicate its confidence
  level about different parts of its response
* **Critical thinking**: Encourages the LLM to identify oversimplifications and
  edge cases it might be missing
* **Follow-up guidance**: Provides natural next questions to explore areas of
  uncertainty

## Usage:

This technique works particularly well for:
* Complex technical questions where accuracy is critical
* Exploratory research where you need to know what you don't know
* Decision-making scenarios where understanding limitations is important
* Code review or architectural discussions where trade-offs matter

## Considerations:

The effectiveness depends on the LLM's ability to accurately assess its own
confidence. While this technique can surface potential issues, it's not a
guarantee against all hallucinations. Always verify critical information
through other means.

Experience suggests this technique is "sometimes useful" rather than universally
applicable. It may be most valuable as a learning tool when you're new to working
with LLMs, helping you develop intuition about when to push back on or question
responses. Over time, you naturally gain a sense for an LLM's blind spots and may
find the explicit uncertainty maps less necessary. Consider using this as training
wheels while building your judgment, rather than as a permanent addition to all
prompts.

---

## Contact

- **Tim Waugh** — [twaugh@redhat.com](mailto:twaugh@redhat.com) — (Secure Flow)

**Date added**: 2025-12-16 | **Last updated**: 2025-12-16

**Status**: moved-in
