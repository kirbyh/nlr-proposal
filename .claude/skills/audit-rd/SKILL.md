---
name: audit-rd
description: Multi-agent audit of Results & Discussion for logical coherence, numerical integrity, citation validity, and first-use definitions. Launches parallel agents, reconciles reports, applies fixes with traceable correction table, and creates MEMORY.md [LEARN] rules.
argument-hint: "[optional: path to R&D manuscript file, defaults to manuscript/04_results_discussion.md]"
allowed-tools: ["Read", "Write", "Edit", "Grep", "Glob", "Bash", "Agent", "Task"]
---

# /audit-rd — Multi-Agent Results & Discussion Audit

Run a comprehensive audit of the Results & Discussion section covering logical coherence, numerical integrity, and citation validity.

**Input:** `$ARGUMENTS` — optional path to R&D file. Defaults to `manuscript/04_results_discussion.md`.

---

## Overview

This skill launches two parallel agents, then acts as manager to reconcile their findings, apply fixes, and create memory rules.

```
Manager (this context)
  ├── Agent A: Logic & Continuity Reviewer  ──→  disk report
  ├── Agent B: Reference Verification       ──→  disk report
  │
  ├── Manager Review → redeploy if unsatisfied (max 2 rounds)
  ├── Apply fixes with traceable correction table
  └── Compile final report + MEMORY.md [LEARN] rules
```

---

## Step 1: Locate Target File

```
TARGET = $ARGUMENTS or "manuscript/04_results_discussion.md"
```

Read the target file. If it doesn't exist, abort with error.

---

## Step 2: Build Citation Inventory

Before launching agents, extract ALL `[@...]` citations from the target file:

1. Grep for `@[a-zA-Z]` patterns in the target file
2. For each citation key, look up the PDF path in `Bibliography_base.bib` (search for the key, then extract the `file = {...}` field)
3. Build a table: citation key, source description, PDF path
4. Save inventory to `quality_reports/data_verification/YYYY-MM-DD_rd_citation_inventory.md`

---

## Step 3: Launch Agent A — Logic & Continuity Reviewer

Launch via Agent tool (subagent_type: general-purpose). Agent A reads ONLY the manuscript file (no PDFs).

### Agent A Prompt Template

```
You are Agent A in a multi-agent audit of [TARGET]. Your role is Logic & Continuity Reviewer.

Read the file and perform these checks:

1. NARRATIVE ARC & CONTINUITY
   - Do subsections flow logically?
   - Are paragraph transitions smooth?
   - Does each subsection build on the previous one?

2. INTERNAL NUMERICAL CONSISTENCY
   For EVERY number in the prose, verify against tables in the same file:
   - All percentage values — arithmetically correct?
   - All computed values — match table entries?
   - All fold-differences — recompute
   - All unit conversions from cited literature — recompute independently
   - All "within a factor of X" claims — verify ratio

3. INTERPRETIVE STATEMENTS — FLAG UNSUPPORTED CLAIMS
   For EACH interpretive or explanatory statement, assess:
   - Is it directly supported by data presented in the manuscript?
   - Does it invoke mechanisms not tested?
   - Is it a causal claim where only correlation exists?
   List every interpretive statement with verdict: SUPPORTED / PARTIALLY SUPPORTED / SPECULATIVE

4. FIRST-USE DEFINITIONS
   Check EVERY acronym, symbol, and parameter is defined on first use.
   List undefined terms.

5. UNITS CONVENTION
   Check that log-transformed quantities do not carry units on numerical values.
   Units should appear on the definition (e.g., "log K (units)") not the number.

6. DANGLING TAGS & COMMENTS
   Search for: [REF], [PLACEHOLDER], [CONFIRM], [DATA NEEDED], @Claude, HTML comments.
   List all with line numbers.

7. TABLE & FIGURE INTEGRITY
   - Column headers complete and unambiguous?
   - Figure references in sequential order of first mention?
   - Cross-subsection contradictions?

OUTPUT: Write report to quality_reports/data_verification/YYYY-MM-DD_rd_logic_review.md

Categorize findings as: CRITICAL / MAJOR / MINOR / INFO
Include "Interpretive Statements Assessment" section at end.
```

---

## Step 4: Launch Agent B — Reference Verification (parallel with Agent A)

Launch via Agent tool (subagent_type: general-purpose). Agent B reads the manuscript AND source PDFs.

### Agent B Prompt Template

```
You are Agent B in a multi-agent audit of [TARGET]. Your role is Reference Verification.

STEP 1: AUTO-EXTRACT ALL CLAIM-CITATION PAIRS
Scan the entire file. For every [@...] citation, extract the sentence or clause it supports.
This must be exhaustive — do not rely on a pre-made list.

STEP 2: VERIFY EACH PAIR AGAINST SOURCE
For each claim-citation pair, read the source PDF at [PATH FROM INVENTORY].
For books, read table of contents first, then targeted pages only.
For web resources, mark as UNVERIFIABLE from local source.

For each pair:
1. Find the specific sentence, figure, or table supporting the claim
2. Record exact quote with page number
3. Context classification:
   - DIRECT EVIDENCE — source explicitly states what manuscript claims
   - INFERRED SUPPORT — source provides data from which claim can be reasonably inferred
   - BACKGROUND STATEMENT — source provides general context only
4. Discrepancy classification (if any):
   - MINOR WORDING DRIFT — accurate paraphrase, not precise
   - QUANTITATIVE MISMATCH — numbers differ
   - INCORRECT ATTRIBUTION — claim attributed to wrong source

STEP 3: INDEPENDENT RECOMPUTATION
For numerical claims derived from cited literature, independently recompute the values.
Show your calculation. Flag mismatches.

OUTPUT: Write report to quality_reports/data_verification/YYYY-MM-DD_rd_reference_verification.md

Format per claim:
### C[N]: [Claim summary]
**Manuscript text:** "[exact quote]"
**Citation:** @key
**Source text:** "[exact quote from paper, p. XX]"
**Context classification:** Direct evidence / Inferred support / Background statement
**Verdict:** VERIFIED / PARTIALLY SUPPORTED / UNSUPPORTED / UNVERIFIABLE
**Discrepancy type (if any):** Minor wording drift / Quantitative mismatch / Incorrect attribution
**Independent recomputation (if numerical):** [show calculation]
**Notes:** [corrections needed]
```

---

## Step 5: Manager Review

After both agents complete, read both disk reports and evaluate:

### Pass Criteria
- All HIGH/CRITICAL items VERIFIED or corrected
- No UNSUPPORTED items without corrective action
- All numerical values match tables and source papers
- All acronyms/symbols defined on first use (or fixes proposed)

### Redeployment Triggers (max 2 rounds)
- UNSUPPORTED claim → redeploy Agent B with broader page range
- Numerical mismatch → redeploy Agent A to recheck
- Conflicting findings → redeploy both on specific item

---

## Step 6: Apply Fixes with Traceable Correction Table

Apply all corrections to the target file. Log EVERY change in a correction table:

| # | Original Text | Corrected Text | Reason | Supporting Citation | Discrepancy Class |
|---|--------------|----------------|--------|--------------------|--------------------|
| 1 | ... | ... | ... | ... | ... |

Include the correction table in the final report.

**Rules:**
- Do NOT change the user's log units convention (units on definition, not on values)
- Remove @Claude comments only after addressing each one
- Add first-use definitions for any undefined acronyms/symbols

---

## Step 7: Compile Final Report + Memory Rules

### Final Report
Save to: `quality_reports/data_verification/YYYY-MM-DD_rd_reference_verification.md`

Contents:
- Summary table (ALL claim-citation pairs with verdicts and classifications)
- Detailed entries per claim with exact supporting quotes
- Traceable correction table
- Items requiring user input (if any)

### Memory Rules
For each confirmed error, add a GENERALIZED `[LEARN]` entry to MEMORY.md:

```
[LEARN:category] Generalized rule that prevents the entire ERROR CLASS
from recurring — not just the specific instance.
```

---

## Principles

- **Exhaustive extraction:** Never assume a pre-made claim list is complete. Auto-extract every citation.
- **Source-grounded:** Every verdict must cite a specific page, figure, or table from the source.
- **Recompute, don't trust:** Independently verify every numerical claim derived from literature.
- **Traceable corrections:** Every change gets logged with original text, corrected text, reason, and source.
- **Generalize learnings:** Memory rules should prevent the error CLASS, not just the specific instance.
- **Manager gates:** HIGH/CRITICAL items must be VERIFIED or corrected before the audit passes.
- **Context management:** If context pressure is high, compact between phases — all results are on disk.
