import logging
import shutil
import tempfile
from .base import TargetBase
from git import Repo

LOG = logging.getLogger(__name__)
DEFAULT_MESSAGE = "updating repo programatically (via surgen)"

class GitTarget(TargetBase):
    def __init__(self, target, message=None, commit=True):
        super(GitTarget, self).__init__(target)
        self._message = message
        self._workspace = None
        self._commit = commit

    @property
    def workspace(self):
        return self._workspace

    def prepare(self):
        self._workspace = tempfile.mkdtemp()
        self.log("cloning {0}...".format(self.workspace))
        self._repo = Repo.clone_from(self._target, self.workspace)

    def commit(self, summary):
        """
        summary: a summary of the action performed on the target.
        """
        if not self._commit:
            self.log("committing disabled for {0}".format(self))
            return

        message = "{0}\n\n{1}".format(self._message or DEFAULT_MESSAGE, str(summary))

        try:
            self._repo.git.add(".")
            if self._repo.is_dirty():
                self.log("committing changes to {0}".format(self._target))
                self._repo.index.commit(message)
                self._repo.git.push()
            else:
                self.log("no changes found. skipping commit...")
        except Exception as e:
            LOG.exception("")
            print(e)
            self.log("unable to push to {0}".format(self._target))

    def cleanup(self):
        shutil.rmtree(self._workspace)
