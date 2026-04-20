#!/usr/bin/env python3
"""
Validate all Markdown radar entries for the AOEpeople techradar framework.

This script validates that Markdown files in radar/ have valid frontmatter
(ring, segment, title) and non-empty body content.
"""

import sys
from pathlib import Path
from typing import Dict, List, Tuple

try:
    import yaml
except ImportError as e:
    print(f"Error: Missing required dependency: {e}")
    print("Run: pip install -r requirements.txt")
    sys.exit(1)


VALID_RINGS = {"adopt", "trial", "assess", "hold"}
VALID_SEGMENTS = {"techniques", "platforms", "tools", "tips"}


def find_markdown_files(radar_dir: Path) -> List[Path]:
    """Find all Markdown files in the radar directory."""
    return sorted(p for p in radar_dir.rglob("*.md") if p.name != "README.md")


def parse_markdown_frontmatter(filepath: Path) -> Tuple[bool, Dict, List[str]]:
    """Parse and validate frontmatter from a Markdown radar entry."""
    errors = []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return False, {}, [f"Error reading file: {e}"]

    # Check for frontmatter delimiters
    if not content.startswith("---"):
        return False, {}, ["File does not start with '---' frontmatter delimiter"]

    parts = content.split("---", 2)
    if len(parts) < 3:
        return False, {}, ["Missing closing '---' frontmatter delimiter"]

    # Parse the frontmatter YAML
    try:
        frontmatter = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        return False, {}, [f"Frontmatter YAML parsing error: {e}"]

    if not frontmatter or not isinstance(frontmatter, dict):
        return False, {}, ["Frontmatter is empty or not a dictionary"]

    # Validate required frontmatter fields
    required_fields = ["title", "ring", "segment"]
    for field in required_fields:
        if field not in frontmatter:
            errors.append(f"Missing required frontmatter field: '{field}'")

    # Validate ring value
    if "ring" in frontmatter and frontmatter["ring"] not in VALID_RINGS:
        errors.append(
            f"Invalid ring '{frontmatter['ring']}'. "
            f"Must be one of: {', '.join(sorted(VALID_RINGS))}"
        )

    # Validate segment value
    if "segment" in frontmatter and frontmatter["segment"] not in VALID_SEGMENTS:
        errors.append(
            f"Invalid segment '{frontmatter['segment']}'. "
            f"Must be one of: {', '.join(sorted(VALID_SEGMENTS))}"
        )

    # Validate featured is boolean if present
    if "featured" in frontmatter and not isinstance(frontmatter["featured"], bool):
        errors.append(f"Field 'featured' must be boolean, got: {frontmatter['featured']}")

    # Validate internal is boolean if present
    if "internal" in frontmatter and not isinstance(frontmatter["internal"], bool):
        errors.append(f"Field 'internal' must be boolean, got: {frontmatter['internal']}")

    # Validate tags is a list if present
    if "tags" in frontmatter and not isinstance(frontmatter["tags"], list):
        errors.append(f"Field 'tags' must be a list, got: {type(frontmatter['tags']).__name__}")

    # Check that body content exists (after frontmatter)
    body = parts[2].strip()
    if not body:
        errors.append("Markdown body content is empty")

    return len(errors) == 0, frontmatter, errors


def main():
    """Main validation entry point."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    radar_dir = project_root / "radar"

    print("Validating radar entries...")
    print()

    all_valid = True
    invalid_files = []

    if not radar_dir.exists():
        print("Error: radar/ directory not found", file=sys.stderr)
        sys.exit(1)

    md_files = find_markdown_files(radar_dir)

    if not md_files:
        print("Warning: No Markdown files found in radar/", file=sys.stderr)
        sys.exit(0)

    print(f"Found {len(md_files)} Markdown radar entries in radar/")
    print()

    for md_path in md_files:
        relative_path = md_path.relative_to(project_root)
        is_valid, frontmatter, errors = parse_markdown_frontmatter(md_path)

        if is_valid:
            print(f"  ✓ {relative_path}")
        else:
            print(f"  ✗ {relative_path}")
            for error in errors:
                print(f"    - {error}")
            all_valid = False
            invalid_files.append(relative_path)

    print()

    if all_valid:
        print(f"✓ All {len(md_files)} radar entries are valid!")
        sys.exit(0)
    else:
        print(f"✗ Validation failed: {len(invalid_files)} file(s) have errors")
        print()
        print("Invalid files:")
        for f in invalid_files:
            print(f"  - {f}")
        sys.exit(1)


if __name__ == "__main__":
    main()
