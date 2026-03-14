# Manuscript: Submission Guidelines

**Journal:** Wind Energy Science (WES)
**Publisher:** Copernicus Publications
**Article Type:** Research Article

---

## Submission Requirements

| Item | Requirement |
|------|-------------|
| Article type | Research Article |
| Body word count | No strict limit (typical: 6000-10000 words) |
| Abstract | ~200-300 words (unstructured) |
| Keywords | [ASK USER — typically 4-8] |
| Figures + Tables | No strict limit |
| Citation style | Author-year (Copernicus style) |
| Figure format | PDF, PNG, or EPS; min 300 DPI for raster |
| Data availability | **Required** — Code and Data Availability section mandatory |
| AI disclosure | **Required** — must disclose AI tool usage |
| License | CC BY 4.0 (open access) |

---

## Required Sections (in order)

1. **Title/Authorship** — Title, author list, affiliations, correspondence
2. **Abstract + Keywords**
3. **Introduction**
4. **Materials and Methods** (or appropriate heading)
5. **Results and Discussion** (can be combined or separate)
6. **Conclusions**
7. **Code and Data Availability** — repository URLs, DOIs, access instructions
8. **Author Contributions** — CRediT-style recommended
9. **Competing Interests** — must declare
10. **Acknowledgments**
11. **References** — Copernicus author-year style
12. **Appendices / Supporting Information** (if applicable)

---

## Copernicus-Specific Notes

- **Two-stage review:** Discussion paper (open) → revised manuscript → final paper
- **LaTeX template available:** Copernicus provides `copernicus.cls` for submission
- **Author-year citations:** `\citet{Smith2020}` → Smith (2020); `\citep{Smith2020}` → (Smith, 2020)
- **Open access:** All WES papers are CC BY 4.0
- **Formatting details:** [ASK USER — specific template preferences, single/double column, etc.]

---

## File Structure

```
manuscript/
├── README.md                      # This file (submission guidelines)
├── 00_metadata.md                 # Title, authors, affiliations
├── 01_abstract.md                 # Abstract
├── 02_introduction.md             # Introduction
├── 03_materials_methods.md        # Methods
├── 04_results_discussion.md       # Results & Discussion
├── 05_conclusions.md              # Conclusions
├── 06_cover_letter.md             # Cover letter for WES
├── 07_data_availability.md        # Code and Data Availability (WES required)
├── 08_supporting_information.md   # SI content
└── draft.docx                     # Pandoc export (do NOT edit directly)
```

**Export to Word:**
```bash
pandoc manuscript/01_abstract.md manuscript/02_introduction.md \
  manuscript/03_materials_methods.md manuscript/04_results_discussion.md \
  manuscript/05_conclusions.md manuscript/07_data_availability.md \
  -o manuscript/draft.docx
```
