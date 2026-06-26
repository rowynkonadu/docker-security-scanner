#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
IMAGE="${1:-}"

if [ -z "$IMAGE" ]; then
  echo "Usage: $0 <docker-image>"
  exit 1
fi

if command -v python3 >/dev/null 2>&1; then
  PYTHON=python3
elif command -v python >/dev/null 2>&1; then
  PYTHON=python
else
  echo "Error: python3 or python is required to generate the HTML report."
  exit 1
fi

echo "Scanning $IMAGE..."
docker run --rm -v "$SCRIPT_DIR:/out" aquasec/trivy image --format json -o /out/trivy.json "$IMAGE"
"$PYTHON" "$SCRIPT_DIR/src/generate_report.py"
echo "Done. Open $SCRIPT_DIR/report.html"
