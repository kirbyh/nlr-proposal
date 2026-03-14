# Integrity Controls

**Origin:** These controls prevent cascading errors in multi-step calculations. A single wrong unit annotation or unverified input can propagate through all downstream calculations.

These controls are MANDATORY for any calculation involving published equations or any factual claim about document contents.

---

## 1. Primary Source Gate

Before using any equation, verify inputs from the **original paper PDF** — not from our SI annotations, not from intermediate quality reports, not from memory. Cite the exact page/equation number. See also Control #9 for claims about our own manuscript contents.

## 2. Unit Chain Verification

For every multi-step unit conversion, write out the explicit chain:
```
[EXAMPLE: value: X units → ÷ conversion_factor → Y units → log = Z]
```
Every intermediate value must have explicit units. No implicit conversions.

## 3. Physical Plausibility Gate

After computing a predicted value, check it against literature ranges:
<!-- Replace with your field's expected ranges -->
- [QUANTITY 1]: typically [RANGE] ([UNITS])
- [QUANTITY 2]: typically [RANGE] ([UNITS])
- [QUANTITY 3]: typically [RANGE] ([UNITS])

If a result falls >2 OOM outside the expected range, **STOP and verify inputs** before proceeding.

## 4. Rationalization Detector

Before explaining away an implausible result, ask: **"Have I verified every input against the primary source?"**

A large prediction error from a well-calibrated model is almost certainly an input error, not a model limitation. Do not generate plausible narratives before checking inputs.

## 5. Devil's Advocate Requirement

In multi-agent verification workflows, at least one agent must be tasked with the hypothesis: **"The answer is wrong — find the input error."** Agents that only verify arithmetic given the inputs will miss unit errors.

## 6. Safety/Regulatory Claim Causal Chain

Any claim with safety or regulatory implications must trace through a complete causal chain:
<!-- Replace with your field's causal chain -->
1. [INPUT PARAMETERS] → verified source
2. [INTERMEDIATE CALCULATION] → computed with verified parameters
3. [PREDICTION] → from verified calculation
4. [CONCLUSION] → from prediction vs threshold/standard

If any link uses unverified inputs, the chain is broken.

## 7. Coefficient Fabrication Guard

Every numerical value in a calculation must have a pinpointed source location (file:line or paper:page:equation). Values that appear without source attribution must be flagged immediately.

## 8. Social Deference Guard

When a user questions a verified calculation, re-derive from first principles and present the work. Do NOT construct post-hoc theories to explain a discrepancy (e.g., reinterpreting unit labels to make two independent equations agree). If every step checks out, say so with confidence and ask the user to trace through their source. Agreement between independently calibrated equations is not a verification criterion.

## 9. Document Content Verification Gate

**Never claim that specific content exists — or does not exist — in a document without reading that document first.** Session logs, memory, verification CSVs, and prior conversation context are NOT substitutes for the authoritative file.

**The rule:**

1. **Read before citing.** Before stating "Table X shows...", "the manuscript says...", "you already report...", "the SI does not mention...", or any claim about what a document contains, use the Read tool on the authoritative file. A Read tool call for the cited file MUST exist within the last 3 assistant messages. If not, re-read before claiming.
2. **Cite the location.** Every content claim must include file:line or section header.
3. **Absence claims require equal rigor.** Claiming a document does *not* contain something ("the manuscript doesn't mention X") is equally dangerous — it can cause the user to skip work they need to do. Read the full relevant section before asserting absence.
4. **Do not proceed on memory alone.** If you have not read the file in this conversation, you MUST read it before making the claim.
