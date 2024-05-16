import h5py

with h5py.File('/home/jc981073/interact-ppi/output_embeddings.h5', 'r') as file:
    # List all groups
    print("Keys: %s" % file.keys())
    a_group_key = list(file.keys())[0]

    # Get the data
    data = list(file[a_group_key])
    print(data)

