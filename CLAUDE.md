# CLAUDE.MD -- KH Wake Modeling Manuscript

**Project:** [ASK USER — project title]
**Institution:** [ASK USER — institution]
**Journal Target:** Wind Energy Science (WES) — Research Article
**Branch:** main

---

## Core Principles

- **Plan first** -- enter plan mode before non-trivial tasks; save plans to `quality_reports/plans/`
- **Verify after** -- confirm outputs at the end of every task
- **Single source of truth** -- `manuscript/` Markdown files are authoritative; Word export is derived
- **Quality gates** -- nothing ships below 80/100
- **[LEARN] tags** -- when corrected, save `[LEARN:category] wrong → right` to MEMORY.md
- **Figures: analysis only** -- Claude interprets figures but never generates them (use user's preferred tool)
- **Verify calculations** -- all spreadsheet values must be independently re-derived before use
- **Prose role constraint** -- Claude edits/revises existing prose and debugs code. Claude does NOT generate new prose from scratch as first pass — the user writes first drafts, Claude refines.
- **Zotero-first citations** -- never add entries to Bibliography_base.bib directly; flag missing refs for user to add via Zotero

---

## Multi-Repository Workflow

This project spans multiple repositories. See `.claude/rules/multi-repo-workflow.md` for full details.

| Repository | Access | Path |
|-----------|--------|------|
| KH Wake Modeling (this repo) | Read + Write | (working directory) |
| Analysis repo | Read + Write | [ASK USER — set via `/onboard`] |
| Obsidian vault | Read + Append-only | [ASK USER — set via `/onboard`] |
| LES data repo | **Read-only (ABSOLUTE)** | [ASK USER — set via `/onboard`] |
| Dependencies/libraries | Read-only | [ASK USER — set via `/onboard`] |

---

## Folder Structure

```
KH-Wake-Modeling/
├── CLAUDE.md                        # This file
├── MEMORY.md                        # Persistent project learnings
├── Bibliography_base.bib            # Bibliography (Copernicus author-year)
├── Figures/                         # Exported figures + raw images
├── manuscript/                      # PRIMARY: Markdown section files
│   ├── README.md                    # WES submission guidelines
│   ├── 00_metadata.md              # Title, authors, affiliations
│   ├── 01_abstract.md              # Abstract (~200-300 words)
│   ├── 02_introduction.md          # Introduction
│   ├── 03_materials_methods.md     # Methods
│   ├── 04_results_discussion.md    # Results & Discussion
│   ├── 05_conclusions.md           # Conclusions
│   ├── 06_cover_letter.md          # Cover letter
│   ├── 07_data_availability.md     # Code and Data Availability (WES required)
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
  manuscript/05_conclusions.md manuscript/07_data_availability.md \
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
| `/onboard` | First-run interactive project configuration |

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

## Notation Conventions

<!-- [ASK USER] Fill via /onboard -->

| Symbol | Meaning | Units |
|--------|---------|-------|
| [ASK USER] | | |

---

## Wind Energy Science (WES) Format Requirements

- **Article type:** Research Article
- **Body word count:** No strict limit (typical: 6000-10000 words)
- **Abstract:** ~200-300 words (unstructured)
- **Keywords:** [ASK USER — typically 4-8]
- **Citation style:** Copernicus author-year — `Smith et al. (2020)` narrative, `(Smith et al., 2020)` parenthetical
- **Open access:** CC BY 4.0 (mandatory)
- **Data availability:** Code and Data Availability section **required**
- **AI disclosure:** **Required** — must disclose AI tool usage
- **Review process:** Two-stage — open discussion paper then revised manuscript
- **Analysis language:** [ASK USER — Python, MATLAB, R, etc.]

## Current Manuscript State

| Section | File | Status | Word Target |
|---------|------|--------|-------------|
| Metadata | `00_metadata.md` | STUB | — |
| Abstract | `01_abstract.md` | STUB | ~200-300 |
| Introduction | `02_introduction.md` | STUB | [ASK USER] |
| Materials & Methods | `03_materials_methods.md` | STUB | [ASK USER] |
| Results & Discussion | `04_results_discussion.md` | STUB | [ASK USER] |
| Conclusions | `05_conclusions.md` | STUB | [ASK USER] |
| Cover Letter | `06_cover_letter.md` | STUB | — |
| Data Availability | `07_data_availability.md` | STUB | — |
| SI | `08_supporting_information.md` | STUB | — |
