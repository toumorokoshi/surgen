import pytest
from surgen.procedure import from_string
from surgen.exceptions import ProcedureNotFound


def test_scope_works(tmpdir):
    """
    scripts which define variables in the global scope should
    have access to them.
    """

    SCRIPT = """
import os
from surgen import Procedure

class Scope(Procedure):

    def operate(self):
        print(os.path)
        return __file__

    """.strip()
    cls = from_string(SCRIPT, "foo")
    p = cls("foo", tmpdir.strpath)
    assert p.operate() == "foo"


def test_procedure_not_found_works(tmpdir):
    """
    no procedure class should raise an exception.
    """
    SCRIPT = """
import os
from surgen import Procedure
    """.strip()
    with pytest.raises(ProcedureNotFound):
        cls = from_string(SCRIPT, "foo")
