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

## Studies with no numeric performance figure (44 of 46)

These need a human to open the paper and read the results table. Highest value first: studies that already name a model and a material, so only the number is missing.

| Study | Models named | Materials | Method | Date | DOI |
|---|---|---|---|---|---|
| [Conservation-Resolved Error Decomposition: A Benchmark Axis for Electronic-Structure Methods and Machine-Learned Interat](https://doi.org/10.26434/chemrxiv.15007478/v1) | MACE | OFF23 | hybrid DFT, MLIP | 2026-08-17 | [10.26434/chemrxiv.15007478/v1](https://doi.org/10.26434/chemrxiv.15007478/v1) |
| [HIP: Hessian Interatomic Potentials](https://doi.org/10.5281/zenodo.22003592) | EquiformerV2 | molecule / organic | MLIP | 2026-08-19 | [10.5281/zenodo.22003592](https://doi.org/10.5281/zenodo.22003592) |
| [HIP: Hessian Interatomic Potentials](https://doi.org/10.5281/zenodo.22003591) | EquiformerV2 | molecule / organic | MLIP | 2026-08-19 | [10.5281/zenodo.22003591](https://doi.org/10.5281/zenodo.22003591) |
| [The CHGNet uMLIP model fine-tuned for 2Hc-WS2](https://doi.org/10.5281/zenodo.22059540) | CHGNet | WS2, MoS2 | DFT, MLIP | 2026-08-22 | [10.5281/zenodo.22059540](https://doi.org/10.5281/zenodo.22059540) |
| [Equivariance as a Substitutable Resource: A Unified Scaling Law for Machine-Learned Interatomic Potentials](https://doi.org/10.5281/zenodo.22063928) | MACE | molecule / organic | MLIP | 2026-08-23 | [10.5281/zenodo.22063928](https://doi.org/10.5281/zenodo.22063928) |
| [Equivariance as a Substitutable Resource: A Unified Scaling Law for Machine-Learned Interatomic Potentials](https://doi.org/10.5281/zenodo.22063807) | MACE | molecule / organic | MLIP | 2026-08-23 | [10.5281/zenodo.22063807](https://doi.org/10.5281/zenodo.22063807) |
| [A computed thermoelectric feature database for 50,992 GNoME materials](https://doi.org/10.26434/chemrxiv.15007873/v1) | CHGNet, GNoME | thermoelectric | DFT, MLIP | 2026-08-26 | [10.26434/chemrxiv.15007873/v1](https://doi.org/10.26434/chemrxiv.15007873/v1) |
| [Universal Thermodynamic Interatomic Potentials for Crystalline Materials](http://arxiv.org/abs/2608.14502v1) | UMA |  | MD, MLIP, free energy | 2026-08-14 | [link](http://arxiv.org/abs/2608.14502v1) |
| [Data-Efficient Construction of Material-Specific Machine-Learning Interatomic Potentials from Ab Initio Molecular Dynami](http://arxiv.org/abs/2608.14899v1) | GRACE-1L-OAM, SevenNet-0, MACE-MP-0, MatterSim |  | DFT, AIMD, MD, MLIP | 2026-08-14 | [link](http://arxiv.org/abs/2608.14899v1) |
| [GRACE-OFF: A machine-learned interatomic potential for organic liquids using the GRACE architecture](https://doi.org/10.26434/chemrxiv.15001529/v2) | GRACE, MACE |  | MLIP | 2026-08-18 | [10.26434/chemrxiv.15001529/v2](https://doi.org/10.26434/chemrxiv.15001529/v2) |
| [How AI Coding Agents Can Unlock Materials Simulation with NVIDIA ALCHEMI Toolkit](https://developer.nvidia.com/blog/how-ai-coding-agents-can-unlock-materials-simulation-with-nvidia-alchemi-toolkit/) | ALCHEMI |  |  | 2026-08-18 | [link](https://developer.nvidia.com/blog/how-ai-coding-agents-can-unlock-materials-simulation-with-nvidia-alchemi-toolkit/) |
| [Exploring celecoxib polymorph landscape using AIMNet2 machine learning interatomic potential](https://doi.org/10.17615/xd5h-sd62) | AIMNet2 |  | DFT, MLIP | 2026-08-20 | [10.17615/xd5h-sd62](https://doi.org/10.17615/xd5h-sd62) |
| [Data-Efficient and Fast Machine Learning Molecular Dynamics through Integrated Active Learning and Knowledge Distillatio](https://doi.org/10.1021/acs.jctc.6c00917) | DeePMD, MACE |  | DFT, MD, MLIP | 2026-08-21 | [10.1021/acs.jctc.6c00917](https://doi.org/10.1021/acs.jctc.6c00917) |
| [FastMD](https://doi.org/10.5281/zenodo.22051980) | ALIGNN, CHGNet |  | MD, MLIP | 2026-08-22 | [10.5281/zenodo.22051980](https://doi.org/10.5281/zenodo.22051980) |
| [FastMD](https://doi.org/10.5281/zenodo.22051979) | ALIGNN, CHGNet |  | MD, MLIP | 2026-08-22 | [10.5281/zenodo.22051979](https://doi.org/10.5281/zenodo.22051979) |
| [PhononBench:A Large-Scale Phonon-Based Benchmark for Dynamical Stability in Crystal Generation](https://doi.org/10.1088/3050-287x/ae9ee4) | MatterSim, MatterGen |  | phonons | 2026-08-26 | [10.1088/3050-287x/ae9ee4](https://doi.org/10.1088/3050-287x/ae9ee4) |
| [Realistic Simulations of Energy Materials Using Foundation Models and Electrode-Potential Learning](https://doi.org/10.26434/chemrxiv.15007895/v1) | SevenNet |  | DFT, MLIP | 2026-08-26 | [10.26434/chemrxiv.15007895/v1](https://doi.org/10.26434/chemrxiv.15007895/v1) |
| [Materials Discovery and Design](https://doi.org/10.1002/9783527852048.ch9) |  | polymer |  | 2026-08-14 | [10.1002/9783527852048.ch9](https://doi.org/10.1002/9783527852048.ch9) |
| [Neural Networks Accelerate Ab Initio Multiple Spawning Simulations: A Case Study of Using Machine Learning Potentials fo](https://doi.org/10.26434/chemrxiv.15007443/v1) |  | molecule / organic | DFT, MLIP | 2026-08-14 | [10.26434/chemrxiv.15007443/v1](https://doi.org/10.26434/chemrxiv.15007443/v1) |
| [G2RINS: A Generative String-and-Graph Polymer Representation to Assist Computational Materials Discovery](https://doi.org/10.26434/chemrxiv.15007504/v1) |  | polymer | MD | 2026-08-17 | [10.26434/chemrxiv.15007504/v1](https://doi.org/10.26434/chemrxiv.15007504/v1) |
| [Optimization of active learning strategies for infrared spectra prediction in catalysis](https://doi.org/10.26434/chemrxiv.15007549/v1) |  | catalyst, molecule / organic | DFT, AIMD, MD, MLIP | 2026-08-18 | [10.26434/chemrxiv.15007549/v1](https://doi.org/10.26434/chemrxiv.15007549/v1) |
| [Local Symmetry Breaking and Correlated Fluctuations in Quantum Materials from Atomistic Foundation Models](https://doi.org/10.26434/chemrxiv.15001387/v2) |  | superconductor | DFT, AIMD, MD, phonons | 2026-08-19 | [10.26434/chemrxiv.15001387/v2](https://doi.org/10.26434/chemrxiv.15001387/v2) |
| [Machine Learning Guided Discovery of Corundum High Entropy Oxides](http://arxiv.org/abs/2608.20596v1) |  | oxide | MLIP | 2026-08-20 | [link](http://arxiv.org/abs/2608.20596v1) |
| [Machine Learning Guided Discovery of Corundum High Entropy Oxides](https://doi.org/10.48550/arxiv.2608.20596) |  | oxide | MLIP | 2026-08-20 | [10.48550/arxiv.2608.20596](https://doi.org/10.48550/arxiv.2608.20596) |
| [Vibrational, structural, and chemical fingerprints of ion diffusion in crystalline solids](http://arxiv.org/abs/2608.21624v1) |  | solid electrolyte | MD, MLIP, free energy | 2026-08-21 | [link](http://arxiv.org/abs/2608.21624v1) |
| [Vibrational, structural, and chemical fingerprints of ion diffusion in crystalline solids](https://doi.org/10.48550/arxiv.2608.21624) |  | solid electrolyte | MD, MLIP, free energy | 2026-08-21 | [10.48550/arxiv.2608.21624](https://doi.org/10.48550/arxiv.2608.21624) |
| [Bayesian Neural Networks versus deep ensembles for uncertainty quantification in machine learning interatomic potentials](https://doi.org/10.1088/2632-2153/ae9de8) |  | molecule / organic | MLIP | 2026-08-24 | [10.1088/2632-2153/ae9de8](https://doi.org/10.1088/2632-2153/ae9de8) |
| [Y-Mn-B Magnetic Materials: A DFT and Machine Learning Dataset](https://doi.org/10.5281/zenodo.22084773) |  | magnetic material, Y3MnB7, YMnB4 | DFT, phonons, MLIP | 2026-08-24 | [10.5281/zenodo.22084773](https://doi.org/10.5281/zenodo.22084773) |
| [Y-Mn-B Magnetic Materials: A DFT and Machine Learning Dataset](https://doi.org/10.5281/zenodo.22084774) |  | magnetic material, Y3MnB7, YMnB4 | DFT, phonons, MLIP | 2026-08-24 | [10.5281/zenodo.22084774](https://doi.org/10.5281/zenodo.22084774) |
| [Insights into Lithium Diffusion in Crystalline and Amorphous Solid Electrolytes with Machine Learning Interatomic Potent](https://doi.org/10.26434/chemrxiv.15007863/v1) |  | solid electrolyte, Li-ion battery, glass / amorphous, Li3YCl6 | MD, MLIP | 2026-08-26 | [10.26434/chemrxiv.15007863/v1](https://doi.org/10.26434/chemrxiv.15007863/v1) |
| [High-throughput Discovery of Magnetic Rare Earth Transition Metal Alloys](http://arxiv.org/abs/2608.25270v1) |  | alloy | DFT, MLIP | 2026-08-26 | [link](http://arxiv.org/abs/2608.25270v1) |
| [High-throughput Discovery of Magnetic Rare Earth Transition Metal Alloys](https://doi.org/10.48550/arxiv.2608.25270) |  | alloy, magnetic material | DFT, MLIP | 2026-08-26 | [10.48550/arxiv.2608.25270](https://doi.org/10.48550/arxiv.2608.25270) |
| [A Hierarchical Synergistic Deep Learning Framework Integrating Composition, Structure, and Ionic Transport for Solid-Sta](http://arxiv.org/abs/2608.25592v1) |  | solid electrolyte |  | 2026-08-26 | [link](http://arxiv.org/abs/2608.25592v1) |
| [Electrostatic Phenomenology Benchmarks for Machine-Learned Interatomic Potentials in Electrochemistry: Beyond the Energy](http://arxiv.org/abs/2608.14153v1) |  |  | MLIP | 2026-08-14 | [link](http://arxiv.org/abs/2608.14153v1) |
| [Graph neural network prediction of temperature-dependent hydrogen diffusion and thermal conductivity tensors of tungsten](http://arxiv.org/abs/2608.15609v1) |  |  | MD | 2026-08-16 | [link](http://arxiv.org/abs/2608.15609v1) |
| [Unlocking Multi-Component Bulk-Materials Molecular Dynamics with a Small-Footprint Machine Learning Interatomic Potentia](http://arxiv.org/abs/2608.16329v1) |  |  | MD, MLIP | 2026-08-17 | [link](http://arxiv.org/abs/2608.16329v1) |
| [Dynamic Ensembles of Phosphine-Stabilized Gold Nanoclusters](http://arxiv.org/abs/2608.19404v1) |  |  | MD, MLIP | 2026-08-19 | [link](http://arxiv.org/abs/2608.19404v1) |
| [Machine Learning to Foundation Models: Artificial Intelligence for Nanophotonic Modeling and Scientific Discovery](https://doi.org/10.48550/arxiv.2608.21612) |  |  | MLIP | 2026-08-21 | [10.48550/arxiv.2608.21612](https://doi.org/10.48550/arxiv.2608.21612) |
| [Attention-based composition learning for thermodynamic and electronic property prediction in inorganic materials](https://doi.org/10.1016/j.nxmate.2026.103265) |  |  | DFT | 2026-08-25 | [10.1016/j.nxmate.2026.103265](https://doi.org/10.1016/j.nxmate.2026.103265) |
| [Enhancing materials discovery with valence-constrained design in generative modeling](https://www.nature.com/articles/s43588-026-01037-2) |  |  |  | 2026-08-26 | [10.1038/s43588-026-01037-2](https://doi.org/10.1038/s43588-026-01037-2) |
| [Comparative study of ensemble-based uncertainty quantification methods for neural network interatomic potentials](https://doi.org/10.1088/2632-2153/ae9fb4) |  |  | DFT, phonons, MLIP | 2026-08-27 | [10.1088/2632-2153/ae9fb4](https://doi.org/10.1088/2632-2153/ae9fb4) |
| [Carbon Nanotube-Induced Magnetic Shielding Effects on 129Xe NMR from Equivariant Neural Networks](https://doi.org/10.26434/chemrxiv.15007956/v1) |  |  | MD, MLIP | 2026-08-27 | [10.26434/chemrxiv.15007956/v1](https://doi.org/10.26434/chemrxiv.15007956/v1) |
| [Benchmarking of Fast and Interpretable UF Machine Learning Potentials](http://arxiv.org/abs/2608.27277v1) |  |  | DFT, MD, MLIP | 2026-08-27 | [link](http://arxiv.org/abs/2608.27277v1) |
| [Packora: Systematic Design for Generative Molecular Crystal Structure Prediction](http://arxiv.org/abs/2608.26962v1) |  |  |  | 2026-08-27 | [link](http://arxiv.org/abs/2608.26962v1) |

## Summary of gaps

- Studies with no identifiable model name: **29**
- Studies with no identifiable calculation method: **5**
- Studies with no numeric metric: **44**
- Benchmarked models missing at least one field: **15**

The dominant cause is structural, not fixable by better parsing: abstracts rarely quote error values, and full text is usually paywalled.

