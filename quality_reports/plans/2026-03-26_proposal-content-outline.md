# Proposal Content Outline — NLR Director's Fellowship
**Status:** APPROVED (research scope confirmed 2026-03-26)
**Deadline:** ~2026-04-02
**Page limit:** 2 pages hard limit

---

## Methodological Thesis (one sentence to anchor all writing)

> The multi-scale analytical models that govern tidal array design require physics-based closure parameters — near-wake mixing rates and confinement-corrected induction fields — that cannot be derived from actuator disk theory; blade-resolved high-fidelity simulation provides these closures for the first time and enables a multi-fidelity modeling hierarchy from rotor physics to array-scale engineering design.

---

## Section 01 — Motivation and Research Gap (~200 words, ~0.3 page)

**Goal:** Establish the energy opportunity, identify the specific modeling gap, bridge to Kirby's approach.

**Key claims to make (in order):**

1. **Hook — energy opportunity:** Tidal stream energy is a predictable, dispatchable domestic energy resource. Unlike other renewables, tidal is governed by celestial mechanics — it is fully forecastable years in advance. Global practical resource ~110 TWh/year (Coles et al. 2025); significant US potential at Cook Inlet, Gulf of Maine, Puget Sound. Current global installed capacity ~35 MW with contracted build-out to 188 MW by 2030 — technology at an inflection point.

2. **The physics problem:** Extracting tidal energy requires arraying turbines across tidal channels. Channel boundaries create *confinement* — the ratio of turbine swept area to channel cross-section (blockage) is orders of magnitude larger than in wind. This amplifies power extraction beyond the Betz limit (Garrett & Cummins 2007) but also creates bidirectional coupling between device-scale rotor physics and array-scale bypass flow that has no analog in wind energy.

3. **The modeling gap:** The multi-scale analytical framework for tidal arrays (Garrett & Cummins 2007; Nishino & Willden 2013; Gupta & Young 2017) is well-developed but requires closure parameters — specifically near-wake turbulent mixing rates and confinement-modified induction fields — that cannot be computed from actuator disk theory. Every existing high-fidelity tidal study uses actuator disks (e.g., Nishino & Willden 2013 with up to 40 disks); no blade-resolved simulations exist for confined arrays. The free-surface boundary condition — known to modify effective blockage at non-negligible Froude numbers (Whelan et al. 2009) — has never been studied with physically accurate rotor models.

4. **Bridge:** Kirby's PhD expertise in LES and reduced-order modeling of the atmospheric boundary layer transfers directly: swap atmospheric boundary layer → tidal channel, wind turbine → hydrokinetic rotor. The multi-fidelity ExaWind stack (Sprague et al. 2020; Sharma et al. 2024) — developed at NLR — provides the high-fidelity simulation infrastructure. The gap is not tools; it is the physics-informed closure models that connect scales.

**Citations to include:** Coles et al. (2025), Garrett & Cummins (2007) [check bib], Nishino & Willden (2013), Gupta & Young (2017), Whelan et al. (2009), Sprague et al. (2020), Sharma et al. (2024)

**Framing note:** No climate change language. Frame around: domestic energy production, predictability/reliability, US energy security, technology readiness.

---

## Section 02 — Research Objectives (~200 words, ~0.3 page)

**Goal:** 3 numbered objectives, each specific, achievable in 2-3 years, with clear methodological and application components.

**Proposed objectives:**

**Objective 1:** Characterize the hydrodynamics of confined tidal turbine arrays using blade-resolved high-fidelity simulation (ExaWind/Nalu-Wind), quantifying tip vortex dynamics, near-wake turbulent mixing rates, and confinement-modified rotor induction as functions of local and global blockage ratio — spanning the continuum from a single turbine to a partial cross-stream fence.

**Objective 2:** Develop and validate physics-informed actuator rotor models for confined tidal flows, calibrated from Objective 1, and deploy them in multi-phase (free-surface) simulations (OpenFOAM/interFoam) to determine the Froude-number threshold above which free-surface deformation constitutes a significant correction to array performance predictions.

**Objective 3:** Synthesize the multi-scale closure models from Objectives 1 and 2 into an open-source tidal array engineering design framework and demonstrate its utility through site-specific power extraction assessments at US tidal energy sites (Cook Inlet, Gulf of Maine, Puget Sound).

**Overarching question (optional, to lead the section):**
"How does the physical coupling between blade-level flow physics and array-scale channel dynamics govern the performance of tidal turbine arrays, and how can this coupling be represented efficiently in engineering design tools?"

---

## Section 03 — Research Approach and Work Plan (~550 words, ~0.8 page)

**Goal:** Convince reviewers the work is feasible, well-scoped, and methodologically rigorous. Show the multi-fidelity pipeline clearly. Map collaborators to work.

**Suggested structure:**

### 3.1 Multi-fidelity modeling hierarchy (~150 words)

Describe the three-tier pipeline as a coherent methodology, not three separate projects:
- **Tier 1 (ExaWind):** Blade-resolved RANS/hybrid-LES → device-scale physics, closure model development
- **Tier 2 (OpenFOAM):** Multi-phase RANS + improved actuator models → free-surface coupling
- **Tier 3 (Engineering model):** Fast-running array design tool → site assessment

Key framing: this mirrors the ExaWind multifidelity philosophy (blade-resolved → actuator-line → plant model) adapted to the structurally distinct confined-channel regime. Each tier is a publishable deliverable.

### 3.2 Aim 1 details (~150 words)

- Code: AMR-Wind / Nalu-Wind (blade-resolved, overset mesh, hybrid RANS/LES)
- Geometry: NREL reference tidal turbine or equivalent; axial-flow, single and arrays
- Cases: Sweep blockage ratio B_L ∈ [0.1, 0.5], rotor spacing s/D ∈ [2, 8]; inflow turbulence profiles matching real tidal channels
- Key unknowns targeted: tip vortex deformation under confinement, near-wake recovery length, momentum flux in bypass flow
- OpenFAST/actuator model outputs: corrected thrust and power coefficients as functions of local blockage; improved induction model
- Validation: Ouro & Stoesser (2019) single-turbine case as primary validation; published flume data for array cases
- Collaborators: Mike Sprague (HPC, ExaWind); Jason Jonkman (OpenFAST corrections)

### 3.3 Aim 2 details (~100 words)

- Code: OpenFOAM, VoF free-surface (interFoam), rotating mesh or actuator body
- Rotor model: Physics-informed actuator disk/line from Aim 1 (replacing stock Betz-limit models)
- Cases: Single turbine and partial fence; sweep Froude number Fr ∈ [0.05, 0.4], submersion depth h/D ∈ [1.0, 3.0]
- Hypothesis: Fr-threshold below which rigid-lid assumption is adequate; above threshold, potential energy exchange with free surface constitutes non-negligible correction to effective blockage and wake recovery
- Baseline comparison: Whelan et al. (2009) analytical model extended with Aim 1 rotor model
- Collaborator: Hannah Ross (blockage theory; OpenFAST marine turbine modeling)

### 3.4 Aim 3 details (~100 words)

- Engineering model: New framework (not FLORIS extension) built on Aim 1+2 closure models
- Key physics included: confinement-corrected induction, near-wake mixing parameterization, Froude-number blockage correction, partial fence / full array configurations
- Validation: Cross-validated against Aims 1 and 2; compared to published array experiments (Stansby & Ouro 2022; McNaughton et al. 2022)
- Case studies: Cook Inlet (high-head, strong semidiurnal), Gulf of Maine (resonant basin), Puget Sound (constrained strait) — three distinct US regimes using publicly available tidal resource data (NOAA)
- Deliverable: Open-source tool; target NLR release analogous to FLORIS for wind

### 3.5 Work plan / timeline (~50 words)

| Year | Focus                                                                                                 |
| ---- | ----------------------------------------------------------------------------------------------------- |
| 1    | Aim 1: baseline ExaWind simulations (single turbine, validation); Aim 2 setup (OpenFOAM VoF baseline) |
| 2    | Aim 1: partial fence to full array; actuator model development; Aim 2: Froude sweep                   |
| 3    | Aim 3: engineering model development; US site case studies; tool release                              |

---

## Section 04 — Broader Impact (~200 words, ~0.3 page)

**Goal:** Domestic energy relevance, methodological transferability, NLR's specific capabilities.

**Key claims:**

1. **US energy production:** Tidal stream represents a largely untapped domestic energy resource. Case studies at Cook Inlet, Gulf of Maine, and Puget Sound will provide the first physics-informed estimates of extractable power at these sites — directly informing federal and state energy planning.

2. **Technology maturity:** The engineering design tool (Aim 3) provides the tidal energy sector with a FLORIS-equivalent — a fast-running, physics-validated design tool that commercial developers currently lack. This lowers barriers to project development and de-risks investment.

3. **Methodological transferability:** The multi-fidelity approach (blade-resolved LES → improved actuator model → engineering tool) is not specific to tidal energy. The framework applies to any confined-flow energy conversion problem: run-of-river hydrokinetic systems, estuarine energy harvesting, tidal barrages. Results will be published and tools released open-source through NLR.

4. **NLR unique position:** This work leverages NLR's ExaWind stack, OpenFAST infrastructure, and existing collaborations (Ross, Sprague, Jonkman) in ways that could not be achieved at a university. The fellowship period positions NLR as a leading institution in HFM of marine energy — a growing federal priority.

**Framing note:** Frame around grid reliability, domestic energy security, economic development in coastal/tidal regions. No climate language.

---

## Section 05 — References

Target: keep within the 2-page limit. ~8-12 references, prioritize:
1. Garrett & Cummins (2007) — blockage theory foundation
2. Nishino & Willden (2013) — two-scale model (primary gap)
3. Whelan et al. (2009) — free-surface baseline
4. Gupta & Young (2017) — three-scale analytical model
5. Adcock et al. (2021) — review context
6. Ouro & Stoesser (2019) — validation target
7. Sprague et al. (2020) or Sharma et al. (2024) — ExaWind
8. Coles et al. (2025) — resource quantification
9. Stansby & Ouro (2022) or McNaughton et al. (2022) — array experiments

**Action needed:** Verify all are in `Bibliography_base.bib`. Flag missing entries for Kirby to add via Zotero.

---

## Page Budget Check

| Section | Target words | Target pages |
|---------|-------------|--------------|
| Motivation + gap | ~200 | ~0.30 |
| Objectives | ~200 | ~0.30 |
| Approach + work plan | ~550 | ~0.80 |
| Broader impact | ~200 | ~0.30 |
| References | — | ~0.30 |
| **Total** | **~1150** | **~2.00** |

---

## Writing Process

1. Kirby writes first draft of each section using the key claims above as a guide
2. Claude refines, restructures, checks internal consistency, flags missing citations
3. Claude runs `/proofread` after each section is drafted
4. Export to Word/PDF and check page count before final review
