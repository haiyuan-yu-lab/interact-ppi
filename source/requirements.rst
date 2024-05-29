Requirements
============

Below outlines all the necessary Python & other libraries and utilities 

Python Libraries
----------------

To enable the program defined within this repository, please install several Python libraries and external tools. Here’s a comprehensive list of the required installations:

- **Biopython** for handling PDB files and structures::

    pip install biopython

- **numpy** for various numerical operations::

    pip install numpy

- **scipy** for the ConvexHull function::

    pip install scipy

- **meshio** for reading and writing mesh files::

    pip install meshio

- **pdb-tools** for manipulating PDB files::

    pip install pdb-tools

- **torch** to enable using the ESM model (fair-esm)::

    pip install torch

- **fair-esm** for using the ESM model::

    pip install fair-esm

- **h5py** for using HDF5 file I/O functions::

    pip install h5py

- **matplotlib** for plotting the results::

    pip install matplotlib

External Tools
--------------

NACCESS: This is a tool for calculating accessible surface areas of proteins. It needs to be downloaded and installed separately. You can find it `here <http://wolf.bms.umist.ac.uk/naccess/>`_.

Utility Functions
-----------------

Ensure that your utility functions (`parse_pdb`, `aa_mapping`, `is_aa`, `extract_sequences`) are properly defined in a module named `util.py` and `sequence_extractor.py`.

Additional Steps
----------------

NACCESS Installation: Download and follow the installation instructions for NACCESS from `here <http://wolf.bms.umist.ac.uk/naccess/>`_.

Utility Functions: Ensure that your `util.py` and `sequence_extractor.py` files are correctly placed in the same directory as your main script or in the Python path.

Summary of Required Installations
---------------------------------

- **Python Libraries**: Install via pip install commands provided above.
- **External Tool (NACCESS)**: Install manually from the provided link.

Once everything is set up, you can run your scripts as usual, ensuring that you provide the correct file paths and parameters required by your functions.
