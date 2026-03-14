---
name: onboard
description: "Interactive first-run configuration for the KH Wake Modeling project. Collects project details, repo paths, and preferences via ~10 skippable questions. Updates CLAUDE.md, MEMORY.md, domain-reviewer agent, and creates external-repos.json."
user_invocable: true
---

# /onboard — Project Configuration

You are running the first-time setup for the KH Wake Modeling manuscript project. Ask the user ~10 questions to configure the project. Every question is skippable — if the user says "skip" or "later", leave the `[ASK USER]` marker in place.

## Protocol

1. **Greet** — explain this is a one-time setup that configures the project. All answers can be changed later by editing the files directly.

2. **Ask questions one at a time** (or in small groups of 2-3 related questions). Wait for answers before proceeding.

3. **After all questions**, apply the answers to the relevant files.

---

## Questions

### Group 1: Project Identity
1. **Project title** — What is the full title of this manuscript?
2. **Authors** — List all authors and their affiliations (for `00_metadata.md`)
3. **Institution** — Primary institution for CLAUDE.md header

### Group 2: External Repository Paths
4. **Analysis repo path** — Where is the analysis/post-processing repository on this machine? (Read+Write access)
5. **Obsidian vault path** — Where is your Obsidian vault with research notes? (Read + append-only)
6. **LES data repo path** — Where is the LES simulation data? (Read-only, ABSOLUTE — Claude will never write here)
7. **Dependencies/libraries path** — Any shared utility repos? (Read-only)

### Group 3: Tooling & Preferences
8. **Analysis language** — What language do you primarily use for data analysis? (Python, MATLAB, R, Julia, etc.)
9. **Zotero .bib location** — Where does Zotero export your .bib file? (Will be copied/symlinked to `Bibliography_base.bib`)
10. **Domain description** — Brief description of your specific research area (e.g., "Kelvin-Helmholtz instability in wind turbine wakes using LES") — this helps the domain-reviewer agent

### Group 4: Optional
11. **Notation conventions** — Any key symbols/notation to register? (Can be added incrementally later)
12. **Slide infrastructure** — Do you plan to use Beamer/Quarto slides for presentations? (yes/no/later)
13. **Journal formatting preferences** — Any specific WES template preferences? (single column, double column, etc.)

---

## After Collecting Answers

### Update files with collected answers:

1. **`CLAUDE.md`** — Replace `[ASK USER]` markers with actual values:
   - Project title, institution
   - Analysis language
   - Multi-repo paths
   - Notation (if provided)
   - Keywords (if provided)

2. **`manuscript/00_metadata.md`** — Fill in title, authors, affiliations

3. **`manuscript/README.md`** — Fill any remaining `[ASK USER]` markers

4. **`.claude/rules/manuscript-conventions.md`** — Fill toolchain, unit conventions (if provided)

5. **`.claude/rules/knowledge-base-template.md`** — Fill notation, models, anti-patterns (if provided)

6. **`.claude/agents/domain-reviewer.md`** — Replace `[ASK USER]` with domain description

7. **`.claude/state/external-repos.json`** — Create with repo paths:
   ```json
   {
     "analysis": {"path": "/path/to/analysis", "access": "read-write"},
     "obsidian": {"path": "/path/to/vault", "access": "read-append"},
     "les_data": {"path": "/path/to/les", "access": "read-only"},
     "dependencies": {"path": "/path/to/deps", "access": "read-only"}
   }
   ```

8. **`.claude/hooks/protect-files.sh`** — Add LES data path to protection list (if provided)

9. **`MEMORY.md`** — Add entries for:
   - Project identity (title, authors, institution)
   - External repo locations
   - User preferences (analysis language, tools)

### Final Steps

- Run `grep -r "ASK USER" CLAUDE.md .claude/rules/ .claude/agents/ manuscript/` to show remaining unconfigured items
- Tell the user they can re-run `/onboard` anytime to fill in skipped items
- Suggest next steps: "You can now start writing in manuscript/ files. Use `/interview-me` to explore your research questions, or `/lit-review` to survey the literature."
