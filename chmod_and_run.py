import os
import subprocess

def execute_scripts(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.sh'):
                script_path = os.path.join(dirpath, filename)
                
                if not os.access(script_path, os.X_OK):
                    os.chmod(script_path, 0o400)
                
                subprocess.run(['bash', script_path])

if __name__ == "__main__":
    current_directory = os.getcwd()
    execute_scripts(current_directory)
