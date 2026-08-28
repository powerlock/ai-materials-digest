# AI and Materials Discovery - Daily Digest

Automatically compiled from arXiv, Crossref, OpenAlex, journal RSS feeds, the
NVIDIA / Microsoft Research / Google DeepMind blogs, and GitHub releases.
Newest entries appear directly below this line.

<!-- NEW-ENTRIES-BELOW -->

## 2026-08-28

46 new item(s). Top hit: **Insights into Lithium Diffusion in Crystalline and Amorphous Solid Electrolytes with Machine Learning Interato** (score 53, Crossref).

### Journal articles

- **[Exploring celecoxib polymorph landscape using AIMNet2 machine learning interatomic potential](https://doi.org/10.17615/xd5h-sd62)**
  <br>*UNC Libraries | 2026-08-20 | doi:10.17615/xd5h-sd62 | score 52*
  <br>Changquan Calvin Sun, Peikun Zheng, Yuriy A Abramov, Olexandr Isayev

  The crystal form a drug adopts can change everything from how it dissolves to whether it works in the clinic, yet predicting which polymorphs a flexible molecule will produce remains one of the most stubborn problems in pharmaceutical science. Competing forms typically differ in energy by less than 2 kJ mol-1, a precision that quantum chemistry can reach only at forbidding cost. Here we deploy AIMNet2, a machine-learned interatomic potential refined by active learning on cluster reference data, to map the polymorphic landscape of celecoxib, a widely prescribed COX-2 inhibitor whose form I exhibits record-breaking elastic flexibility. A GPU-accelerated workflow generates and ranks hundreds of...

  `matched: machine learning interatomic potential, machine-learned interatomic potential, interatomic potential, machine learning, active learning, crystal`


- **[Bayesian Neural Networks versus deep ensembles for uncertainty quantification in machine learning interatomic potentials](https://doi.org/10.1088/2632-2153/ae9de8)**
  <br>*Machine Learning Science and Technology | 2026-08-24 | doi:10.1088/2632-2153/ae9de8 | score 46*
  <br>Riccardo Farris, Emanuele Telari, Nongnuch Artrith, Konstantin M. Neyman

  Abstract Neural-network-based machine learning interatomic potentials have emerged as powerful tools for predicting atomic energies and forces, enabling accurate and efficient simulations in atomistic modeling. A key limitation of traditional deep learning approaches, however, is their inability to provide reliable estimates of predictive uncertainty. Such uncertainty quantification is critical for assessing model reliability, especially in materials science, where often the model is applied on out-of-distribution data. Different strategies have been proposed to address this challenge, with deep ensembles (DE) and Bayesian neural networks (BNN) being among the most widely used. In this work,...

  `matched: machine learning interatomic potential, interatomic potential, machine learning, neural network, deep learning`


- **[Data-Efficient and Fast Machine Learning Molecular Dynamics through Integrated Active Learning and Knowledge Distillation](https://doi.org/10.1021/acs.jctc.6c00917)**
  <br>*Journal of Chemical Theory and Computation | 2026-08-21 | doi:10.1021/acs.jctc.6c00917 | score 38*
  <br>Xiliang Lian, Alfredo Pasquarello

  Abstract We develop data-efficient machine learning interatomic potentials (MLIPs) for fast molecular dynamics simulations by combining DeePMD and MACE models within an active learning and knowledge distillation framework. Using liquid water as a case study, we first independently train DeePMD and MACE models from scratch through active learning. We find that MACE requires around 3 times less training data than DeePMD, but its inference speed is 10 times lower. We also show that starting from a pretrained foundation model based on the MACE architecture further reduces the training data by a factor of 7, resulting in a fine-tuned foundation model with a 25 times data reduction compared to Dee...

  `matched: machine learning interatomic potential, interatomic potential, molecular dynamics, machine learning, foundation model, active learning`


- **[Y-Mn-B Magnetic Materials: A DFT and Machine Learning Dataset](https://doi.org/10.5281/zenodo.22084773)**
  <br>*Zenodo (CERN European Organization for Nuclear Research) | 2026-08-24 | doi:10.5281/zenodo.22084773 | score 36*
  <br>Weiyi Xia, Wei-Shen Tee, Maxim Moraru, Ying Wai Li

  This dataset contains the crystallographic structures, thermodynamic-stability data, and selected phonon and electronic-structure outputs supporting the manuscript: “Discovery of novel magnetic Y-Mn-B compounds via advanced machine learning guided framework.” The data were generated using an advanced implementation of the exa-AMD materials-discovery framework. More than one million hypothetical structures were initially screened using a crystal graph convolutional neural network, followed by structural relaxation and convex-hull sorting using a machine-learning interatomic potential. The selected low-energy structures were subsequently validated using first-principles density functional theo...

  `matched: interatomic potential, machine learning, neural network, crystal, dataset, magnet`


- **[Comparative study of ensemble-based uncertainty quantification methods for neural network interatomic potentials](https://doi.org/10.1088/2632-2153/ae9fb4)**
  <br>*Machine Learning Science and Technology | 2026-08-27 | doi:10.1088/2632-2153/ae9fb4 | score 33*
  <br>Yonatan Kurniawan, Mingjian Wen, Ellad B. Tadmor, Mark K. Transtrum

  Abstract Machine learning interatomic potentials (MLIPs) enable atomistic simulations with near first-principles accuracy at substantially reduced computational cost, making them powerful tools for large-scale materials modeling. The accuracy of MLIPs is typically validated on a held-out dataset of ab initio energies and atomic forces. However, accuracy on these small-scale properties does not guarantee reliability for emergent, system-level behavior-precisely the regime where atomistic simulations are most needed, but for which direct validation is often computationally prohibitive. As a practical heuristic, predictive precision-quantified as inverse uncertainty-is commonly used as a proxy...

  `matched: machine learning interatomic potential, interatomic potential, machine learning, neural network, dataset`


- **[PhononBench:A Large-Scale Phonon-Based Benchmark for Dynamical Stability in Crystal Generation](https://doi.org/10.1088/3050-287x/ae9ee4)**
  <br>*AI for Science | 2026-08-26 | doi:10.1088/3050-287x/ae9ee4 | score 33*
  <br>Xiao-Qi Han, Ze-Feng Gao, Wen-Kao Li, Peng-Jie Guo

  Recent advances in generative artificial intelligence have enabled crystal-design methods based on graph neural networks, diffusion models, and large language models. Existing evaluations commonly follow the stability–uniqueness–novelty (S.U.N.) framework, but typically assess stability using thermodynamic criteria, which do not fully capture dynamical stability. Although dynamical stability influences material synthesis and persistence, experimental realization also depends on anharmonicity, finite temperature, defects, disorder, and synthesis conditions. Its high computational cost has hindered systematic large-scale evaluation of generated crystals. Here, we introduce PhononBench, the fir...

  `matched: artificial intelligence, large language model, graph neural network, diffusion model, neural network, benchmark`


- **[Attention-based composition learning for thermodynamic and electronic property prediction in inorganic materials](https://doi.org/10.1016/j.nxmate.2026.103265)**
  <br>*Next Materials | 2026-08-25 | doi:10.1016/j.nxmate.2026.103265 | score 33*
  <br>Purnachary M, Avula Edukondalu, T. Adilakshmi

  Consistent prediction of material properties such as formation energy and electronic bandgap is very important for accelerating materials discovery in the data-driven era. Although recent machine learning and deep learning models have shown promising results, their performance mainly depends on the quality of the dataset and the effective capture of complex composition–property relationships. In this study, we present an integrated framework that addresses these difficulties through three main contributions. First, a curated dataset was built by collecting formation energies and band gaps obtained from density functional theory (DFT) calculations for various inorganic compositions. Special c...

  `matched: density functional theory, materials discovery, machine learning, formation energy, deep learning, inorganic`


- **[Enhancing materials discovery with valence-constrained design in generative modeling](https://www.nature.com/articles/s43588-026-01037-2)**
  <br>*Nature Computational Science | 2026-08-26 | doi:10.1038/s43588-026-01037-2 | score 27*

  `matched: materials discovery, generative model`


- **[HIP: Hessian Interatomic Potentials](https://doi.org/10.5281/zenodo.22003592)**
  <br>*Zenodo (CERN European Organization for Nuclear Research) | 2026-08-19 | doi:10.5281/zenodo.22003592 | score 27*
  <br>Andreas Burger

  HIPs are machine learning interatomic potentials (MLIPs) that directly predict the Hessian, in addition to the usual energy and forces. This repo primarily trains HIP-EquiformerV2 on the HORM Hessian dataset, which consists of off-equilibrium geometries of small, neutral organic molecules, contained H, C, N, O, based on Transition1x, at the $\omega$B97X/6-31G(d) level of theory. Paper: https://arxiv.org/abs/2509.21624 Official repo: https://github.com/BurgerAndreas/hip

  `matched: machine learning interatomic potential, interatomic potential, machine learning, dataset`


- **[HIP: Hessian Interatomic Potentials](https://doi.org/10.5281/zenodo.22003591)**
  <br>*Zenodo (CERN European Organization for Nuclear Research) | 2026-08-19 | doi:10.5281/zenodo.22003591 | score 27*
  <br>Andreas Burger

  HIPs are machine learning interatomic potentials (MLIPs) that directly predict the Hessian, in addition to the usual energy and forces. This repo primarily trains HIP-EquiformerV2 on the HORM Hessian dataset, which consists of off-equilibrium geometries of small, neutral organic molecules, contained H, C, N, O, based on Transition1x, at the $\omega$B97X/6-31G(d) level of theory. Paper: https://arxiv.org/abs/2509.21624 Official repo: https://github.com/BurgerAndreas/hip

  `matched: machine learning interatomic potential, interatomic potential, machine learning, dataset`


- **[Interatomic Potential Prediction Based on Charge Equilibration and Equivariant Transformer](https://doi.org/10.70267/cai.26v3n4.3545)**
  <br>*Computers and artificial intelligence. | 2026-08-24 | doi:10.70267/cai.26v3n4.3545 | score 25*
  <br>Yijun Shi, Tao Luo

  Conventional local machine-learning interatomic potentials describe atomic environments with a finite cutoff radius and therefore have difficulty capturing long-range electrostatic coupling in polar, charged, or charge-transfer systems. This paper proposes CE-ETNet (Charge-Equilibration-Enhanced Equivariant Transformer Network), an equivariant Transformer interatomic potential constrained by charge equilibration. The model learns local chemical environments formed by atom types, geometric edges, and radial basis features through an equivariant representation encoder, and predicts atomic electronegativities. Under the constraint of total charge conservation, a differentiable charge equilibrat...

  `matched: interatomic potential, transformer, equivariant`


- **[Materials Discovery and Design](https://doi.org/10.1002/9783527852048.ch9)**
  <br>*OpenAlex | 2026-08-14 | doi:10.1002/9783527852048.ch9 | score 25*
  <br>Chonghuan Zhang

  This chapter surveys how artificial intelligence is transforming materials discovery and design by shifting the field from intuition-driven trial-and-error experimentation toward datadriven prediction, optimization, and inverse design. It begins by introducing the major roles of AI in materials science through a three-stage workflow: data acquisition and feature engineering as the knowledge foundation, high-throughput virtual screening and predictive modeling as efficient navigation of large materials spaces, and inverse design and autonomous generation as active creation of new materials with target properties. Building on this workflow, this chapter reviews core model families used in AI-d...

  `matched: artificial intelligence, materials discovery, inverse design`


- **[The CHGNet uMLIP model fine-tuned for 2Hc-WS2](https://doi.org/10.5281/zenodo.22059540)**
  <br>*Zenodo (CERN European Organization for Nuclear Research) | 2026-08-22 | doi:10.5281/zenodo.22059540 | score 24*
  <br>Pjotrs Zguns

  The CHGNet uMLIP model fine-tuned for 2Hc-WS2 in P. Žguns, I. Pudza, A. Kuzmin, Benchmarking CHGNet Universal Machine Learning Interatomic Potential Against DFT and EXAFS: Case of Layered WS2 and MoS2, J. Chem. Theory Comput. 21 (2025) 8142–8150. Doi: 10.1021/acs.jctc.5c00955

  `matched: machine learning interatomic potential, interatomic potential, machine learning, benchmark, dft`


- **[FastMD](https://doi.org/10.5281/zenodo.22051980)**
  <br>*Zenodo (CERN European Organization for Nuclear Research) | 2026-08-22 | doi:10.5281/zenodo.22051980 | score 24*
  <br>Siyu Hu

  This repo contains the software, input structures, benchmark configurations, analysis scripts, and numerical results associated with the study “Topology-Aware CUDA Graph Acceleration of Molecular Dynamics with Machine Learning Interatomic Potentials.” It provides CUDA Graph and kernel-optimized molecular-dynamics implementations for the MatRIS, CHGNet, and ALIGNN machine-learning interatomic potentials. The archived materials include scripts and configurations for the MatRIS, CHGNet, and ALIGNN application benchmarks, DynaMat-v1.0 benchmark sampling metadata, raw timing and GPU-memory measurements, representative profiling outputs, numerical data underlying the manuscript figures and tables,...

  `matched: machine learning interatomic potential, interatomic potential, molecular dynamics, machine learning, benchmark`


- **[FastMD](https://doi.org/10.5281/zenodo.22051979)**
  <br>*Zenodo (CERN European Organization for Nuclear Research) | 2026-08-22 | doi:10.5281/zenodo.22051979 | score 24*
  <br>Siyu Hu

  This repo contains the software, input structures, benchmark configurations, analysis scripts, and numerical results associated with the study “Topology-Aware CUDA Graph Acceleration of Molecular Dynamics with Machine Learning Interatomic Potentials.” It provides CUDA Graph and kernel-optimized molecular-dynamics implementations for the MatRIS, CHGNet, and ALIGNN machine-learning interatomic potentials. The archived materials include scripts and configurations for the MatRIS, CHGNet, and ALIGNN application benchmarks, DynaMat-v1.0 benchmark sampling metadata, raw timing and GPU-memory measurements, representative profiling outputs, numerical data underlying the manuscript figures and tables,...

  `matched: machine learning interatomic potential, interatomic potential, molecular dynamics, machine learning, benchmark`


### Preprints (arXiv / ChemRxiv / other)

- **[Insights into Lithium Diffusion in Crystalline and Amorphous Solid Electrolytes with Machine Learning Interatomic Potentials](https://doi.org/10.26434/chemrxiv.15007863/v1)**
  <br>*Crossref | 2026-08-26 | doi:10.26434/chemrxiv.15007863/v1 | score 53*
  <br>Mishra, Qi, Ong

  Amorphization is a widely used approach to tune the ionic conductivity in solid electrolytes, but its effect in different anion chemistries remains poorly understood. In this work, we employ molecular dynamics (MD) simulations with machine learning interatomic potentials (MLIPs) to quantify the effects of amorphization on Li-ion transport in lithium solid electrolytes from three anion chemistries: Li3YCl6 (LYC), Li0.33La0.56TiO3 (LLTO) and Li7P3S11 (LPS). With amorphization, it is observed that the ionic conductivity increases for LYC, decreases for LLTO and remains relatively unchanged for LPS, in agreement with previous experiments. Coordination analysis at 300K reveals that these ionic co...

  `matched: machine learning interatomic potential, interatomic potential, molecular dynamics, machine learning, electrolyte, crystal`


- **[Carbon Nanotube-Induced Magnetic Shielding Effects on 129Xe NMR from Equivariant Neural Networks](https://doi.org/10.26434/chemrxiv.15007956/v1)**
  <br>*ChemRxiv | 2026-08-27 | doi:10.26434/chemrxiv.15007956/v1 | score 49*
  <br>Ouail Zakary, Tiia Jacklin, Perttu Lantto

  Equivariant graph neural networks (EGNNs) have shown success in building efficient and accurate machine learning interatomic potentials (MLIPs) for molecular dynamics (MD) and in enabling the prediction of nuclear magnetic resonance (NMR) parameters in complex systems. In this work, we use EGNNs to fine-tune an atomistic foundation model (AFM) and to build an NMR machine learning model. The former is used to build an MLIP for large-scale MD simulations of xenon in carbon nanotubes, while the latter is used to predict the 129 Xe NMR magnetic shielding tensor, σ , directly from the MD snapshots. Both models are data-efficient and remain accurate well beyond their training data. Using this dual...

  `matched: machine learning interatomic potential, interatomic potential, graph neural network, molecular dynamics, machine learning, foundation model`


- **[Electrostatic Phenomenology Benchmarks for Machine-Learned Interatomic Potentials in Electrochemistry: Beyond the Energy-Force Metric](http://arxiv.org/abs/2608.14153v1)**
  <br>*arXiv | 2026-08-14 | score 47*
  <br>Barbara Sumić, Ria Vasdev, Sudheesh Kumar Ethirajan, Jing Yang et al.

  Accurate treatment of long-range interactions in machine learning interatomic potentials (MLIPs) is essential for electrochemical simulations. However, aggregate energy and force errors alone are insufficient to establish an MLIP's physical accuracy since they do not detect qualitative inconsistencies in the model such as the prediction of image-charge attraction, dielectric screening, or charge transfer. We introduce a benchmark suite EPhEct (Electrostatic Phenomena for Electrochemistry) of focused test cases designed to evaluate MLIPs on electrochemically relevant physical phenomena. The tests probe for image-charge attraction at a metal electrode, the splitting between longitudinal and tr...

  `matched: machine learning interatomic potential, machine-learned interatomic potential, interatomic potential, machine learning, benchmark`


- **[Unlocking Multi-Component Bulk-Materials Molecular Dynamics with a Small-Footprint Machine Learning Interatomic Potential](http://arxiv.org/abs/2608.16329v1)**
  <br>*arXiv | 2026-08-17 | score 43*
  <br>Yucheng Ouyang, Xin Chen, Ying Liu, Lifang Wang et al.

  Bulk materials, as opposed to nanomaterials, require molecular dynamics (MD) simulations on a large spatial scale (~10^9 atoms or more) to adequately capture their atomic-scale physical properties. Previously, the introduction of machine-learning interatomic potentials (MLIPs) has extended MD to this scale, but even single-component bulk systems require tens of thousands of GPUs on high-end supercomputers. However, multi-component bulk MD simulations remain barely achievable, as the HBM footprint of existing MLIPs - already substantial for single-component systems - grows explosively in multi-component scenarios. This paper proposes an MLIP with a small HBM footprint - less than 3% that of e...

  `matched: machine learning interatomic potential, interatomic potential, molecular dynamics, machine learning`


- **[A computed thermoelectric feature database for 50,992 GNoME materials](https://doi.org/10.26434/chemrxiv.15007873/v1)**
  <br>*Crossref | 2026-08-26 | doi:10.26434/chemrxiv.15007873/v1 | score 40*
  <br>Deshpande

  Machine-learning interatomic potentials now make it feasible to compute rich physical property sets for very large libraries of hypothetical crystals, but such feature sets are rarely released in analysis-ready form, and thermal-transport descriptors — central to thermoelectric performance — are especially scarce. Here we present a computed feature database for 50,992 novel, thermodynamically plausible crystalline materials drawn from Google DeepMind's Graph Networks for Materials Exploration (GNoME) database and filtered for thermoelectric relevance (non-metallic, finite band gap, energy above the Materials Project convex hull ≤ 0.05 eV/atom). For every material we provide composition and c...

  `matched: interatomic potential, materials project, thermoelectric, convex hull, band gap, crystal`


- **[Y-Mn-B Magnetic Materials: A DFT and Machine Learning Dataset](https://doi.org/10.5281/zenodo.22084774)**
  <br>*arXiv (Cornell University) | 2026-08-24 | doi:10.5281/zenodo.22084774 | score 36*
  <br>Weiyi Xia, Wei-Shen Tee, Maxim Moraru, Ying Wai Li

  This dataset contains the crystallographic structures, thermodynamic-stability data, and selected phonon and electronic-structure outputs supporting the manuscript: “Discovery of novel magnetic Y-Mn-B compounds via advanced machine learning guided framework.” The data were generated using an advanced implementation of the exa-AMD materials-discovery framework. More than one million hypothetical structures were initially screened using a crystal graph convolutional neural network, followed by structural relaxation and convex-hull sorting using a machine-learning interatomic potential. The selected low-energy structures were subsequently validated using first-principles density functional theo...

  `matched: interatomic potential, machine learning, neural network, crystal, dataset, magnet`


- **[Conservation-Resolved Error Decomposition: A Benchmark Axis for Electronic-Structure Methods and Machine-Learned Interatomic Potentials](https://doi.org/10.26434/chemrxiv.15007478/v1)**
  <br>*Crossref | 2026-08-17 | doi:10.26434/chemrxiv.15007478/v1 | score 36*
  <br>Bian, Guo, Zheng, Li et al.

  Benchmarks rank electronic-structure methods, semiempirical methods, and machine-learned potentials by errors on single molecules, whereas thermochemical applications use balanced energy dierences. A molecular score combines error components that a stated balance removes with those it retains, and a finite reaction benchmark samples only selected stoichiometries. We propose conservation-resolved error decomposition (CRED), which projects the molecular error vector onto the subspace spanned by conserved counts. The orthogonal residual is the reaction-visible error coordinate, and its per-molecule norm defines the conservation-resolved surviving error (CRSE). CRED requires one energy per molec...

  `matched: machine-learned interatomic potential, interatomic potential, benchmark`


- **[Benchmarking of Fast and Interpretable UF Machine Learning Potentials](http://arxiv.org/abs/2608.27277v1)**
  <br>*arXiv | 2026-08-27 | score 35*
  <br>Pawan Prakash, Sam Dong, Richard G. Hennig

  Machine learning interatomic potentials (MLIPs) have emerged as a powerful alternative to density functional theory (DFT) for molecular dynamics simulations, offering near-DFT accuracy at a fraction of the computational cost. However, many state-of-the-art MLIPs remain computationally demanding and act as black boxes, limiting physical interpretability. In this work, we evaluate the ultra-fast force field (UF$^3$) potential, which employs linear regression with cubic B-spline basis to represent effective two- and three-body interactions. We show that UF$^3$ displays accuracy comparable to established models such as GAP, MTP, NNP (Behler Parrinello), and qSNAP MLIPs. We further investigate th...

  `matched: machine learning interatomic potential, density functional theory, interatomic potential, molecular dynamics, machine learning, benchmark`


- **[Equivariance as a Substitutable Resource: A Unified Scaling Law for Machine-Learned Interatomic Potentials](https://doi.org/10.5281/zenodo.22063928)**
  <br>*Zenodo (CERN European Organization for Nuclear Research) | 2026-08-23 | doi:10.5281/zenodo.22063928 | score 35*
  <br>Fuxing Lin

  Equivariant neural-network interatomic potentials dominate ionic-liquid (IL) modeling, yet how much their advantage is worth has remained qualitative. Using a controlled MACE l_max ablation across 8 ILs and non-IL molecules (ether, ethanol, methane), we derive quantitative laws of equivariance substitutability unified into a scaling law with beta_eff governed by a sharp capacity-dependent phase transition (C* ~ 52.6 channels). Cross-family: equivariance value drops steeply with molecular complexity kappa - IL strong transition (66.5->6.1), ether small seed-dependent gap (|gap|<3), small molecules redundant. This version adds the complete Ngo & Ravanbakhsh (ICLR 2026) citation and ether N30 l...

  `matched: machine-learned interatomic potential, interatomic potential, equivariant`


- **[Equivariance as a Substitutable Resource: A Unified Scaling Law for Machine-Learned Interatomic Potentials](https://doi.org/10.5281/zenodo.22063807)**
  <br>*Zenodo (CERN European Organization for Nuclear Research) | 2026-08-23 | doi:10.5281/zenodo.22063807 | score 35*
  <br>Fuxing Lin

  Equivariant neural-network interatomic potentials dominate ionic-liquid (IL) modeling, yet how much their advantage is worth has remained qualitative. Using a controlled MACE l_max ablation across 8 ILs and non-IL molecules (ether 17 atoms, ethanol, methane), we derive quantitative laws of equivariance substitutability unified into a scaling law with beta_eff governed by a sharp capacity-dependent phase transition (C* ~ 52.6 channels). Cross-family: the equivariance value drops steeply with molecular complexity kappa - complex ILs strong transition (gap 66.5->6.1), medium ether gap small (|gap|<3 meV, seed-dependent: +2.87/+2.19/+0.65 at 32ch N15/N30/128ch N15, -0.95 at seed 7), small molecu...

  `matched: machine-learned interatomic potential, interatomic potential, equivariant`


- **[Vibrational, structural, and chemical fingerprints of ion diffusion in crystalline solids](http://arxiv.org/abs/2608.21624v1)**
  <br>*arXiv | 2026-08-21 | score 35*
  <br>Gavin Winter, Juno Nam, Rafael Gómez-Bombarelli

  Predicting mobile-ion self-diffusivity $D^*$ from molecular dynamics (MD) simulations is essential for identifying promising solid-state electrolytes, but directly simulating ion diffusion is computationally expensive, particularly with high-accuracy machine learning interatomic potentials (MLIPs). Diffusion is a slow, emergent process that requires long trajectories to converge. Thermodynamic properties, by contrast, converge much faster: the enthalpy $h$, vibrational entropy $s_{vib}$, and 2-body, excess configurational entropy $s^{ex}_{2,config}$ can be extracted from comparatively short MD trajectories, and they encode rich information about the free energy landscape from which transport...

  `matched: machine learning interatomic potential, solid-state electrolyte, interatomic potential, molecular dynamics, machine learning, electrolyte`


- **[Vibrational, structural, and chemical fingerprints of ion diffusion in crystalline solids](https://doi.org/10.48550/arxiv.2608.21624)**
  <br>*arXiv (Cornell University) | 2026-08-21 | doi:10.48550/arxiv.2608.21624 | score 35*
  <br>Gavin Winter, Juno Nam, Rafael Gómez-Bombarelli

  Predicting mobile-ion self-diffusivity $D^*$ from molecular dynamics (MD) simulations is essential for identifying promising solid-state electrolytes, but directly simulating ion diffusion is computationally expensive, particularly with high-accuracy machine learning interatomic potentials (MLIPs). Diffusion is a slow, emergent process that requires long trajectories to converge. Thermodynamic properties, by contrast, converge much faster: the enthalpy $h$, vibrational entropy $s_{vib}$, and 2-body, excess configurational entropy $s^{ex}_{2,config}$ can be extracted from comparatively short MD trajectories, and they encode rich information about the free energy landscape from which transport...

  `matched: machine learning interatomic potential, solid-state electrolyte, interatomic potential, molecular dynamics, machine learning, electrolyte`


- **[Universal Thermodynamic Interatomic Potentials for Crystalline Materials](http://arxiv.org/abs/2608.14502v1)**
  <br>*arXiv | 2026-08-14 | score 35*
  <br>Juno Nam, Bowen Deng, Xiaochen Du, Luis Barroso-Luque et al.

  Free energies govern solid-state phase stability, yet computational materials discovery still relies largely on ground-state energies because free energy calculations require ensemble averages. We introduce the thermodynamic interatomic potential (TIP), which extends an interatomic potential from its static energy to a thermodynamically consistent Gibbs free energy model, with thermodynamic responses following from temperature and pressure by automatic differentiation. We implement TIP[UMA] using the universal potential UMA, train it on free energies from quasi-harmonic to molecular dynamics fidelity, and calibrate it to higher-resolution calculations or experiment. From a single evaluation,...

  `matched: interatomic potential, materials discovery, universal potential, molecular dynamics, crystal`


- **[GRACE-OFF: A machine-learned interatomic potential for organic liquids using the GRACE architecture](https://doi.org/10.26434/chemrxiv.15001529/v2)**
  <br>*Crossref | 2026-08-18 | doi:10.26434/chemrxiv.15001529/v2 | score 32*
  <br>Picha, Karwounopoulos, Erhard, Boresch et al.

  `matched: machine-learned interatomic potential, interatomic potential`


- **[Machine Learning to Foundation Models: Artificial Intelligence for Nanophotonic Modeling and Scientific Discovery](https://doi.org/10.48550/arxiv.2608.21612)**
  <br>*arXiv (Cornell University) | 2026-08-21 | doi:10.48550/arxiv.2608.21612 | score 31*
  <br>Chaobin Yang, Xueqing Liu, Yiqun Fu, Fengbo Zhou

  Artificial intelligence (AI) is increasingly used to model, design, and study nanophotonic systems. This review traces the development of the field from classical machine learning and deep learning to generative models, transfer learning, transformers, and emerging foundation models. It first introduces major nanophotonic platforms, including nanoparticles, nanoholes, metasurfaces, photonic crystals, multilayer thin films, and integrated photonic devices, together with their main forward and inverse problems. It then reviews data-driven methods for predicting optical spectra and fields, generating structures from target responses, improving designs through optimization, and accounting for fa...

  `matched: artificial intelligence, machine learning, foundation model, generative model, deep learning, transformer`


- **[Data-Efficient Construction of Material-Specific Machine-Learning Interatomic Potentials from Ab Initio Molecular Dynamics Trajectories](http://arxiv.org/abs/2608.14899v1)**
  <br>*arXiv | 2026-08-14 | score 31*
  <br>Jonas Hänseroth, Christian Dreßler

  Pretrained machine-learning interatomic potentials, so-called universal or foundation models offer an appealing starting point for atomistic simulations, but their accuracy for material-specific observables often remains limited without additional reference data (fine-tuning). Here, we systematically quantify how much first-principles data are required to convert universal models into ab initio-accurate material-specific potentials, and ask whether fine-tuning is necessarily preferable to training from scratch. We compare five universal MLIP frameworks, MACE-MP-0, SevenNet-0, GRACE-1L-OAM, MatterSim-v1-5M and ORB-v2, across seven chemically diverse systems incorporating rare and reactive eve...

  `matched: interatomic potential, molecular dynamics, foundation model, mattersim`


- **[High-throughput Discovery of Magnetic Rare Earth Transition Metal Alloys](http://arxiv.org/abs/2608.25270v1)**
  <br>*arXiv | 2026-08-26 | score 29*
  <br>Shuo Tao, Osman Goni Ridwan, Liqin Ke, Qiang Zhu

  We present an accelerated materials discovery framework that combines diffusion-based crystal structure generation with hierarchical screening to identify new rare-earth--transition-metal magnets simultaneously achieving high magnetization and thermodynamic stability. Using this workflow, we systematically explored over 3000 binary (R-T) and ternary (R-T-T$'$) compositions spanning R~$\in \{\text{Y, Sm}\}$, T~$\in \{\text{Fe, Co, Ni}\}$, and T$' \in \{\text{Ti, V, Cr, Mn, Cu, Zn}\}$, and filtered approximately 240{,}000 generated crystal structures through machine-learning interatomic potential prescreening and spin-polarized density functional theory validation. We identify 300+ low-energy...

  `matched: density functional theory, interatomic potential, materials discovery, crystal, magnet, alloy`


- **[High-throughput Discovery of Magnetic Rare Earth Transition Metal Alloys](https://doi.org/10.48550/arxiv.2608.25270)**
  <br>*arXiv (Cornell University) | 2026-08-26 | doi:10.48550/arxiv.2608.25270 | score 29*
  <br>Shuo Tao, Osman Goni Ridwan, Liqin Ke, Qiang Zhu

  We present an accelerated materials discovery framework that combines diffusion-based crystal structure generation with hierarchical screening to identify new rare-earth--transition-metal magnets simultaneously achieving high magnetization and thermodynamic stability. Using this workflow, we systematically explored over 3000 binary (R-T) and ternary (R-T-T$'$) compositions spanning R~$\in \{\text{Y, Sm}\}$, T~$\in \{\text{Fe, Co, Ni}\}$, and T$' \in \{\text{Ti, V, Cr, Mn, Cu, Zn}\}$, and filtered approximately 240{,}000 generated crystal structures through machine-learning interatomic potential prescreening and spin-polarized density functional theory validation. We identify 300+ low-energy...

  `matched: density functional theory, interatomic potential, materials discovery, crystal, magnet, alloy`


- **[Local Symmetry Breaking and Correlated Fluctuations in Quantum Materials from Atomistic Foundation Models](https://doi.org/10.26434/chemrxiv.15001387/v2)**
  <br>*Crossref | 2026-08-19 | doi:10.26434/chemrxiv.15001387/v2 | score 29*
  <br>Zakary, Yin, Aryal

  Short-range structural distortions retained within nominally high-symmetry crystals underlie the anomalous physical properties of many advanced materials. These distortions reflect local symmetry breaking and correlated fluctuations extending over nanometer length scales and picosecond timescales, making their accurate modeling challenging. Here, we demonstrate that such distortions can be modeled using a machine learning-based framework, taking RuP, the parent compound of ruthenium-pnictide superconductors, as a representative quantum material. By fine-tuning an atomistic foundation model on ab initio molecular dynamics data, we obtain an interatomic potential that captures the temperature-...

  `matched: interatomic potential, molecular dynamics, machine learning, foundation model, superconductor, crystal`


- **[Neural Networks Accelerate Ab Initio Multiple Spawning Simulations: A Case Study of Using Machine Learning Potentials for Excited State Dynamics](https://doi.org/10.26434/chemrxiv.15007443/v1)**
  <br>*Crossref | 2026-08-14 | doi:10.26434/chemrxiv.15007443/v1 | score 29*
  <br>Unzueta, Wang, Martinez

  Nonadiabatic simulations are critical for understanding photochemical reactions but are often computationally prohibitive, limiting their application to relatively small molecules and short timescales. Machine learning interatomic potentials (MLIPs) promise to remove most of the cost by replacing the electronic structure calls that dominate these simulations, while retaining chemical accuracy. We evaluate independent MLIPs fit to the ground and first excited state for two prototypical photochemical molecules — ethylene and the deprotonated green fluorescent protein chromophore. Despite sub-chemical-accuracy errors on held-out test data, the MLIPs predict qualitatively wrong potential energy...

  `matched: machine learning interatomic potential, interatomic potential, machine learning, neural network`


- **[Packora: Systematic Design for Generative Molecular Crystal Structure Prediction](http://arxiv.org/abs/2608.26962v1)**
  <br>*arXiv | 2026-08-27 | score 27*
  <br>Nayoung Kim, Kiyoung Seong, Sungsoo Ahn

  Molecular crystal structure prediction (CSP) is important in pharmaceuticals, agrochemicals, and organic electronics, where subtle differences in molecular conformation and packing can strongly affect material properties. We present Packora, a flow-based generative model for molecular CSP that jointly predicts atomic coordinates and the lattice from molecular graphs. Packora supports multi-component and organometallic crystals and can condition on any subset of molecular conformers, stereochemical labels, and space-group information within a single model. Inspired by the CCDC CSP blind test, we evaluate generation and ranking separately, using generation to isolate generator quality and rank...

  `matched: crystal structure prediction, generative model, crystal`


- **[Machine Learning Guided Discovery of Corundum High Entropy Oxides](http://arxiv.org/abs/2608.20596v1)**
  <br>*arXiv | 2026-08-20 | score 26*
  <br>Abraham A. Mancilla, Oliver A. Dicks, Solveig S. Aamlid, Mario Ulises González-Rivas et al.

  Early thinking in the field of high entropy oxides (HEOs) emphasized their likely abundance, with combinatorial arguments hinting at a myriad of new materials. The experimental reality has proven more challenging: the stability of HEOs cannot be straightforwardly predicted based on ionic radii, lattice geometry, and charge-balancing considerations alone. In this work, we employ machine learning interatomic potentials (MLIPs) to predict the synthesizability of HEOs of the form $A_2$O$_3$ derived from a selection of trivalent cations. From nearly 500 possible compositions, we identify 16 promising candidates for experimental validation with solid-state and combustion synthesis. We discover thr...

  `matched: machine learning interatomic potential, experimental validation, interatomic potential, machine learning`


- **[Machine Learning Guided Discovery of Corundum High Entropy Oxides](https://doi.org/10.48550/arxiv.2608.20596)**
  <br>*arXiv (Cornell University) | 2026-08-20 | doi:10.48550/arxiv.2608.20596 | score 26*
  <br>Abraham A. Mancilla, Oliver A. Dicks, Solveig S. Aamlid, Mario Ulises González-Rivas

  Early thinking in the field of high entropy oxides (HEOs) emphasized their likely abundance, with combinatorial arguments hinting at a myriad of new materials. The experimental reality has proven more challenging: the stability of HEOs cannot be straightforwardly predicted based on ionic radii, lattice geometry, and charge-balancing considerations alone. In this work, we employ machine learning interatomic potentials (MLIPs) to predict the synthesizability of HEOs of the form $A_2$O$_3$ derived from a selection of trivalent cations. From nearly 500 possible compositions, we identify 16 promising candidates for experimental validation with solid-state and combustion synthesis. We discover thr...

  `matched: machine learning interatomic potential, experimental validation, interatomic potential, machine learning`


- **[Optimization of active learning strategies for infrared spectra prediction in catalysis](https://doi.org/10.26434/chemrxiv.15007549/v1)**
  <br>*Crossref | 2026-08-18 | doi:10.26434/chemrxiv.15007549/v1 | score 26*
  <br>Bedirkhanov, Bhatia, Krejčí, Rinke et al.

  Infrared (IR) spectroscopy is a key tool for probing catalytic processes, but interpreting experimental spectra can be challenging and often requires guidance from theoretical simulations. In our recent work, we introduced PALIRS [Bhatia et al., npj Comput. Mater., 2025, 11, 324], a Python-based Active Learning Code for Infrared Spectroscopy, employing machine-learned interatomic potentials (MLIPs) to predict IR spectra. PALIRS achieved accuracy comparable to advanced quantum mechanical approaches like ab initio molecular dynamics (AIMD) at a fraction of the computational cost. In this work, we extend PALIRS by systematically comparing MLIP training strategies within the active learning loop...

  `matched: machine-learned interatomic potential, interatomic potential, molecular dynamics, active learning`


- **[G2RINS: A Generative String-and-Graph Polymer Representation to Assist Computational Materials Discovery](https://doi.org/10.26434/chemrxiv.15007504/v1)**
  <br>*Crossref | 2026-08-17 | doi:10.26434/chemrxiv.15007504/v1 | score 26*
  <br>Zaldivar, Tian, Sun, Kappatou et al.

  There is considerable interest in developing generative models for the design of new polymeric materials. A major challenge towards the development of such models is designing machine-readable representations that capture the hierarchical and stochastic nature of polymers. In this work, we introduce G2RINS, a generative line and graph notation that builds on G-BigSMILES to account for the multistep hierarchical microstructure of real polymers by properly describing prepolymers and branching. This new string representation considerably improves the descriptive capabilities of the overall framework. Additionally, our dedicated Python implementation automatically converts G2RINS strings into ge...

  `matched: materials discovery, generative model, polymer`


- **[A Hierarchical Synergistic Deep Learning Framework Integrating Composition, Structure, and Ionic Transport for Solid-State Electrolyte Discovery](http://arxiv.org/abs/2608.25592v1)**
  <br>*arXiv | 2026-08-26 | score 25*
  <br>Hongwei Du, Dingyang Lv, Baole Wei, Yongheng Li et al.

  Inorganic solid-state electrolytes must combine high room-temperature ionic conductivity, a wide electrochemical window, excellent electronic insulation, and favorable mechanical compliance. Single models struggle to support reliable multi-objective screening across vast chemical spaces because of training-data distribution mismatch, cross-property dataset heterogeneity, and scarce kinetic transport data. To overcome these limitations, we develop a hierarchical synergistic deep-learning framework that sequentially coordinates efficiency, accuracy, and reliability through four complementary modules. The in-house-developed L-G-DCNN and a multi-fidelity implementation built on DenseGNN serve as...

  `matched: solid-state electrolyte, deep learning, electrolyte, inorganic, dataset`


- **[Dynamic Ensembles of Phosphine-Stabilized Gold Nanoclusters](http://arxiv.org/abs/2608.19404v1)**
  <br>*arXiv | 2026-08-19 | score 25*
  <br>Caitlin A. McCandler, Disha Sanwal, Jutta Rogal

  Atomically precise phosphine-stabilized gold nanoclusters are commonly characterized by single-crystal X-ray diffraction, yet the extent to which these static structures represent finite-temperature behavior remains unclear. To explore the free-energy landscapes, equilibrium populations, and isomerization kinetics of these nanoclusters in the gas phase, we establish a general framework that combines molecular dynamics simulations based on a machine-learned interatomic potential with Markov state models (MSMs). Analysis of the MSMs indicates that experimentally reported crystal structures frequently correspond to minor metastable states or transient configurations rather than the dominant fin...

  `matched: machine-learned interatomic potential, interatomic potential, molecular dynamics, x-ray diffraction, crystal`


- **[Integrating Multi-Task Surrogate Modelling with Reinforcement Learning for Autonomous CO2 Reduction Catalyst Discovery: A Proof-of-Concept Framework](https://doi.org/10.26434/chemrxiv.15007484/v1)**
  <br>*Crossref | 2026-08-17 | doi:10.26434/chemrxiv.15007484/v1 | score 25*
  <br>Chakraborty

  Computational design of heterogeneous catalysts for CO2 reduction remains constrained by the prohibitive cost of density functional theory (DFT) calculations and the vast compositional search space of transition-metal alloys. We present a proof-of-concept framework that integrates three AI components: (i) a multi-task neural network surrogate trained on physics-informed synthetic data that simultaneously predicts activation energy (R2 = 0.984), turnover frequency (R2 = 0.984), selectivity (R2 = 0.974), and stability (R2 = 0.559); (ii) a proximal policy optimisation (PPO) agent that autonomously navigates an 18-dimensional action space of metal–facet–alloy compo-sitions, identifying Fe(111) a...

  `matched: density functional theory, surrogate model, neural network, catalyst, alloy, dft`


- **[Realistic Simulations of Energy Materials Using Foundation Models and Electrode-Potential Learning](https://doi.org/10.26434/chemrxiv.15007895/v1)**
  <br>*Crossref | 2026-08-26 | doi:10.26434/chemrxiv.15007895/v1 | score 24*
  <br>Chae, Kim, I, Lee et al.

  Here, we evaluate SevenNet-Omni [Kim et al., Nat. Commun. 2026, 17, 3432], a universal machine-learning interatomic potential (MLIP), in realistic energy-material systems whose long timescale simulations are beyond the practical reach of density-functional theory (DFT). Tests span explicit solvation, metal-support interfaces, and reactive battery surfaces and interfaces, all of which involve realistic cross-domain interactions between inorganic materials and organic species. Without system-specific fine-tuning, SevenNet-Omni achieves sufficient accuracy for these out-of-domain systems, demonstrating strong transferability. To extend MLIPs to electrochemical systems, we also develop a model t...

  `matched: interatomic potential, foundation model, inorganic, battery, dft`


- **[Graph neural network prediction of temperature-dependent hydrogen diffusion and thermal conductivity tensors of tungsten containing helium bubbles and grain boundaries](http://arxiv.org/abs/2608.15609v1)**
  <br>*arXiv | 2026-08-16 | score 24*
  <br>S. Saito, M. I. Kobayashi, T. Kasahara

  Helium bubbles and grain boundaries in tungsten plasma-facing components alter hydrogen-isotope transport and thermal conduction by orders of magnitude, yet evaluating these transport properties for a given microstructure requires hours of molecular dynamics (MD) per configuration. We present a graph neural network surrogate that maps a tungsten atomic configuration containing helium bubbles and grain boundaries directly to the full $3\times3$ symmetric tensors of the hydrogen diffusion coefficient $D_H(T)$ and the thermal conductivity $κ(T)$ at arbitrary temperature. Anisotropy is captured by a rotation-equivariant tensor pooling layer; temperature enters through predicted temperature-indep...

  `matched: graph neural network, molecular dynamics, neural network, equivariant`


### Industry labs and code releases

- **[How AI Coding Agents Can Unlock Materials Simulation with NVIDIA ALCHEMI Toolkit](https://developer.nvidia.com/blog/how-ai-coding-agents-can-unlock-materials-simulation-with-nvidia-alchemi-toolkit/)**
  <br>*NVIDIA Developer Blog | 2026-08-18 | score 19*

  Atomistic simulation requires three things: knowledge of the science, compute-efficient implementation of simulations, and accessible interfaces to the...

  `matched: alchemi`


---

