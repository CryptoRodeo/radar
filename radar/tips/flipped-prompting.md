---
title:      "Flipped Prompting"
ring:       assess
segment:    tips
tags:       [prompting]
featured:   true
internal:   true
---

Flipped prompting is a technique where you make the LLM ask you for details of the work you want it to do instead of having to specify all the details as part of the initial prompt.

This can be useful to reduce hallucinations and improve the accuracy of the response and reduce the cognitive load of writing the prompt.

This works particularly well when using the "Plan Mode" in Cursor that has a dedicated question-asking UI.

## Example (ADR writing)

> Help me write a new ADR, I have what I need to be in it in my head, but its hard for me to put it together in writing,
> so ask me questions until we have all the details of the ADR. Try to ask narrow questions I can answer shortly rather
> then very open ones that would require elaborate complex answers. Do not add any details I do not explicitly provide
> without asking about them first.

## Example (Code generation)

> I want to add Google Analytics as well as Amplitude based data collection to this site, both to be governed by
> Orest Bida’s Vanilla CookieConsent (v3) I'm unsure about the details of accomplishing this so please make suggestions
> and ask me simple guiding questions until we get the complete picture. We need to deal with everything from getting
> the basic functionality to managing the needed secrets and automating software updates.

---

## Contact

- **Barak Korren** — [bkorren@redhat.com](mailto:bkorren@redhat.com) — (Secure Flow)

**Date added**: 2026-02-01 | **Last updated**: 2026-02-01
