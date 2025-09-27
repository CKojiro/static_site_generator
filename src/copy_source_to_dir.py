import os
import shutil

def copy_source_to_dir(source, destination):
    if os.path.exists(destination):
        for item in os.listdir(destination):
            item_path = os.path.join(destination, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Removed directory: {item_path}")
            else:
                os.remove(item_path)
                print(f"Removed file: {item_path}")
    else:
        os.makedirs(destination, exist_ok=True)

    def recursive_copy(src, dest):
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            dest_path = os.path.join(dest, item)
            if os.path.isdir(src_path):
                os.makedirs(dest_path, exist_ok=True)
                print(f"Creating directory: {dest_path}")
                recursive_copy(src_path, dest_path)
            else:
                shutil.copy2(src_path, dest_path)
                print(f"Copied file: {src_path} -> {dest_path}")
    recursive_copy(source, destination)
