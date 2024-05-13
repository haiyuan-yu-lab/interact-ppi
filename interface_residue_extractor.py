from Bio.PDB import PDBParser, MMCIFParser, Polypeptide
import numpy as np
from util import *


'''
This module defines functions to extract residues from each chain that are parts of the protein-protein interaction.
'''
def get_interface_residues(file_path, chain_ids, threshold):
    '''
    Identify residues in given chain IDs that form a PPI within the given distance threshold.

    Args:
    file_path (str): A path of the PDB or MMCIF file.
    chain_ids (list): a list of two chain IDs.
    threshold (float): A threshold of the distance between residues to consider them as parts of the PPI interface.

    Returns:
    a dictionary that contains the indices of the residues in each chain that are parts of the PPI.
    '''

    parser = parse_pdb(file_path)
    pdb_id = file_path.split('/')[-1].split('.')[0]
    structure = parser.get_structure(pdb_id, file_path)

    try:
        chain1 = structure[0][chain_ids[0]]
        chain2 = structure[0][chain_ids[1]]
    except KeyError:
        return {chain_ids[0]: [], chain_ids[1]: []}

    interface_residues = {chain_ids[0]: set(), chain_ids[1]: set()}
    for residue1 in chain1:
        for residue2 in chain2:
            if Polypeptide.is_aa(residue1) and Polypeptide.is_aa(residue2):
                min_distance = find_ca_distance(residue1, residue2)
                if min_distance <= threshold:
                    interface_residues[chain_ids[0]].add(residue1.id[1])
                    interface_residues[chain_ids[1]].add(residue2.id[1])
    return {key: sorted(value) for key, value in interface_residues.items()}


