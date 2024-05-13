from Bio.PDB import PDBParser, MMCIFParser 
import argparse
import os
from Bio.PDB.Polypeptide import is_aa

def extract_sequences(file_path, chain_ids, file_ext, protein_id):
    '''
    Extract sequences that correspond to given chains. 

    Args:

    file_path (str): path of a PDB or MMCIF file
    chain_ids (str): a list of the chain IDs
    file_ext (str): type of the file (e.g. pdb or cif)
    protein_id (str): a label for the protein structure
    '''
    parser = MMCIFParser() if file_ext == 'cif' else PDBParser()

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


def main():
    
    parser = argparse.ArgumentParser(description="Extract sequences for given chains from a PDB/MMCIF file.")
    parser.add_argument('file_path', type=str, help="Path to the PDB or MMCIF file")
    parser.add_argument('chain_ids', nargs='?', default=None, help="Comma-separated chain IDs for extracting denoted chains.")
    parser.add_argument('-a', action='store_true', help = "Use this flag to extract sequences from every chain")

    args = parser.parse_args()

    # Validate the file path and chain IDs
    if not validate_filepath(args.file_path):
        return

    file_ext = args.file_path.split('.')[-1].lower()
    protein_id = os.path.basename(args.file_path).split('.')[0]

    if args.a:
        chain_ids = 'all'
    elif args.chain_ids:
        chain_ids = args.chain_ids.split(',')  # Directly split by commas if chain IDs are provided
    else:
        print("Error: Provide specific chain IDs or use '-a' flag to extract sequences from all chains.")
        return

    if not validate_chain_ids(chain_ids):
        return

    chain_sequences = extract_sequences(args.file_path, chain_ids, file_ext, protein_id)

    # Feel free to comment out the following lines
    for chain, seq in chain_sequences.items():
        print(f"Chain {chain}: {seq}")




if __name__ == "__main__":
    main()


