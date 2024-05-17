import torch
import esm
import h5py
from util import *
from Bio import PDB
from sequence_extractor import extract_sequences
import matplotlib.pyplot as plt


def convert_to_list_of_tuples(sequence):
    '''
    helper function to convert a sequence dictionary to a data structure used in the example code https://pypi.org/project/fair-esm/0.1.1/
    '''
    aa_list = []

    for chain_id in sequence:
        seq = sequence[chain_id]
        aa_list.append((chain_id, seq))
    return aa_list

def generate_per_seq_embeddings(data, batch_labels, token_embeddings):
    # Generate per-sequence embeddings
    sequence_embeddings = []
    for chain_id in [chain[0] for chain in data]:  # Extract chain IDs from data
        chain_start_idx = batch_labels.index(chain_id)
        chain_end_idx = chain_start_idx + len([chain[1] for chain in data if chain[0] == chain_id])
        chain_embeddings = token_embeddings[chain_start_idx:chain_end_idx].mean(0)
        sequence_embeddings.append(chain_embeddings.numpy())
    return sequence_embeddings

def get_embeddings(data, model, batch_converter): # sequence : {'A': ABCDE, 'B': AMKSH,...}
    
    batch_labels, batch_strs, batch_tokens = batch_converter(data)

    # Extract per-residue embeddings (on CPU)
    with torch.no_grad():
        results = model(batch_tokens, repr_layers=[6], return_contacts=True)
    token_embeddings = results["representations"][6]

    # Generate per-sequence embeddings 

    sequence_embeddings = generate_per_seq_embeddings(data, batch_labels, token_embeddings)

    return sequence_embeddings, results

def write_h5(data, sequence_embeddings, protein_id):
    output_file = protein_id + ".h5"

    # Write embeddings to HDF5 file
    with h5py.File(output_file, 'w') as file:
        for i, chain_id in enumerate([chain[0] for chain in data]):  # Extract chain IDs from data
            file.create_dataset(f'{chain_id}', data=sequence_embeddings[i])


def read_h5(file_path):

    embeddings = {}
    with h5py.File(file_path, 'r') as hf:
        for key in hf.keys():
            embeddings[key] = np.array(hf[key])
    
    print(type(embeddings))
    # Investigate the contents
    for key, value in embeddings.items():
        print(f"Chain ID: {key}")
        print(f"Shape of embeddings: {value.shape}")
        print(f"Embeddings: {value}")


    return embeddings

def main():
    
    pdb_path = '/home/jc981073/interact-ppi/scratch/5ewz.pdb'
    chain_ids = ['A','B']
    file_ext = 'pdb'
    protein_id = '5ewz'

    sequence_dict = extract_sequences(pdb_path, chain_ids, file_ext, protein_id)
    data = convert_to_list_of_tuples(sequence_dict)
    print(f"chain A: {len(data[0][1])}")
    print(f"chain B: {len(data[1][1])}")
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

    h5_file = '5ewz.h5'

    h5_embeddings = read_h5(h5_file)
    


if __name__ == "__main__":
    main()
