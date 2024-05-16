import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '../module/')

from sequence_extractor import *
import argparse

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


