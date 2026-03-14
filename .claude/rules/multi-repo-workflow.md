# Multi-Repository Workflow

This project spans multiple repositories with different access levels. Claude must respect these tiers strictly.

---

## Access Tiers

| Repository | Access | Purpose | Path |
|-----------|--------|---------|------|
| **KH Wake Modeling** (this repo) | Read + Write | Manuscript, analysis scripts, quality reports | (working directory) |
| **Analysis repo** | Read + Write | Data processing, model runs, figure generation | [ASK USER — set via `/onboard`] |
| **Obsidian vault** | Read + Append-only | Research notes, literature summaries, meeting notes | [ASK USER — set via `/onboard`] |
| **LES data repo** | **Read-only (ABSOLUTE)** | Large-eddy simulation output data | [ASK USER — set via `/onboard`] |
| **Dependencies/libraries** | Read-only | External tools, shared utilities | [ASK USER — set via `/onboard`] |

---

## Rules

1. **LES repo is ABSOLUTE read-only.** Never write, edit, move, or delete any file in the LES data path. Not even temporary files. If a script needs intermediate output from LES data, write it to the analysis repo or this repo.

2. **Obsidian vault is append-only for writes.** You may read any note. You may append to existing notes (e.g., adding a summary or tagging). You must NEVER overwrite, restructure, or delete Obsidian notes.

3. **Path resolution:** Repo paths are stored in `.claude/state/external-repos.json` (created by `/onboard`). If this file doesn't exist, ask the user for paths before proceeding.

4. **Cross-repo references:** When citing data or figures from the analysis repo, use relative references where possible. Document the source repo and commit hash for reproducibility.

5. **No secrets across repos.** Never copy credentials, API keys, or access tokens between repositories.
