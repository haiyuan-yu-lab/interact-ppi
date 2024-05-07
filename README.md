# INTERACT-PPI

**INTERACT-PPI** (INTErface Embedding and Representation for ACTive Protein-Protein Interactions) is a project to build protein representations that capture the key features of protein-protein interfaces (PPI) for downstream applications such as generative protein design and PPI prediction.

## Project Overview

### Project Schematics
To accomplish our project initiatives, we identify and extract interfaces from known protein-protein interactions for potential applications such as generating a target-specific binder with high confidence and accuracy and predicting the PPI interfaces. Based on these extracted interfaces, we envision constructing a pipeline mainly into three phases: feature extraction, representation construction, and neural network modeling.

![05_05 ML_subgroup meeting](https://github.com/haiyuan-yu-lab/interact-ppi/assets/35699839/1542712d-45bf-4a01-8b4d-67e53f1bef06)

#### Phase 1: Feature extraction
We first aim to compute the biophysical, geometric, and sequential features of interfaces to provide meaningful insights into their characteristics.

- **Sequence Features:** extracts residue-level features using Evolutionary Scale Modeling (ESM).
- **Biophysical features:** extract biophysical features such as dihedral angles and solvent accessible surface area (SASA) to gain insights about the structural stability and foldings of those interfaces.
- **Geometric features:** identifies the spatial orientation and translation vectors of proteins.
- **Normal Vectors:** gives the information about the position of the partner interfacing protein.

#### Phase 2: Representation construction
We then build a representation that captures those extracted features, using the following architectures and modelings:
- **Graph-Based Representation:** creates a graph representation whose nodes represent residues, and edges display relationships based on distance thresholds and interactions.
- **Compatibility Scores:** evaluates compatibility among residues to determine potential interacting pairs through contrastive learning.
- **Geodesic Embedding:** uses graph-based machine learning (U-Net, GNNs) methods to embed the residues with extracted information in a multidimensional space.


#### Phase 3: Neural network modeling



