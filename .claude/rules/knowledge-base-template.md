---
paths:
  - "manuscript/**/*.md"
  - "Figures/**"
  - "scripts/**/*.py"
  - "explorations/**"
---

# Project Knowledge Base: KH Wake Modeling

Read this before creating or modifying any manuscript content, figures, or analysis scripts.

---

## Notation Registry

<!-- [ASK USER] Fill in via /onboard — wind energy / wake modeling notation -->

| Rule | Convention | Example | Anti-Pattern |
|------|-----------|---------|-------------|
| [ASK USER] | | | |

---

## Symbol Reference

<!-- [ASK USER] Fill in all symbols used in your manuscript -->

| Symbol | Meaning | Units |
|--------|---------|-------|
| [ASK USER] | | |

---

## Key Models

<!-- [ASK USER] Fill in the wake models / LES codes used -->

| Model | Equation | Notes |
|-------|---------|-------|
| [ASK USER] | | |

---

## Design Principles

<!-- [ASK USER] Fill in your field's design principles for figures, analysis, etc. -->

| Principle | Rationale |
|-----------|----------|
| [ASK USER] | |

---

## Anti-Patterns (Do Not Do This)

<!-- [ASK USER] Fill in common mistakes in your field -->

| Anti-Pattern | Why It's Wrong | Correct Approach |
|-------------|----------------|-----------------|
| [ASK USER] | | |

---

## Code Conventions (scripts/)

| Convention | Rule |
|------------|------|
| Path handling | Use `pathlib.Path` or `os.path.join`; no hardcoded absolute paths |
| Data import | Use appropriate library for file format (pandas, xarray, etc.) |
| Reproducibility | Set random seeds if any stochastic operations |
| Output | Save processed data to `quality_reports/data_verification/`; save figures to `Figures/` |
| Comments | Explain WHY (unit conversions, model assumptions), not WHAT |
| Line length | ≤100 characters except documented formulas |
