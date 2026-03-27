# Research Approach and Work Plan

<!-- Target: ~0.8 page (~550 words) — this is the core of the proposal -->
<!-- Goal: Convince reviewers the work is feasible, well-scoped, and methodologically rigorous -->

<!--
Suggested structure:
1. High-fidelity modeling approach
   - Simulation framework (ExaWind/AMR-Wind or other)
   - Key physical modeling choices (free surface? FSI? turbulence?)
   - Computational resource plan (node-hours, scaling ref: NLR ExaWind benchmarks)

2. Engineering / reduced-order modeling
   - What fast-running model will be developed or extended?
   - How does it connect to the high-fidelity data?

3. Validation strategy
   - What experimental or field data exists for comparison?
   - Collaborator role (Hannah Ross, Mike Sprague, Jason Jonkman)

4. Work plan / timeline (Years 1, 2, 3)
   - Year 1: [setup, baseline simulations, ...]
   - Year 2: [parametric studies, model development, ...]
   - Year 3: [validation, engineering tool, dissemination, ...]
-->

Resolving the multi-scale hydrodynamics of confined tidal arrays requires a modeling hierarchy spanning blade-level flow physics, multi-phase array-scale dynamics, and industry-ready engineering design. This proposal advances three integrated aims.

**Aim 1 — Blade-resolved simulation of confined tidal flows (Years 1–2).** The primary unresolved question in multi-scale tidal array modeling is: what are the blade- and rotor-level mechanisms by which confinement amplifies power extraction and thrust loading, and how do these mechanisms evolve from a lone turbine to a partial cross-stream fence to a full array? Using AMR-Wind and Nalu-Wind from the ExaWind stack, blade-resolved hybrid RANS/LES simulations of axial-flow tidal turbines will be conducted across a systematic range of local and global blockage ratios and rotor spacings in idealized tidal channel geometries. Key outputs — tip vortex dynamics, near-wake turbulent mixing rates, and confinement-corrected thrust and power coefficients — will provide the physics-based closures missing from existing analytical blockage models (Nishino & Willden 2013; Garrett & Cummins 2007), and will yield specific corrections to actuator disk and line methods and to OpenFAST for use in lower-fidelity contexts. Simulations will be validated against published experimental data (Ouro & Stoesser 2019). This work is led by Heck, with HPC and software support from Sprague and OpenFAST integration from Jonkman.

**Aim 2 — Free-surface effects on array performance (Years 1–3).** Channel confinement is bounded above by a free surface whose deformation depends on Froude number and rotor thrust loading (Whelan et al. 2009). Physics-informed actuator rotor models developed in Aim 1 will be implemented in OpenFOAM (VoF, interFoam) to investigate regimes where free-surface deformation constitutes a significant departure from rigid-lid predictions. The central hypothesis is that free-surface effects are negligible at low Froude numbers but become significant at shallow submersion depths and high array packing densities, where the exchange of potential energy with the free surface materially alters effective blockage and wake recovery. This aim is conducted in close collaboration with Ross, whose blockage modeling expertise directly informs the analytical baseline and model development.

**Aim 3 — Tidal array engineering design framework (Years 2–3).** Physical insights from Aims 1 and 2 will be distilled into a next-generation engineering simulation framework for tidal channels — a tidal analog to FLORIS — incorporating confinement-corrected induction models, near-wake mixing parameterizations, and Froude-number-dependent blockage corrections. The framework will be validated against Aims 1 and 2 simulations and published array experiments (Stansby & Ouro 2022; McNaughton et al. 2022), then applied to Cook Inlet, the Gulf of Maine, and Puget Sound to estimate practical energy extraction potential at three geographically and hydrodynamically distinct US tidal sites.

| Year | Primary activities |
|------|--------------------|
| 1 | Aim 1: single-turbine and small-array ExaWind simulations, validation; Aim 2: OpenFOAM baseline and VoF setup |
| 2 | Aim 1: partial fence to full array, actuator model development; Aim 2: Froude number and submersion depth sweep |
| 3 | Aim 3: engineering framework, US site case studies, open-source release |
