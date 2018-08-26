from surgen.surgen import _procedures_from_dir
from .utils import PROCEDURE_DIR


def test_procedures_in_lexical_order():
    """ procedures should return back in lexical order. """
    procedures = _procedures_from_dir(PROCEDURE_DIR)
    procedure_file_list = list(procedures.keys())
    assert procedure_file_list == sorted(procedure_file_list)
