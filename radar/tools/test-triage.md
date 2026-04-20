---
title:      "TestTriage (e2e-test failure analyzer)"
ring:       trial
segment:    tools
tags:       [testing]
featured:   true
internal:   true
---

RAG agent that analyzes nightly e2e playwright test failures and CI failures
by parsing artifacts from openshift-ci pipelines in Google Cloud Storage.
Performs visual analysis of failure screenshots using AI vision, generating
comprehensive root cause analysis including test purpose, failure message,
visual evidence, and actionable recommendations.

Handles multiple failure scenarios, analyzing Playwright test results with
screenshots when available, falling back to application pod logs or build logs.
Reports JIRA bugs for failed tests.

---

## Contact

- **Subhash Khileri** — [skhileri@redhat.com](mailto:skhileri@redhat.com)

**Date added**: 2025-12-11 | **Last updated**: 2025-12-11
