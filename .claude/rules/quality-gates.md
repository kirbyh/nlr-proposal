---
paths:
  - "manuscript/**/*.md"
  - "Slides/**/*.tex"
  - "Quarto/**/*.qmd"
  - "scripts/**/*.py"
  - "scripts/**/*.R"
---

# Quality Gates & Scoring Rubrics

## Thresholds

- **80/100 = Commit** -- good enough to save
- **90/100 = PR** -- ready for deployment
- **95/100 = Excellence** -- aspirational

## Quarto Slides (.qmd)

| Severity | Issue | Deduction |
|----------|-------|-----------|
| Critical | Compilation failure | -100 |
| Critical | Equation overflow | -20 |
| Critical | Broken citation | -15 |
| Critical | Typo in equation | -10 |
| Major | Text overflow | -5 |
| Major | TikZ label overlap | -5 |
| Major | Notation inconsistency | -3 |
| Minor | Font size reduction | -1 per slide |
| Minor | Long lines (>100 chars) | -1 (EXCEPT documented math formulas) |

## R Scripts (.R)

| Severity | Issue | Deduction |
|----------|-------|-----------|
| Critical | Syntax errors | -100 |
| Critical | Domain-specific bugs | -30 |
| Critical | Hardcoded absolute paths | -20 |
| Major | Missing set.seed() | -10 |
| Major | Missing figure generation | -5 |

## Beamer Slides (.tex)

| Severity | Issue | Deduction |
|----------|-------|-----------|
| Critical | XeLaTeX compilation failure | -100 |
| Critical | Undefined citation | -15 |
| Critical | Overfull hbox > 10pt | -10 |

## Enforcement

- **Score < 80:** Block commit. List blocking issues.
- **Score < 90:** Allow commit, warn. List recommendations.
- User can override with justification.

## Quality Reports

Generated **only at merge time**. Use `templates/quality-report.md` for format.
Save to `quality_reports/merges/YYYY-MM-DD_[branch-name].md`.

## Manuscript Sections (.md in manuscript/)

<!-- Customize these for your field -->

| Severity | Issue | Deduction |
|----------|-------|-----------|
| Critical | Incorrect equation or units | -20 |
| Critical | Calculation error | -20 |
| Critical | Unverified value from spreadsheet (not independently re-derived) | -15 |
| Critical | Citation in text missing from Bibliography_base.bib | -15 |
| Major | Missing experimental condition | -10 |
| Major | Comparison to literature in inconsistent units | -8 |
| Major | Word count exceeds journal limit | -5 |
| Major | Abstract outside word limit range | -5 |
| Minor | Notation inconsistency (symbol used differently in two sections) | -3 |
| Minor | Missing error bars or n= in figure caption | -2 |
| Minor | Passive voice overuse (>30% of sentences) | -1 |

## Tolerance Thresholds ([YOUR FIELD])

<!-- Replace with your field's tolerance thresholds -->

| Quantity | Tolerance | Rationale |
|----------|-----------|-----------|
| [QUANTITY 1] | [TOLERANCE] | [RATIONALE] |
| [QUANTITY 2] | [TOLERANCE] | [RATIONALE] |
| [QUANTITY 3] | [TOLERANCE] | [RATIONALE] |
