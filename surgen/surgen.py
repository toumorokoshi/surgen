import os
from collections import OrderedDict
from clint.textui import colored, puts, indent
from .procedure import from_file
from .exceptions import ProcedureNotFound
from .results import ResultStatus, Result, Results

import logging

LOG = logging.getLogger(__name__)


class Surgen(object):
    """ the main context to perform operations. """

    def __init__(self, procedures_by_name):
        self._procedures_by_name = procedures_by_name
        # lists data about performed procedures
        self._performed_procedure_data = []

    def operate(self, target, ignore_errors, dry_run):
        """
        perform the operation on the target directory.
        return an exit code.
        """
        puts("Perfoming procedures on {0}".format(target))
        target.prepare()
        try:
            results = Results()
            with indent(2):
                for name, procedure_cls in self._procedures_by_name.items():
                    puts("{0}:".format(name))
                    with indent(2):
                        status = self._run_procedure(
                            name, procedure_cls, target.workspace, dry_run
                        )
                        results.add(Result(procedure=name, status=status))
                        if not ignore_errors and status == ResultStatus["FAIL"]:
                            with indent(-4):
                                puts(colored.red("Surgen ending early"))
                                self._print_results(results)
                            return 1
            if not dry_run:
                target.commit(results)
            self._print_results(results)
            self._performed_procedure_data.append(
                (target, results)
            )
            return 1 if ResultStatus["FAIL"] in results else 0
        finally:
            target.cleanup()

    def _print_results(self, results):
        puts(colored.green("Complete! {0} procedure(s) performed.".format(len(self._procedures_by_name))))
        puts(colored.green("{PASS} success, {FAIL} failed, {SKIP} skipped".format(**results.count_by_status)))

    def _run_procedure(self, name, procedure_cls, target_dir, dry_run):
        puts(colored.yellow("executing...".format(name)))
        procedure = procedure_cls(name, target_dir)
        should_not_run_reason = procedure.should_not_run()
        if should_not_run_reason:
            puts(colored.yellow("skipping, should_not_run returned: {0}".format(should_not_run_reason)))
            return ResultStatus["SKIP"]
        if not dry_run:
            try:
                with indent(2):
                    result = procedure.operate()
            except Exception as e:
                LOG.debug("", exc_info=True)
                puts(colored.red("procedure raised an exception! {0}".format(e)))
                return ResultStatus["FAIL"]
            puts(colored.green("complete!"))
        return ResultStatus["PASS"]

    def print_total_summary(self):
        """ print the total summary. """
        for target, results in self._performed_procedure_data:
            puts(colored.green("{0}: {PASS} | {FAIL} | {SKIP}".format(target, **results.count_by_status)))


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
