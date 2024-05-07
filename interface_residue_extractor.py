from Bio.PDB import PDBParser, MMCIFParser, Polypeptide
import numpy as np

'''
This module defines functions to extract residues from each chain that are parts of the protein-protein interaction.
'''

def parse_pdb(file_path):
    file_ext = file_path.split('.')[-1]
    if file_ext.lower() == 'pdb':
        parser = PDBParser(QUIET=False)
    elif file_ext.lower() == 'cif':
        parser = MMCIFParser(QUIET=False)
    else:
        raise ValueError("Unsupported file format. Please use '.pdb' or '.cif' files.")
    return parser

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

def find_ca_distance(residue1, residue2):
    '''
    Helper function to compute the distances between alpha carbons of given residues.

    Args:
    residue1 (Residue): A residue from the first chain in the list of chain IDs.
    residue2 (residue): A residue from the second chain in the list of chain IDs.

    Returns: A Euclidean distance between those residues.
    '''
    ca_1 = residue1["CA"].get_coord()
    ca_2 = residue2["CA"].get_coord()
    distance = np.linalg.norm(ca_1 - ca_2)
    return distance

