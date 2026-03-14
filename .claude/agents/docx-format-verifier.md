# DOCX Format Verifier Agent

**Purpose:** Verify that `manuscript/draft.docx` matches [YOUR JOURNAL] formatting requirements after Pandoc export.

## When to Use

After running `scripts/export_manuscript.sh`, invoke this agent to check formatting and iterate on fixes.

## Workflow

1. Run `python scripts/verify_docx_format.py` and capture output
2. If all PASS: report success
3. If any FAIL:
   - Identify root cause (reference.docx style issue, Lua filter gap, Pandoc behavior)
   - Apply fix to the appropriate source file:
     - Style issues → `scripts/generate_reference_docx.py`
     - Unicode conversion → `scripts/unicode-sub-super.lua`
     - Content issues → `manuscript/*.md` source files
   - Re-run: `python scripts/generate_reference_docx.py` (if reference changed)
   - Re-run: `bash scripts/export_manuscript.sh`
   - Re-run: `python scripts/verify_docx_format.py`
4. Loop steps 2-3 up to **5 rounds**
5. After max rounds or all PASS: present summary to user

## WARN Items (manual steps)

Some items may show WARN and require manual Word steps:
- **Line numbers:** Layout > Line Numbers > Continuous
- **Page numbers:** Insert > Page Number > Bottom of Page > Plain Number 3
- **Title bold:** May need manual bold if custom-style div doesn't carry through

Report these clearly so the user knows what to do after opening the .docx.

## Exit Criteria

- All automated checks PASS, or
- Only WARN items remain (with clear manual instructions), or
- 5 fix rounds exhausted (report remaining issues)
