# CLAUDE.MD -- Research Manuscript Development with Claude Code

**Project:** [YOUR PROJECT TITLE]
**Institution:** [YOUR INSTITUTION]
**Journal Target:** [YOUR TARGET JOURNAL] — [ARTICLE TYPE]
**Branch:** main

---

## Core Principles

- **Plan first** -- enter plan mode before non-trivial tasks; save plans to `quality_reports/plans/`
- **Verify after** -- confirm outputs at the end of every task
- **Single source of truth** -- `manuscript/` Markdown files are authoritative; Word export is derived
- **Quality gates** -- nothing ships below 80/100
- **[LEARN] tags** -- when corrected, save `[LEARN:category] wrong → right` to MEMORY.md
- **Figures: analysis only** -- Claude interprets figures but never generates them (use your preferred tool)
- **Verify calculations** -- all spreadsheet values must be independently re-derived before use

---

## Folder Structure

```
[YOUR-PROJECT-NAME]/
├── CLAUDE.md                        # This file
├── MEMORY.md                        # Persistent project learnings
├── Bibliography_base.bib            # Bibliography ([YOUR CITATION STYLE])
├── Figures/                         # Exported figures + raw images
├── manuscript/                      # PRIMARY: Markdown section files
│   ├── README.md                    # Submission guidelines
│   ├── 00_metadata.md               # Title, authors, affiliations
│   ├── 01_abstract.md               # [YOUR ABSTRACT WORD LIMIT]
│   ├── 02_introduction.md           # Introduction
│   ├── 03_materials_methods.md      # Methods
│   ├── 04_results_discussion.md     # Results & Discussion
│   ├── 05_conclusions.md            # Conclusions (if separate)
│   ├── 06_cover_letter.md           # Cover letter
│   └── 08_supporting_information.md # SI content
├── .claude/                         # Rules, skills, agents, hooks
├── scripts/                         # Utility scripts
├── quality_reports/                 # Plans, session logs, merge reports, data verification
├── explorations/                    # Research sandbox (fast-track, 60/100 threshold)
├── templates/                       # Session log, quality report templates
├── master_supporting_docs/          # Supporting papers and reference materials
│
│   -- SECONDARY (slides for future presentations) --
├── Slides/                          # Beamer .tex files (if needed)
├── Quarto/                          # RevealJS .qmd files (if needed)
├── Preambles/header.tex             # LaTeX headers
└── docs/                            # GitHub Pages (auto-generated from slides)
```

---

## Commands

```bash
# Export manuscript to Word (primary output)
pandoc manuscript/01_abstract.md manuscript/02_introduction.md \
  manuscript/03_materials_methods.md manuscript/04_results_discussion.md \
  -o manuscript/draft.docx

# Quality score (for any file type)
python scripts/quality_score.py manuscript/04_results_discussion.md

# LaTeX slides (secondary — only if preparing presentations)
cd Slides && TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode file.tex
BIBINPUTS=..:$BIBINPUTS bibtex file
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode file.tex
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode file.tex
```

---

## Quality Thresholds

| Score | Gate | Meaning |
|-------|------|---------|
| 80 | Commit | Good enough to save |
| 90 | PR | Peer-review ready |
| 95 | Excellence | Submission-ready |

---

## Skills Quick Reference

### Primary (Manuscript Workflow)

| Command | What It Does |
|---------|-------------|
| `/review-paper [file]` | Comprehensive manuscript review |
| `/proofread [file]` | Grammar/typo/consistency review |
| `/lit-review [topic]` | Literature search + synthesis |
| `/research-ideation [topic]` | Research questions + strategies |
| `/interview-me [topic]` | Interactive research interview |
| `/validate-bib` | Cross-reference citations vs bib file |
| `/commit [msg]` | Stage, commit, PR, merge |
| `/learn [skill-name]` | Extract discovery into persistent skill |
| `/context-status` | Show session health + context usage |
| `/deep-audit` | Repository-wide consistency audit |

### Secondary (Data Analysis & Scripting)

| Command | What It Does |
|---------|-------------|
| `/data-analysis [dataset]` | End-to-end analysis workflow |

### Tertiary (Slides — only if needed)

| Command | What It Does |
|---------|-------------|
| `/compile-latex [file]` | 3-pass XeLaTeX + bibtex |
| `/deploy [LectureN]` | Render Quarto + sync to docs/ |
| `/translate-to-quarto [file]` | Beamer → Quarto translation |
| `/visual-audit [file]` | Slide layout audit |
| `/pedagogy-review [file]` | Narrative, notation, pacing review |
| `/qa-quarto [LectureN]` | Adversarial Quarto vs Beamer QA |
| `/slide-excellence [file]` | Combined multi-agent review |

---

## Notation Conventions ([YOUR FIELD])

<!-- Replace with your field's notation conventions -->

| Symbol | Meaning | Units |
|--------|---------|-------|
| *[SYM1]* | [Description] | [Units] |
| *[SYM2]* | [Description] | [Units] |
| *[SYM3]* | [Description] | [Units] |

---

## Current Manuscript State

| Section | File | Status | Word Target |
|---------|------|--------|-------------|
| Metadata | `00_metadata.md` | STUB | — |
| Abstract | `01_abstract.md` | STUB | [YOUR LIMIT] |
| Introduction | `02_introduction.md` | STUB | [YOUR LIMIT] |
| Materials & Methods | `03_materials_methods.md` | STUB | [YOUR LIMIT] |
| Results & Discussion | `04_results_discussion.md` | STUB | [YOUR LIMIT] |
| Conclusions | `05_conclusions.md` | STUB | [YOUR LIMIT] |
| Cover Letter | `06_cover_letter.md` | STUB | — |
| SI | `08_supporting_information.md` | STUB | — |

**[YOUR JOURNAL] Format Requirements:**
<!-- Fill in your target journal's specific format requirements -->
- **Article type:** [YOUR ARTICLE TYPE]
- **Body word count:** [YOUR LIMIT]
- **Abstract:** [YOUR LIMIT]
- **Keywords:** [REQUIRED? HOW MANY?]
- **Citation style:** [YOUR STYLE]
- **Data availability:** [REQUIRED?]
