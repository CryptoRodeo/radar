#!/bin/bash
set -eo pipefail

# Build a public version of the radar, excluding entries with 'internal: true'.
# Wraps build_radar_app.sh — patches radar/ and config.json before build,
# restores originals afterward (even on failure).

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

RADAR_DIR="$PROJECT_ROOT/radar"
CONFIG_FILE="$PROJECT_ROOT/config.json"
RADAR_BACKUP="$PROJECT_ROOT/.radar_backup"
CONFIG_BACKUP="$PROJECT_ROOT/.config_backup.json"

cleanup() {
    echo "Restoring original files..."
    if [ -d "$RADAR_BACKUP" ]; then
        rm -rf "$RADAR_DIR"
        mv "$RADAR_BACKUP" "$RADAR_DIR"
    fi
    if [ -f "$CONFIG_BACKUP" ]; then
        mv "$CONFIG_BACKUP" "$CONFIG_FILE"
    fi
}

trap cleanup EXIT

echo "=== Public Radar Build ==="
echo ""

# Back up originals
cp -r "$RADAR_DIR" "$RADAR_BACKUP"
cp "$CONFIG_FILE" "$CONFIG_BACKUP"

# Remove entries with 'internal: true' in frontmatter
removed=0
for md_file in $(find "$RADAR_DIR" -name "*.md" -not -name "README.md"); do
    # Extract frontmatter (between first two --- delimiters) and check for internal: true
    if sed -n '/^---$/,/^---$/p' "$md_file" | grep -q '^internal:[[:space:]]*true$'; then
        echo "  Excluding internal entry: $(basename "$md_file" .md)"
        rm "$md_file"
        removed=$((removed + 1))
    fi
done

echo ""
echo "Excluded $removed internal entries."
echo ""

# Patch config.json: set basePath to "/"
node -e "
const fs = require('fs');
const config = JSON.parse(fs.readFileSync('$CONFIG_FILE', 'utf8'));
config.basePath = '/';
fs.writeFileSync('$CONFIG_FILE', JSON.stringify(config, null, 2) + '\n');
"

echo "Patched config.json basePath to \"/\""
echo ""

# Run the standard build
bash "$SCRIPT_DIR/build_radar_app.sh"

echo ""
echo "=== Public radar build complete ==="
