import os
from collections import OrderedDict
from clint.textui import colored, puts, indent
from .procedure import from_file

import logging

LOG = logging.getLogger(__name__)

class Surgen(object):
    """ the main context to perform operations. """

    def __init__(self, procedures_by_name)
        self._procedures_by_name = procedures_by_name

    def operate(self, target_dir):
        """
        perform the operation on the target directory.
        return an exit code.
        """
        puts(colored.green("Perfoming procedures on {0}...".format(target_dir)))
        with indent(4):
            for name, procedure_cls in self._procedures_by_name.items():
                puts(colored.yellow("perfoming procedure {0}...".format(name)))
                result = self.operate(procedure, target_dir)
                if result != 0:
                    puts(colored.red("procedure failed with code {0}".format(result)))
                    return result

    def operate(self, name, procedure_cls, target_dir):
        procedure = procedure_cls(name, target_dir)
        try:
            procedure.operate()
        except Exception as e:
            LOG.debug("", exc_info=True)
            puts(colored.red("procedure raised an exception! {0}".format(e))


def surgen_from_directory(procedure_dir):
    """ load a surgen object from a directory """
    return Surgen(_procedures_from_dir(procedure_dir))

def _procedures_from_dir(procedure_dir):
    procedures_by_name = OrderedDict()
    for d in os.listdir(procedure_dir):
        if os.path.isdir(d):
            puts(colored.yellow("skipping {0}, it is a directory."))
            continue
        if not d.endswith(".py"):
            puts(colored.yellow("skipping {0}, it does not end with extension .py".format(d)))
            continue
        name = d[:-len(".py")]
        full_path = os.path.join(procedure_dir, d)
        procedures_by_name[name] = from_file(d)
    return procedures_by_name
