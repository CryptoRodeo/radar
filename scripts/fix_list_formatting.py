#!/usr/bin/env python3
"""
Fix list formatting in blip descriptions:
1. Convert - list markers to *
2. Add blank lines before and after lists
"""

import re
import sys
from pathlib import Path


def fix_description_lists(description: str) -> str:
    """Fix list formatting in a description string."""
    lines = description.split('\n')
    result = []
    in_list = False

    for i, line in enumerate(lines):
        # Check if this line is a list item (starts with "- " after any whitespace)
        is_list_item = bool(re.match(r'^- ', line))

        # Starting a new list - ensure blank line before
        if is_list_item and not in_list:
            # Add blank line before list if previous line wasn't blank
            if result and result[-1].strip():
                result.append('')
            in_list = True

        # Ending a list - ensure blank line after
        if not is_list_item and in_list:
            # Add blank line after list if current line isn't blank
            if line.strip():
                result.append('')
            in_list = False

        # Convert - to * for list items
        if is_list_item:
            line = re.sub(r'^- ', '* ', line)

        result.append(line)

    return '\n'.join(result)


def process_blip_file(filepath: Path) -> bool:
    """Process a single blip file. Returns True if modified."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the description block
    # Match description: |- followed by indented content until next non-indented line
    # Pattern matches either "  <content>" or blank lines
    pattern = r'(description: \|-\n)((?:  .*\n|\n)*)'

    def replace_description(match):
        prefix = match.group(1)
        desc_content = match.group(2)

        # Remove the leading 2 spaces from each line for processing
        lines = desc_content.rstrip('\n').split('\n')
        unindented = '\n'.join(line[2:] if len(line) >= 2 else line.strip() for line in lines)

        # Fix the lists
        fixed = fix_description_lists(unindented)

        # Re-indent
        fixed_lines = fixed.split('\n')
        reindented = '\n'.join(('  ' + line if line else '') for line in fixed_lines)

        return prefix + reindented + '\n'

    new_content = re.sub(pattern, replace_description, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True

    return False


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
            if process_blip_file(filepath):
                print(f"✓ Fixed lists in {filepath.relative_to(project_root)}")
                modified_count += 1
            else:
                print(f"  No changes needed in {filepath.relative_to(project_root)}")
        except Exception as e:
            print(f"✗ Error processing {filepath.relative_to(project_root)}: {e}", file=sys.stderr)
            sys.exit(1)

    print(f"\n✓ Fixed lists in {modified_count} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
