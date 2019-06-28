from typing import List, Tuple


def replace(substitutions: List[Tuple[str, str]], contents: str) -> str:
    """ 
    apply substitutions to a string, returning the result.
    """
    for string_to_replace, replacement_string in substitutions:
        contents = contents.replace(string_to_replace, replacement_string)
    return contents


def remove(removals: List[str], contents: str) -> str:
    """ 
    remove the specified strings from the contents, returning
    the result
    """
    for r in removals:
        contents = contents.replace(r, "")
    return contents


def insert(injections: List[str], contents: str) -> str:
    """
    inject the provided list of strings into the top
    of the document.
    """
    header = "\n".join(injections) + "\n"
    return header + contents
