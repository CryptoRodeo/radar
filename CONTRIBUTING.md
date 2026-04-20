# Contributing to the Portfolio & Delivery Technology Radar

Thank you for contributing to our technology radar! This guide will help you add or update technology blips.

## How to Contribute

### 1. Choose the Right Location

Blips are organized by quadrant. Choose the appropriate quadrant for your technology:

- **techniques/**: Development and process techniques (e.g., TDD, pair programming, trunk-based development)
- **platforms/**: Infrastructure, deployment, and cloud platforms (e.g., Kubernetes, AWS, OpenShift)
- **tools/**: Development and operational tools (e.g., GitLab CI, Prometheus, Ansible)
- **tips/**: Tips and recommendations for working with technology (e.g., using LLMs to understand codebases, debugging techniques)

### 2. Create or Update a Markdown File

Each technology should have its own Markdown file in the `radar/<quadrant>/` directory. The filename should be the kebab-case version of the technology name:

```
radar/tools/gitlab-ci.md
```

### 3. Fill in the Required Fields

Create a Markdown file with YAML frontmatter:

```markdown
---
title:      "Technology Name"
ring:       adopt|trial|assess|hold
segment:    techniques|platforms|tools|tips
tags:       [relevant-tag]
featured:   false
---

A brief description of the technology and your team's experience with it.
Be specific about what worked, what didn't, and any recommendations.
```

**Ring Meanings:**
- **adopt**: Proven in production, high confidence, actively using
- **trial**: Worth pursuing in projects that can handle the risk
- **assess**: Worth exploring to understand potential
- **hold**: Proceed with caution or avoid based on experience

### 4. Add Optional Metadata

You can include additional metadata in the body of the Markdown file after the description:

```markdown
---

## Contact

- **Your Name** — [email@redhat.com](mailto:email@redhat.com)

## Authorization

- **Status**: approved
- **Note**: Approved for all teams

**Date added**: 2026-04-02 | **Last updated**: 2026-04-02
```

### Optional: Authorization Status

Add an **Authorization** section to indicate the organizational approval status:

| Status | Meaning |
|--------|---------|
| `approved` | Approved for broad organizational use |
| `conditionally_approved` | Approved with conditions (document in Note) |
| `under_evaluation` | Being formally evaluated for approval |
| `blocked` | Cannot be used — procurement, licensing, or policy issue |
| `restricted` | Previously evaluated and rejected, or cancelled |

This is especially useful for "Hold" blips where the reason matters — a technology blocked by procurement (Codex) is fundamentally different from one cancelled after evaluation (Sealights).

### 5. Write Helpful Descriptions

Good descriptions include:

- **Context**: What problem were you solving?
- **Experience**: What actually happened when you used it?
- **Specifics**: Concrete examples, metrics, or outcomes
- **Recommendations**: Who should use it and when?
- **Warnings**: What to watch out for?

**Example of a good description:**

```markdown
We adopted GitLab CI for all new projects in Q2 2024. Over 15 projects now use it
for CI/CD. The YAML-based configuration is straightforward, and the integration
with GitLab repositories is seamless.

Pros:
- Built-in container registry integration
- Good documentation and community support
- Shared runners reduce infrastructure management

Cons:
- YAML syntax can be verbose for complex pipelines
- Limited support for matrix builds compared to GitHub Actions

Recommendation: Use for any project hosted on GitLab. Consider GitHub Actions
if you need complex build matrices.
```

### 6. Update CODEOWNERS (if needed)

If you want to be notified of changes to your blips, add yourself to the `CODEOWNERS` file:

```
/radar/tools/gitlab-ci.md @your-gitlab-username @teammate1 @teammate2
```

### 7. Test Locally (Optional)

You can validate your entry and preview the radar before submitting:

```bash
# Validate all radar entries
make validate

# Or, build and serve the radar locally at http://localhost:8000
make serve
```

The `make serve` command is recommended - it will build and start a local web server. Visit http://localhost:8000 to see exactly how your blips will appear on the live radar.

### 8. Submit a Merge Request

1. Create a new branch: `git checkout -b add-blip-technology-name`
2. Add your changes: `git add radar/`
3. Commit with sign-off: `git commit -S -s -m "Add blip for Technology Name"`
4. Push: `git push -u origin add-blip-technology-name`
5. Create a merge request on GitLab

The CI pipeline will automatically validate your changes.

## Updating Existing Blips

Technology experiences evolve. If your team's assessment of a technology has changed:

1. Update the `ring` field if the recommendation changed
2. Update the `description` to reflect new experiences
3. Update `last_updated` to today's date
4. Explain what changed in your merge request description

## Guidelines

### Do:
- ✅ Share real, specific experiences
- ✅ Update blips as your experience evolves
- ✅ Include both successes and failures
- ✅ Be honest about problems you encountered
- ✅ Provide context for your recommendations

### Don't:
- ❌ Add technologies you haven't actually used
- ❌ Be vague ("it's good" or "it's bad")
- ❌ Make recommendations without explaining why
- ❌ Copy marketing materials or vendor descriptions
- ❌ Add technologies outside your team's area without discussion

## Questions?

- Check `radar/README.md` for entry format details
- Review existing entries in `radar/` for examples
- Ask in the merge request if you're unsure
- Contact the repository maintainers for help

## Inner Source Community

This radar is only valuable if it's actively maintained. We're looking for:

- Regular contributors who share their experiences
- Co-maintainers to help review merge requests
- Teams willing to keep their blips current

If you're interested in helping maintain this radar, please reach out!
