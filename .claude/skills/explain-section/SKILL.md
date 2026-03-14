---
name: explain-section
description: Multi-agent pedagogical explanation of any manuscript section. Verifies equations against primary sources, then launches a 4-agent dialogue (Explainer, Undergrad, Professor, PhD) to build deep understanding. Saves output to important_explanations/.
argument-hint: "<section-name or file path> [--skip-verify to skip equation verification]"
allowed-tools: ["Read", "Write", "Edit", "Grep", "Glob", "Bash", "Agent"]
---

# /explain-section — Multi-Agent Pedagogical Explanation

Generate a deep, intuition-building explanation of a manuscript section's technical content using a 4-agent dialogue.

**Input:** `$ARGUMENTS` — section name (e.g., "methods equations", "statistical model") or file path.

---

## Overview

This skill has two phases: verification (optional) and explanation.

```
Phase 1: Equation/Claim Verification (can be skipped with --skip-verify)
  ├── Identify equations and key technical claims in the target section
  ├── Find primary sources (manuals, papers, code)
  └── Term-by-term verification → report to quality_reports/data_verification/

Phase 2: 4-Agent Pedagogical Explanation
  ├── Explainer: Domain researcher, builds intuition through analogies
  ├── Undergrad: Early UG learner, asks "why?" and "what does that mean?"
  ├── Professor: Rigor guardian, catches misleading oversimplifications
  ├── PhD: Whiteboard-readiness checker, flags gaps in logical chain
  └── Output → quality_reports/data_verification/important_explanations/
```

---

## Step 1: Identify Target Content

```
TARGET = $ARGUMENTS
```

If TARGET is a file path, read it. If it's a section name, find the relevant file in `manuscript/` or `manuscript/08_supporting_information.md`.

Extract:
- All equations (numbered and inline)
- Key technical claims and assumptions
- Variable definitions and notation

---

## Step 2: Equation Verification (Phase 1)

**Skip if `--skip-verify` is passed.**

For each equation found:

1. **Find primary source** — check in order:
   - Papers in `master_supporting_docs/`
   - Code in `scripts/`

2. **Term-by-term comparison** — every coefficient, sign, exponent, variable

3. **Physical sign check** (Devil's Advocate) — for each equation, construct a physical scenario and verify the equation predicts correct behavior

4. **Write verification report** to `quality_reports/data_verification/YYYY-MM-DD_[section]_verification.md`

5. **Gate:** If errors found, fix them before proceeding. Present fixes to user.

---

## Step 3: Pedagogical Explanation (Phase 2)

Launch a general-purpose Agent with the following architecture:

### Agent Roles

| Agent | Role | Calibration |
|-------|------|-------------|
| **Explainer** | Domain researcher building intuition through analogies | Targets someone with intro-level knowledge but no specialized experience |
| **Undergrad** | Early undergraduate learner | Asks "why?" and "what does that mean physically?" until genuinely satisfied; flags jargon |
| **Professor** | Rigor guardian | Intervenes when analogies become misleading or lose mathematical precision; ensures dimensional consistency |
| **PhD** | Whiteboard-talk readiness checker | Must feel confident they could present the topic from scratch on a whiteboard; flags gaps in logical chain |

### Explanation Structure

1. **Big picture** — what is the physical system? What question does the model answer? Use a concrete analogy.
2. **Key scales/mechanisms** — identify the 2-4 main physical processes at work
3. **Equation-by-equation walk-through**:
   - Physical analogy for each equation
   - The actual equation with EVERY term labeled
   - Undergrad Q&A loop until satisfied
   - Professor rigor check after each
4. **Key dimensionless groups or parameters** (if applicable) — what they tell you
5. **When the model/approach fails** — assumptions and their limits
6. **PhD whiteboard check** — reconstruct from memory in 5-7 bullet points

### Convergence Criteria

The loop runs until ALL of:
- Undergrad agent has no remaining questions
- Professor confirms no oversimplifications that would mislead
- PhD confirms they could give a whiteboard talk from this explanation alone

---

## Step 4: Write Output

Save the explanation to:
```
quality_reports/data_verification/important_explanations/[topic_name].md
```

The file should include:
- The agent dialogue woven into the explanation (makes reasoning visible)
- All equations in LaTeX
- A summary table at the end
- A note on which primary sources were verified against

---

## Step 5: Update Session Log

Append to the current session log:
- What section was explained
- Whether verification found any errors
- The output file path

---

## Example Usage

```
/explain-section methods equations
/explain-section manuscript/03_materials_methods.md
/explain-section statistical model --skip-verify
```
