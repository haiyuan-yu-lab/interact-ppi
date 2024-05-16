import sys
sys.path.append('../module/')

import argparse
from interface_residue_extractor import get_interface_residues

def main():
    parser = argparse.ArgumentParser(description='Extract Protein-Protein Interface Residues from multiple PDB files listed in a text file.')
    parser.add_argument('file_list_path', type=str, help='Path to a text file containing paths to PDB or CIF files')
    parser.add_argument('chain_ids', type=str, help='Comma-separated chain IDs to analyze, e.g., "A,B"')
    parser.add_argument('threshold', type=float, help='Distance threshold to define interface residues')

    args = parser.parse_args()

    chain_ids = args.chain_ids.split(',')

     
    if len(chain_ids) != 2:
        print("Error: You must provide two chain IDs, separated by a comma (e.g., A,B).")
        sys.exit(1)  

    
    with open(args.file_list_path, 'r') as file:
        file_paths = file.read().splitlines()

    for file_path in file_paths:
        file_path = file_path.strip()
        print(file_path)
        results = get_interface_residues(file_path, chain_ids, args.threshold)
        print(f'Results for {file_path}: {results}')

if __name__ == "__main__":
    main()

