# AI and Materials Discovery

**A survey of the three industrial programs: NVIDIA, Microsoft, and Google DeepMind**

Compiled 2026-08-28. Every factual claim is sourced; statements that could not be verified in public documentation are explicitly marked *not publicly documented*.

---

## 1. Why AI changed materials discovery

Every technology generation is gated by materials: silicon for chips, layered oxides for lithium-ion cathodes, superconductors for MRI magnets. Historically each new stable compound cost months to years of trial-and-error synthesis, and computational screening was limited by the cost of quantum mechanics. Density functional theory (DFT) scales roughly as O(N^3) in the number of atoms: 10 atoms takes minutes, 100 atoms takes hours, and 1,000+ atoms can take weeks, which makes brute-force DFT screening of millions of candidates impossible ([NVIDIA, 2024](https://developer.nvidia.com/blog/revolutionizing-ai-driven-material-discovery-using-nvidia-alchemi/)).

Modern AI attacks four distinct stages of the discovery pipeline, and the three programs surveyed here each specialize in different stages:

| Stage | What it means | Dominant AI method | Who leads (of the three) |
|---|---|---|---|
| 1. Hypothesis generation | Read the literature, propose chemistries | LLMs / agentic systems | Microsoft (Discovery platform) |
| 2. Solution-space definition | Enumerate or invent candidate structures | Generative models (diffusion), substitution + random search | Microsoft (MatterGen), Google (GNoME pipelines) |
| 3. Property prediction | Predict energy, stability, moduli, conductivity | Machine-learning interatomic potentials (MLIPs), graph neural networks (GNNs) | NVIDIA (ALCHEMI/MACE), Microsoft (MatterSim), Google (GNoME) |
| 4. Experimental validation | Synthesize and characterize | Active learning, self-driving labs | Google/Berkeley Lab (A-Lab), Microsoft (SIAT, PNNL) |

The unifying technical idea is the **MLIP**: a neural network (usually an equivariant GNN, with atoms as nodes and interatomic distances within a cutoff radius as edges) trained on DFT energies and forces. An MLIP reaches near-DFT accuracy at a cost close to classical force fields, which is what makes screening at the scale of 10^6 structures possible ([NVIDIA, 2024](https://developer.nvidia.com/blog/revolutionizing-ai-driven-material-discovery-using-nvidia-alchemi/)).

---

## 2. Introductions from the three starting sources

### 2.1 NVIDIA — ALCHEMI: AI Lab for Chemistry and Materials Innovation

Source: [Revolutionizing AI-Driven Material Discovery Using NVIDIA ALCHEMI](https://developer.nvidia.com/blog/revolutionizing-ai-driven-material-discovery-using-nvidia-alchemi/) (Nov 18, 2024)

NVIDIA's entry point is **infrastructure, not discovery**. ALCHEMI does not claim to have found new materials itself; it supplies the GPU software layer — CUDA kernels, Python toolkits, and containerized inference microservices (NIM) — that other people's models run on. The stated goal is to shorten the design-to-production cycle "from a decade to months."

The launch deliverable was the **Batched Geometry Relaxation NIM**, built on [NVIDIA Warp](https://github.com/NVIDIA/warp), which runs hundreds of geometry relaxations concurrently on a single GPU instead of one at a time. Reported speedups were up to **100x with MACE-MP-0** and up to **800x with AIMNet2**. The first named customer, **SES AI**, used it to map **100,000 candidate electrolyte molecules in half a day** for lithium-metal batteries.

### 2.2 Microsoft — MatterGen and MatterSim

Source: [AI meets materials discovery: The vision behind MatterGen and MatterSim](https://www.microsoft.com/en-us/research/story/ai-meets-materials-discovery/)

Microsoft Research's AI for Science group frames the problem as **inverse design**. The origin question, asked by Tian Xie during his MIT PhD in 2018, was: *"Can you build a model that takes constraints and criteria as input and generates a viable material as output?"*

The answer is a complementary pair of models:

- **MatterGen** is "the idea generator, the visionary" — a diffusion model that generates thousands of candidate crystals under user-defined constraints (a target band gap of 3 eV, a high bulk modulus, a magnetic density with no critical elements).
- **MatterSim** is "the gatekeeper, the realist" — an atomistic MLIP that predicts which of those imagined structures are actually stable and viable, across elements, temperatures, and pressures.

This is a genuine paradigm shift from screening: instead of "fitting puzzle pieces from a box," you "design entirely new puzzles customized to defined parameters." Ziheng Lu's stated ambition is blunt: replace 80–90% of quantum-mechanical calculations with machine learning.

### 2.3 Google DeepMind — GNoME

Source: [Millions of new materials discovered with deep learning](https://deepmind.google/blog/millions-of-new-materials-discovered-with-deep-learning/) (Nov 29, 2023)

DeepMind's contribution is **scale**. **GNoME (Graph Networks for Materials Exploration)**, published in [Nature](https://doi.org/10.1038/s41586-023-06735-9), predicted **2.2 million new crystal structures** — described as roughly "800 years' worth of knowledge" — of which **380,000 are the most stable** and therefore the best experimental targets.

The context numbers are the important part of the story:

| Source of knowledge | Number of computationally stable inorganic crystals |
|---|---|
| Human experimentation (ICSD) | ~20,000 |
| Prior computational efforts (Materials Project, OQMD, WBM) | ~48,000 |
| After GNoME | **421,000** |

Highlights include **52,000 new graphene-like layered compounds** (versus ~1,000 previously known) and **528 candidate lithium-ion conductors** (25x a previous study). Critically, **736 of GNoME's structures were independently synthesized by external labs** in concurrent work, and a companion Nature paper from Lawrence Berkeley National Laboratory demonstrated **autonomous robotic synthesis** driven by these predictions.

---

## 3. Head-to-head comparison

### 3.1 Master comparison table

| Criterion | NVIDIA (ALCHEMI) | Microsoft Research (AI for Science) | Google DeepMind |
|---|---|---|---|
| **Strategic role** | GPU infrastructure + inference microservices for everyone else's models | Inverse design: generate, then simulate | Exhaustive discovery at scale |
| **Models developed** | ALCHEMI NIM microservices: Batched Geometry Relaxation (BGR), Batched Molecular Dynamics (BMD), Batched Conformer Search (BCS); ALCHEMI Toolkit / Toolkit-Ops; Warp; cuEquivariance; cuEST. Hosts third-party MLIPs: MACE-MP-0, MACE-MPA-0, AIMNet2 / AIMNet2-NSE, TensorNet-MatPES | MatterGen (diffusion generative model, Nature 2025); MatterSim (MLIP, 17M configurations); Skala (learned DFT exchange-correlation functional); DiG; AI2BMD; TamGen; Microsoft Discovery (agentic R&D platform) | GNoME (equivariant GNN, two pipelines + 6 rounds of active learning); GNoME NequIP-style interatomic potentials; SimGen/UniMat (diffusion generation, ICLR 2024) |
| **Models under development** | VASP microservice (early access, ~3x geometry-optimization speedup via MPS); Batched DFT microservice (GPU4PySCF backend); BCS availability status unclear | Skala successors ("improves with additional training data"); automated MatterGen -> MatterSim -> DFT -> synthesis closed loop; Microsoft Discovery in gated preview; MatterSim Graphormer weights "to be released" | No successor announced. Repo to-do list still includes training colabs, reference structures, and electronic band-structure properties. GNoME data still being ingested into the Materials Project in tranches |
| **Chemistry calculations** | MLIP inference (near-DFT accuracy at classical cost); FIRE2 relaxation; NVE/NVT/NPT MD; DFT-D3(BJ) dispersion; Ewald/PME electrostatics; GPU DFT via GPU4PySCF and cuEST; VASP on GPU | DFT at PBE(+U) with Materials Project settings for training labels; DFT validation of generated candidates; MatterSim MD via ASE and LAMMPS ML-IAP; phonons via phonopy; Gibbs free energies to ~15 meV/atom up to 1,000 K; Skala runs inside PySCF / GPU4PySCF | All DFT in VASP, PBE + PAW, 520 eV cutoff, PBE+U for some transition metals, Materials-Project-compatible (pymatgen/atomate); r2SCAN meta-GGA re-validation of a subset; convex-hull decomposition energies; MD with learned potentials for zero-shot ionic conductivity |
| **Materials discovered / targeted** | No first-party discoveries. Partner results: SES AI Li-metal electrolytes (100k molecules in half a day, 17 candidates, 2 synthesized, ~20% cycle-life gain); ENEOS + Preferred Networks immersion-cooling fluids (10M -> ~1,000 in 3 weeks) and ~100M -> ~1,000 OER catalysts; Universal Display OLED emitters; L'Oreal formulations; Lila Sciences magnets/catalysts | TaCr2O6 (target bulk modulus 200 GPa, synthesized and measured); PFAS-free datacenter immersion coolant (367,000 candidates screened in ~200 h); rare-earth-free magnets (computational); solid-state electrolytes with PNNL (32M -> 18 candidates in 80 h, one synthesized) | 2.2M predicted crystals; 380,000 stable candidates released; 421,000 total known stable; ~52,000 layered compounds; 528 Li-ion conductors; 736 already made independently; external follow-ups synthesized Cs2LiCrCl6, Cs2LiRuCl6, Cs2LiIrCl6 |
| **Experimental methods** | Positions "self-driving lab + active learning" as stage 4 of its workflow; realized through partners (Lila Sciences AI Science Factories, Microsoft Discovery/PNNL). No NVIDIA-operated lab | Classical solid-state synthesis of TaCr2O6 from Cr metal + Ta2O5 at SIAT/CAS; powder XRD + Rietveld refinement; XPS; nanoindentation for Young's modulus (bulk modulus via DFT Poisson ratio); coolant prototype synthesized and validated by immersing a running motherboard; PNNL electrolyte synthesis | A-Lab at Berkeley Lab: 3 robotic arms, 8 box furnaces, ~200 precursor powders, target 100–200 samples/day; robotic powder dosing, mixing, sintering; automated XRD + Rietveld; recipes proposed by NLP models text-mined from literature and refined by active learning |
| **Openness** | Toolkit/Toolkit-Ops Apache 2.0, Warp BSD-3; NIM containers require NVIDIA AI Enterprise license | MatterGen, MatterSim, Skala all **MIT** with public weights; Microsoft Discovery gated | Code Apache 2.0; **dataset CC BY-NC 4.0 (non-commercial)**; production GNoME checkpoint **not released** |

### 3.2 Model inventory in detail

| Model | Owner | Type | Training data | Weights public? |
|---|---|---|---|---|
| MACE-MP-0 | ACEsuit (hosted by NVIDIA) | Equivariant MLIP, 89 elements | MPtrj, ~1.6M crystals, PBE+U | Yes (MIT) |
| MACE-MPA-0 | ACEsuit (bundled in ALCHEMI NIM) | Equivariant MLIP, 89 elements | MPtrj + sAlex (+3.5M crystals) | Yes (MIT) |
| AIMNet2 / AIMNet2-NSE | Isayev Lab (hosted by NVIDIA) | Molecular MLIP, 14 elements; NSE handles open-shell/spin | wB97M-D3/def2-TZVPP | Yes |
| TensorNet-MatPES | MatPES (mountable in ALCHEMI NIM) | MLIP, periodic materials | MatPES PBE and r2SCAN v2025.1 | Yes |
| MatterGen | Microsoft | Diffusion over coordinates + atom types + lattice; GemNet-T score network; property adapters + classifier-free guidance | Alex-MP-20 (~600k structures, <0.1 eV/atom above hull), MP-20 (~45k) | Yes (MIT, GitHub + Hugging Face) |
| MatterSim v1 | Microsoft | MLIP (M3GNet backbone; Graphormer variant unreleased) | ~17M configurations, 0–5,000 K, 0–1,000 GPa; MPF2021, MPtrj, Alexandria | Yes, 1M and 5M parameter checkpoints |
| Skala | Microsoft | Learned XC functional (~385k parameters) for DFT | Coupled-cluster atomization energies and high-accuracy wavefunction data | Yes (skala-1.1) |
| GNoME | Google DeepMind | Equivariant message-passing GNN (NequIP-style, JAX/e3nn-jax/jraph) | Bootstrapped through 6 active-learning rounds of VASP data | **No** — architecture code only |

**GNoME accuracy benchmarks:** final relaxed-structure energy MAE ~11 meV/atom; stability hit-rate above 80% when a full structure is given, ~33% per 100 trials from composition alone ([Nature](https://doi.org/10.1038/s41586-023-06735-9)).

---

## 4. Hands-on: how to actually use these models

> All commands below are transcribed from the official repositories and documentation as of 2026-08-28. Linux + an NVIDIA GPU is assumed throughout; CPU fallback exists only for MatterSim single-point calculations and Skala.

### 4.1 Microsoft MatterGen — generate new crystals on demand

Repository: <https://github.com/microsoft/mattergen> (MIT). Weights: <https://huggingface.co/microsoft/mattergen>.

Install:

```bash
pip install uv
uv venv .venv --python 3.10
source .venv/bin/activate
uv pip install -e .
```

Unconditional generation:

```bash
export MODEL_NAME=mattergen_base
export RESULTS_PATH=results/
mattergen-generate $RESULTS_PATH --pretrained-name=$MODEL_NAME --batch_size=16 --num_batches 1
```

Property-conditioned generation (this is the interesting part — inverse design). Available conditional checkpoints: `chemical_system`, `space_group`, `dft_mag_density`, `dft_band_gap`, `ml_bulk_modulus`, `dft_mag_density_hhi_score`, `chemical_system_energy_above_hull`.

```bash
export MODEL_NAME=dft_mag_density
export RESULTS_PATH="results/$MODEL_NAME/"
mattergen-generate $RESULTS_PATH \
  --pretrained-name=$MODEL_NAME \
  --batch_size=16 \
  --properties_to_condition_on="{'dft_mag_density': 0.15}" \
  --diffusion_guidance_factor=2.0
```

Two properties at once — a lithium-oxygen compound within 0.05 eV/atom of the convex hull:

```bash
export MODEL_NAME=chemical_system_energy_above_hull
mattergen-generate "results/$MODEL_NAME/" \
  --pretrained-name=$MODEL_NAME \
  --batch_size=16 \
  --properties_to_condition_on="{'energy_above_hull': 0.05, 'chemical_system': 'Li-O'}" \
  --diffusion_guidance_factor=2.0
```

Fine-tune on your own property:

```bash
export PROPERTY=dft_mag_density
mattergen-finetune adapter.pretrained_name=mattergen_base \
  data_module=mp_20 \
  +lightning_module/diffusion_module/model/property_embeddings@adapter.adapter.property_embeddings_adapt.$PROPERTY=$PROPERTY \
  ~trainer.logger \
  data_module.properties=["$PROPERTY"]
```

**Caveat straight from the repo:** the open-source evaluation script uses MatterSim, not DFT, for stability screening. The Nature paper used DFT. Anything in an unusual chemistry must be confirmed with real DFT before you believe it.

### 4.2 Microsoft MatterSim — near-DFT energies, forces, MD, phonons

Repository: <https://github.com/microsoft/mattersim> (MIT). `pip install mattersim`.

Single-point properties through an ASE calculator:

```python
import torch
from ase.build import bulk
from ase.units import GPa
from mattersim.forcefield import MatterSimCalculator

device = "cuda" if torch.cuda.is_available() else "cpu"
si = bulk("Si", "diamond", a=5.43)
si.calc = MatterSimCalculator(device=device)

print(f"Energy per atom (eV/atom)   = {si.get_potential_energy() / len(si)}")
print(f"Forces of first atom (eV/A) = {si.get_forces()[0]}")
print(f"Stress[0][0] (GPa)          = {si.get_stress(voigt=False)[0][0] / GPa}")
```

Use the larger 4.5M-parameter model with `MatterSimCalculator(load_path="MatterSim-v1.0.0-5M.pth", device=device)`.

Phonon workflow (the standard dynamic-stability check — imaginary modes mean the structure will not survive):

```python
import numpy as np
from ase.build import bulk
from mattersim.forcefield.potential import MatterSimCalculator
from mattersim.applications.phonon import PhononWorkflow

si = bulk("Si", "diamond", a=5.43)
si.calc = MatterSimCalculator()

ph = PhononWorkflow(
    atoms=si,
    find_prim=False,
    work_dir="/tmp/phonon_si_example",
    amplitude=0.01,
    supercell_matrix=np.diag([4, 4, 4]),
)
has_imag, phonons = ph.run()
print(f"Has imaginary phonon: {has_imag}")
```

Fine-tune on your own DFT or high-level data:

```bash
torchrun --nproc_per_node=1 src/mattersim/training/finetune_mattersim.py \
  --load_model_path mattersim-v1.0.0-1m \
  --train_data_path tests/data/high_level_water.xyz
```

Large-scale MD is available through the LAMMPS `ML-IAP` interface with single- and multi-GPU support.

### 4.3 Microsoft Skala — a neural exchange-correlation functional

Repository: <https://github.com/microsoft/skala> (MIT). Interfaces: PySCF (CPU), GPU4PySCF (GPU), ASE. Released functional: `skala-1.1`.

```bash
# CPU
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install skala

# GPU
mamba env create -n skala -f environment-gpu.yml
mamba activate skala
pip install skala
```

Usage follows the PySCF pattern (`from skala.pyscf import SkalaKS, mol_from_xyz`); check <https://microsoft.github.io/skala/> for the exact versioned API. A Psi4 interface is *not publicly documented*.

### 4.4 Google DeepMind GNoME — the dataset, and its one big limitation

Repository: <https://github.com/google-deepmind/materials_discovery>. **Code Apache 2.0, dataset CC BY-NC 4.0 — non-commercial use only.**

Download the data (~381k stable structures on the hull, >520k within 1 meV/atom as of the Aug 2024 expansion):

```bash
gcloud storage cp --recursive gs://gdm_materials_discovery/ data/
# or, with the older tool
gsutil -m cp -r gs://gdm_materials_discovery/ data/
```

Or use the repo helper scripts:

```bash
python -m venv ~/venv/gnome && source ~/venv/gnome/bin/activate
pip install absl-py google-cloud-storage
python scripts/download_data_wget.py --data_dir ./data
```

Key files:

| File | Contents |
|---|---|
| `gnome_data/stable_materials_summary.csv` | Compositions, formation energies, decomposition energies (PBE) |
| `gnome_data/stable_materials_r2scan.csv` | r2SCAN meta-GGA re-validation energies |
| `gnome_data/by_composition.zip`, `by_id.zip`, `by_reduced_formula.zip` | CIF structure files |

Model code:

```bash
pip install -r requirements.txt
pip install e3nn-jax
pip install git+https://github.com/mariogeiger/nequip-jax
```

```python
from model.gnome import load_model
config, model, params = load_model("path/to/checkpoint_directory")
```

**The critical limitation:** the production GNoME checkpoint is **not distributed**. `load_model` needs a checkpoint directory you do not have — the Matbench Discovery model card lists GNoME's `checkpoint_url` as `missing`. In practice you consume the *dataset*, and if you want the *model* you retrain the released architecture yourself. If you need a ready-to-run universal MLIP today, use MatterSim, MACE-MPA-0, or Orb instead.

Query GNoME entries through the Materials Project instead (easier for coursework):

```bash
pip install mp-api
```

```python
from mp_api.client import MPRester

with MPRester("YOUR_MP_API_KEY") as mpr:
    docs = mpr.materials.summary.search(
        elements=["Li", "Mn", "O"],
        include_gnome=True,   # requires accepting the BY-NC terms on your MP dashboard
        fields=["material_id", "formula_pretty", "builder_meta",
                "decomposition_energy_per_atom"],
    )

gnome_docs = [d for d in docs if d.builder_meta.batch_id == "gnome_r2scan_statics"]
print(f"Found {len(gnome_docs)} GNoME-derived entries")
```

Note that ingestion is incremental: roughly 117k GNoME materials were in the Materials Project at the reported release, with the rest queued for later data releases.

### 4.5 The A-Lab autonomous synthesis stack

The Berkeley Lab robotic lab software is open source:

| Repo | Purpose |
|---|---|
| <https://github.com/CederGroupHub/alabos> | AlabOS workflow-management framework (MIT); needs MongoDB + RabbitMQ |
| <https://github.com/CederGroupHub/alab_control> | Device drivers for the lab hardware |
| <https://github.com/CederGroupHub/alab_gpss_public> | A-Lab platform orchestration and analysis scripts |

```bash
git clone https://github.com/CederGroupHub/alabos
cd alabos
pip install -e .
```

```python
from alab_management.builders import ExperimentBuilder

exp = ExperimentBuilder(
    name="MyExperiment",
    tags=["test"],
    description="First autonomous synthesis run",
)
# add tasks, then submit to the alabos server
```

### 4.6 NVIDIA ALCHEMI — GPU-batched relaxation and MD

Open-source layers (no license fee):

| Component | Repository | License |
|---|---|---|
| ALCHEMI Toolkit | <https://github.com/NVIDIA/nvalchemi-toolkit> | Apache 2.0 |
| ALCHEMI Toolkit-Ops (batched neighbor lists, DFT-D3(BJ), Ewald/PME, integrators) | <https://github.com/NVIDIA/nvalchemi-toolkit-ops> | Apache 2.0 |
| NVIDIA Warp | <https://github.com/NVIDIA/warp> | BSD-3-Clause |
| cuEquivariance (CUDA kernels for MACE, NequIP, Allegro) | <https://github.com/NVIDIA/cuEquivariance> | NVIDIA license |

```bash
pip install nvalchemi-toolkit
# CUDA 13 build with MACE support
pip install --extra-index-url https://download.pytorch.org/whl/cu130 \
            --extra-index-url https://pypi.nvidia.com \
            'nvalchemi-toolkit[cu13,mace]'

pip install warp-lang
pip install cuequivariance cuequivariance-torch cuequivariance-ops-torch-cu12
```

The NIM microservices are containers on NGC and **require an NVIDIA AI Enterprise license for self-hosted production use** (list price from ~$4,500/GPU/year, with education and Inception discounts). Requirements: Linux, Docker + NVIDIA Container Toolkit, compute capability >= 8.0, >= 8 GB VRAM, ~15 GB disk, glibc >= 2.35.

```bash
export NGC_API_KEY=<your NGC API key>
docker pull nvcr.io/nim/nvidia/alchemi-bgr:1.0.0
docker run --rm -ti --name alchemi-bgr --gpus=all \
    -e NGC_API_KEY -p 8000:8000 --shm-size=8g \
    nvcr.io/nim/nvidia/alchemi-bgr:1.0.0
```

Wait for `/v1/health/ready` to return `{"status":"ready"}`, then post structures from ASE:

```python
import requests
import ase.io

INFER = "http://localhost:8000/v1/infer"
atoms_list = ase.io.read("structures.extxyz", index=":")

def ase_to_api(atoms, sid=None):
    data = {
        "coord": atoms.positions.flatten().tolist(),
        "numbers": atoms.numbers.tolist(),
        "charge": atoms.info.get("charge", 0),
        "mult": atoms.info.get("mult", 1),
    }
    if atoms.cell.volume > 0:
        data["cell"] = atoms.cell.array.flatten().tolist()
        data["pbc"] = atoms.pbc.tolist()
    if sid:
        data["structure_id"] = sid
    return data

payload = {"atoms": [ase_to_api(a, f"struct_{i}") for i, a in enumerate(atoms_list)],
           "opttol": 0.001}
resp = requests.post(INFER, json=payload)
resp.raise_for_status()
print(resp.json())
```

Batched molecular dynamics is the same pattern with the `alchemi-bmd:1.0.0` container. MACE-MPA-0 ships pre-bundled; AIMNet2-NSE and TensorNet-MatPES can be mounted in for organics/radicals and additional PBE/r2SCAN materials coverage respectively.

### 4.7 Which one should you use?

| If you want to... | Use |
|---|---|
| Learn the field with zero cost and a laptop | MatterSim (CPU fallback) + Materials Project API |
| Invent structures with a target property | MatterGen |
| Screen a large candidate library fast on one GPU | MatterSim, MACE-MPA-0, or ALCHEMI Toolkit |
| Screen millions of candidates in production | ALCHEMI NIM (BGR/BMD), licensed |
| Mine an existing catalog of stable candidates | GNoME dataset (non-commercial) or Materials Project |
| Get chemical accuracy for small molecules | Skala inside PySCF/GPU4PySCF |
| Automate the synthesis loop | AlabOS |

---

## 5. Read the fine print: the novelty debate

This topic is a good teaching case in scientific skepticism, because the headline numbers have been seriously challenged.

- **Cheetham & Seshadri (2024)**, *Chemistry of Materials*, reviewed GNoME's output and found "scant evidence for compounds that fulfill the trifecta of novelty, credibility, and utility" — many entries had known analogues or lacked crystallographic credibility ([doi:10.1021/acs.chemmater.4c00643](https://doi.org/10.1021/acs.chemmater.4c00643)).
- **Palgrave, Schoop and co-workers (2024)** re-analyzed the A-Lab XRD data and concluded that automated Rietveld refinement had misidentified products and ignored substitutional disorder ([doi:10.26434/chemrxiv-2024-5p9j4](https://doi.org/10.26434/chemrxiv-2024-5p9j4)).
- The A-Lab authors issued a **Nature Author Correction**: "novel" was intended as "new to the prediction platform," not "new to science." After manual re-analysis, 36 of 40 reported successes were confirmed and 4 were inconclusive; the article now states **36 of 57 targets** realized in 17 days (the preprint had claimed 41 of 58).
- A 2026 *Materials Horizons* commentary similarly disputes that Microsoft's synthesized TaCr2O6 phase is new, arguing it relates to previously reported Ta(1/2)Cr(1/2)O2 ([RSC](https://pubs.rsc.org/en/content/articlehtml/2026/mh/d6mh00268d)). The measured bulk modulus (158 +/- 11 GPa against a 200 GPa target) stands regardless.

The honest summary: AI has produced an enormous, genuinely useful **candidate space** and demonstrable acceleration of screening. Confirmed, novel, *useful* materials attributable to these systems remain a much smaller number, and every published claim still passes or fails on ordinary crystallography. NVIDIA's own documentation makes the same point — MLIP foundation models are not universal, and each new chemistry must be validated against DFT or experiment.

---

## 6. Suggested exercises

1. **Convex hull reasoning.** Download `stable_materials_summary.csv` from GNoME and plot `decomposition_energy_per_atom` for a chosen chemical system. Which candidates sit exactly on the hull, and what does that mean physically?
2. **Inverse design.** Run MatterGen conditioned on `chemical_system: 'Li-O'` with `energy_above_hull: 0.05`, then relax the outputs with MatterSim. What fraction survive?
3. **Trust the potential?** Compute the phonon spectrum of silicon with MatterSim and compare to the experimental dispersion. Find a chemistry where the MLIP fails.
4. **Functional matters.** Compare PBE and r2SCAN energies for the same compounds in the GNoME files. How many materials change stability classification with the functional?
5. **Peer review.** Read the DeepMind blog and then the Cheetham & Seshadri perspective. Write one page on what "discovery" should mean.

---

## 7. References

**Primary sources**

1. NVIDIA, *Revolutionizing AI-Driven Material Discovery Using NVIDIA ALCHEMI*, Nov 18, 2024. <https://developer.nvidia.com/blog/revolutionizing-ai-driven-material-discovery-using-nvidia-alchemi/>
2. Microsoft Research, *AI meets materials discovery: The vision behind MatterGen and MatterSim*. <https://www.microsoft.com/en-us/research/story/ai-meets-materials-discovery/>
3. Google DeepMind, *Millions of new materials discovered with deep learning*, Nov 29, 2023. <https://deepmind.google/blog/millions-of-new-materials-discovered-with-deep-learning/>

**Peer-reviewed papers**

4. Merchant, A. et al. *Scaling deep learning for materials discovery*, Nature (2023). <https://doi.org/10.1038/s41586-023-06735-9>
5. Szymanski, N. J. et al. *An autonomous laboratory for the accelerated synthesis of novel materials*, Nature (2023). <https://www.nature.com/articles/s41586-023-06734-w> (plus Author Correction)
6. Zeni, C., Xie, T. et al. *A generative model for inorganic materials design* (MatterGen), Nature (2025). <https://doi.org/10.1038/s41586-025-08628-5>
7. Yang, H. et al. *MatterSim: A Deep Learning Atomistic Model Across Elements, Temperatures and Pressures*, arXiv:2405.04967. <https://arxiv.org/abs/2405.04967>
8. Cheetham, A. K. & Seshadri, R. *Artificial Intelligence Driving Materials Discovery?*, Chem. Mater. (2024). <https://doi.org/10.1021/acs.chemmater.4c00643>
9. Leeman, J. et al. *Challenges in High-Throughput Inorganic Materials Prediction and Autonomous Synthesis*, ChemRxiv (2024). <https://doi.org/10.26434/chemrxiv-2024-5p9j4>

**Code and data**

10. MatterGen — <https://github.com/microsoft/mattergen> (MIT)
11. MatterSim — <https://github.com/microsoft/mattersim> (MIT)
12. Skala — <https://github.com/microsoft/skala> (MIT)
13. GNoME — <https://github.com/google-deepmind/materials_discovery> (code Apache 2.0, data CC BY-NC 4.0)
14. AlabOS — <https://github.com/CederGroupHub/alabos> (MIT)
15. ALCHEMI Toolkit — <https://github.com/NVIDIA/nvalchemi-toolkit> (Apache 2.0)
16. NVIDIA Warp — <https://github.com/NVIDIA/warp> (BSD-3-Clause)
17. Materials Project API — <https://docs.materialsproject.org/>
