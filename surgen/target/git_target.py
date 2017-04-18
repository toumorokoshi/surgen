import shutil
import tempfile
from .base import TargetBase
from git import Repo


class GitTarget(TargetBase):
    def __init__(self, target):
        super(GitTarget, self).__init__(target)
        self._workspace = tempfile.mkdtemp()

    @property
    def workspace(self):
        return self._workspace

    def before_procedures(self):
        self._repo = Repo.clone_from(self._target, self.workspace)

    def after_procedures(self):
        # Commit & Push
        shutil.rmtree(self._workspace)

    def __str__(self):
        return "{0} (git)".format(self._target)
