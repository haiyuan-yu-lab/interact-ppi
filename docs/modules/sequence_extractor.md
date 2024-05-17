# Sequence extraction by chains

Given the path of a PDB/MMCIF file and IDs of the chain, this function extract sequences that correspond to their chains. 

## Implementation

We use a driver script defined in ```./driver/extract_sequences.py``` to implement functions defined in this module. 

### Example

```bash
python3 extract_sequences.py <filepath> <chain IDs>
```

## Arguments

- ```<filepath>```: Path to a ```PDB``` or ``` MMCIF ``` file. 
- ```<chain_ids>```: a list of the chains in PDB/MMCIF.

