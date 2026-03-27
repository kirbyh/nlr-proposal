# Session Log: 2026-03-26 — Research Direction Synthesis

**Status:** COMPLETED

## Objective

Evaluate three initial research directions for the NLR Director's Fellowship proposal, synthesize into a coherent three-aim research plan, and prepare for proposal drafting.

## Research Directions Evaluated

### Direction 1 — Rotor-level flow physics under confinement and array effects
**Decision: Keep as core (Aim 1).**
Directly fills the gap in Nishino & Willden (2013): their two-scale model requires near-wake mixing closure that actuator disks cannot provide. Blade-resolved LES (ExaWind/Nalu-Wind) under realistic confinement is the methodological hook.

### Direction 2 — RANS + cavitation prediction
**Decision: Demote to conditional Year 3 extension.**
Genuine methodological novelty, but adding two-phase cavitation to ExaWind is a major codebase overhaul, not a fellowship-scale extension. One sentence in the approach. Revisit if Year 1-2 cases reveal cavitation-prone regimes.

### Direction 3 — Multi-scale bridging (blades → rotors → arrays/wakes)
**Decision: Keep as methodological spine (informs all aims).**
The scale-coupling in confined tidal channels is the central thesis. ExaWind multifidelity architecture (Sprague et al. 2020) maps directly onto the research structure.

## Agreed Research Plan: Three Aims

### Aim 1 — High-fidelity characterization of confined tidal turbine flows (ExaWind)
- **Tool:** AMR-Wind / Nalu-Wind (blade-resolved RANS/hybrid-LES)
- **Scope:** Lone turbine → paired rotors → partial fence → full array continuum; sweep blockage ratio and rotor spacing
- **Inflow:** Axial-flow turbines only; include environmental turbulence (shear, seabed-generated turbulence)
- **Outputs:** Tip vortex dynamics, near-wake turbulent mixing rates, confinement-corrected induction fields, rotor loading under confinement
- **Key gap addressed:** Near-wake mixing closure in Nishino & Willden (2013) two-scale analytical model
- **OpenFAST connection:** Aim 1 outputs feed specific recommendations/corrections to actuator disk/line models and OpenFAST (→ Jason Jonkman collaboration)
- **Validation:** Ouro & Stoesser (2019) as primary validation target; published flume data

### Aim 2 — Free-surface effects on array performance (OpenFOAM, multi-phase)
- **Tool:** OpenFOAM (VoF, interFoam + rotating mesh or improved actuator model)
- **Rotor model:** Physics-informed actuator disk/line from Aim 1 (not stock actuator models)
- **Physics question:** How does free-surface deformation modify effective blockage and downstream wake recovery, as a function of Froude number and array packing density?
- **Hypothesis:** Free-surface effects negligible at low Fr; significant departure from rigid-lid results at shallow submersion depths and dense packing, where potential energy exchange is non-negligible
- **Analytical baseline:** Whelan et al. (2009) — extend from actuator disk to physics-informed rotor model
- **Scope:** Single rotor → partial fence; Fr sweep, submersion depth sweep, blockage ratio sweep
- **Note:** Novelty is the calibrated actuator model from Aim 1 + Froude-number threshold characterization; not solver development

### Aim 3 — Tidal array engineering design framework (tidal-FLORIS equivalent)
- **Tool:** New engineering model (not extending existing FLORIS — known differences in rotor dynamics, wake, free surface, confinement)
- **Closures from:** Aims 1 and 2 (confinement-corrected induction, Froude-number-corrected blockage, near-wake mixing rates)
- **Validation:** Validate against Aims 1+2 simulations and published data
- **Application:** Case studies at Cook Inlet (AK), Gulf of Maine, Puget Sound — three distinct tidal regimes, US domestic energy sites
- **Deliverable:** Open-source tool; publishable as standalone contribution

## Design Decisions

| Decision | Alternatives Considered | Rationale |
|----------|------------------------|-----------|
| Build new tidal-FLORIS instead of extending FLORIS | Extend existing FLORIS | Rotor dynamics, wake structure, free surface, and confinement are sufficiently different to justify new framework |
| Scope Aim 1 to axial-flow turbines | Include cross-flow turbines (Snortland et al.) | Scope control; axial-flow is dominant deployed technology; cross-flow left for future |
| Cavitation as Year 3 extension | Core Aim 2 methodology | Codebase overhaul risk; not appropriate for fellowship scope |
| US site case studies in Aim 3 | Generic validation | Strengthens domestic energy framing; connects to DOE/NLR priorities |

## Key Literature Mapped to Aims

| Paper | Role |
|-------|------|
| Adcock et al. (2021) | Review context; multiscale framing |
| Nishino & Willden (2013) | Primary gap (near-wake mixing closure) — Aim 1 |
| Gupta & Young (2017) | Three-scale analytical baseline — Aim 1/3 |
| Whelan et al. (2009) | Free-surface analytical baseline — Aim 2 |
| Ouro & Stoesser (2019) | Aim 1 validation target |
| Stansby & Ouro (2022) | Array modeling — Aim 1/3 context |
| McNaughton et al. (2022) | Constructive interference — Aim 3 application |
| Sprague et al. (2020) | ExaWind multifidelity framing — Aim 1 |
| Sharma et al. (2024) | ExaWind hybrid RANS/LES capability — Aim 1 |
| Coles et al. (2025) | Global/US resource quantification — Aim 3 / impact framing |
| Neill et al. (2021) | Resource context; environmental interactions |
| Ji et al. (2025) | Yaw effects on tidal turbine — Aim 1 context |

## Open Questions / Blockers

- [ ] Does Hannah Ross have OpenFOAM experience, or is Aim 2 entirely Kirby's contribution?
- [ ] Are specific published flume datasets (beyond Ouro & Stoesser 2019) available for Aim 1 validation?
- [ ] Are NOAA tidal resource data sufficient for Cook Inlet / GoM / Puget Sound Aim 3 case studies, or do we need NLR-specific data access?
- [ ] Confirm AI disclosure requirement with NLR guidelines before submission

## Next Steps

- [ ] Draft `01_overview.md` (motivation + gap, ~200 words) — Kirby writes first draft
- [ ] Draft `02_objectives.md` (research questions, ~200 words) — Kirby writes first draft
- [ ] Draft `03_approach.md` (methods + work plan, ~550 words) — Kirby writes first draft
- [ ] Draft `04_impact.md` (broader impact, ~200 words) — Kirby writes first draft
- [ ] Validate citations against `Bibliography_base.bib`
- [ ] Export to Word/PDF and check page count
