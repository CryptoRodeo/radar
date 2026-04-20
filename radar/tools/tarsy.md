---
title:      "TARSy"
ring:       assess
segment:    tools
tags:       [sre-observability]
featured:   true
internal:   true
---

TARSy is an intelligent Site Reliability Engineering system that automatically
processes alerts through sequential agent chains, retrieves runbooks,
and uses MCP (Model Context Protocol) servers to gather system information
for comprehensive multi-stage incident analysis.

It's designed to handle complex incident scenarios where multiple agents
collaborate to diagnose issues and provide recommendations for remediation.
It integrates with MCP servers to access system information, ensuring a
systematic approach to incident response.

TARSy was developed (and is still being actively developed and enhanced) by the Dev Sandbox
team as an open source project. It's already used daily by the team for alert analysis and
remediation in production, saving hours of manual investigation of various system alerts
including Kubernetes, ArgoCD, suspicious user activities, AWS alerts, and more.

More information about TARSy can be found here: https://docs.google.com/presentation/d/1vT2sTL2FyTElhEoLQCngGWce0g80RLCHmDEhF2VEVUI/edit?usp=sharing
and here: https://github.com/codeready-toolchain/tarsy-bot

See also a short demo recording (9m): https://drive.google.com/file/d/1R5exZTm4t5S4I2qZ1g1-iBKUf_gkCLZ0/view
and a longer demo with the RHDH team: https://drive.google.com/file/d/1i76pxFLjvqoOtWqSkd-oM-2iIV8lIhnj/view

---

## Contact

- **Alexey Kazakov** — [alkazako@redhat.com](mailto:alkazako@redhat.com) — (Developer Sandbox)

**Maturity**: stable

**Date added**: 2026-01-21 | **Last updated**: 2026-01-21
