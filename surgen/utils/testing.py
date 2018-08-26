import difflib
import logging
import os
import shutil
import tempfile
from pprint import pprint
from surgen.procedure import from_file

DIFFER = difflib.Differ()
LOG = logging.getLogger(__name__)


def compare_procedure(procedure_file, inp, output):
    """
    test a procedure against a filesystem, by taking in:

    :param surgen.Procedure procedure: the procedure to test
    :param str inp: the directory containing the input to operate on
    :param str output: the directory containing the output to validate against
    """
    tmp_dir = tempfile.mkdtemp()
    shutil.rmtree(tmp_dir)
    shutil.copytree(inp, tmp_dir)
    procedure_cls = from_file(procedure_file)
    p = procedure_cls("dummy", tmp_dir)
    assert not p.should_not_run(), "procedure indicated this should not run."
    p.operate()
    _assert_identical_directories(output, tmp_dir)


def _assert_identical_directories(l, r):
    for root, _, file_names in os.walk(l):
        for name in file_names:
            relative_path = os.path.join(root, os.curdir + os.sep + name)[len(l) :]
            # remove absolute at top, if it exists
            relative_path = relative_path.lstrip(os.sep)
            l_path = os.path.join(l, relative_path)
            r_path = os.path.join(r, relative_path)
            with open(l_path) as l_fh:
                with open(r_path) as r_fh:
                    result = list(
                        difflib.ndiff(
                            l_fh.read().splitlines(), r_fh.read().splitlines()
                        )
                    )
                    result = [r for r in result if not r.startswith(" ")]
                    if result:
                        pprint(result)
                    assert not result, "contents of {} != {}.".format(l_path, r_path)
