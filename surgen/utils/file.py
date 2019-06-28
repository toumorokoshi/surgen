import os
import typing


def find(root_dir: str, name: str) -> typing.Optional[str]:
    """
    recurse through the desired directory, and return a py.path.local
    object that matches that name.
    """
    for root, _, file_names in os.walk(root_dir):
        if name in file_names:
            return os.path.join(root, name)
