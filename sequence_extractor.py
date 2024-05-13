import os
from Bio.PDB.Polypeptide import is_aa
from util import *

def extract_sequences(file_path, chain_ids, file_ext, protein_id):
    '''
    Extract sequences that correspond to given chains. 

    Args:

    file_path (str): path of a PDB or MMCIF file
    chain_ids (str): a list of the chain IDs
    file_ext (str): type of the file (e.g. pdb or cif)
    protein_id (str): a label for the protein structure
    '''
    parser = parse_pdb(file_path)

    structure = parser.get_structure(protein_id, file_path)

    sequences = {}

    for model in structure:
        for chain in model:
            if chain_ids == 'all' or chain.id in chain_ids:
                # residue.id[0] indicates 'hetfield'. If 'hetfield' is an empty space, then we can define that the residue is a standard AA.
                sequence = ''.join([residue.resname for residue in chain.get_residues() if is_aa(residue)])
                sequences[chain.id] = sequence

                if not sequence:
                    print(f"Warning: Chain {chain.id} is an empty sequence.")
    return sequences



def validate_filepath(file_path):
    '''
    Helper function to check the validity of the user-input filepath.

    Args:

    file_path (str): a path of a PDB or MMCIF file.

    Returns:

    True if the file exists in a correct format.
    False otherwise
    '''
    if not os.path.isfile(file_path):
        print(f"File does not exist in {file_path}")
        return False
    
    file_ext = file_path.split('.')[-1].lower()

    if file_ext not in ['pdb', 'cif']:
        print(f"Error: Unsupported file format. Please use either .pdb or .cif format.")
        return False
    return True


def validate_chain_ids(chain_ids):
    '''
    Helper function to check the validity of the user-input chain IDs. 

    Args:
    
    chain_ids (str): a list of the chains separated by commas or denoted with the keyword '-a'.

    True if chain IDs are correctly formatted.
    False otherwise
    '''
    if chain_ids == 'all':
        return True

    try:
        chain_ids = [chain_id.strip() for chain_id in chain_ids]

        for chain_id in chain_ids:
            if not chain_id:
                return False
    except Exception as e:
        print(f"Error: Please ensure that chain IDs are typed in a right format.{e}")
        return False


    return True




