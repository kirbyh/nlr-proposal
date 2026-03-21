# CLAUDE.MD -- NLR Director's Fellowship Proposal

**Project:** Director's Fellowship Proposal — Tidal Array Hydrokinetic Energy
**Author:** Kirby Heck (MIT, PhD candidate)
**Target:** National Laboratory of the Rockies (NLR) Director's Fellowship
**Submission Deadline:** ~2026-04-02 (approximately 2 weeks from 2026-03-19)
**Branch:** main

---

## Core Principles

- **Plan first** -- enter plan mode before non-trivial tasks; save plans to `quality_reports/plans/`
- **Verify after** -- confirm outputs at the end of every task
- **Single source of truth** -- `manuscript/` Markdown files are authoritative; Word/PDF export is derived
- **Quality gates** -- nothing ships below 80/100
- **[LEARN] tags** -- when corrected, save `[LEARN:category] wrong → right` to MEMORY.md
- **Prose role constraint** -- Claude edits/revises existing prose. Claude does NOT generate new prose from scratch as first pass — Kirby writes first drafts, Claude refines.
- **Zotero-first citations** -- Zotero library at `C:\Users\Kirby\Zotero\storage`, subcollection `2026-NLR`. Never add bib entries directly; flag missing refs for Kirby to add via Zotero.
- **Political framing** -- Avoid climate change language and wind energy framing. Lean into energy extraction efficiency, domestic energy production, grid reliability, and national energy security.
- **Methodological hook required** -- every version of the proposal must have a clear methodological novelty claim, not just an application pitch.

---

## Strategic Framing

### Fellowship Criteria
The NLR Director's Fellowship values proposals that satisfy BOTH:
1. **High-impact application** — relevant to US energy production (tidal/hydrokinetic arrays)
2. **Methodological interest** — advances in high-fidelity or engineering modeling methods

### Kirby's Core Transfer
PhD expertise in LES + ROM of the atmospheric boundary layer (wind energy) transfers directly to:
- High-fidelity tidal array simulation (swap atmospheric BL → tidal channel flow)
- Blockage and confinement effects (amplified in tidal vs. wind)
- Wake interactions in arrays
- Rotor/structure dynamics under unsteady loading

### Research Angle Candidates (brainstorming as of 2026-03-19)
- Free surface / wave modeling or tidal coupling (high methodological novelty)
- Fluid-structure interactions for improved rotor design (→ Jason Jonkman collaboration)
- Improved rotor design under high confinement (→ Hannah Ross collaboration)
- Wake recovery in confined flow (existing literature, needs differentiation)
- Ducted rotors in tidal applications
- Bathymetric effects / micrositing in tidal basins

### NLR Collaborators
| Name | Expertise | Role |
|------|-----------|------|
| Hannah Ross | Hydrokinetic energy, blockage modeling | Primary collaborator |
| Mike Sprague | HPC, ExaWind stack | Computational support |
| Jason Jonkman | Rotor dynamics, engineering modeling | Structural dynamics |
| Misha Sinner | (TBD) | Potential collaborator |

---

## Folder Structure

```
nlr-proposal/
├── CLAUDE.md                        # This file
├── MEMORY.md                        # Persistent project learnings
├── Bibliography_base.bib            # Bibliography
├── manuscript/                      # PRIMARY: Proposal section files
│   ├── README.md                    # Proposal format guidelines
│   ├── 00_metadata.md              # Title, author, contact
│   ├── 01_overview.md              # Motivation + research gap (~0.3 page)
│   ├── 02_objectives.md            # Research questions + objectives (~0.3 page)
│   ├── 03_approach.md              # Methods + work plan (~0.8 page)
│   ├── 04_impact.md                # Broader impact + relevance (~0.3 page)
│   └── 05_references.md            # References (within 2-page limit or separate)
├── notes/                           # Call notes + working notes
├── papers/                          # Uploaded PDFs + .md summaries
├── .claude/                         # Rules, skills, agents, hooks
├── scripts/                         # Utility scripts
├── quality_reports/                 # Plans, session logs
├── explorations/                    # Research sandbox (60/100 threshold)
└── templates/                       # Session log, quality report templates
```

---

## Commands

```bash
# Export proposal to Word
pandoc manuscript/01_overview.md manuscript/02_objectives.md \
  manuscript/03_approach.md manuscript/04_impact.md \
  -o manuscript/proposal_draft.docx

# Export to PDF via LaTeX
pandoc manuscript/01_overview.md manuscript/02_objectives.md \
  manuscript/03_approach.md manuscript/04_impact.md \
  --pdf-engine=xelatex -o manuscript/proposal_draft.pdf

# Quality score
python scripts/quality_score.py manuscript/03_approach.md
```

---

## Proposal Format Requirements

- **Length:** 2 pages (hard limit — check if references count separately)
- **Format:** Research proposal (not structured like a journal article)
- **Budget:** Not required
- **Computational estimates:** Node-hours may be useful — use ExaWind/Nalu published scaling data
- **Analysis language:** Python (post-processing); ExaWind stack is C++/C
- **AI disclosure:** Confirm requirement with NLR guidelines

### Page Budget (approximate)
| Section | Target Length |
|---------|--------------|
| Motivation + gap | ~0.3 page |
| Research objectives | ~0.3 page |
| Approach + work plan | ~0.8 page |
| Broader impact | ~0.3 page |
| References | ~0.3 page (or separate) |

---

## Quality Thresholds

| Score | Gate | Meaning |
|-------|------|---------|
| 80 | Commit | Good enough to save |
| 90 | PR | Ready for mentor feedback |
| 95 | Excellence | Submission-ready |

---

## Skills Quick Reference

### Primary (Proposal Workflow)

| Command | What It Does |
|---------|-------------|
| `/review-paper [file]` | Comprehensive proposal review |
| `/proofread [file]` | Grammar/typo/consistency review |
| `/lit-review [topic]` | Literature search + synthesis |
| `/research-ideation [topic]` | Research questions + strategies |
| `/interview-me [topic]` | Interactive research interview |
| `/validate-bib` | Cross-reference citations vs bib file |
| `/commit [msg]` | Stage, commit, PR, merge |
| `/learn [skill-name]` | Extract discovery into persistent skill |
| `/context-status` | Show session health + context usage |
| `/onboard` | Re-run project configuration |

---

## Notation Conventions

| Symbol | Meaning | Units |
|--------|---------|-------|
| TBD | | |

---

## Current Proposal State

| Section | File | Status | Page Target |
|---------|------|--------|-------------|
| Metadata | `00_metadata.md` | STUB | — |
| Motivation + Gap | `01_overview.md` | STUB | ~0.3 |
| Research Objectives | `02_objectives.md` | STUB | ~0.3 |
| Approach + Work Plan | `03_approach.md` | STUB | ~0.8 |
| Broader Impact | `04_impact.md` | STUB | ~0.3 |
| References | `05_references.md` | STUB | ~0.3 |
