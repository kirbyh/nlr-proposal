---
# Always-on: loads every session (no paths filter)
---

# Manuscript Conventions: [YOUR PROJECT TITLE]

These rules apply to all work on this manuscript project. Read before any manuscript editing, data handling, or analysis task.

---

## Primary Artifact

The **Markdown section files in `manuscript/`** are the authoritative source of truth. The Word export (`manuscript/draft.docx`) is derived via Pandoc and is NOT edited directly — all edits happen in the `.md` files.

```
manuscript/00_metadata.md        → title, authors, affiliations
manuscript/01_abstract.md        → [YOUR ABSTRACT WORD LIMIT]
manuscript/02_introduction.md    → introduction
manuscript/03_materials_methods.md → methods
manuscript/04_results_discussion.md → results & discussion
manuscript/05_conclusions.md     → conclusions (if separate section)
manuscript/06_cover_letter.md    → cover letter for [YOUR JOURNAL]
manuscript/08_supporting_information.md → SI content
```

**Word export command:**
```bash
pandoc manuscript/01_abstract.md manuscript/02_introduction.md \
  manuscript/03_materials_methods.md manuscript/04_results_discussion.md \
  manuscript/05_conclusions.md -o manuscript/draft.docx
```

---

## [YOUR JOURNAL] Format Requirements

<!-- Fill in your target journal's specific requirements -->
- **Article type:** [YOUR ARTICLE TYPE]
- **Body word count:** [YOUR LIMIT]
- **Abstract:** [YOUR LIMIT] (unstructured/structured?)
- **Keywords:** [REQUIRED? HOW MANY?]
- **Figures + Tables:** [LIMITS?]
- **Citation style:** [YOUR STYLE] (e.g., ACS numbered superscripts, APA author-year)
- **Figure submission format:** [FORMAT, DPI]
- **Data availability:** [REQUIRED?]
- **Abbreviations:** [RULES]

---

## Citation Format

<!-- Customize for your citation style -->
- In text: [YOUR FORMAT] (e.g., `[1]`, `[2,3]` for numbered; `(Smith et al., 2020)` for author-year)
- In `Bibliography_base.bib`: key format `AuthorYYYY_keyword` (e.g., `Smith2020_methodology`)
- [ANY ADDITIONAL RULES]

---

## Unit Conventions

<!-- Replace with your field's unit conventions -->

| Quantity | Preferred Unit | Notes |
|---------|---------------|-------|
| [QUANTITY 1] | [UNIT] | [NOTES] |
| [QUANTITY 2] | [UNIT] | [NOTES] |
| [QUANTITY 3] | [UNIT] | [NOTES] |

---

## Writing Style

- **Voice:** Active voice preferred (past tense for experimental descriptions)
  - Good: "We measured..."
  - Bad: "...was measured..."
- **Precision:** Every quantitative claim must include the value, units, and n= or uncertainty
- **No overclaiming:** Limitations must be stated; do not generalize beyond tested conditions
- **Concision:** [YOUR JOURNAL] audience is expert; define terms once, not repeatedly

---

## Supplementary Information (SI) Conventions

Items that belong in SI (not main text):
- Raw data tables with all replicates
- Calibration curves and QA/QC data
- Extended statistical outputs beyond summary statistics
- [ADD YOUR FIELD-SPECIFIC SI ITEMS]

Items that must stay in main text:
- [YOUR FIELD-SPECIFIC MAIN TEXT REQUIREMENTS]

---

## Toolchain (Do Not Deviate)

| Task | Tool | Claude's Role |
|------|------|--------------|
| Final publication figures | **[YOUR TOOL]** (user) | Analysis and interpretation ONLY; never generate figures |
| Intermediate data | **[YOUR TOOL]** (user) | Verify calculations; extract values into manuscript |
| Scripting / automation | **Python** | Write and run scripts on request |
| Word export | **Pandoc** | `pandoc manuscript/*.md -o manuscript/draft.docx` |
| Version control | **Git** | Standard `/commit` workflow |

**Figure rule (critical):** When the user provides an exported figure (image file), Claude describes, interprets, and suggests improvements to the figure design — but does NOT recreate it in code or propose an alternative rendering.

---

## Data Ingestion Protocols

### Lab Notebook / ELN PDFs
1. User provides PDF pages from lab notebook
2. Read using `pdf-processing.md` rule: max 5 pages per chunk, one chunk at a time
3. Extract experimental conditions, observations, and raw data into a structured Markdown table
4. Save extracted data to `quality_reports/data_verification/YYYY-MM-DD_eln_[experiment].md`
5. Use extracted table as input for Methods drafting — do not transcribe directly without structuring

### Calculation Spreadsheets
1. User provides Excel spreadsheet
2. **Independently re-derive every key calculation** from raw data (do not trust existing formulas)
3. Flag any discrepancies between spreadsheet values and re-derived values
4. Document verified values in `quality_reports/data_verification/YYYY-MM-DD_spreadsheet_[name].md`
5. Only use verified values in manuscript — if discrepancy is unresolved, ask the user

---

## Slide Infrastructure (Secondary)

The repo contains Beamer/Quarto infrastructure inherited from the template. This is preserved for potential future presentations but is **not the primary workflow**. Slide-related skills (`/compile-latex`, `/deploy`, etc.) are available but should only be used when explicitly requested.

Do not spontaneously apply slide-related rules (Beamer sync, TikZ, no-pause) to manuscript files.
