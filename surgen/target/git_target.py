import shutil
import tempfile
from .base import TargetBase
from git import Repo


class GitTarget(TargetBase):
    def __init__(self, target):
        super(GitTarget, self).__init__(target)
        self._workspace = None

    @property
    def workspace(self):
        return self._workspace

    def prepare(self):
        self._workspace = tempfile.mkdtemp()
        self._repo = Repo.clone_from(self._target, self.workspace)

    def commit(self, summary):
        """
        summary: a summary of the action performed on the target.
        """
        self._repo.git.add(".")
        self._repo.git.commit("-am", summary)
        self._repo.git.push("origin", "master")

    def cleanup(self):
        shutil.rmtree(self._workspace)
