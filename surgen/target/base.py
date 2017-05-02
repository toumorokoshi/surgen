class TargetBase(object):
    TARGET_TYPE = "base"

    def __init__(self, target):
        self._target = target

    @property
    def workspace(self):
        raise NotImplementedError()

    def prepare(self):
        pass

    def commit(self, summary):
        pass

    def __str__(self):
        return "{0}: ({1})".format(
            self.__class__.__name__, self._target
        )
