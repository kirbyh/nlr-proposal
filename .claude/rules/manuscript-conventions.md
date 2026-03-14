---
paths:
  - "manuscript/**/*.md"
  - "Bibliography_base.bib"
---

# Manuscript Conventions: KH Wake Modeling

These rules apply to all work on this manuscript project. Read before any manuscript editing, data handling, or analysis task.

---

## Primary Artifact

The **Markdown section files in `manuscript/`** are the authoritative source of truth. The Word export (`manuscript/draft.docx`) is derived via Pandoc and is NOT edited directly — all edits happen in the `.md` files.

```
manuscript/00_metadata.md           → title, authors, affiliations
manuscript/01_abstract.md           → abstract (~200-300 words)
manuscript/02_introduction.md       → introduction
manuscript/03_materials_methods.md  → methods
manuscript/04_results_discussion.md → results & discussion
manuscript/05_conclusions.md        → conclusions
manuscript/06_cover_letter.md       → cover letter for WES
manuscript/07_data_availability.md  → code and data availability (WES required)
manuscript/08_supporting_information.md → SI content
```

**Word export command:**
```bash
pandoc manuscript/01_abstract.md manuscript/02_introduction.md \
  manuscript/03_materials_methods.md manuscript/04_results_discussion.md \
  manuscript/05_conclusions.md manuscript/07_data_availability.md \
  -o manuscript/draft.docx
```

---

## Role Constraint

**Claude edits/revises existing prose and debugs code — Claude does NOT generate new prose from scratch as first pass.** The user writes first drafts; Claude refines, restructures, and improves them. This ensures the user's voice and domain expertise drive the narrative.

Exceptions:
- Boilerplate sections (data availability, author contributions) may be drafted by Claude
- Code comments and documentation may be written by Claude
- Outline/structure suggestions are fine — but full paragraph generation requires user's first draft

---

## Wind Energy Science Format Requirements

- **Article type:** Research Article
- **Body word count:** No strict limit (typical: 6000-10000 words)
- **Abstract:** ~200-300 words (unstructured)
- **Keywords:** [ASK USER — typically 4-8]
- **Figures + Tables:** No strict limit
- **Citation style:** Copernicus author-year — `Smith et al. (2020)` or `(Smith et al., 2020)`
- **Figure submission format:** PDF, PNG, or EPS; min 300 DPI for raster
- **Data availability:** **Required** — Code and Data Availability section
- **AI disclosure:** **Required** — must disclose AI tool usage
- **License:** CC BY 4.0 (open access, mandatory)
- **Formatting details:** [ASK USER — specific preferences]

---

## Citation Format (Zotero-First)

- In text: `Smith et al. (2020)` (narrative) or `(Smith et al., 2020)` (parenthetical)
- In Markdown: `[@Smith2020]` or `[@Smith2020; @Jones2021]` for Pandoc
- In `Bibliography_base.bib`: managed via Zotero export only — see `.claude/rules/zotero-citation-workflow.md`
- **Never add entries to .bib directly** — flag missing refs for user to add via Zotero

---

## Unit Conventions

| Quantity | Preferred Unit | Notes |
|---------|---------------|-------|
| [ASK USER] | | |

---

## Writing Style

- **Voice:** Active voice preferred (past tense for methods/results)
  - Good: "We simulated..."
  - Bad: "...was simulated..."
- **Precision:** Every quantitative claim must include the value, units, and uncertainty where applicable
- **No overclaiming:** Limitations must be stated; do not generalize beyond tested conditions
- **Concision:** WES audience is expert; define terms once, not repeatedly

---

## Supplementary Information (SI) Conventions

Items that belong in SI (not main text):
- Extended sensitivity analysis tables
- Grid convergence details beyond summary
- Additional validation cases
- Raw data tables
- [ASK USER — field-specific SI items]

Items that must stay in main text:
- Primary results and key comparisons
- Main validation case
- [ASK USER — field-specific main text requirements]

---

## Toolchain (Do Not Deviate)

| Task | Tool | Claude's Role |
|------|------|--------------|
| Final publication figures | **[ASK USER]** (user) | Analysis and interpretation ONLY; never generate figures |
| Data processing | **[ASK USER]** (user) | Verify calculations; extract values into manuscript |
| Scripting / automation | **[ASK USER]** | Write and run scripts on request |
| Word export | **Pandoc** | `pandoc manuscript/*.md -o manuscript/draft.docx` |
| Version control | **Git** | Standard `/commit` workflow |

**Figure rule (critical):** When the user provides an exported figure (image file), Claude describes, interprets, and suggests improvements to the figure design — but does NOT recreate it in code or propose an alternative rendering.

---

## Data Ingestion Protocols

### Calculation Spreadsheets
1. User provides spreadsheet
2. **Independently re-derive every key calculation** from raw data (do not trust existing formulas)
3. Flag any discrepancies between spreadsheet values and re-derived values
4. Document verified values in `quality_reports/data_verification/YYYY-MM-DD_spreadsheet_[name].md`
5. Only use verified values in manuscript — if discrepancy is unresolved, ask the user

### LES / Simulation Data
1. Data resides in the LES repo (read-only — see multi-repo-workflow rule)
2. Extract relevant statistics via scripts in the analysis repo
3. Document data provenance: simulation case name, grid resolution, averaging period
4. Cross-check extracted values against user's Obsidian notes where available

---

## Slide Infrastructure (Secondary)

The repo contains Beamer/Quarto infrastructure inherited from the template. This is preserved for potential future presentations but is **not the primary workflow**. Slide-related skills (`/compile-latex`, `/deploy`, etc.) are available but should only be used when explicitly requested.

Do not spontaneously apply slide-related rules (Beamer sync, TikZ, no-pause) to manuscript files.
