import os
import py

def find(root_dir, name):
    """
    recurse through the desired directory, and return a py.path.local
    object that matches that name.
    """
    for root, _, file_names in os.walk(root_dir):
        if name in file_names:
            return py.path.local(os.path.join(root, name))
