.PHONY: help validate build serve clean install

help:
	@echo "Portfolio & Delivery Technology Radar - Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  make install      - Install Python dependencies"
	@echo "  make validate     - Validate all radar Markdown entries"
	@echo "  make build        - Build full radar application with AOEpeople techradar"
	@echo "  make serve        - Build and serve radar locally on http://localhost:8000"
	@echo "  make clean        - Remove generated files"
	@echo "  make help         - Show this help message"

install:
	pip3 install --user -r requirements.txt

validate:
	python3 scripts/validate_blips.py

build: validate
	bash scripts/build_radar_app.sh

serve: build
	@echo ""
	@echo "Starting local server..."
	@echo "Radar available at: http://localhost:8000/"
	@echo "Press Ctrl+C to stop"
	@echo ""
	cd public && python3 -m http.server 8000

clean:
	rm -rf public .techradar
	mkdir -p public
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.pyc' -delete
