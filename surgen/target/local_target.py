from .base import TargetBase


class LocalTarget(TargetBase):
    @property
    def workspace(self):
        return self._target
