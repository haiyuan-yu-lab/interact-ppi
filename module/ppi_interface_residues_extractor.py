import os
import subprocess
from util import *
from sequence_extractor import extract_sequences

def run_naccess(pdb_file, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Change to the output directory to run NACCESS
    os.chdir(output_dir)

    # Run NACCESS
    command = f"naccess {os.path.basename(pdb_file)}"
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    os.chdir(original_dir)

    if result.returncode != 0:
        print(f"NACCESS failed for {pdb_file}. Error: {result.stderr.strip()}")
        raise RuntimeError(f"NACCESS failed for {pdb_file}. Please check the file format and contents.")

    # Check if the expected RSA file was generated
    rsa_file = os.path.join(output_dir, os.path.basename(pdb_file).replace('.pdb', '.rsa'))
    if not os.path.exists(rsa_file):
        raise FileNotFoundError(f"RSA file {rsa_file} not found for {pdb_file}")
    return rsa_file

def parse_rsa_file(rsa_filename):
    sasa_data = {}
    print(f"Reading RSA file: {rsa_filename}")
    try:
        with open(rsa_filename, 'r') as file:
            for line in file:
                if line.startswith('RES'):
                    parts = line.split()
                    residue = parts[1]
                    chain = parts[2]
                    res_num = parts[3]
                    asa = float(parts[4])
                    rsa = float(parts[5])
                    sasa_data[(chain, res_num)] = {'residue': residue, 'asa': asa, 'rsa': rsa}
    except Exception as e:
        print(f"Error reading RSA file {rsa_filename}: {e}")
    return sasa_data

def identify_interface_residues(isolated_sasa, complex_sasa, rsa_threshold=15.0, asa_decrease=1.0):
    interface_residues = {}
    for key, iso_data in isolated_sasa.items():
        if key in complex_sasa:
            com_data = complex_sasa[key]
            if iso_data['rsa'] >= rsa_threshold and (iso_data['asa'] - com_data['asa']) >= asa_decrease:
                chain = key[0]
                if chain not in interface_residues:
                    interface_residues[chain] = []
                interface_residues[chain].append(aa_mapping.get(iso_data['residue'], '?'))
    return interface_residues

def split_pdb_by_chain(pdb_file, chain_ids):
    for chain_id in chain_ids:
        output_file = f"{os.path.splitext(pdb_file)[0]}_chain{chain_id}.pdb"
        command = f"pdb_selchain -{chain_id} {pdb_file} > {output_file}"
        print(f"Running command: {command}") # pdb_selchain -A /home/jc981073/interact-ppi/scratch/5ewz.pdb > /home/jc981073/interact-ppi/scratch/5ewz_chainA.pdb
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        out_id = output_file.split('.')[0]


def process_pdb_file(pdb_file, chain_ids):
    pdb_id = os.path.basename(pdb_file).split('.')[0]
    file_ext = pdb_file.split('.')[-1].lower()

    sequences = extract_sequences(pdb_file, chain_ids, file_ext, pdb_id)

    split_pdb_by_chain(pdb_file, chain_ids)

    isolated_rsa_files = []
    for chain_id in chain_ids:
        chain_pdb_file = f"{os.path.splitext(pdb_file)[0]}_chain{chain_id}.pdb"
        print(f"Running NACCESS for chain {chain_id} PDB file: {chain_pdb_file}")
        rsa_file = run_naccess(chain_pdb_file, os.path.dirname(pdb_file))
        isolated_rsa_files.append(rsa_file)

    print(f"Running NACCESS for complex PDB file: {pdb_file}")
    complex_rsa_file = run_naccess(pdb_file, os.path.dirname(pdb_file))

    isolated_sasa = {}
    for rsa_file in isolated_rsa_files:
        isolated_sasa.update(parse_rsa_file(rsa_file))

    complex_sasa = parse_rsa_file(complex_rsa_file)

    return identify_interface_residues(isolated_sasa, complex_sasa)