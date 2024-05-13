def parse_pdb(file_path):
    file_ext = file_path.split('.')[-1]
    if file_ext.lower() == 'pdb':
        parser = PDBParser(QUIET=False)
    elif file_ext.lower() == 'cif':
        parser = MMCIFParser(QUIET=False)
    else:
        raise ValueError("Unsupported file format. Please use '.pdb' or '.cif' files.")
    return parser
