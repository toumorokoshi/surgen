"""surgen, a codebase upgrade tool

Usage:
  surgen [-d -i -v --driver=<driver> --log=<level> <procedure_dir> <target>]

Options:
  <procedure_dir>         the directory containing surgen procedure files [default: ./procedures/]
  <target>                the target to operate on. [default: .]
  --driver=<driver>       the target driver to use. [default: local]
  --log=<level>           log at the specified log level. levels follow those in the verboselogs python library.
  -d, --dry-run           skips execution if provided
  -i, --ignore-errors     continues if a procedure fails
  -h, --help              show this usage guide
"""
import os
import docopt
import logging
import sys
from .surgen import Surgen, surgen_from_directory
from .target import target_from_str, LocalTarget
from .log import setup_logging

DEFAULT_PROCEDURE_DIR = os.path.join(os.curdir, "surgen_procedures")
DEFAULT_TARGET_DIR = os.curdir
DEFAULT_DRIVER = "local"


def main(argv=sys.argv[1:]):
    options = docopt.docopt(__doc__, argv=argv, options_first=True)
    level = options.get("--log") or logging.INFO
    setup_logging(level)
    s = surgen_from_directory(options.get("<procedure_dir>") or DEFAULT_PROCEDURE_DIR)
    d = options.get("--driver") or DEFAULT_DRIVER
    t = (
        target_from_str(d, options.get("<target>"))
        if options.get("<target>")
        else LocalTarget(DEFAULT_TARGET_DIR)
    )
    return s.operate(t, options["--ignore-errors"], options["--dry-run"])
