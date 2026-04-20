# Portfolio & Delivery AI Technology Radar

A community-maintained technology radar about use of AI tech in the Portfolio and Delivery organization (under Shai Revivo) to share experiences, successes, and lessons learned with various technologies.

View the rendered radar at https://pnd.pages.redhat.com/ai/radar/

## Purpose

This radar serves as a living knowledge base where teams can:

- **Recommend technologies** that have proven successful in real projects
- **Warn against technologies** that have caused problems based on actual experience
- **Highlight emerging tools** worth experimenting with
- **Share stories** - both success stories and cautionary tales

## How It Works

Each technology (a "blip" on the radar) is a Markdown file with YAML frontmatter in the `radar/` directory, organized by date. Teams and individuals contribute their experiences by adding or updating these Markdown files. A GitLab CI pipeline validates the entries and builds an interactive radar visualization using the [AOEpeople techradar](https://github.com/AOEpeople/aoe_technology_radar) framework, published via GitLab Pages.

## Current Status

**This is a proof of concept.** The radar will become a living, maintained resource only if we can attract an active inner source community around it. Contributions, feedback, and co-maintainers are welcome!

## Relationship to Other Initiatives

Unlike catalog-style registries (e.g., inscope.corp.redhat.com/ai-projects), this radar is **curated and opinionated**. Entries represent judgments based on real experience, helping late adopters follow in the footsteps of early adopters who found success.

The radar is scoped to Portfolio and Delivery but follows an inner source model—peer organizations are welcome to collaborate if they find it valuable.

## Technology Position (Rings)

- **Adopt**: Technologies we have high confidence in and actively use in production
- **Trial**: Technologies worth pursuing in projects that can handle the risk
- **Assess**: Technologies worth exploring to understand their potential
- **Hold**: Technologies to proceed with caution or avoid based on experience

## Directory Structure

Radar entries are organized by quadrant in the `radar/` directory. Each Markdown file contains YAML frontmatter specifying the title, ring, and segment (quadrant).

```
radar/
├── techniques/          # Development and process techniques
├── platforms/           # Infrastructure, deployment, and cloud platforms
├── tools/              # Development and operational tools
└── tips/               # Tips and recommendations
```

## Contributing

1. Add or update a Markdown file in `radar/<quadrant>/` (e.g., `radar/tools/my-tool.md`)
2. Include frontmatter with `title`, `ring`, `segment`, `tags`, and `featured` fields
3. Submit a merge request
4. The pipeline will validate and build the radar with your changes
5. Once merged to `main`, the radar is automatically updated

### Entry format

```markdown
---
title:      "My Technology"
ring:       assess
segment:    tools
tags:       []
featured:   false
---

Description of the technology and your experience with it.
```

Valid rings: `adopt`, `trial`, `assess`, `hold`
Valid segments: `techniques`, `platforms`, `tools`, `tips`

## Local Development

### Prerequisites

- **Python 3.11+**: For validating radar entries
- **Node.js 20+**: For building the full radar visualization (optional, only needed for `make build` and `make serve`)

### Setup

#### Linux

```bash
# Install Python dependencies
make install
```

#### macOS

```bash
# Create a virtual environment (required on modern macOS due to PEP 668)
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> **Note for macOS users**: Modern Python installations via Homebrew block system-wide pip installs. You must use a virtual environment and activate it before running make commands.

### Commands

```bash
# Activate virtual environment first (macOS)
source .venv/bin/activate

# Install Python dependencies (Linux, or if not using venv)
make install

# Validate all radar entries
make validate

# Build the complete radar application (requires Node.js)
# This builds the AOEpeople techradar with our data
make build

# Build and serve the radar locally at http://localhost:8000 (requires Node.js)
make serve

# Clean all generated files
make clean
```

### Quick Testing

For quick validation of your changes without Node.js:
```bash
make validate
```

For full preview of how the radar will look:
```bash
make serve
```
Then visit http://localhost:8000 in your browser to see the interactive radar with your blips.

## Visualization

This radar uses the open-source [AOEpeople techradar](https://github.com/AOEpeople/aoe_technology_radar) framework to visualize the technology landscape. We reuse their framework rather than building custom visualization, keeping maintenance minimal.

The build process:
1. Validates Markdown entries in the `radar/` directory
2. Builds the AOEpeople techradar static site using Next.js
3. Publishes everything to GitLab Pages

When you visit the published radar, it displays an interactive visualization of your team's technology blips organized by quadrant and ring.
