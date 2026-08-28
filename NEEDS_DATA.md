# Needs data - awaiting further input

Generated 2026-08-28. Every field below was blank in the automated sources. Fill any of them in `manual_data.json` and rerun `python build_summary.py`; your values take priority and are never overwritten.

```jsonc
// manual_data.json
{
  "models": {
    "MACE-MPA-0": { "kappa_srme": 0.412, "notes": "from Table 2 of the paper" }
  },
  "studies": {
    "10.1038/s41586-025-08628-5": {
      "models": ["MatterGen"],
      "materials": ["TaCr2O6"],
      "methods": ["DFT", "solid-state synthesis"],
      "metrics": [["bulk modulus error", 20, "%"]],
      "sort_value": 80
    }
  }
}
```

## Models with missing fields (15 of 65)

| Model | Missing fields | DOI | Repo |
|---|---|---|---|
| **EquFlashV2** | DOI | [link](https://proceedings.mlr.press/v267/lee25l.html) | [repo](https://github.com/SamsungDS/GGNN) |
| **EquFlash** | DOI | [link](https://proceedings.mlr.press/v267/lee25l.html) | [repo](https://github.com/SamsungDS/GGNN) |
| **NequIP-GNoME** | Phonon kSRME, Geometry-opt RMSD | [10.1038/s41586-023-06735-9](https://doi.org/10.1038/s41586-023-06735-9) | [repo](https://github.com/google-deepmind/materials_discovery) |
| **Eqnorm MPtrj** | DOI | [link](https://github.com/yzchen08/eqnorm) | [repo](https://github.com/yzchen08/eqnorm) |
| **ESNet** | Phonon kSRME, Geometry-opt RMSD | [10.21203/rs.3.rs-5979703/v1](https://doi.org/10.21203/rs.3.rs-5979703/v1) | [repo](https://github.com/zzz-sl/ESNet) |
| **ALIGNN** | Phonon kSRME, Geometry-opt RMSD | [10.1038/s41524-021-00650-1](https://doi.org/10.1038/s41524-021-00650-1) | [repo](https://github.com/usnistgov/alignn) |
| **MEGNet** | Phonon kSRME, Geometry-opt RMSD | [10.1021/acs.chemmater.9b01294](https://doi.org/10.1021/acs.chemmater.9b01294) | [repo](https://github.com/materialsvirtuallab/megnet) |
| **CGCNN** | Phonon kSRME, Geometry-opt RMSD | [10.1103/PhysRevLett.120.145301](https://doi.org/10.1103/PhysRevLett.120.145301) | [repo](https://github.com/CompRhys/aviary) |
| **EMA-GNN** | Phonon kSRME, Geometry-opt RMSD | [10.6084/m9.figshare.33111509](https://doi.org/10.6084/m9.figshare.33111509) | [repo](https://github.com/submerged-in-matrix/gnome-repro-structural) |
| **CGCNN+P** | Phonon kSRME, Geometry-opt RMSD | [10.1038/s41524-022-00891-8](https://doi.org/10.1038/s41524-022-00891-8) | [repo](https://github.com/JasonGibsonUfl/Augmented_CGCNN) |
| **Wrenformer** | Phonon kSRME, Geometry-opt RMSD | [10.1126/sciadv.abn4117](https://doi.org/10.1126/sciadv.abn4117) | [repo](https://github.com/CompRhys/aviary) |
| **AlchemBERT** | Phonon kSRME, Geometry-opt RMSD | [10.26434/chemrxiv-2024-r4dnl](https://doi.org/10.26434/chemrxiv-2024-r4dnl) | [repo](https://gitee.com/liuxiaotong15/alchemBERT) |
| **BOWSR** | Phonon kSRME | [10.1016/j.mattod.2021.08.012](https://doi.org/10.1016/j.mattod.2021.08.012) | [repo](https://github.com/materialsvirtuallab/maml) |
| **Voronoi RF** | Phonon kSRME, Geometry-opt RMSD | [10.1103/PhysRevB.96.024104](https://doi.org/10.1103/PhysRevB.96.024104) | [repo](https://github.com/janosh/matbench-discovery) |
| **ALIGNN FF** | Accuracy (%), MAE (meV/atom), RMSE (meV/atom), F1, R2, Phonon kSRME, Geometry-opt RMSD, Parameter count | [10.1039/D2DD00096B](https://doi.org/10.1039/D2DD00096B) | [repo](https://github.com/usnistgov/alignn) |

## Studies with no numeric performance figure (88 of 91)

These need a human to open the paper and read the results table. Highest value first: studies that already name a model and a material, so only the number is missing.

| Study | Models named | Materials | Method | Date | DOI |
|---|---|---|---|---|---|
| [Conservation-Resolved Error Decomposition: A Benchmark Axis for Electronic-Structure Methods and Machine-Learned Interat](https://doi.org/10.26434/chemrxiv.15007478/v1) | MACE | OFF23 | hybrid DFT, MLIP | 2026-08-17 | [10.26434/chemrxiv.15007478/v1](https://doi.org/10.26434/chemrxiv.15007478/v1) |
| [HIP: Hessian Interatomic Potentials](https://doi.org/10.5281/zenodo.22003592) | EquiformerV2 | molecule / organic | MLIP | 2026-08-19 | [10.5281/zenodo.22003592](https://doi.org/10.5281/zenodo.22003592) |
| [HIP: Hessian Interatomic Potentials](https://doi.org/10.5281/zenodo.22003591) | EquiformerV2 | molecule / organic | MLIP | 2026-08-19 | [10.5281/zenodo.22003591](https://doi.org/10.5281/zenodo.22003591) |
| [Integration of Machine Learning and Solid-State Chemistry for the Discovery of Electrochemical Materials for Fuel Cells ](https://doi.org/10.5281/zenodo.22021890) | ALIGNN, MEGNet, CGCNN | Li-ion battery, catalyst, oxide | DFT | 2026-08-20 | [10.5281/zenodo.22021890](https://doi.org/10.5281/zenodo.22021890) |
| [Integration of Machine Learning and Solid-State Chemistry for the Discovery of Electrochemical Materials for Fuel Cells ](https://doi.org/10.5281/zenodo.22021889) | ALIGNN, MEGNet, CGCNN | Li-ion battery, catalyst, oxide | DFT | 2026-08-20 | [10.5281/zenodo.22021889](https://doi.org/10.5281/zenodo.22021889) |
| [The CHGNet uMLIP model fine-tuned for 2Hc-WS2](https://doi.org/10.5281/zenodo.22059539) | CHGNet | WS2, MoS2 | DFT, MLIP | 2026-08-22 | [10.5281/zenodo.22059539](https://doi.org/10.5281/zenodo.22059539) |
| [The CHGNet uMLIP model fine-tuned for 2Hc-WS2](https://doi.org/10.5281/zenodo.22059540) | CHGNet | WS2, MoS2 | DFT, MLIP | 2026-08-22 | [10.5281/zenodo.22059540](https://doi.org/10.5281/zenodo.22059540) |
| [Equivariance as a Substitutable Resource: A Unified Scaling Law for Machine-Learned Interatomic Potentials](https://doi.org/10.5281/zenodo.22063928) | MACE | molecule / organic | MLIP | 2026-08-23 | [10.5281/zenodo.22063928](https://doi.org/10.5281/zenodo.22063928) |
| [Equivariance as a Substitutable Resource: A Unified Scaling Law for Machine-Learned Interatomic Potentials](https://doi.org/10.5281/zenodo.22063807) | MACE | molecule / organic | MLIP | 2026-08-23 | [10.5281/zenodo.22063807](https://doi.org/10.5281/zenodo.22063807) |
| [A computed thermoelectric feature database for 50,992 GNoME materials](https://doi.org/10.26434/chemrxiv.15007873/v1) | CHGNet, GNoME | thermoelectric | DFT, MLIP | 2026-08-26 | [10.26434/chemrxiv.15007873/v1](https://doi.org/10.26434/chemrxiv.15007873/v1) |
| [Universal Thermodynamic Interatomic Potentials for Crystalline Materials](http://arxiv.org/abs/2608.14502v1) | UMA |  | MD, MLIP, free energy | 2026-08-14 | [link](http://arxiv.org/abs/2608.14502v1) |
| [Data-Efficient Construction of Material-Specific Machine-Learning Interatomic Potentials from Ab Initio Molecular Dynami](http://arxiv.org/abs/2608.14899v1) | GRACE-1L-OAM, SevenNet-0, MatterSim, MACE-MP-0 |  | DFT, AIMD, MD, MLIP | 2026-08-14 | [link](http://arxiv.org/abs/2608.14899v1) |
| [GRACE-OFF: A machine-learned interatomic potential for organic liquids using the GRACE architecture](https://doi.org/10.26434/chemrxiv.15001529/v2) | GRACE, MACE |  | MLIP | 2026-08-18 | [10.26434/chemrxiv.15001529/v2](https://doi.org/10.26434/chemrxiv.15001529/v2) |
| [How AI Coding Agents Can Unlock Materials Simulation with NVIDIA ALCHEMI Toolkit](https://developer.nvidia.com/blog/how-ai-coding-agents-can-unlock-materials-simulation-with-nvidia-alchemi-toolkit/) | ALCHEMI |  |  | 2026-08-18 | [link](https://developer.nvidia.com/blog/how-ai-coding-agents-can-unlock-materials-simulation-with-nvidia-alchemi-toolkit/) |
| [Exploring celecoxib polymorph landscape using AIMNet2 machine learning interatomic potential](https://doi.org/10.17615/xd5h-sd62) | AIMNet2 |  | DFT, MLIP | 2026-08-20 | [10.17615/xd5h-sd62](https://doi.org/10.17615/xd5h-sd62) |
| [Accurate and Efficient NMR Crystallography through Machine-Learning Geometry Optimization and Shielding Prediction](https://doi.org/10.1021/acs.jpclett.6c02446) | UMA |  | PBE, hybrid DFT, DFT | 2026-08-21 | [10.1021/acs.jpclett.6c02446](https://doi.org/10.1021/acs.jpclett.6c02446) |
| [Benchmarking Machine Learning Methods for Predicting Adiabatic Redox Potentials](https://doi.org/10.26434/chemrxiv.15007720/v1) | MACE |  | DFT | 2026-08-21 | [10.26434/chemrxiv.15007720/v1](https://doi.org/10.26434/chemrxiv.15007720/v1) |
| [Data-Efficient and Fast Machine Learning Molecular Dynamics through Integrated Active Learning and Knowledge Distillatio](https://doi.org/10.1021/acs.jctc.6c00917) | DeePMD, MACE |  | DFT, MD, MLIP | 2026-08-21 | [10.1021/acs.jctc.6c00917](https://doi.org/10.1021/acs.jctc.6c00917) |
| [FastMD](https://doi.org/10.5281/zenodo.22051980) | ALIGNN, CHGNet |  | MD, MLIP | 2026-08-22 | [10.5281/zenodo.22051980](https://doi.org/10.5281/zenodo.22051980) |
| [FastMD](https://doi.org/10.5281/zenodo.22051979) | ALIGNN, CHGNet |  | MD, MLIP | 2026-08-22 | [10.5281/zenodo.22051979](https://doi.org/10.5281/zenodo.22051979) |
| [PhononBench:A Large-Scale Phonon-Based Benchmark for Dynamical Stability in Crystal Generation](https://doi.org/10.1088/3050-287x/ae9ee4) | MatterSim, MatterGen |  | phonons | 2026-08-26 | [10.1088/3050-287x/ae9ee4](https://doi.org/10.1088/3050-287x/ae9ee4) |
| [Realistic Simulations of Energy Materials Using Foundation Models and Electrode-Potential Learning](https://doi.org/10.26434/chemrxiv.15007895/v1) | SevenNet |  | DFT, MLIP | 2026-08-26 | [10.26434/chemrxiv.15007895/v1](https://doi.org/10.26434/chemrxiv.15007895/v1) |
| [Materials Discovery and Design](https://doi.org/10.1002/9783527852048.ch9) |  | polymer |  | 2026-08-14 | [10.1002/9783527852048.ch9](https://doi.org/10.1002/9783527852048.ch9) |
| [Neural Networks Accelerate Ab Initio Multiple Spawning Simulations: A Case Study of Using Machine Learning Potentials fo](https://doi.org/10.26434/chemrxiv.15007443/v1) |  | molecule / organic | DFT, MLIP | 2026-08-14 | [10.26434/chemrxiv.15007443/v1](https://doi.org/10.26434/chemrxiv.15007443/v1) |
| [Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks v](http://arxiv.org/abs/2608.14990v1) |  | MOF, CO2 |  | 2026-08-15 | [link](http://arxiv.org/abs/2608.14990v1) |
| [Crystal-structure design by agentic AI in a language of motifs](https://doi.org/10.48550/arxiv.2608.15900) |  | magnetic material | DFT | 2026-08-16 | [10.48550/arxiv.2608.15900](https://doi.org/10.48550/arxiv.2608.15900) |
| [G2RINS: A Generative String-and-Graph Polymer Representation to Assist Computational Materials Discovery](https://doi.org/10.26434/chemrxiv.15007504/v1) |  | polymer | MD | 2026-08-17 | [10.26434/chemrxiv.15007504/v1](https://doi.org/10.26434/chemrxiv.15007504/v1) |
| [Atomistic Structure Generation and Neural-Network Screening of Hard Carbons to Identify High-Capacity Sodium Storage](http://arxiv.org/abs/2608.17716v1) |  | Li-ion battery | MLIP | 2026-08-18 | [link](http://arxiv.org/abs/2608.17716v1) |
| [Optimization of active learning strategies for infrared spectra prediction in catalysis](https://doi.org/10.26434/chemrxiv.15007549/v1) |  | catalyst, molecule / organic | DFT, AIMD, MD, MLIP | 2026-08-18 | [10.26434/chemrxiv.15007549/v1](https://doi.org/10.26434/chemrxiv.15007549/v1) |
| [JANUS: A Multi-modal Foundation Neural Sampler for Disordered Materials](http://arxiv.org/abs/2608.19116v1) |  | alloy | Monte Carlo | 2026-08-19 | [link](http://arxiv.org/abs/2608.19116v1) |
| [Enhancing EBSD throughput of battery electrode materials using super-resolution generative adversarial networks](http://arxiv.org/abs/2608.19117v1) |  | Li-ion battery |  | 2026-08-19 | [link](http://arxiv.org/abs/2608.19117v1) |
| [Local Symmetry Breaking and Correlated Fluctuations in Quantum Materials from Atomistic Foundation Models](https://doi.org/10.26434/chemrxiv.15001387/v2) |  | superconductor | DFT, AIMD, MD, phonons | 2026-08-19 | [10.26434/chemrxiv.15001387/v2](https://doi.org/10.26434/chemrxiv.15001387/v2) |
| [Lithium Layers Govern Wave-like Cross-Plane Transport and Thermal Anisotropy in LiCoO2](https://doi.org/10.1021/acsaem.6c01338) |  | Li-ion battery, LiCoO2, CoO2 | DFT, MD, phonons, MLIP | 2026-08-20 | [10.1021/acsaem.6c01338](https://doi.org/10.1021/acsaem.6c01338) |
| [Machine Learning Guided Discovery of Corundum High Entropy Oxides](http://arxiv.org/abs/2608.20596v1) |  | oxide | MLIP | 2026-08-20 | [link](http://arxiv.org/abs/2608.20596v1) |
| [Machine Learning Guided Discovery of Corundum High Entropy Oxides](https://doi.org/10.48550/arxiv.2608.20596) |  | oxide | MLIP | 2026-08-20 | [10.48550/arxiv.2608.20596](https://doi.org/10.48550/arxiv.2608.20596) |
| [Atomic-Scale Origin of the Cation Field Strength Dependence of Mechanical Properties in Divalent-Cation Aluminosilicate ](https://doi.org/10.1021/acs.jpcb.6c03531) |  | oxide, glass / amorphous | r2SCAN, PBE, DFT, MD | 2026-08-21 | [10.1021/acs.jpcb.6c03531](https://doi.org/10.1021/acs.jpcb.6c03531) |
| [Charge-State-Aware Machine-Learned Molecular Dynamics for Reactive Systems with Charge Transfer](https://doi.org/10.26434/chemrxiv.15007718/v1) |  | NH3 | DFT, AIMD, MD, MLIP | 2026-08-21 | [10.26434/chemrxiv.15007718/v1](https://doi.org/10.26434/chemrxiv.15007718/v1) |
| [Stable Models, Unstable Candidates: Target Transferability in MOF Machine Learning for Gas Uptake Prediction](https://doi.org/10.26434/chemrxiv.15007729/v1) |  | MOF, CO2, CH4 |  | 2026-08-21 | [10.26434/chemrxiv.15007729/v1](https://doi.org/10.26434/chemrxiv.15007729/v1) |
| [Vibrational, structural, and chemical fingerprints of ion diffusion in crystalline solids](http://arxiv.org/abs/2608.21624v1) |  | solid electrolyte | MD, MLIP, free energy | 2026-08-21 | [link](http://arxiv.org/abs/2608.21624v1) |
| [Vibrational, structural, and chemical fingerprints of ion diffusion in crystalline solids](https://doi.org/10.48550/arxiv.2608.21624) |  | solid electrolyte | MD, MLIP, free energy | 2026-08-21 | [10.48550/arxiv.2608.21624](https://doi.org/10.48550/arxiv.2608.21624) |
| [First-Principles Atomistic Structure and Dynamics of Polyethylene During High-Pressure Radical Polymerization via Machin](http://arxiv.org/abs/2608.21741v1) |  | polymer, high pressure | DFT | 2026-08-22 | [link](http://arxiv.org/abs/2608.21741v1) |
| [First-Principles Atomistic Structure and Dynamics of Polyethylene During High-Pressure Radical Polymerization via Machin](https://doi.org/10.48550/arxiv.2608.21741) |  | polymer, high pressure | DFT, MLIP | 2026-08-22 | [10.48550/arxiv.2608.21741](https://doi.org/10.48550/arxiv.2608.21741) |
| [Polymer-Linked Nanoparticle Networks Running on Heat Can Act as Computing Devices](http://arxiv.org/abs/2608.22841v1) |  | polymer | MD, phonons | 2026-08-24 | [link](http://arxiv.org/abs/2608.22841v1) |
| [Bayesian Neural Networks versus deep ensembles for uncertainty quantification in machine learning interatomic potentials](https://doi.org/10.1088/2632-2153/ae9de8) |  | molecule / organic | MLIP | 2026-08-24 | [10.1088/2632-2153/ae9de8](https://doi.org/10.1088/2632-2153/ae9de8) |
| [Y-Mn-B Magnetic Materials: A DFT and Machine Learning Dataset](https://doi.org/10.5281/zenodo.22084773) |  | magnetic material, Y3MnB7, YMnB4 | DFT, phonons, MLIP | 2026-08-24 | [10.5281/zenodo.22084773](https://doi.org/10.5281/zenodo.22084773) |
| [Y-Mn-B Magnetic Materials: A DFT and Machine Learning Dataset](https://doi.org/10.5281/zenodo.22084774) |  | magnetic material, Y3MnB7, YMnB4 | DFT, phonons, MLIP | 2026-08-24 | [10.5281/zenodo.22084774](https://doi.org/10.5281/zenodo.22084774) |
| [Machine Learning Prediction of Transport Properties in Amorphous Polymer Electrolytes Using Chemically Informed Structur](https://doi.org/10.26434/chemrxiv.15000431/v2) |  | polymer, glass / amorphous |  | 2026-08-25 | [10.26434/chemrxiv.15000431/v2](https://doi.org/10.26434/chemrxiv.15000431/v2) |
| [Mechanistic study of mixed lithium halides solid-state electrolytes](https://doi.org/10.1103/czy4-7lfp) |  | solid electrolyte, alloy | HSE06, MLIP | 2026-08-26 | [10.1103/czy4-7lfp](https://doi.org/10.1103/czy4-7lfp) |
| [Insights into Lithium Diffusion in Crystalline and Amorphous Solid Electrolytes with Machine Learning Interatomic Potent](https://doi.org/10.26434/chemrxiv.15007863/v1) |  | solid electrolyte, Li-ion battery, glass / amorphous, Li3YCl6 | MD, MLIP | 2026-08-26 | [10.26434/chemrxiv.15007863/v1](https://doi.org/10.26434/chemrxiv.15007863/v1) |
| [High-throughput Discovery of Magnetic Rare Earth Transition Metal Alloys](http://arxiv.org/abs/2608.25270v1) |  | alloy | DFT, MLIP | 2026-08-26 | [link](http://arxiv.org/abs/2608.25270v1) |
| [High-throughput Discovery of Magnetic Rare Earth Transition Metal Alloys](https://doi.org/10.48550/arxiv.2608.25270) |  | alloy, magnetic material | DFT, MLIP | 2026-08-26 | [10.48550/arxiv.2608.25270](https://doi.org/10.48550/arxiv.2608.25270) |
| [A Hierarchical Synergistic Deep Learning Framework Integrating Composition, Structure, and Ionic Transport for Solid-Sta](http://arxiv.org/abs/2608.25592v1) |  | solid electrolyte |  | 2026-08-26 | [link](http://arxiv.org/abs/2608.25592v1) |
| [When less is more: simplified models for interpretable materials design](https://doi.org/10.26434/chemrxiv.15008004/v1) |  | polymer |  | 2026-08-28 | [10.26434/chemrxiv.15008004/v1](https://doi.org/10.26434/chemrxiv.15008004/v1) |
| [From Empirical Design To Autonomous Ecosystems: AI-Driven Advances, Challenges, And Future Directions In Precision Nanom](https://doi.org/10.5281/zenodo.21931873) |  |  |  | 2026-08-14 | [10.5281/zenodo.21931873](https://doi.org/10.5281/zenodo.21931873) |
| [From Empirical Design To Autonomous Ecosystems: AI-Driven Advances, Challenges, And Future Directions In Precision Nanom](https://doi.org/10.5281/zenodo.21931872) |  |  |  | 2026-08-14 | [10.5281/zenodo.21931872](https://doi.org/10.5281/zenodo.21931872) |
| [The Past and Future of AI Scientists](http://arxiv.org/abs/2608.14407v1) |  |  | MLIP | 2026-08-14 | [link](http://arxiv.org/abs/2608.14407v1) |
| [Electrostatic Phenomenology Benchmarks for Machine-Learned Interatomic Potentials in Electrochemistry: Beyond the Energy](http://arxiv.org/abs/2608.14153v1) |  |  | MLIP | 2026-08-14 | [link](http://arxiv.org/abs/2608.14153v1) |
| [Crystal-structure design by agentic AI in a language of motifs](http://arxiv.org/abs/2608.15900v1) |  |  | DFT | 2026-08-16 | [link](http://arxiv.org/abs/2608.15900v1) |
| [Graph neural network prediction of temperature-dependent hydrogen diffusion and thermal conductivity tensors of tungsten](http://arxiv.org/abs/2608.15609v1) |  |  | MD | 2026-08-16 | [link](http://arxiv.org/abs/2608.15609v1) |
| [ChemReporter: A Framework for Curating and Exporting Large-Scale Chemical Datasets for MLIP Training](http://arxiv.org/abs/2608.16418v1) |  |  | MLIP | 2026-08-17 | [link](http://arxiv.org/abs/2608.16418v1) |
| [Discovery of novel magnetic Y-Mn-B compounds via advanced machine learning guided framework](http://arxiv.org/abs/2608.17200v1) |  |  | DFT | 2026-08-17 | [link](http://arxiv.org/abs/2608.17200v1) |
| [Extracting a nitrile-centered, ether-assisted motif hierarchy for lithium-battery electrolyte design from billion-scale ](http://arxiv.org/abs/2608.16364v1) |  |  |  | 2026-08-17 | [link](http://arxiv.org/abs/2608.16364v1) |
| [Machine Learning-Accelerated Band-Edge Engineering of Pnictogen Chalcohalide Solid Solutions for Solar Energy Technologi](http://arxiv.org/abs/2608.16611v1) |  |  | DFT | 2026-08-17 | [link](http://arxiv.org/abs/2608.16611v1) |
| [Unlocking Multi-Component Bulk-Materials Molecular Dynamics with a Small-Footprint Machine Learning Interatomic Potentia](http://arxiv.org/abs/2608.16329v1) |  |  | MD, MLIP | 2026-08-17 | [link](http://arxiv.org/abs/2608.16329v1) |
| [Active learning molecular beam epitaxy of complex quantum materials](http://arxiv.org/abs/2608.17742v1) |  |  |  | 2026-08-18 | [link](http://arxiv.org/abs/2608.17742v1) |
| [PyAPX: python toolkit for atomic configuration pattern exploration](https://doi.org/10.1038/s41598-026-66072-5) |  |  | DFT, MLIP | 2026-08-19 | [10.1038/s41598-026-66072-5](https://doi.org/10.1038/s41598-026-66072-5) |
| [A single design choice determines whether machine learning models of materials make physically impossible predictions](http://arxiv.org/abs/2608.18714v1) |  |  | DFT | 2026-08-19 | [link](http://arxiv.org/abs/2608.18714v1) |
| [Dynamic Ensembles of Phosphine-Stabilized Gold Nanoclusters](http://arxiv.org/abs/2608.19404v1) |  |  | MD, MLIP | 2026-08-19 | [link](http://arxiv.org/abs/2608.19404v1) |
| [Generative AI and Emerging Technologies: Transforming Engineering, Innovation and Entrepreneurship](https://doi.org/10.5281/zenodo.22025110) |  |  |  | 2026-08-20 | [10.5281/zenodo.22025110](https://doi.org/10.5281/zenodo.22025110) |
| [Generative AI and Emerging Technologies: Transforming Engineering, Innovation and Entrepreneurship](https://doi.org/10.5281/zenodo.22025109) |  |  |  | 2026-08-20 | [10.5281/zenodo.22025109](https://doi.org/10.5281/zenodo.22025109) |
| [Machine Learning to Foundation Models: Artificial Intelligence for Nanophotonic Modeling and Scientific Discovery](https://doi.org/10.48550/arxiv.2608.21612) |  |  | MLIP | 2026-08-21 | [10.48550/arxiv.2608.21612](https://doi.org/10.48550/arxiv.2608.21612) |
| [Diagnosing and narrowing the simulation-to-real gap in powder X-ray diffraction with a wet-dry agentic loop](http://arxiv.org/abs/2608.22400v1) |  |  |  | 2026-08-23 | [link](http://arxiv.org/abs/2608.22400v1) |
| [Dataset for the publication- A cylindrical sintering method for more realistic grain boundaries in nanocrystalline thin ](https://doi.org/10.5281/zenodo.22111105) |  |  |  | 2026-08-24 | [10.5281/zenodo.22111105](https://doi.org/10.5281/zenodo.22111105) |
| [Dataset for the publication- A cylindrical sintering method for more realistic grain boundaries in nanocrystalline thin ](https://doi.org/10.5281/zenodo.22111106) |  |  |  | 2026-08-24 | [10.5281/zenodo.22111106](https://doi.org/10.5281/zenodo.22111106) |
| [Machine learning for biomaterials design](https://doi.org/10.1038/s44222-026-00476-w) |  |  |  | 2026-08-25 | [10.1038/s44222-026-00476-w](https://doi.org/10.1038/s44222-026-00476-w) |
| [Continuous Scalar Kernels for Quotients of Variable-Cell Periodic Structures: Compactness, Acquisition, and Target Bound](https://doi.org/10.26434/chemrxiv.15006891/v3) |  |  | MLIP | 2026-08-25 | [10.26434/chemrxiv.15006891/v3](https://doi.org/10.26434/chemrxiv.15006891/v3) |
| [Multiscale Modelling of Ferroelectrics using a Physics-Informed Neural Network Driven by Molecular Dynamics Data: Parame](http://arxiv.org/abs/2608.24733v1) |  |  | MD | 2026-08-25 | [link](http://arxiv.org/abs/2608.24733v1) |
| [Attention-based composition learning for thermodynamic and electronic property prediction in inorganic materials](https://doi.org/10.1016/j.nxmate.2026.103265) |  |  | DFT | 2026-08-25 | [10.1016/j.nxmate.2026.103265](https://doi.org/10.1016/j.nxmate.2026.103265) |
| [DeepField: Condensed-Phase Quantum Learning for All-Atom Protein Dynamics in Explicit Water](https://doi.org/10.26434/chemrxiv.15007896/v1) |  |  | MD, MLIP | 2026-08-26 | [10.26434/chemrxiv.15007896/v1](https://doi.org/10.26434/chemrxiv.15007896/v1) |
| [Preprint of the publication- A cylindrical sintering method for more realistic grain boundaries in nanocrystalline thin ](https://doi.org/10.5281/zenodo.22112768) |  |  |  | 2026-08-26 | [10.5281/zenodo.22112768](https://doi.org/10.5281/zenodo.22112768) |
| [Preprint of the publication- A cylindrical sintering method for more realistic grain boundaries in nanocrystalline thin ](https://doi.org/10.5281/zenodo.22112767) |  |  |  | 2026-08-26 | [10.5281/zenodo.22112767](https://doi.org/10.5281/zenodo.22112767) |
| [Enhancing materials discovery with valence-constrained design in generative modeling](https://www.nature.com/articles/s43588-026-01037-2) |  |  |  | 2026-08-26 | [10.1038/s43588-026-01037-2](https://doi.org/10.1038/s43588-026-01037-2) |
| [Comparative study of ensemble-based uncertainty quantification methods for neural network interatomic potentials](https://doi.org/10.1088/2632-2153/ae9fb4) |  |  | DFT, phonons, MLIP | 2026-08-27 | [10.1088/2632-2153/ae9fb4](https://doi.org/10.1088/2632-2153/ae9fb4) |
| [Carbon Nanotube-Induced Magnetic Shielding Effects on 129Xe NMR from Equivariant Neural Networks](https://doi.org/10.26434/chemrxiv.15007956/v1) |  |  | MD, MLIP | 2026-08-27 | [10.26434/chemrxiv.15007956/v1](https://doi.org/10.26434/chemrxiv.15007956/v1) |
| [Benchmarking of Fast and Interpretable UF Machine Learning Potentials](http://arxiv.org/abs/2608.27277v1) |  |  | DFT, MD, MLIP | 2026-08-27 | [link](http://arxiv.org/abs/2608.27277v1) |
| [Packora: Systematic Design for Generative Molecular Crystal Structure Prediction](http://arxiv.org/abs/2608.26962v1) |  |  |  | 2026-08-27 | [link](http://arxiv.org/abs/2608.26962v1) |
| [Neural network finds twisted crystals that steer light at the nanoscale](https://www.nature.com/articles/s41563-026-02744-x) |  |  |  | 2026-08-28 | [10.1038/s41563-026-02744-x](https://doi.org/10.1038/s41563-026-02744-x) |
| [Autoregressive Generative Latent Diffusion Models for Magnetohydrodynamics](https://doi.org/10.1109/icops53334.2026.11660190) |  |  |  | 2026-08-28 | [10.1109/icops53334.2026.11660190](https://doi.org/10.1109/icops53334.2026.11660190) |

## Summary of gaps

- Studies with no identifiable model name: **68**
- Studies with no identifiable calculation method: **24**
- Studies with no numeric metric: **88**
- Benchmarked models missing at least one field: **15**

The dominant cause is structural, not fixable by better parsing: abstracts rarely quote error values, and full text is usually paywalled.

