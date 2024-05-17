# Extract residues in PPI-interface [ESM-2](https://github.com/facebookresearch/esm)

This module aims to extract residues that participate in PPI interfaces from given two chains, using ESM-2 Protein Language Model (PLM).  

## Implementation

We use a driver script defined in ```./driver/esm2_extract_residues.py``` to implement the functionality.

### Example

```bash
python3 esm2_extract_residues.py <filepath> <chain IDs>
```

## Arguments

- ```<filepath>```: Path to a textfile preferrably in a ```.txt``` or ```.tsv``` format, containing a list of the paths to PDB or MMCIF files, separated by newline characters. 
- ```<chain_ids>```: a list of two chains IDs that are input for scrutinizing residues in the PPI interface.

