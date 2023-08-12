import os

def set_permissions(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.sh'):
                filepath = os.path.join(dirpath, filename)
                os.chmod(filepath, 0o400)  

if __name__ == "__main__":
    current_directory = os.getcwd()
    set_permissions(current_directory)