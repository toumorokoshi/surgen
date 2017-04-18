from .base import TargetBase


class LocalTarget(TargetBase):
    def __str__(self):
        return "{0} (local)".format(self._target)
