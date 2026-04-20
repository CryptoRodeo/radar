#!/usr/bin/env python3
"""
Convert contact field from object to list in all blip files.
"""

import sys
from pathlib import Path
import yaml

def convert_contact_to_list(filepath: Path):
    """Convert contact from object to list if needed."""
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)

    # Convert contact from object to list if it's not already a list
    if 'contact' in data and not isinstance(data['contact'], list):
        data['contact'] = [data['contact']]

        with open(filepath, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        return True
    return False

def main():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    blips_dir = project_root / "blips"

    # Find all YAML files
    blip_files = list(blips_dir.rglob("*.yaml")) + list(blips_dir.rglob("*.yml"))
    blip_files = [f for f in blip_files if not f.name.lower().startswith("readme")]

    updated = 0
    for filepath in sorted(blip_files):
        if convert_contact_to_list(filepath):
            print(f"  ✓ Updated {filepath.relative_to(project_root)}")
            updated += 1

    print(f"\n✓ Converted {updated} blip file(s) to use contact as list")
    return 0

if __name__ == "__main__":
    sys.exit(main())
