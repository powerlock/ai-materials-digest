# Needs data - awaiting further input

Generated 2026-09-02. Every field below was blank in the automated sources. Fill any of them in `manual_data.json` and rerun `python build_summary.py`; your values take priority and are never overwritten.

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

## Studies with no numeric performance figure (136 of 141)

These need a human to open the paper and read the results table. Highest value first: studies that already name a model and a material, so only the number is missing.

| Study | Models named | Materials | Method | Date | DOI |
|---|---|---|---|---|---|
| [Conservation-Resolved Error Decomposition: A Benchmark Axis for Electronic-Structure Methods and Machine-Learned Interat](https://doi.org/10.26434/chemrxiv.15007478/v1) | MACE | OFF23 | hybrid DFT, MLIP | 2026-08-17 | [10.26434/chemrxiv.15007478/v1](https://doi.org/10.26434/chemrxiv.15007478/v1) |
| [HIP: Hessian Interatomic Potentials](https://doi.org/10.5281/zenodo.22003592) | EquiformerV2 | molecule / organic | MLIP | 2026-08-19 | [10.5281/zenodo.22003592](https://doi.org/10.5281/zenodo.22003592) |
| [Integration of Machine Learning and Solid-State Chemistry for the Discovery of Electrochemical Materials for Fuel Cells ](https://doi.org/10.5281/zenodo.22021890) | MEGNet, ALIGNN, CGCNN | Li-ion battery, catalyst, oxide | DFT | 2026-08-20 | [10.5281/zenodo.22021890](https://doi.org/10.5281/zenodo.22021890) |
| [The CHGNet uMLIP model fine-tuned for 2Hc-WS2](https://doi.org/10.5281/zenodo.22059539) | CHGNet | WS2, MoS2 | DFT, MLIP | 2026-08-22 | [10.5281/zenodo.22059539](https://doi.org/10.5281/zenodo.22059539) |
| [Equivariance as a Substitutable Resource: A Unified Scaling Law for Machine-Learned Interatomic Potentials](https://doi.org/10.5281/zenodo.22063807) | MACE | molecule / organic | MLIP | 2026-08-23 | [10.5281/zenodo.22063807](https://doi.org/10.5281/zenodo.22063807) |
| [A computed thermoelectric feature database for 50,992 GNoME materials](https://doi.org/10.26434/chemrxiv.15007873/v1) | CHGNet, GNoME | thermoelectric | DFT, MLIP | 2026-08-26 | [10.26434/chemrxiv.15007873/v1](https://doi.org/10.26434/chemrxiv.15007873/v1) |
| [Cross-Scale Assessment of MACE Foundation Models and from Scratch Trained Potentials for Bi-Pt Systems](https://doi.org/10.26434/chemrxiv.15007985/v1) | MACE | Bi18Pt24 | DFT, phonons, MLIP | 2026-08-27 | [10.26434/chemrxiv.15007985/v1](https://doi.org/10.26434/chemrxiv.15007985/v1) |
| [Generative artificial intelligence for reliable mechanistic reasoning for corrosion](http://arxiv.org/abs/2609.00099v1) | Llama | alloy |  | 2026-08-31 | [link](http://arxiv.org/abs/2609.00099v1) |
| [Universal Thermodynamic Interatomic Potentials for Crystalline Materials](http://arxiv.org/abs/2608.14502v1) | UMA |  | MD, MLIP, free energy | 2026-08-14 | [link](http://arxiv.org/abs/2608.14502v1) |
| [Data-Efficient Construction of Material-Specific Machine-Learning Interatomic Potentials from Ab Initio Molecular Dynami](http://arxiv.org/abs/2608.14899v1) | GRACE-1L-OAM, SevenNet-0, MACE-MP-0, MatterSim |  | DFT, AIMD, MD, MLIP | 2026-08-14 | [link](http://arxiv.org/abs/2608.14899v1) |
| [GRACE-OFF: A machine-learned interatomic potential for organic liquids using the GRACE architecture](https://doi.org/10.26434/chemrxiv.15001529/v2) | GRACE, MACE |  | MLIP | 2026-08-18 | [10.26434/chemrxiv.15001529/v2](https://doi.org/10.26434/chemrxiv.15001529/v2) |
| [How AI Coding Agents Can Unlock Materials Simulation with NVIDIA ALCHEMI Toolkit](https://developer.nvidia.com/blog/how-ai-coding-agents-can-unlock-materials-simulation-with-nvidia-alchemi-toolkit/) | ALCHEMI |  |  | 2026-08-18 | [link](https://developer.nvidia.com/blog/how-ai-coding-agents-can-unlock-materials-simulation-with-nvidia-alchemi-toolkit/) |
| [Exploring celecoxib polymorph landscape using AIMNet2 machine learning interatomic potential](https://doi.org/10.17615/xd5h-sd62) | AIMNet2 |  | DFT, MLIP | 2026-08-20 | [10.17615/xd5h-sd62](https://doi.org/10.17615/xd5h-sd62) |
| [Benchmarking Machine Learning Methods for Predicting Adiabatic Redox Potentials](https://doi.org/10.26434/chemrxiv.15007720/v1) | MACE |  | DFT | 2026-08-21 | [10.26434/chemrxiv.15007720/v1](https://doi.org/10.26434/chemrxiv.15007720/v1) |
| [Data-Efficient and Fast Machine Learning Molecular Dynamics through Integrated Active Learning and Knowledge Distillatio](https://doi.org/10.1021/acs.jctc.6c00917) | DeePMD, MACE |  | DFT, MD, MLIP | 2026-08-21 | [10.1021/acs.jctc.6c00917](https://doi.org/10.1021/acs.jctc.6c00917) |
| [Accurate and Efficient NMR Crystallography through Machine-Learning Geometry Optimization and Shielding Prediction](https://doi.org/10.1021/acs.jpclett.6c02446) | UMA |  | PBE, hybrid DFT, DFT | 2026-08-21 | [10.1021/acs.jpclett.6c02446](https://doi.org/10.1021/acs.jpclett.6c02446) |
| [FastMD](https://doi.org/10.5281/zenodo.22051980) | CHGNet, ALIGNN |  | MD, MLIP | 2026-08-22 | [10.5281/zenodo.22051980](https://doi.org/10.5281/zenodo.22051980) |
| [PhononBench:A Large-Scale Phonon-Based Benchmark for Dynamical Stability in Crystal Generation](https://doi.org/10.1088/3050-287x/ae9ee4) | MatterGen, MatterSim |  | phonons | 2026-08-26 | [10.1088/3050-287x/ae9ee4](https://doi.org/10.1088/3050-287x/ae9ee4) |
| [Grain-Boundary Premelting in High-Entropy Transition Metal Carbides](https://doi.org/10.48550/arxiv.2608.27273) | MACE |  | MD, Monte Carlo, MLIP | 2026-08-27 | [10.48550/arxiv.2608.27273](https://doi.org/10.48550/arxiv.2608.27273) |
| [ase-calculator-kit: a unified ASE calculator factory for MLIP and DFT calculators](https://doi.org/10.5281/zenodo.21807793) | MatterSim, SevenNet, CHGNet, NequIP, MACE, UMA |  | DFT, MLIP | 2026-08-28 | [10.5281/zenodo.21807793](https://doi.org/10.5281/zenodo.21807793) |
| [GMD Task 4 composition-support audit - structures and public-checkpoint predictions](https://doi.org/10.5281/zenodo.22215787) | NequIP, MACE |  | DFT, MLIP | 2026-08-31 | [10.5281/zenodo.22215787](https://doi.org/10.5281/zenodo.22215787) |
| [Realistic Simulations of Energy Materials Using Foundation Models and Electrode-Potential Learning](https://doi.org/10.26434/chemrxiv.15007895/v2) | SevenNet |  | DFT, MLIP | 2026-08-31 | [10.26434/chemrxiv.15007895/v2](https://doi.org/10.26434/chemrxiv.15007895/v2) |
| [Diagnosing Latent Energy Decomposition in Machine-Learning Interatomic Potentials via Interacting Quantum Atoms](http://arxiv.org/abs/2609.00674v1) | Allegro |  | MLIP | 2026-09-01 | [link](http://arxiv.org/abs/2609.00674v1) |
| [Unveiling Phase Transformation Mechanism in BN from Large-Scale Machine Learning Molecular Dynamics](https://doi.org/10.26434/chemrxiv.15008201/v1) | MACE |  | DFT, AIMD, MD, MLIP | 2026-09-02 | [10.26434/chemrxiv.15008201/v1](https://doi.org/10.26434/chemrxiv.15008201/v1) |
| [Materials Discovery and Design](https://doi.org/10.1002/9783527852048.ch9) |  | polymer |  | 2026-08-14 | [10.1002/9783527852048.ch9](https://doi.org/10.1002/9783527852048.ch9) |
| [Neural Networks Accelerate Ab Initio Multiple Spawning Simulations: A Case Study of Using Machine Learning Potentials fo](https://doi.org/10.26434/chemrxiv.15007443/v1) |  | molecule / organic | DFT, MLIP | 2026-08-14 | [10.26434/chemrxiv.15007443/v1](https://doi.org/10.26434/chemrxiv.15007443/v1) |
| [Discovering Physically Interpretable Mathematical Expression for Predicting CO2 Adsorption in Metal-Organic Frameworks v](http://arxiv.org/abs/2608.14990v1) |  | MOF, CO2 |  | 2026-08-15 | [link](http://arxiv.org/abs/2608.14990v1) |
| [Crystal-structure design by agentic AI in a language of motifs](https://doi.org/10.48550/arxiv.2608.15900) |  | magnetic material | DFT | 2026-08-16 | [10.48550/arxiv.2608.15900](https://doi.org/10.48550/arxiv.2608.15900) |
| [G2RINS: A Generative String-and-Graph Polymer Representation to Assist Computational Materials Discovery](https://doi.org/10.26434/chemrxiv.15007504/v1) |  | polymer | MD | 2026-08-17 | [10.26434/chemrxiv.15007504/v1](https://doi.org/10.26434/chemrxiv.15007504/v1) |
| [Optimization of active learning strategies for infrared spectra prediction in catalysis](https://doi.org/10.26434/chemrxiv.15007549/v1) |  | catalyst, molecule / organic | DFT, AIMD, MD, MLIP | 2026-08-18 | [10.26434/chemrxiv.15007549/v1](https://doi.org/10.26434/chemrxiv.15007549/v1) |
| [Atomistic Structure Generation and Neural-Network Screening of Hard Carbons to Identify High-Capacity Sodium Storage](http://arxiv.org/abs/2608.17716v1) |  | Li-ion battery | MLIP | 2026-08-18 | [link](http://arxiv.org/abs/2608.17716v1) |
| [Local Symmetry Breaking and Correlated Fluctuations in Quantum Materials from Atomistic Foundation Models](https://doi.org/10.26434/chemrxiv.15001387/v2) |  | superconductor | DFT, AIMD, MD, phonons | 2026-08-19 | [10.26434/chemrxiv.15001387/v2](https://doi.org/10.26434/chemrxiv.15001387/v2) |
| [Enhancing EBSD throughput of battery electrode materials using super-resolution generative adversarial networks](http://arxiv.org/abs/2608.19117v1) |  | Li-ion battery |  | 2026-08-19 | [link](http://arxiv.org/abs/2608.19117v1) |
| [JANUS: A Multi-modal Foundation Neural Sampler for Disordered Materials](http://arxiv.org/abs/2608.19116v1) |  | alloy | Monte Carlo | 2026-08-19 | [link](http://arxiv.org/abs/2608.19116v1) |
| [Lithium Layers Govern Wave-like Cross-Plane Transport and Thermal Anisotropy in LiCoO2](https://doi.org/10.1021/acsaem.6c01338) |  | Li-ion battery, LiCoO2, CoO2 | DFT, MD, phonons, MLIP | 2026-08-20 | [10.1021/acsaem.6c01338](https://doi.org/10.1021/acsaem.6c01338) |
| [Machine Learning Guided Discovery of Corundum High Entropy Oxides](https://doi.org/10.48550/arxiv.2608.20596) |  | oxide | MLIP | 2026-08-20 | [10.48550/arxiv.2608.20596](https://doi.org/10.48550/arxiv.2608.20596) |
| [Stable Models, Unstable Candidates: Target Transferability in MOF Machine Learning for Gas Uptake Prediction](https://doi.org/10.26434/chemrxiv.15007729/v1) |  | MOF, CO2, CH4 |  | 2026-08-21 | [10.26434/chemrxiv.15007729/v1](https://doi.org/10.26434/chemrxiv.15007729/v1) |
| [Atomic-Scale Origin of the Cation Field Strength Dependence of Mechanical Properties in Divalent-Cation Aluminosilicate ](https://doi.org/10.1021/acs.jpcb.6c03531) |  | oxide, glass / amorphous | r2SCAN, PBE, DFT, MD | 2026-08-21 | [10.1021/acs.jpcb.6c03531](https://doi.org/10.1021/acs.jpcb.6c03531) |
| [Charge-State-Aware Machine-Learned Molecular Dynamics for Reactive Systems with Charge Transfer](https://doi.org/10.26434/chemrxiv.15007718/v1) |  | NH3 | DFT, AIMD, MD, MLIP | 2026-08-21 | [10.26434/chemrxiv.15007718/v1](https://doi.org/10.26434/chemrxiv.15007718/v1) |
| [Vibrational, structural, and chemical fingerprints of ion diffusion in crystalline solids](https://doi.org/10.48550/arxiv.2608.21624) |  | solid electrolyte | MD, MLIP, free energy | 2026-08-21 | [10.48550/arxiv.2608.21624](https://doi.org/10.48550/arxiv.2608.21624) |
| [First-Principles Atomistic Structure and Dynamics of Polyethylene During High-Pressure Radical Polymerization via Machin](https://doi.org/10.48550/arxiv.2608.21741) |  | polymer, high pressure | DFT, MLIP | 2026-08-22 | [10.48550/arxiv.2608.21741](https://doi.org/10.48550/arxiv.2608.21741) |
| [Y-Mn-B Magnetic Materials: A DFT and Machine Learning Dataset](https://doi.org/10.5281/zenodo.22084773) |  | magnetic material, Y3MnB7, YMnB4 | DFT, phonons, MLIP | 2026-08-24 | [10.5281/zenodo.22084773](https://doi.org/10.5281/zenodo.22084773) |
| [Bayesian Neural Networks versus deep ensembles for uncertainty quantification in machine learning interatomic potentials](https://doi.org/10.1088/2632-2153/ae9de8) |  | molecule / organic | MLIP | 2026-08-24 | [10.1088/2632-2153/ae9de8](https://doi.org/10.1088/2632-2153/ae9de8) |
| [Polymer-Linked Nanoparticle Networks Running on Heat Can Act as Computing Devices](http://arxiv.org/abs/2608.22841v1) |  | polymer | MD, phonons | 2026-08-24 | [link](http://arxiv.org/abs/2608.22841v1) |
| [Machine Learning Prediction of Transport Properties in Amorphous Polymer Electrolytes Using Chemically Informed Structur](https://doi.org/10.26434/chemrxiv.15000431/v2) |  | polymer, glass / amorphous |  | 2026-08-25 | [10.26434/chemrxiv.15000431/v2](https://doi.org/10.26434/chemrxiv.15000431/v2) |
| [Mechanistic study of mixed lithium halides solid-state electrolytes](https://doi.org/10.1103/czy4-7lfp) |  | solid electrolyte, alloy | HSE06, MLIP | 2026-08-26 | [10.1103/czy4-7lfp](https://doi.org/10.1103/czy4-7lfp) |
| [High-throughput Discovery of Magnetic Rare Earth Transition Metal Alloys](https://doi.org/10.48550/arxiv.2608.25270) |  | alloy, magnetic material | DFT, MLIP | 2026-08-26 | [10.48550/arxiv.2608.25270](https://doi.org/10.48550/arxiv.2608.25270) |
| [Text Embedding-Assisted Prediction of Corrosion Inhibition Efficiency Using Machine Learning under Small-Sample Conditio](https://doi.org/10.26434/chemrxiv.15007865/v1) |  | alloy |  | 2026-08-26 | [10.26434/chemrxiv.15007865/v1](https://doi.org/10.26434/chemrxiv.15007865/v1) |
| [Insights into Lithium Diffusion in Crystalline and Amorphous Solid Electrolytes with Machine Learning Interatomic Potent](https://doi.org/10.26434/chemrxiv.15007863/v1) |  | solid electrolyte, Li-ion battery, glass / amorphous, Li3YCl6 | MD, MLIP | 2026-08-26 | [10.26434/chemrxiv.15007863/v1](https://doi.org/10.26434/chemrxiv.15007863/v1) |
| [Atomistic Simulation Frameworks for Lithium-Ion Battery Materials: From First-Principles to Machine Learning Potentials](https://doi.org/10.1007/s42493-026-00160-6) |  | Li-ion battery | DFT | 2026-08-26 | [10.1007/s42493-026-00160-6](https://doi.org/10.1007/s42493-026-00160-6) |
| [A Hierarchical Synergistic Deep Learning Framework Integrating Composition, Structure, and Ionic Transport for Solid-Sta](http://arxiv.org/abs/2608.25592v1) |  | solid electrolyte |  | 2026-08-26 | [link](http://arxiv.org/abs/2608.25592v1) |
| [Designing High-Entropy Alloys: From Physical Metallurgy to Machine Learning Enabled Discovery](https://doi.org/10.20944/preprints202608.1952.v1) |  | alloy | MLIP | 2026-08-27 | [10.20944/preprints202608.1952.v1](https://doi.org/10.20944/preprints202608.1952.v1) |
| [When less is more: simplified models for interpretable materials design](https://doi.org/10.26434/chemrxiv.15008004/v1) |  | polymer |  | 2026-08-28 | [10.26434/chemrxiv.15008004/v1](https://doi.org/10.26434/chemrxiv.15008004/v1) |
| [Ferroelastic hysteresis, shear modulus softening, and the tetragonal↔cubic transition in davemaoite](https://doi.org/10.1126/sciadv.aed7601) |  | perovskite | MD, MLIP | 2026-08-28 | [10.1126/sciadv.aed7601](https://doi.org/10.1126/sciadv.aed7601) |
| [Machine learning interatomic potential study of grain boundaries thermal conductance and tensile strength in hexagonal b](https://doi.org/10.17632/c5pynk4jyj) |  | 2D material, nitride | AIMD, MLIP | 2026-08-28 | [10.17632/c5pynk4jyj](https://doi.org/10.17632/c5pynk4jyj) |
| [uMOF: A Universal Database, Benchmark, and Machine Learning Interatomic Potentials for Metal-Organic Frameworks](http://arxiv.org/abs/2608.28100v1) |  | MOF | r2SCAN, DFT, MLIP | 2026-08-28 | [link](http://arxiv.org/abs/2608.28100v1) |
| [Work Function and High-Coverage Adsorption Energy as Hydrogen-Evolution Descriptors on Ag-Au-Pd-Pt Alloys](http://arxiv.org/abs/2608.28347v1) |  | alloy |  | 2026-08-28 | [link](http://arxiv.org/abs/2608.28347v1) |
| [Compact Variational Neural Networks for Spectral Inference from a Single Nonlinear 2D Perovskite Photodetector](http://arxiv.org/abs/2608.27977v1) |  | perovskite |  | 2026-08-28 | [link](http://arxiv.org/abs/2608.27977v1) |
| [QUBO-Compatible Active Learning for Inverse Design of High-Entropy Alloys](http://arxiv.org/abs/2608.28239v1) |  | alloy |  | 2026-08-28 | [link](http://arxiv.org/abs/2608.28239v1) |
| [Atomistic simulations of high-entropy alloys: from density functional theory to machine-learning interatomic potentials](https://doi.org/10.1007/s10853-026-13520-2) |  | alloy | DFT, MLIP, free energy | 2026-08-29 | [10.1007/s10853-026-13520-2](https://doi.org/10.1007/s10853-026-13520-2) |
| [Multiscale insights into the diffusion of SF6/N2 mixtures via machine-learning interatomic potentials](https://doi.org/10.1038/s41598-026-67691-8) |  | SF6 | DFT, AIMD, MD, MLIP | 2026-08-30 | [10.1038/s41598-026-67691-8](https://doi.org/10.1038/s41598-026-67691-8) |
| [AI-Guided Self-Driving Laboratories for Advanced Materials Discovery](https://doi.org/10.69709/caic.2026.133382) |  | alloy |  | 2026-08-31 | [10.69709/caic.2026.133382](https://doi.org/10.69709/caic.2026.133382) |
| [Inverse design of functional materials: a case study in thermoelectrics](https://www.nature.com/articles/s41524-026-02307-3) |  | thermoelectric |  | 2026-08-31 | [10.1038/s41524-026-02307-3](https://doi.org/10.1038/s41524-026-02307-3) |
| [Cartesian tensor equivariant machine-learning force field for spin-dependent atomistic simulations](http://arxiv.org/abs/2608.30338v1) |  | magnetic material | MLIP | 2026-08-31 | [link](http://arxiv.org/abs/2608.30338v1) |
| [Machine learning driven multi-property prediction for rare earth permanent magnet materials](https://www.nature.com/articles/s41524-026-02299-0) |  | magnetic material |  | 2026-09-01 | [10.1038/s41524-026-02299-0](https://doi.org/10.1038/s41524-026-02299-0) |
| [Fourier Neural Operators for Composition-Driven Crystal Structure Discovery](http://arxiv.org/abs/2609.00900v1) |  | catalyst |  | 2026-09-01 | [link](http://arxiv.org/abs/2609.00900v1) |
| [Lead-free piezoelectric perovskites for arterial-pulse e-skin: from configurational complexity to equivariant machine-le](http://arxiv.org/abs/2609.00580v1) |  | perovskite |  | 2026-09-01 | [link](http://arxiv.org/abs/2609.00580v1) |
| [Multiscale modelling of ferroelectrics using a physics-informed neural network driven by molecular dynamics data: parame](https://www.nature.com/articles/s41524-026-02300-w) |  | perovskite | MD, finite element | 2026-09-02 | [10.1038/s41524-026-02300-w](https://doi.org/10.1038/s41524-026-02300-w) |
| [AI-Driven Blockchain Tokenization as a Catalyst for Global Economic Transformation in Real Estate and Digital Services](https://doi.org/10.4018/979-8-3373-7267-9.ch015) |  | catalyst |  | 2026-09-02 | [10.4018/979-8-3373-7267-9.ch015](https://doi.org/10.4018/979-8-3373-7267-9.ch015) |
| [Design of an optical-metrology-assisted MEMS thermoelectric microwave power sensor based on BP neural network optimizati](https://doi.org/10.1117/12.3122449) |  | thermoelectric |  | 2026-09-02 | [10.1117/12.3122449](https://doi.org/10.1117/12.3122449) |
| [Accelerating the Discovery of Deep-Ultraviolet Nonlinear Optical Materials by Combining Machine Learning Interatomic Pot](https://doi.org/10.1021/acs.cgd.6c00461.s001) |  | LiB2O3F | DFT, MLIP | 2026-09-02 | [10.1021/acs.cgd.6c00461.s001](https://doi.org/10.1021/acs.cgd.6c00461.s001) |
| [From Empirical Design To Autonomous Ecosystems: AI-Driven Advances, Challenges, And Future Directions In Precision Nanom](https://doi.org/10.5281/zenodo.21931873) |  |  |  | 2026-08-14 | [10.5281/zenodo.21931873](https://doi.org/10.5281/zenodo.21931873) |
| [Electrostatic Phenomenology Benchmarks for Machine-Learned Interatomic Potentials in Electrochemistry: Beyond the Energy](http://arxiv.org/abs/2608.14153v1) |  |  | MLIP | 2026-08-14 | [link](http://arxiv.org/abs/2608.14153v1) |
| [The Past and Future of AI Scientists](http://arxiv.org/abs/2608.14407v1) |  |  | MLIP | 2026-08-14 | [link](http://arxiv.org/abs/2608.14407v1) |
| [Graph neural network prediction of temperature-dependent hydrogen diffusion and thermal conductivity tensors of tungsten](http://arxiv.org/abs/2608.15609v1) |  |  | MD | 2026-08-16 | [link](http://arxiv.org/abs/2608.15609v1) |
| [Machine Learning-Accelerated Band-Edge Engineering of Pnictogen Chalcohalide Solid Solutions for Solar Energy Technologi](http://arxiv.org/abs/2608.16611v1) |  |  | DFT | 2026-08-17 | [link](http://arxiv.org/abs/2608.16611v1) |
| [Extracting a nitrile-centered, ether-assisted motif hierarchy for lithium-battery electrolyte design from billion-scale ](http://arxiv.org/abs/2608.16364v1) |  |  |  | 2026-08-17 | [link](http://arxiv.org/abs/2608.16364v1) |
| [Discovery of novel magnetic Y-Mn-B compounds via advanced machine learning guided framework](http://arxiv.org/abs/2608.17200v1) |  |  | DFT | 2026-08-17 | [link](http://arxiv.org/abs/2608.17200v1) |
| [Unlocking Multi-Component Bulk-Materials Molecular Dynamics with a Small-Footprint Machine Learning Interatomic Potentia](http://arxiv.org/abs/2608.16329v1) |  |  | MD, MLIP | 2026-08-17 | [link](http://arxiv.org/abs/2608.16329v1) |
| [ChemReporter: A Framework for Curating and Exporting Large-Scale Chemical Datasets for MLIP Training](http://arxiv.org/abs/2608.16418v1) |  |  | MLIP | 2026-08-17 | [link](http://arxiv.org/abs/2608.16418v1) |
| [Active learning molecular beam epitaxy of complex quantum materials](http://arxiv.org/abs/2608.17742v1) |  |  |  | 2026-08-18 | [link](http://arxiv.org/abs/2608.17742v1) |
| [PyAPX: python toolkit for atomic configuration pattern exploration](https://doi.org/10.1038/s41598-026-66072-5) |  |  | DFT, MLIP | 2026-08-19 | [10.1038/s41598-026-66072-5](https://doi.org/10.1038/s41598-026-66072-5) |
| [A single design choice determines whether machine learning models of materials make physically impossible predictions](http://arxiv.org/abs/2608.18714v1) |  |  | DFT | 2026-08-19 | [link](http://arxiv.org/abs/2608.18714v1) |
| [Dynamic Ensembles of Phosphine-Stabilized Gold Nanoclusters](http://arxiv.org/abs/2608.19404v1) |  |  | MD, MLIP | 2026-08-19 | [link](http://arxiv.org/abs/2608.19404v1) |
| [Generative AI and Emerging Technologies: Transforming Engineering, Innovation and Entrepreneurship](https://doi.org/10.5281/zenodo.22025110) |  |  |  | 2026-08-20 | [10.5281/zenodo.22025110](https://doi.org/10.5281/zenodo.22025110) |
| [Machine Learning to Foundation Models: Artificial Intelligence for Nanophotonic Modeling and Scientific Discovery](https://doi.org/10.48550/arxiv.2608.21612) |  |  | MLIP | 2026-08-21 | [10.48550/arxiv.2608.21612](https://doi.org/10.48550/arxiv.2608.21612) |
| [Diagnosing and narrowing the simulation-to-real gap in powder X-ray diffraction with a wet-dry agentic loop](http://arxiv.org/abs/2608.22400v1) |  |  |  | 2026-08-23 | [link](http://arxiv.org/abs/2608.22400v1) |
| [Dataset for the publication- A cylindrical sintering method for more realistic grain boundaries in nanocrystalline thin ](https://doi.org/10.5281/zenodo.22111105) |  |  |  | 2026-08-24 | [10.5281/zenodo.22111105](https://doi.org/10.5281/zenodo.22111105) |
| [Continuous Scalar Kernels for Quotients of Variable-Cell Periodic Structures: Compactness, Acquisition, and Target Bound](https://doi.org/10.26434/chemrxiv.15006891/v3) |  |  | MLIP | 2026-08-25 | [10.26434/chemrxiv.15006891/v3](https://doi.org/10.26434/chemrxiv.15006891/v3) |
| [Attention-based composition learning for thermodynamic and electronic property prediction in inorganic materials](https://doi.org/10.1016/j.nxmate.2026.103265) |  |  | DFT | 2026-08-25 | [10.1016/j.nxmate.2026.103265](https://doi.org/10.1016/j.nxmate.2026.103265) |
| [Machine learning for biomaterials design](https://doi.org/10.1038/s44222-026-00476-w) |  |  |  | 2026-08-25 | [10.1038/s44222-026-00476-w](https://doi.org/10.1038/s44222-026-00476-w) |
| [DeepField: Condensed-Phase Quantum Learning for All-Atom Protein Dynamics in Explicit Water](https://doi.org/10.26434/chemrxiv.15007896/v1) |  |  | MD, MLIP | 2026-08-26 | [10.26434/chemrxiv.15007896/v1](https://doi.org/10.26434/chemrxiv.15007896/v1) |
| [Preprint of the publication- A cylindrical sintering method for more realistic grain boundaries in nanocrystalline thin ](https://doi.org/10.5281/zenodo.22112768) |  |  |  | 2026-08-26 | [10.5281/zenodo.22112768](https://doi.org/10.5281/zenodo.22112768) |
| [Enhancing materials discovery with valence-constrained design in generative modeling](https://www.nature.com/articles/s43588-026-01037-2) |  |  |  | 2026-08-26 | [10.1038/s43588-026-01037-2](https://doi.org/10.1038/s43588-026-01037-2) |
| [Bayesian Optimization for Self-Driving Materials Laboratories: From Algorithms to Physics-Informed Workflows](http://arxiv.org/abs/2608.26016v1) |  |  |  | 2026-08-26 | [link](http://arxiv.org/abs/2608.26016v1) |
| [Comparative study of ensemble-based uncertainty quantification methods for neural network interatomic potentials](https://doi.org/10.1088/2632-2153/ae9fb4) |  |  | DFT, phonons, MLIP | 2026-08-27 | [10.1088/2632-2153/ae9fb4](https://doi.org/10.1088/2632-2153/ae9fb4) |
| [A multi-scale mixture of experts model for cross-size structural prediction of Cu nanoparticles](https://doi.org/10.1038/s41524-026-02280-x) |  |  | DFT, MD, MLIP | 2026-08-27 | [10.1038/s41524-026-02280-x](https://doi.org/10.1038/s41524-026-02280-x) |
| [Benchmarking of Fast and Interpretable UF Machine Learning Potentials](https://doi.org/10.48550/arxiv.2608.27277) |  |  | DFT, MD, MLIP | 2026-08-27 | [10.48550/arxiv.2608.27277](https://doi.org/10.48550/arxiv.2608.27277) |
| [Carbon Nanotube-Induced Magnetic Shielding Effects on 129Xe NMR from Equivariant Neural Networks](https://doi.org/10.26434/chemrxiv.15007956/v1) |  |  | MD, MLIP | 2026-08-27 | [10.26434/chemrxiv.15007956/v1](https://doi.org/10.26434/chemrxiv.15007956/v1) |
| [Commentary on ten selected 2025 papers in AI for Materials Science](https://doi.org/10.20517/jmi.2026.36) |  |  |  | 2026-08-27 | [10.20517/jmi.2026.36](https://doi.org/10.20517/jmi.2026.36) |
| [Packora: Systematic Design for Generative Molecular Crystal Structure Prediction](http://arxiv.org/abs/2608.26962v1) |  |  |  | 2026-08-27 | [link](http://arxiv.org/abs/2608.26962v1) |
| [Docking-Score Landscapes Shape Active-Learning Performance across Vina, Glide, and SILCS](https://doi.org/10.26434/chemrxiv-2025-3t356/v2) |  |  |  | 2026-08-28 | [10.26434/chemrxiv-2025-3t356/v2](https://doi.org/10.26434/chemrxiv-2025-3t356/v2) |
| [Autoregressive Generative Latent Diffusion Models for Magnetohydrodynamics](https://doi.org/10.1109/icops53334.2026.11660190) |  |  |  | 2026-08-28 | [10.1109/icops53334.2026.11660190](https://doi.org/10.1109/icops53334.2026.11660190) |
| [Crystal structure prediction with nuclear quantum and finite-temperature effects via deep free energy learning](https://doi.org/10.1103/3qjr-mgv7) |  |  | free energy | 2026-08-28 | [10.1103/3qjr-mgv7](https://doi.org/10.1103/3qjr-mgv7) |
| [Neural network finds twisted crystals that steer light at the nanoscale](https://www.nature.com/articles/s41563-026-02744-x) |  |  |  | 2026-08-28 | [10.1038/s41563-026-02744-x](https://doi.org/10.1038/s41563-026-02744-x) |
| [OrbGNN: A Wave function-based Machine Learning Interelectronic Representation](http://arxiv.org/abs/2608.27806v1) |  |  | MLIP | 2026-08-28 | [link](http://arxiv.org/abs/2608.27806v1) |
| [High-quality, high-information datasets for universal atomistic machine learning](https://doi.org/10.24435/materialscloud:vm-51) |  |  | r2SCAN, meta-GGA, DFT | 2026-08-29 | [10.24435/materialscloud:vm-51](https://doi.org/10.24435/materialscloud:vm-51) |
| [Volumetric reference data of the orbit: a deep learning MRI analysis in the German national cohort](https://doi.org/10.1038/s41598-026-68393-x) |  |  |  | 2026-08-29 | [10.1038/s41598-026-68393-x](https://doi.org/10.1038/s41598-026-68393-x) |
| [DFT and machine learning insights into productive versus self-metathesis selectivity in ruthenium-catalyzed ethenolysis](https://doi.org/10.1016/j.jcat.2026.117142) |  |  | DFT | 2026-08-29 | [10.1016/j.jcat.2026.117142](https://doi.org/10.1016/j.jcat.2026.117142) |
| [PCFM-based small-sample data augmentation and inverse design of an all-dielectric metasurface supporting triple Fano res](https://doi.org/10.1016/j.optcom.2026.133711) |  |  |  | 2026-08-29 | [10.1016/j.optcom.2026.133711](https://doi.org/10.1016/j.optcom.2026.133711) |
| [Accelerating Materials Discovery: A Review of Machine Learning in X‐Ray Absorption Spectroscopy](https://doi.org/10.1002/aisy.70529) |  |  |  | 2026-08-30 | [10.1002/aisy.70529](https://doi.org/10.1002/aisy.70529) |
| [Learning 3D void growth and coalescence in heterogeneous polycrystalline materials using vision Transformer models](https://doi.org/10.1016/j.engfracmech.2026.112576) |  |  |  | 2026-08-30 | [10.1016/j.engfracmech.2026.112576](https://doi.org/10.1016/j.engfracmech.2026.112576) |
| [DFA-Grasp: Depth Foundation Model-Augmented Transparent Object Depth Completion for Robotic Grasping](https://doi.org/10.1016/j.robot.2026.105733) |  |  | MLIP | 2026-08-30 | [10.1016/j.robot.2026.105733](https://doi.org/10.1016/j.robot.2026.105733) |
| [Cesium Clustering and Fluoroberyllate Network Disruption in FLiBe: A Total Scattering and Molecular Dynamics Study](http://arxiv.org/abs/2608.29898v1) |  |  | MD | 2026-08-30 | [link](http://arxiv.org/abs/2608.29898v1) |
| [Compiling Matter: An AI-Driven Research Program for Universal Nanofabrication, Matter Compilation, and Programmable Matt](https://doi.org/10.5281/zenodo.22206444) |  |  | MLIP | 2026-08-31 | [10.5281/zenodo.22206444](https://doi.org/10.5281/zenodo.22206444) |
| [CrystalGRW: generative modeling of crystal structures with targeted crystallographic properties via geodesic random walk](https://doi.org/10.1038/s41598-026-62470-x) |  |  | DFT | 2026-08-31 | [10.1038/s41598-026-62470-x](https://doi.org/10.1038/s41598-026-62470-x) |
| [Workflow design as a research variable in computational materials discovery](https://doi.org/10.26434/chemrxiv.15008076/v1) |  |  |  | 2026-08-31 | [10.26434/chemrxiv.15008076/v1](https://doi.org/10.26434/chemrxiv.15008076/v1) |
| [Nonlinear Crystal Structure Prediction](https://doi.org/10.5281/zenodo.22195386) |  |  |  | 2026-08-31 | [10.5281/zenodo.22195386](https://doi.org/10.5281/zenodo.22195386) |
| [bayesaenet: uncertainty quantification for machine learning interatomic potentials](https://doi.org/10.5281/zenodo.22201403) |  |  | MLIP | 2026-08-31 | [10.5281/zenodo.22201403](https://doi.org/10.5281/zenodo.22201403) |
| [Learning Materials Properties from Scarce Labels and Unlabeled Crystals](http://arxiv.org/abs/2608.30682v1) |  |  |  | 2026-08-31 | [link](http://arxiv.org/abs/2608.30682v1) |
| [AdaptNTK: Adaptive Uncertainty Quantification and Active Learning for Neural Network Potentials](http://arxiv.org/abs/2609.00488v1) |  |  | DFT, MD, MLIP | 2026-08-31 | [link](http://arxiv.org/abs/2609.00488v1) |
| [GigaPath-Flash and GigaTIME-Flash: Toward population-scale discovery with efficient pathology foundation models](https://www.microsoft.com/en-us/research/blog/gigapath-flash-and-gigatime-flash-toward-population-scale-discovery-with-efficient-pathology-foundation-models/) |  |  | MLIP | 2026-08-31 | [link](https://www.microsoft.com/en-us/research/blog/gigapath-flash-and-gigatime-flash-toward-population-scale-discovery-with-efficient-pathology-foundation-models/) |
| [When Do Models Win? A Learning Curve Benchmark for Molecular Property Prediction in Low-Data Regimes](https://doi.org/10.26434/chemrxiv.15001253/v6) |  |  | DFT | 2026-09-01 | [10.26434/chemrxiv.15001253/v6](https://doi.org/10.26434/chemrxiv.15001253/v6) |
| [Multicenter Validation of Foundation Model Adaptation for Automated Pancreatic Tumor Delineation on CT Scans](https://doi.org/10.3390/cancers18172836) |  |  | MLIP | 2026-09-01 | [10.3390/cancers18172836](https://doi.org/10.3390/cancers18172836) |
| [Conditional Latent-Prior Generative Compressed Sensing with Application to Petrophysical Target-Log Reconstruction](https://doi.org/10.2139/ssrn.7385284) |  |  |  | 2026-09-01 | [10.2139/ssrn.7385284](https://doi.org/10.2139/ssrn.7385284) |
| [Active Learning for Neural Classifiers: Selecting Training and Test Areas in Satellite Image Object Recognition](https://doi.org/10.1007/978-3-032-16265-6_4) |  |  |  | 2026-09-01 | [10.1007/978-3-032-16265-6_4](https://doi.org/10.1007/978-3-032-16265-6_4) |
| [Dynamical analysis of fractional order corruption diffusion model with optimal control and cost-effectiveness analysis](https://doi.org/10.1080/0022250x.2026.2726737) |  |  |  | 2026-09-01 | [10.1080/0022250x.2026.2726737](https://doi.org/10.1080/0022250x.2026.2726737) |
| [Accelerating dynamic simulations of photoexcited materials and their evolution by electron-informed machine learning](http://arxiv.org/abs/2609.01492v1) |  |  | DFT, MD | 2026-09-01 | [link](http://arxiv.org/abs/2609.01492v1) |
| [Why Multi-Layer Message Passing Works: Completeness Theory for Graph Neural Network Interatomic Potentials](http://arxiv.org/abs/2609.00528v1) |  |  |  | 2026-09-01 | [link](http://arxiv.org/abs/2609.00528v1) |
| [Element priors and target support shape chemical transfer in materials graph networks](http://arxiv.org/abs/2609.00915v1) |  |  |  | 2026-09-01 | [link](http://arxiv.org/abs/2609.00915v1) |
| [Text-guided flow matching enables sample-efficient crystal structure generation](http://arxiv.org/abs/2609.01076v1) |  |  |  | 2026-09-01 | [link](http://arxiv.org/abs/2609.01076v1) |
| [A Machine Learning–Based Surrogate Model for the Assessment of Geological Fault Reactivation](https://doi.org/10.3997/2214-4609.202637038) |  |  |  | 2026-09-02 | [10.3997/2214-4609.202637038](https://doi.org/10.3997/2214-4609.202637038) |
| [History matching of realistic oil fields using deep-learning based surrogate models and MCMC](https://doi.org/10.3997/2214-4609.202637181) |  |  |  | 2026-09-02 | [10.3997/2214-4609.202637181](https://doi.org/10.3997/2214-4609.202637181) |
| [An MLP Surrogate Model for Accelerated Well Placement Optimization in Hydrocarbon Reservoirs](https://doi.org/10.3997/2214-4609.202637085) |  |  |  | 2026-09-02 | [10.3997/2214-4609.202637085](https://doi.org/10.3997/2214-4609.202637085) |
| [Design of a real-time prediction device for lithium battery SOC based on BP neural network and STM32 chip](https://doi.org/10.1117/12.3122410) |  |  |  | 2026-09-02 | [10.1117/12.3122410](https://doi.org/10.1117/12.3122410) |
| [Deep Learning Surrogate Models for Multiscale, Time-Dependent Heat Transport in Geothermal Reservoirs](https://doi.org/10.3997/2214-4609.202637011) |  |  |  | 2026-09-02 | [10.3997/2214-4609.202637011](https://doi.org/10.3997/2214-4609.202637011) |

## Summary of gaps

- Studies with no identifiable model name: **116**
- Studies with no identifiable calculation method: **55**
- Studies with no numeric metric: **136**
- Benchmarked models missing at least one field: **15**

The dominant cause is structural, not fixable by better parsing: abstracts rarely quote error values, and full text is usually paywalled.

