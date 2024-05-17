# Extract residues in PPI-interface (Euclidean distance)

This module includes functions to extract residues that participate in PPI interfaces. Specifically, this module aims to extract residues from two chains that form ppi-interface within a given threshold. 

## Implementation

We use a driver script defined in ```./driver/extract_interacting_residues.py``` to implement functions defined in this module. 

### Example

```bash
python3 extract_interacting_residues.py <filepath> <chain IDs> <distance threshold>
```

## Arguments

- ```<filepath>```: Path to a textfile preferrably in a ```.txt``` or ```.tsv``` format, containing a list of the paths to PDB or MMCIF files, separated by newline characters. 
- ```<chain_ids>```: a list of two chains IDs that are input for scrutinizing residues in the PPI interface.
- ```<distance threshold>```: The maximum distance in Angstroms between pairwise residues in input chains to consider them as part of the PPI-interface.
