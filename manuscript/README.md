# Manuscript: Submission Guidelines

**Journal:** [YOUR TARGET JOURNAL]
**Publisher:** [YOUR PUBLISHER]
**Article Type:** [YOUR ARTICLE TYPE]

---

## Submission Requirements

<!-- Fill in your target journal's specific requirements -->

| Item | Requirement |
|------|-------------|
| Article type | [YOUR ARTICLE TYPE] |
| Body word count | [YOUR LIMIT] |
| Abstract | [YOUR LIMIT] |
| Keywords | [REQUIRED? HOW MANY?] |
| Figures + Tables | [LIMITS?] |
| Citation style | [YOUR STYLE] |
| Figure format | [FORMAT, DPI] |
| Data availability | [REQUIRED?] |

---

## Required Sections (in order)

<!-- Customize for your journal -->

1. **Title/Authorship** — Title, author list, affiliations
2. **Abstract + Keywords**
3. **Introduction**
4. **Materials and Methods**
5. **Results and Discussion**
6. **Conclusions** (if separate)
7. **Acknowledgments**
8. **References**
9. **Supporting Information**

---

## File Structure

```
manuscript/
├── README.md                   # This file (submission guidelines)
├── 00_metadata.md              # Title, authors, affiliations
├── 01_abstract.md              # Abstract
├── 02_introduction.md          # Introduction
├── 03_materials_methods.md     # Methods
├── 04_results_discussion.md    # Results & Discussion
├── 05_conclusions.md           # Conclusions (if separate)
├── 06_cover_letter.md          # Cover letter for submission
├── 08_supporting_information.md # SI content
└── draft.docx                  # Pandoc export (do NOT edit directly)
```

**Export to Word:**
```bash
pandoc manuscript/01_abstract.md manuscript/02_introduction.md \
  manuscript/03_materials_methods.md manuscript/04_results_discussion.md \
  -o manuscript/draft.docx
```
