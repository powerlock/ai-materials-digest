# AI/ML models for materials discovery — cloud usage examples

Most modern foundation interatomic potentials and generative models are too large or too GPU-dependent to run comfortably on a laptop. The examples below are designed for **Google Colab (free T4 GPU)**, **Kaggle Notebooks**, or a **Hugging Face Space / inference API**. Each snippet installs the package in one cell and runs a minimal prediction in the next.

## Picking a platform

| Platform | GPU | Use case |
|---|---|---|
| **Google Colab** | Free T4 (paid A100/L4) | Quick experiments, one-click notebooks |
| **Kaggle** | Free T4 x2 / P100 | Longer runs, more RAM |
| **Hugging Face** | Inference API or Spaces | Hosting a model, calling via API, no install |

For all three, start with `Runtime → Change runtime type → GPU` (Colab/Kaggle) or select a GPU Space type on Hugging Face.

---

## 1. MACE (MACE-MP-0 / MACE-MPA-0)

Install and run a single energy/force prediction on a molecule or bulk structure.

### Colab / Kaggle cell 1: install

```bash
pip install --upgrade pip
pip install mace-torch
```

### Colab / Kaggle cell 2: ASE calculator example

```python
from ase import build
from mace.calculators import mace_mp

# Load the pretrained Materials Project MACE model
calc = mace_mp(model="medium-mpa-0", device="cuda")

atoms = build.bulk("Si", "diamond", a=5.43)
atoms.calc = calc

print("Energy (eV):", atoms.get_potential_energy())
print("Forces (eV/A):", atoms.get_forces())
```

- Official Colab: https://colab.research.google.com/drive/1D6EtMUjQPey_GkuxUAbPgld6_9ibIa-V
- Docs: https://mace-docs.readthedocs.io/
- Notes: the `mace-torch` package is the one from the MACE authors; a different `mace` package on PyPI is unrelated.

---

## 2. CHGNet

CHGNet is small enough for CPU but much faster on GPU. Good for quick tests.

### Colab / Kaggle cell 1: install

```bash
pip install chgnet
```

### Colab / Kaggle cell 2: predict energy, forces, stress, magmoms

```python
from pymatgen.core import Structure, Lattice
from chgnet.model import CHGNet

# Load pretrained CHGNet
chgnet = CHGNet.load()

# Build a simple LiMnO2-ish structure
structure = Structure(
    Lattice.cubic(4.0),
    ["Li", "Mn", "O", "O"],
    [[0,0,0], [0.5,0.5,0.5], [0.5,0,0.5], [0,0.5,0.5]]
)

prediction = chgnet.predict_structure(structure)
print("Energy:", prediction["e"])
print("Forces:", prediction["f"])
print("Stress:", prediction["s"])
print("Magmoms:", prediction["m"])
```

- GitHub: https://github.com/CederGroupHub/chgnet
- Example notebook: https://colab.research.google.com/github/CederGroupHub/chgnet/blob/main/examples/basics.ipynb

---

## 3. MatterSim (Microsoft)

MatterSim provides an ASE-compatible calculator.

### Colab / Kaggle cell 1: install

```bash
pip install mattersim
```

### Colab / Kaggle cell 2: ASE calculator

```python
import torch
from ase.build import bulk
from mattersim.forcefield import MatterSimCalculator

device = "cuda" if torch.cuda.is_available() else "cpu"

si = bulk("Si", "diamond", a=5.43)
si.calc = MatterSimCalculator(device=device)

print("Energy (eV):", si.get_potential_energy())
print("Forces (eV/A):", si.get_forces()[:2])
```

- Docs: https://microsoft.github.io/mattersim/user_guide/getting_started.html
- Notes: installation can be slow; use a fresh `python=3.12` environment if you install locally.

---

## 4. SevenNet

SevenNet is designed for molecular dynamics; the Python API also supports single-point evaluation.

### Colab / Kaggle cell 1: install

```bash
pip install sevenn
```

### Colab / Kaggle cell 2: ASE calculator

```python
import torch
from ase.build import bulk
from sevenn.calculator import SevenNetCalculator

device = "cuda" if torch.cuda.is_available() else "cpu"

atoms = bulk("Si", "diamond", a=5.43)
# Load the default pretrained SevenNet-0 model
atoms.calc = SevenNetCalculator(model="7net-0", device=device)

print("Energy (eV):", atoms.get_potential_energy())
print("Forces (eV/A):", atoms.get_forces()[:2])
```

- Docs: https://sevennet.readthedocs.io/
- Tutorial notebook: https://github.com/MDIL-SNU/sevennet_tutorial
- Notes: set `Runtime → T4 GPU` for reasonable MD speed.

---

## 5. ORB (Orbital Materials)

ORB models can be installed from PyPI and used directly or through an ASE calculator.

### Colab / Kaggle cell 1: install

```bash
pip install orb-models
```

### Colab / Kaggle cell 2: direct prediction

```python
import ase
from ase.build import bulk
from orb_models.forcefield import pretrained

# Load a pretrained ORB v3 model
orbff, atoms_adapter = pretrained.orb_v3_conservative_inf_omat(device="cuda")

atoms = bulk("Cu", "fcc", a=3.58, cubic=True)
graph = atoms_adapter.from_ase_atoms(atoms, device="cuda")
result = orbff.predict(graph, split=False)

print("Energy (eV):", result["energy"].item())
print("Forces shape:", result["forces"].shape)
print("Stress shape:", result["stress"].shape)
```

- GitHub: https://github.com/orbital-materials/orb-models
- Notes: if you prefer an ASE interface, use `from orb_models.forcefield.calculator import ORBCalculator`.

---

## 6. DeePMD-kit

DeePMD-kit is primarily a training and inference engine for deep potential MD. It is heavier to install and more suited to Kaggle or a Colab paid tier.

### Colab / Kaggle cell 1: install (PyTorch backend, CPU or GPU)

```bash
pip install deepmd-kit[torch]
```

### Colab / Kaggle cell 2: check install and list models

```bash
dp --version
```

- Docs: https://docs.deepmodeling.com/projects/deepmd/
- Notes: use `deepmd-kit[cpu]` for a smaller install if you do not need CUDA. Pretrained checkpoints are usually model-specific; most users train their own on a small DFT dataset.

---

## 7. Hugging Face inference pattern

If a model is published on Hugging Face (or the authors host a Space), you can call it without installing anything:

```python
from huggingface_hub import hf_hub_download
import torch

# Example: download a checkpoint and load with the model's own loader
checkpoint = hf_hub_download(repo_id="your-org/your-model", filename="model.pt")
# then load with the appropriate model class
```

Not every materials model is on Hugging Face yet. For the ones above, the recommended route is still `pip install` in Colab/Kaggle.

---

## General Colab/Kaggle workflow

1. Start a new notebook.
2. `Runtime → Change runtime type → GPU`.
3. Run `!pip install <package>` in the first cell.
4. Restart the runtime if the install prints a warning about numpy/PyTorch incompatibilities.
5. Run the example code in the next cells.
6. Monitor GPU memory: `!nvidia-smi`.

---

## Notes and caveats

- **Device**: the snippets default to `cuda` when available. In Colab, set this explicitly or the code will be extremely slow.
- **Memory**: models like MACE-MPA-0 and ORB can exceed the 15 GB free Colab GPU RAM for large supercells. Reduce the system size first.
- **Commercial clouds**: Colab Pro, Colab Pro+, Kaggle, and Hugging Face Pro give more reliable GPUs and longer runtimes.
- **No guarantees**: the exact package names and model versions change. If a cell fails, check the repository's `README.md` for the latest install command.
