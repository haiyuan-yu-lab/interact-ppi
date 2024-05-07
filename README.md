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
With the graph-based representations designed in Phase 2, we will construct a neural network model to enable geodesic embeddings of residue features into a high-dimensional vector spaces that capture interaction patterns among them. So far, we have envisioned using the following architectures, but this is to be determined in the future.
-  **U-Net**
-  **GNN**


## Requirements
To run the programs for INTERACT-ppi models, you need to install the following libraries and software.

### Software & Libraries
- **Python:** Any 3.x Python version works, but the latest versino is preferrable. You can download it [here](https://www.python.org/downloads)
- **pip:** Check this [reference](https://pip.pypa.io/en/stable/installation/) to install this Python package installer.
- **biopython**: Once ``` pip ``` package is intalled, install the Biopython library using the command ``` pip install biopython ```.


### Module Descriptions
1. **`extract_interacting_residues.py`**
   - Driver script to extract residues participating in PPI interfaces using the functions defined in `interface_residue_extractor.py`.
   
   - **Program implementation example**
     ```bash
     python3 extract_interacting_residues.py <filepath> <chain IDs> <distance threshold>
     ```
   - **Arguments**
     - **`<filepath>`:** Path to a text file in a .txt or .tsv format, containing a list of the paths to PDB or MMCIF files, separated by newline characters.
     - **`<chain IDs>`:** a list of two chain IDs that are to be analyzed for PPI (e.g., "A,B").
     - **`<distance threshold>`:** The maximum distance (in Angstroms) between residues in given chains to consider them as part of a PPI interface.

2. **`interface_residue_extractor.py`**
   - Defines modules to extract residues in two chains within a PDB or MMCIF that form interactions based on a given distance threshold.


3. **`extract_sequences.py`**
   - Extracts sequences from a PDB or MMCIF file for given chains.

   - **Program Implementation example:**
     ```bash
     python3 extract_sequences.py <file_path> <chain_ids>
     ```
   - **Arguments**
     - **`<filepath>`:** a path to a PDB or MMCIF file in a .pdb or .cif format.
     - **`<chain_ids>`:** a list of the chain IDs, separated by commas, for getting the sequences in corresponding chains (e.g., "A,B"). Or, if user wants to get the sequence in every chain, then ``` -a ``` keyword can be used instead of the comma-separated list of chain IDs.


