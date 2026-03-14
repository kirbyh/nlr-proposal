#!/usr/bin/env bash
# export_manuscript.sh — Export manuscript Markdown to formatted Word document
# Usage: bash scripts/export_manuscript.sh
#
# Prerequisites:
#   1. manuscript/reference.docx exists (run: python scripts/generate_reference_docx.py)
#   2. pandoc >= 3.0 installed

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
MANUSCRIPT_DIR="${REPO_DIR}/manuscript"
SCRIPTS_DIR="${REPO_DIR}/scripts"
OUTPUT="${MANUSCRIPT_DIR}/draft.docx"
REFERENCE="${MANUSCRIPT_DIR}/reference.docx"
LUA_FILTER="${SCRIPTS_DIR}/unicode-sub-super.lua"

# Check prerequisites
if [ ! -f "$REFERENCE" ]; then
    echo "ERROR: reference.docx not found. Run: python scripts/generate_reference_docx.py"
    exit 1
fi

if [ ! -f "$LUA_FILTER" ]; then
    echo "ERROR: Lua filter not found at ${LUA_FILTER}"
    exit 1
fi

echo "Exporting manuscript to Word..."

# Customize this file list for your manuscript sections
pandoc \
    "${MANUSCRIPT_DIR}/01_abstract.md" \
    "${MANUSCRIPT_DIR}/02_introduction.md" \
    "${MANUSCRIPT_DIR}/03_materials_methods.md" \
    "${MANUSCRIPT_DIR}/04_results_discussion.md" \
    --reference-doc="${REFERENCE}" \
    --lua-filter="${LUA_FILTER}" \
    --standalone \
    -o "${OUTPUT}"

echo "Exported: ${OUTPUT}"
echo "File size: $(wc -c < "${OUTPUT}") bytes"
