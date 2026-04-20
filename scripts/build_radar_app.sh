#!/bin/bash
set -eo pipefail

# Script to build the radar application using AOEpeople techradar framework
# This sets up the .techradar builder directory and builds a static radar site.

PUBLIC_DIR="public"
BUILDER_DIR=".techradar"
SOURCE_DIR="node_modules/aoe_technology_radar"

echo "Building Technology Radar with AOEpeople techradar framework..."

# Install top-level dependencies if needed
if [ ! -d "node_modules/aoe_technology_radar" ]; then
    echo "Installing top-level dependencies..."
    NODE_ENV=development npm install --prefer-offline
fi

# Check if we need to recreate the builder directory
CURRENT_HASH=$(sha256sum package.json | cut -d' ' -f1)
EXISTING_HASH=""
if [ -f "$BUILDER_DIR/hash" ]; then
    EXISTING_HASH=$(cat "$BUILDER_DIR/hash")
fi

if [ "$CURRENT_HASH" != "$EXISTING_HASH" ] || [ ! -d "$BUILDER_DIR" ] || [ ! -f "$BUILDER_DIR/package.json" ]; then
    echo "Setting up techradar builder..."
    rm -rf "$BUILDER_DIR"
    cp -r "$SOURCE_DIR" "$BUILDER_DIR"

    # Remove husky prepare script and limit build concurrency to reduce memory usage
    cd "$BUILDER_DIR"
    node -e "
const fs = require('fs');
const pkg = JSON.parse(fs.readFileSync('package.json', 'utf8'));
delete pkg.scripts.prepare;
fs.writeFileSync('package.json', JSON.stringify(pkg, null, 2));
let cfg = fs.readFileSync('next.config.js', 'utf8');
cfg = cfg.replace('experimental: {', 'experimental: {\n    cpus: 1,');
fs.writeFileSync('next.config.js', cfg);
"
    # Install builder dependencies (need NODE_ENV=development for devDependencies)
    echo "Installing builder dependencies..."
    rm -rf node_modules package-lock.json
    NODE_ENV=development npm install --prefer-offline
    cd ..

    # Save hash
    echo "$CURRENT_HASH" > "$BUILDER_DIR/hash"
fi

# Bootstrap: create default files if they don't exist
for file in config.json about.md custom.css; do
    if [ ! -f "$file" ]; then
        echo "Warning: $file not found, creating from defaults"
        if [ "$file" = "config.json" ]; then
            cp "$SOURCE_DIR/data/config.default.json" "$file"
        elif [ "$file" = "about.md" ]; then
            cp "$SOURCE_DIR/data/about.md" "$file"
        elif [ "$file" = "custom.css" ]; then
            cp "$SOURCE_DIR/src/styles/custom.css" "$file"
        fi
    fi
done

if [ ! -d "radar" ]; then
    echo "Warning: radar/ directory not found, creating from defaults"
    cp -r "$SOURCE_DIR/data/radar" radar
fi

if [ ! -d "public" ]; then
    mkdir -p public
fi

# Copy project files into builder
echo "Syncing project files to builder..."
mkdir -p "$BUILDER_DIR/data" "$BUILDER_DIR/src/styles"
rm -rf "$BUILDER_DIR/data/radar" && cp -r radar "$BUILDER_DIR/data/radar"
cp config.json "$BUILDER_DIR/data/config.json"
cp about.md "$BUILDER_DIR/data/about.md"
cp custom.css "$BUILDER_DIR/src/styles/custom.css"
# Copy logo and generate favicon from templates
if [ -f "templates/favicon.svg" ]; then
    [ ! -f "$PUBLIC_DIR/logo.svg" ] && cp templates/favicon.svg "$PUBLIC_DIR/logo.svg"
    if command -v magick &> /dev/null; then
        magick -background none templates/favicon.svg -define icon:auto-resize=64,48,32,16 "$PUBLIC_DIR/favicon.ico"
    elif command -v convert &> /dev/null; then
        convert -background none templates/favicon.svg -define icon:auto-resize=64,48,32,16 "$PUBLIC_DIR/favicon.ico"
    fi
fi
rm -rf "$BUILDER_DIR/public" && cp -r public "$BUILDER_DIR/public"
# Remove _next from public to avoid Next.js build conflict
rm -rf "$BUILDER_DIR/public/_next"

# Build data (parse markdown entries into JSON)
echo "Building radar data..."
cd "$BUILDER_DIR"
npm run build:data

# Build static site with Next.js
echo "Building static site..."
NEXT_TELEMETRY_DISABLED=1 NODE_ENV=production npm run build
cd ..

# Copy output to public directory
echo "Copying built files..."
rm -rf "$PUBLIC_DIR"/*
cp -r "$BUILDER_DIR/out"/* "$PUBLIC_DIR/"

echo ""
echo "✓ Radar application built successfully"
echo "  Files are in $PUBLIC_DIR/"
echo ""
echo "To view the radar locally, run:"
echo "  make serve"
