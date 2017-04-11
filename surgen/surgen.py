import os
from collections import OrderedDict
from clint.textui import colored, puts, indent
from .procedure import from_file
from .exceptions import ProcedureNotFound

import logging

LOG = logging.getLogger(__name__)

class Surgen(object):
    """ the main context to perform operations. """

    def __init__(self, procedures_by_name):
        self._procedures_by_name = procedures_by_name

    def operate(self, target_dir):
        """
        perform the operation on the target directory.
        return an exit code.
        """
        puts("Perfoming procedures on {0}".format(target_dir))
        successful_procedures = 0
        with indent(2):
            for name, procedure_cls in self._procedures_by_name.items():
                puts("{0}:".format(name))
                with indent(2):
                    puts(colored.yellow("executing...".format(name)))
                    result = self._run_procedure(name, procedure_cls, target_dir)
                    if result:
                        puts(colored.red("failed with code {0}".format(result)))
                        return result
                    else:
                        puts(colored.green("complete!"))
                        successful_procedures += 1
        puts(colored.green("Complete! {0} procedures performed.".format(successful_procedures)))

    def _run_procedure(self, name, procedure_cls, target_dir):
        procedure = procedure_cls(name, target_dir)
        try:
            procedure.operate()
        except Exception as e:
            LOG.debug("", exc_info=True)
            puts(colored.red("procedure raised an exception! {0}".format(e)))


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
        try:
            procedures_by_name[name] = from_file(full_path)
        except ProcedureNotFound as pnf:
            puts(colored.yellow("skipping {0}: {1}".format(d, pnf)))
            continue
    return procedures_by_name
