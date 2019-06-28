import os
from surgen.utils.file import find
from surgen.tests.utils import PROCEDURE_DIR


def test_find_file():
    """ finding a file should work as expected. """
    assert find(PROCEDURE_DIR, "01_example.py") == os.path.join(
        PROCEDURE_DIR, "01_example.py"
    )
    assert find(PROCEDURE_DIR, "oogabooga") is None
