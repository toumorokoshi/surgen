"""surgen, a codebase upgrade tool

Usage:
  surgen [<procedure_dir> <target_dir> -v]

Options:
  <procedure_dir>  the directory containing surgen procedure files
  <target_dir>  the directory to operate on.
  -v, --verbose     show verbose output
  -h, --help        show this usage guide
"""
import docopt
import logging
import sys
from .surgen import Surgen, surgen_from_directory

def main(argv=sys.argv[1:]):
    options = docopt.docopt(__doc__,  argv=argv, options_first=True)
    level = logging.DEBUG if options["--verbose"] else logging.INFO
    s = surgen_from_directory(options["<procedure_dir>"])
    return s.operate(options["<target_dir>"])
