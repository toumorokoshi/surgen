class TargetBase(object):
    def __init__(self, target):
        self._target = target

    @property
    def workspace(self):
        return self._target

    def before_procedures(self):
        pass

    def after_procedures(self):
        pass

    def __str__(self):
        pass
