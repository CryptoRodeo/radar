#!/usr/bin/env python3
"""
Apply consistent style improvements to blip descriptions:
1. Remove "Status:" lines from description body
2. Convert section headers to markdown H2 (##)
3. Remove excessive blank lines between list items
4. Convert plain URLs to markdown links
5. Make "Note:" bold
"""

import re
import sys
from pathlib import Path


def improve_description_style(description: str) -> str:
    """Apply style improvements to a description string."""
    lines = description.split('\n')
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Remove "Status:" paragraphs (Status: followed by content)
        if re.match(r'^  Status:', line):
            # Skip this line and any continuation lines until we hit a blank line
            i += 1
            while i < len(lines) and lines[i].strip():
                i += 1
            # Also skip the blank line after status
            if i < len(lines) and not lines[i].strip():
                i += 1
            continue

        # Convert section headers to H2 markdown
        # Match lines like "Key benefits:", "Proven use cases at Red Hat:", etc.
        if re.match(r'^  [A-Z][^:]*:', line) and not line.strip().startswith('http'):
            # Don't convert if it's part of a list item continuation
            if i == 0 or not re.match(r'^  \*', lines[i-1]):
                header_text = line.strip().rstrip(':')
                line = f'  ## {header_text}:'

        # Convert "Blog:" or "GitHub:" to bold markdown
        line = re.sub(r'^  (Blog|GitHub):', r'  **\1**:', line)

        # Make "Note:" at start of line bold
        line = re.sub(r'^  Note:', r'  **Note**:', line)

        # Convert plain GitHub URLs to markdown links
        github_match = re.match(r'^  \* (.+): (https://github\.com/[^\s]+)$', line)
        if github_match:
            label = github_match.group(1)
            url = github_match.group(2)
            # Extract repo name from URL
            repo_match = re.search(r'github\.com/([^/]+/[^/]+)', url)
            if repo_match:
                repo = repo_match.group(1)
                line = f'  * {label}: [{repo}]({url})'

        # Convert plain blog URLs to markdown links
        blog_match = re.match(r'^  \* (.+): (https://(?:www\.redhat\.com|source\.redhat\.com)[^\s]+)$', line)
        if blog_match:
            label = blog_match.group(1)
            url = blog_match.group(2)
            # Create a short title from the URL
            title_match = re.search(r'/([^/]+)$', url.rstrip('/'))
            if title_match:
                title = title_match.group(1).replace('_', ' ').replace('-', ' ').title()
                line = f'  * {label}: [{label}]({url})'

        # Convert standalone blog/GitHub lines to markdown
        url_match = re.match(r'^  (Blog|GitHub): (https://[^\s]+)$', line)
        if url_match:
            label = url_match.group(1)
            url = url_match.group(2)
            if 'github.com' in url:
                repo_match = re.search(r'github\.com/([^/]+/[^/]+)', url)
                if repo_match:
                    repo = repo_match.group(1)
                    line = f'  **{label}**: [{repo}]({url})'
            else:
                # For blog URLs, use a descriptive title
                line = f'  **{label}**: [Read more]({url})'

        result.append(line)
        i += 1

    # Now remove excessive blank lines between list items
    final_result = []
    for i, line in enumerate(result):
        # If this is a blank line between two list items, skip it
        is_blank = not line.strip()
        prev_is_list = i > 0 and re.match(r'^  \*', result[i-1])
        next_is_list = i < len(result) - 1 and re.match(r'^  \*', result[i+1])

        if is_blank and prev_is_list and next_is_list:
            continue

        # Also remove blank lines that appear as list item continuations
        if is_blank and prev_is_list and i < len(result) - 1:
            # Check if next line is indented continuation
            if i + 1 < len(result) and re.match(r'^    [^ ]', result[i+1]):
                continue

        final_result.append(line)

    return '\n'.join(final_result)


def process_blip_file(filepath: Path) -> bool:
    """Process a single blip file. Returns True if modified."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the description block
    pattern = r'(description: \|-\n)((?:  .*\n|\n)*)'

    def replace_description(match):
        prefix = match.group(1)
        desc_content = match.group(2)

        # Apply style improvements directly to indented content
        improved = improve_description_style(desc_content.rstrip('\n'))

        # Return with proper formatting
        return prefix + improved + '\n'

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

        # Skip qodo and bugzooka as they're already done
        if filepath.name in ['qodo.yaml', 'bugzooka.yaml']:
            print(f"  Skipping {filepath.relative_to(project_root)} (already styled)")
            continue

        try:
            if process_blip_file(filepath):
                print(f"✓ Improved {filepath.relative_to(project_root)}")
                modified_count += 1
            else:
                print(f"  No changes needed for {filepath.relative_to(project_root)}")
        except Exception as e:
            print(f"✗ Error processing {filepath.relative_to(project_root)}: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc()
            sys.exit(1)

    print(f"\n✓ Improved {modified_count} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
