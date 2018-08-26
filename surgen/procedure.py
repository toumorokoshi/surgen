from .exceptions import ProcedureNotFound
from clint.textui import puts


class Procedure(object):
    """
    the procedure represents the base class that a procedure file
    should extend from.

    it provides several utilities to help interact with a repository.
    """

    def __init__(self, file_name, target_dir):
        self._target_dir = target_dir
        self._file_name = file_name

    @property
    def root(self):
        return self._target_dir

    def should_not_run(self):
        """
        This should return None if the test should execute.
        otherwise, it should provide a string indicating the
        reason why it was skipped.
        """
        return None

    def log(self, message):
        """ log a message. """
        puts(message)

    def operate(self):
        """
        This method should be overriden, with the actual script.

        In the case of an error, an exception should be raised.
        """
        print("foo")

    def __str__(self):
        return self._file_name


def from_file(full_file_path):
    """ load a procedure from a full file path. """
    with open(full_file_path) as fh:
        contents = fh.read()
        return from_string(contents, full_file_path)


def from_string(string, file_name):
    l = {}
    l["__file__"] = file_name
    bytecode = compile(string, file_name, "exec")
    exec(bytecode, l, l)
    for name, value in l.items():
        if (
            isinstance(value, type)
            and issubclass(value, Procedure)
            and value is not Procedure
        ):
            return value
    raise ProcedureNotFound(
        "unable to find class that inherits surgen.Procedure in file {0}".format(
            file_name
        )
    )
