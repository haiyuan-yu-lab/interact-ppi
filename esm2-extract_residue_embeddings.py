import torch
import esm
import h5py
from Bio import PDB
from util import *

# Load the ESM-2 model
model, alphabet = esm.pretrained.esm2_t6_8M_UR50D()
model.eval()

def extract_pdb_sequence(pdb_path):
    """Extract sequences from a PDB file."""
    parser = parse_pdb(pdb_path)
    structure = parser.get_structure('PDB', pdb_path)
    for model in structure:
        for chain in model:
            yield ''.join([residue.resname for residue in chain.get_residues() if PDB.is_aa(residue, standard=True)]), chain.id

def get_embeddings(sequence):
    """Convert amino acid sequence to embedding using the ESM-2 model."""
    data = [("seq", sequence)]
    batch_labels, batch_strs, batch_tokens = alphabet.get_batch_converter()(data)
    with torch.no_grad():
        results = model(batch_tokens, repr_layers=[6])
        token_representations = results['representations'][6]
    return token_representations.squeeze(0).numpy()

def save_embeddings_to_hdf5(embeddings, file_path, chain_id):
    """Save embeddings to an HDF5 file."""
    with h5py.File(file_path, 'a') as h5f:
        h5f.create_dataset(chain_id, data=embeddings)

def main(pdb_file, output_file):
    for sequence, chain_id in extract_pdb_sequence(pdb_file):
        embeddings = get_embeddings(sequence)
        save_embeddings_to_hdf5(embeddings, output_file, chain_id)
        print(f"Embeddings for chain {chain_id} saved.")

if __name__ == "__main__":
    import sys
    pdb_file = sys.argv[1]  # Command line argument for PDB file path
    output_file = "output_embeddings.h5"  # Default output file
    main(pdb_file, output_file)

