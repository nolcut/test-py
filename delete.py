def print_and_delete(folder, filename):
    FaaSr_py.faasr_get_file(local_file=filename, remote_file=filename, remote_folder=folder)
    with open(f"/tmp/{filename}", 'r') as f:
        print(f"downloaded content: {f.readline()}")
    faasr_delete_file(remote_file=filename, remote_folder=folder)
    print("file deleted")
