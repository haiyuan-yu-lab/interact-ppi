from Bio.PDB import PDBParser, MMCIFParser
import numpy as np
from Bio.PDB.Polypeptide import is_aa

def parse_pdb(file_path):
    file_ext = file_path.split('.')[-1]
    if file_ext.lower() == 'pdb':
        parser = PDBParser(QUIET=False)
    elif file_ext.lower() == 'cif':
        parser = MMCIFParser(QUIET=False)
    else:
        raise ValueError("Unsupported file format. Please use '.pdb' or '.cif' files.")
    return parser

def find_ca_distance(residue1, residue2):
    '''
    Helper function to compute the distances between alpha carbons of given residues.

    Args:
    residue1 (Residue): A residue from the first chain in the list of chain IDs.
    residue2 (Residue): A residue from the second chain in the list of chain IDs.

    Returns: A Euclidean distance between those residues.
    '''
    ca_1 = residue1["CA"].get_coord()
    ca_2 = residue2["CA"].get_coord()
    distance = np.linalg.norm(ca_1 - ca_2)
    return distance
