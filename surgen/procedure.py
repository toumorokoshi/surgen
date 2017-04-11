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

    def __str__(self):
        return self._file_name

    def operate(self):
        """ this method should be overriden, with the actual script. """
        print("foo")

def from_file(full_file_path):
    """ load a procedure from a full file path. """
    with open(full_file_path) as fh:
        contents = fh.read()
        g = {}
        l = {}
        exec(contents, g, l)
        for name, value in g.items():
            if isinstance(value, Procedure):
                return value
