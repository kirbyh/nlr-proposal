# Broader Impact and Relevance

In the template, the topic headline is "Measure of a successful outcome" (1 page)

<!-- Target: ~0.3 page (~200 words) -->
<!-- Goal: Why does this matter to NLR specifically, and to US energy more broadly? -->
<!-- Framing: Energy security, domestic resource development, technology pathway to deployment -->

---

For each aim in the **Approach**, we outline metrics for successful outcomes. At a high level, successful completion of this project will produce: (i) a first-of-kind characterization of the coupled flow physics governing tidal array performance across scales, (ii) validated physics-based corrections to engineering rotor representations at multiple fidelities, and (iii) an open-source, industry-ready simulation framework for tidal energy array design.

**Aim 1** will succeed by delineating regimes of scale interaction where local blockage — the proximity of neighboring turbines and channel walls — produces non-negligible departures from isolated-rotor predictions. Specific deliverables include the dependence of rotor power and thrust on local and global blockage ratio across the lone-turbine-to-full-fence continuum; systematic testing of existing blockage correction models (Garrett & Cummins 2007; Nishino & Willden 2013) against blade-resolved simulation data; and new physics-based induction corrections for actuator disk and line methods and blade element momentum theory in OpenFAST. Additionally, established engineering wake models from wind energy (Bastankhah & Porté-Agel 2014; Martínez-Tossas et al. 2019) will be evaluated against confined-flow simulation data to determine their validity and necessary modifications in the tidal setting.

**Aim 2** will succeed by quantifying the sensitivity of key rotor performance metrics — power coefficient, thrust, and wake recovery length — to free-surface deformation, and by mapping the Froude number and submersion depth regimes where the rigid-lid assumption breaks down. Corrected actuator methods from Aim 1 will be validated in OpenFOAM against the Whelan et al. (2009) analytical baseline and available experimental benchmarks, establishing a multi-phase simulation capability for confined tidal arrays that does not currently exist.

**Aim 3** will succeed by delivering a validated, open-source tidal plant flow simulator — analogous to FLORIS for wind — built on the confinement-corrected and free-surface-aware models from Aims 1 and 2. Site-specific assessments at Cook Inlet, the Gulf of Maine, and Puget Sound will provide the first physics-informed estimates of practical tidal energy potential at three geographically distinct US sites. Should the full engineering framework not reach maturity within the fellowship period, a well-defined contingency deliverable remains: systematic evaluation of existing tools against high-fidelity simulation and experimental data in confined tidal flows, which is independently publishable and immediately useful to the community.

The multi-fidelity methodology developed here extends beyond tidal energy to propeller hydrodynamics, estuarine energy harvesters, and laboratory blockage correction for wind- and water-tunnel experiments. All simulation codes and datasets will be released as open-source contributions, and blockage corrections for OpenFAST and actuator methods will be submitted for peer-reviewed publication to maximize adoption across the community.

Ensuring energy security in the US relies on a diverse portfolio of power generation sources. Tidal energy excels for two reasons: there is no reliance on foreign fuel, and the power output is extremely predictable many months in advance. Regional economies in the coastal US have a tremendous untapped resource in tidal energy, but existing engineering models are insufficient for designing and optimizing resilient and robust energy harvesting machines due to the complex multiscale flow physics of turbine arrays in confined channels. The aims of this project target key areas of uncertainty that currently limit the deployment of tidal energy harvesters, and the physical insights, datasets, and engineering tools developed throughout this project would aid industrial partners in deploying safe and reliable power to coastal communities in the US. 

