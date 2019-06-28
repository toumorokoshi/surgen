# this is a module level import to ensure
# verboselogs' monkeypatching works as expected.
import verboselogs

verboselogs.install()
from .procedure import Procedure
