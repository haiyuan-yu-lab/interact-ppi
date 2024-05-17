import torch
import esm
import h5py
import sys

sys.path.insert(1, '../module/')
from sequence_extractor import extract_sequences
from esm2_residue_extractor import *
import argparse

def main():

    parser = argparse.ArgumentParser(description="Extract embeddings of the residues in chains.")
    # Add arguments for users
    parser.add_argument('file_list_path', type=str, help ="Path to a text file containing paths to PDB or CIF files")
    
    args = parser.parse_args()

    
    with open(args.file_list_path, 'r') as file:
        file_paths = file.read().splitlines()

    for file_path in file_paths:
        file_path = file_path.strip()
        file_ext = file_path.split('/')[-1].split('.')[-1]
        protein_id = file_path.split('/')[-1].split('.')[0]

        sequence_dict = extract_sequences(file_path, 'all', file_ext, protein_id)
        
        data = convert_to_list_of_tuples(sequence_dict)
    
        
        model, alphabet = esm.pretrained.esm2_t6_8M_UR50D()
        batch_converter = alphabet.get_batch_converter()
        batch_labels, batch_strs, batch_tokens = batch_converter(data)
        batch_lens = (batch_tokens != alphabet.padding_idx).sum(1)
        model.eval()
        
        print(f"batch_lens: {batch_lens}")
        print('----------------------------------------------')
    
        output_embeddings, results = get_embeddings(data, model, batch_converter)
        print(output_embeddings)
        print('----------------------------------------------')
    
        write_h5(data, output_embeddings, protein_id)

        
        h5_embeddings = read_h5(protein_id +'.h5')



if __name__ == "__main__":
    main()
