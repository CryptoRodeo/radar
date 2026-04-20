---
title:      "Using AI to prevent skill atrophy"
ring:       assess
segment:    tips
tags:       [learning]
featured:   true
---

# The problem

As a software developer, you might work in a Python codebase one quarter,
a Go codebase the next, somehow end up with OCaml, and then find yourself
back in Python again.

After spending months away, you're a little rusty.

The problem isn’t learning new technologies, it’s **skill decay caused by constant context switching**.

How do you maintain your skills over time in such a volatile environment
**without turning it into a second full-time job**?

# Automate your skill maintenance

One solution is to treat LLMs as **personal tutors** and use them to generate
small, recurring lessons that keep your skills sharp.

Instead of constantly re-learning what you forgot, you maintain a *baseline of competence*
over time.

# The setup

Ideally, you want an LLM that supports **persistent project instructions**
(sometimes called Projects or long-lived system prompts), such as ChatGPT or Claude.

This allows you to define your learning constraints once and reuse them every day.
If your tool doesn’t support this, you can still do it. You’ll just need to paste
the instruction each time.

**Here’s an example project instruction**:

(START)

You are a (level-above) Golang engineer mentoring a (your-level) engineer.

Your job is to help the mentee maintain and gradually improve their Go skills
through short, focused daily lessons.

**General rules**:

* Explain Go-specific terminology in simple language.

* Do not assume prior Go knowledge unless it has appeared in recent lessons.

* Prefer practical understanding over formal definitions.

**Lesson selection**:

Before generating a lesson, review recent lessons.

Choose EXACTLY ONE of the following:

1) the next logical concept building on prior lessons

2) reinforcement of a concept the mentee may be weak on

3) a missing prerequisite needed for future topics

Do NOT introduce unrelated topics.

**Cold start behavior**:

If no prior lessons exist, assume the mentee has general programming experience and (your-level) Go experience.

Start with a foundational Go concept that:

* appears frequently in real Go code

* influences how Go code is structured

Clearly state that this lesson establishes the baseline.

**Duplication rules**:

* Do not repeat lessons unless reinforcement is clearly beneficial.

* If repeating, explain briefly *why* the repetition is necessary.

**Time constraint**:

The entire lesson + exercise must fit into a 10-minute learning window.

Aim for:

* ≤ 300 words for explanation

* ≤ 10 minutes of coding or thinking time

**Lesson structure (always follow this)**:

1) Concept (plain-language explanation)

2) Why it matters in real Go code

3) Small example

4) One short exercise

**Exercise rules**:

* The exercise should expose misunderstandings, not be mechanical.

* Prefer “modify this code” or “predict the output” over writing from scratch.

* Include expected output or success criteria.

**Tone**:

* Be concise, practical, and supportive.

* Avoid over-teaching.

(END)

Once this instruction is set, your daily workflow is *trivial*:

> “Generate today’s lesson.”

**That’s it**.

You can repeat this setup for multiple languages, tools, or domains
(Go, Python, Bash, Kubernetes, networking, etc.) and maintain proficiency
across all of them over time.

## Why the 10-minute constraint works

I deliberately limit lessons to 10 minutes because:

- They’re short enough that I can’t justify procrastinating
- They fit into small gaps in the day
- I can stack multiple skill-maintenance sessions without it feeling overwhelming

Consistency beats intensity here.

# Tips

## Learn from your favorite Github projects

If your LLM project allows file uploads you can use those files as learning data.

For example, if you find a **particular Github repository** that represents the level of
engineering you want to reach, upload it and reference it in your LLM project instructions.

Add something like this:

"You and the mentee both work on Project X.
Use it as a reference when generating lessons.

Select small segments of the codebase, explain an important concept they demonstrate,
and generate a short exercise based on that concept."

This turns your favorite Github repositories into continuous learning sources.

## Store your lessons in a Git repo

Create a Git repository for your lessons and save each lesson and exercise.

Keep it simple. Create a directory for each language/concept/domain and store the LLM lesson sessions in simple markdown files.

Over time, this repository becomes a living record of your technical competence.

Even better, this repo can be reused as **input back into the LLM** so it can:

- avoid duplicating lessons
- intentionally reinforce weak areas
- build on what you’ve already covered

You can see an example of this with some lessons and exercise files here: [https://gitlab.cee.redhat.com/bramos/automated-lessons](https://gitlab.cee.redhat.com/bramos/automated-lessons)

# The benefits

* Prevent skill atrophy in an industry that constantly pulls you in different directions.
* Turn learning into a low-friction daily habit
* Externalize your technical memory in a searchable, durable format
* Give LLMs real context so lessons improve over time
* You stay sharp without burning out

---

## Contact

- **Bryan Ramos** — [bramos@redhat.com](mailto:bramos@redhat.com) — (Trusted Software Delivery)

**Date added**: 2026-01-26 | **Last updated**: 2026-01-26
