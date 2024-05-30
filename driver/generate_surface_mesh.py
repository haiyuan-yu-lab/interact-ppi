import sys
import os
import csv
sys.path.insert(1, '../module/')

from ppi_interface_surface_mesh_generator import *
from ppi_interface_residue_extractor import *
import argparse

def main(file):

    with open(file, 'r') as file:
        reader = csv.reader(file)
        lines = [line for line in reader]
    # Paths where we will save the surface mesh and structure
    out_dir = os.path.expanduser('../scratch/surface_mesh/')
    os.makedirs(out_dir, exist_ok = True)

    for line in lines:
        assert len(line) == 3, f"Each line must contain exactly three elements (file_path, chain_id1, chain_id2)"

        file_path, chain_id1, chain_id2 = line

        pdb_id = os.path.basename(file_path).split('.')[0]

        out_pdb_path = os.path.join(out_dir, f"{pdb_id}_interface.pdb")
        out_mesh_path = os.path.join(out_dir, f"{pdb_id}_mesh.vtu")

        try:
            chain_ids = [chain_id1, chain_id2]

            # Extract the interface residues
            interface_residues = process_pdb_file(file_path, chain_ids)

            # Generate surface mesh from the extracted interface residues
            interface_structure, interface_coords, triangles = generate_interface_surface_mesh(file_path, interface_residues, out_pdb_path, out_mesh_path)
        except Exception as e:
            print(f"Erorr processing {file_path}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Generate surface mesh for ppi-interface")

    parser.add_argument("file", help = "CSV file containing PDB file paths and chain IDs.")
    args = parser.parse_args()

    main(args.file)