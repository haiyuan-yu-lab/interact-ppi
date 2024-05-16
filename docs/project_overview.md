# Project Overview

## Project Schematics

To accomplish our project initiatives, we identify and extract interfaces from known protein-protein interactions for potential applications such as generating a target-specific binder with high confidence and accuracy and predicting the PPI interfaces. Based on these extracted interfaces, we envision constructing a pipeline mainly into three phases: feature extraction, representation construction, and neural network modeling.

<!-- Need a very sophisticated drawing of our project schematics-->


### Phase 1: Feature extraction

We first aim to compute the biophysical, geometric, and sequential features of interfaces to provide meaningful insights into their characteristics.

- **Sequence Features:** extracts residue-level features using Evolutionary Scale Modeling (ESM).
- **Biophysical features:** extract biophysical features such as dihedral angles and solvent accessible surface area (SASA) to gain insights about the structural stability and foldings of those interfaces.
- **Geometric features:** identifies the spatial orientation and translation vectors of proteins.
- **Normal Vectors:** gives the information about the position of the partner interfacing protein.

### Phase 2: Representation construction

We then build a representation that captures those extracted features, using the following architectures and modelings:

- **Graph-Based Representation:** creates a graph representation whose nodes represent residues, and edges display relationships based on distance thresholds and interactions.
- **Compatibility Scores:** evaluates compatibility among residues to determine potential interacting pairs through contrastive learning.
- **Geodesic Embedding:** uses graph-based machine learning (U-Net, GNNs) methods to embed the residues with extracted information in a multidimensional space.

### Phase 3: Neural network modeling

With the graph-based representations designed in Phase 2, we will construct a neural network model to enable geodesic embeddings of residue features into a high-dimensional vector spaces that capture interaction patterns among them. So far, we have envisioned using the following architectures, but this is to be determined in the future.

-  **U-Net**
-  **GNN**
