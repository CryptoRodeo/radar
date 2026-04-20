#!/usr/bin/env python3
"""
Convert blip description fields from quoted strings to multiline YAML format.

This script converts descriptions from:
  description: 'single quoted string'
  description: "double quoted string"

To:
  description: |
    multiline block scalar format
"""

import sys
from pathlib import Path
import yaml


def convert_file(filepath: Path) -> bool:
    """Convert a single blip file. Returns True if modified."""
    # Read the file as raw text first
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse as YAML
    data = yaml.safe_load(content)

    if not data or 'description' not in data:
        return False

    description = data['description']

    # Check if description is a string (not already a multiline format)
    if not isinstance(description, str):
        return False

    # Check if file already uses multiline format (description: |)
    # by checking if the line starts with description: and has | on same line or next
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('description:'):
            # Check if it's already multiline format
            if '|' in line or (i + 1 < len(lines) and lines[i + 1].strip() == '|'):
                # Already multiline
                return False
            break

    # Convert all other fields as-is, but specially handle description
    output_lines = []
    output_lines.append(f"name: {data['name']}")
    output_lines.append(f"ring: {data['ring']}")
    output_lines.append(f"quadrant: {data['quadrant']}")
    output_lines.append(f"isNew: {str(data['isNew']).lower()}")

    # Add status if present
    if 'status' in data:
        output_lines.append(f"status: {data['status']}")

    # Add description as multiline block scalar
    output_lines.append("description: |")
    # Indent each line of the description
    for line in description.split('\n'):
        output_lines.append(f"  {line}")

    # Add contact list
    if 'contact' in data:
        output_lines.append("contact:")
        for contact in data['contact']:
            output_lines.append("  - name: " + contact.get('name', ''))
            if 'email' in contact:
                output_lines.append("    email: " + contact['email'])
            if 'slack' in contact:
                output_lines.append("    slack: " + contact['slack'])
            if 'team' in contact:
                output_lines.append("    team: " + contact['team'])

    # Add dates
    date_added = data.get('date_added')
    if isinstance(date_added, str):
        output_lines.append(f"date_added: {date_added}")
    else:
        output_lines.append(f"date_added: {date_added.isoformat()}")

    last_updated = data.get('last_updated')
    if isinstance(last_updated, str):
        output_lines.append(f"last_updated: {last_updated}")
    else:
        output_lines.append(f"last_updated: {last_updated.isoformat()}")

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines) + '\n')

    return True


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    blips_dir = project_root / "blips"

    if not blips_dir.exists():
        print(f"Error: Blips directory not found at {blips_dir}", file=sys.stderr)
        sys.exit(1)

    # Find all YAML files
    yaml_files = sorted(blips_dir.glob("**/*.yaml")) + sorted(blips_dir.glob("**/*.yml"))

    modified_count = 0

    for filepath in yaml_files:
        # Skip README files
        if filepath.name.lower().startswith("readme"):
            continue

        try:
            if convert_file(filepath):
                print(f"✓ Converted {filepath.relative_to(project_root)}")
                modified_count += 1
            else:
                print(f"  Skipped {filepath.relative_to(project_root)} (already multiline)")
        except Exception as e:
            print(f"✗ Error converting {filepath.relative_to(project_root)}: {e}", file=sys.stderr)
            sys.exit(1)

    print(f"\n✓ Converted {modified_count} file(s) to multiline format")
    return 0


if __name__ == "__main__":
    sys.exit(main())
