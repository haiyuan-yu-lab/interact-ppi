import os
import meshio
from util import *

def extract_interface_structure(file_path, interface_residues):
    """
    Extracts the PPI-interface of a given structure and generates the surface mesh.

    Parameters:
    file_path (str): The file path to a structure (PDB/MMCIF).
    interface_residues (dict): Dictionary whose keys are chain IDs and values are their sequences of the interface residues.

    Returns:
    Extracted structure (Structure) and surface mesh (numpy array).
    """
    # Validate the PDB or MMCIF file
    pdb_id = os.path.basename(file_path).split('.')[0]

    # Parse the structure file using the utility function
    parser = parse_pdb(file_path)
    structure = parser.get_structure(pdb_id, file_path)

    # Extract interface residues
    interface_res_atoms = []
    interface_structure = PDB.Structure.Structure(pdb_id + "-ppi")
    model = PDB.Model.Model(0)
    interface_structure.add(model)

    for chain_id, sequence in interface_residues.items():
        chain = structure[0][chain_id]
        chain_pdb = PDB.Chain.Chain(chain_id)
        seq_position = 0

        for residue in chain:
            if is_aa(residue, standard=True):
                res = residue.resname
                print(f"Residue: {res}")
                aa = aa_mapping.get(res)
                if aa and aa==sequence[seq_position]:
                    chain_pdb.add(residue.copy())
                    # Append atom coordinates
                    for atom in residue:
                        interface_res_atoms.append(atom.get_coord())
                    seq_position += 1

                if seq_position >= len(sequence):
                    break

        model.add(chain_pdb)

    # Conduct validation checks on identifying interface atoms.
    assert interface_res_atoms, "No interface atoms identified. Please check your list of the interface residues."
    # Convert the atomic coordinates into Numpy array
    interface_coords = np.array(interface_res_atoms)

    '''
    # Generate surface mesh using MeshPy
    mesh_info = MeshInfo()
    mesh_info.set_points(interface_coords)
    mesh_info.set_facets([[i for i in range(len(interface_coords))]])
    mesh = build(mesh_info)
    '''
    # Generate convex hull for the interface atoms to get surface triangles
    hull = ConvexHull(interface_coords)
    triangles = hull.simplices
    print("Interface coordinates: ", interface_coords)
    print("Triangles: ", triangles)
    return interface_structure, interface_coords, triangles


def save_structure(structure, out_file):
    """
    Saves a structure to a PDB file.

    Parameters:
    structure (Structure): a structure to be loaded to output the PDB file.
    out_file (str): a path where we output the PDB file.
    """

    pdb_io = PDB.PDBIO()
    pdb_io.set_structure(structure)
    pdb_io.save(out_file)


def save_mesh(points, triangles, out_file):
    """
    Saves the surface mesh to a file.

    Parameters:
    mesh (MeshInfo): The surface mesh to be saved.
    out_file (str): The path where we want the mesh to be saved.
    """

    cells = [("triangle", triangles)]
    mesh = meshio.Mesh(points, cells)
    meshio.write(out_file, mesh)

def generate_interface_surface_mesh(file_path, interface_residues, out_file, out_mesh):

    """
    Generates the surface mesh from the residues that participate in forming the PPI-interface.

    Parameters:
    file_path (str): The file path of the PDB/MMCIF structure
    interface_residues (dict): Dictionary of interface
    out_file (str): The file path to save the interface
    out_mesh (str): The file path to save the surface mesh

    Returns:
    interface_structrue (Structure) and surface mesh (MeshInfo) to be saved.
    """

    # Generate interface and suface mesh
    interface_struct, interface_coords, triangles = extract_interface_structure(file_path, interface_residues)

    # Save the extracted ppi-interface & surface mesh to a new PDB
    save_structure(interface_struct, out_file)
    save_mesh(interface_coords, triangles, out_mesh)

    return interface_struct, interface_coords, triangles