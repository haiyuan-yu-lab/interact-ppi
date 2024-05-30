import sys
import os

sys.path.insert(1, '../module/')

from ppi_interface_residue_extractor import *
import argparse


def main(pdb_list_file, chain_ids):
    interface_residues_all = {}
    with open(pdb_list_file, 'r') as file:
        pdb_files = [line.strip() for line in file]

    for pdb_file in pdb_files:
        try:
            interface_residues = process_pdb_file(pdb_file, chain_ids)
            interface_residues_all[pdb_file] = interface_residues
        except Exception as e:
            print(f"Error processing {pdb_file}: {e}")

  
    return interface_residues_all

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Identify protein-protein interface residues.")
    parser.add_argument("pdb_list_file", help="Text file containing list of the paths to PDB or MMCIF files.")
    parser.add_argument("chain_ids", help="Comma-separated list of chain IDs to process (e.g., A,B).")
    args = parser.parse_args()

    chain_ids = args.chain_ids.split(',')
    interface_residues_all = main(args.pdb_list_file, chain_ids)