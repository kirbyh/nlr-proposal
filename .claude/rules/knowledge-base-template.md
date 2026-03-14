---
paths:
  - "manuscript/**/*.md"
  - "Figures/**"
  - "scripts/**/*.py"
  - "explorations/**"
---

# Project Knowledge Base: [YOUR PROJECT TITLE]

Read this before creating or modifying any manuscript content, figures, or analysis scripts.

---

## Notation Registry

<!-- Fill in your field's notation conventions -->

| Rule | Convention | Example | Anti-Pattern |
|------|-----------|---------|-------------|
| [SYMBOL 1] | [CONVENTION] | [EXAMPLE] | [WHAT NOT TO DO] |
| [SYMBOL 2] | [CONVENTION] | [EXAMPLE] | [WHAT NOT TO DO] |

---

## Symbol Reference

<!-- Fill in all symbols used in your manuscript -->

| Symbol | Meaning | Units |
|--------|---------|-------|
| [SYM] | [MEANING] | [UNITS] |

---

## Key Models

<!-- Fill in the models/equations used in your work -->

| Model | Equation | Notes |
|-------|---------|-------|
| [MODEL 1] | [EQUATION] | [NOTES] |
| [MODEL 2] | [EQUATION] | [NOTES] |

---

## Design Principles

<!-- Fill in your field's design principles for figures, analysis, etc. -->

| Principle | Rationale |
|-----------|----------|
| [PRINCIPLE 1] | [RATIONALE] |
| [PRINCIPLE 2] | [RATIONALE] |

---

## Anti-Patterns (Do Not Do This)

<!-- Fill in common mistakes in your field -->

| Anti-Pattern | Why It's Wrong | Correct Approach |
|-------------|----------------|-----------------|
| [ANTI-PATTERN 1] | [WHY] | [CORRECT] |
| [ANTI-PATTERN 2] | [WHY] | [CORRECT] |

---

## Python Code Conventions (scripts/)

| Convention | Rule |
|------------|------|
| Path handling | Use `pathlib.Path` or `os.path.join`; no hardcoded absolute paths |
| Data import | Excel files via `pandas.read_excel`; CSV via `pandas.read_csv` |
| Reproducibility | Set `numpy.random.seed()` if any stochastic operations |
| Output | Save processed data to `quality_reports/data_verification/`; save figures to `Figures/` |
| Comments | Explain WHY (units conversions, model assumptions), not WHAT |
| Line length | ≤100 characters except documented formulas |
