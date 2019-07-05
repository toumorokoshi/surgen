import logging
import shutil
import tempfile
from typing import Dict
from .base import TargetBase
from git import Repo
from git.exc import GitCommandError

LOG = logging.getLogger(__name__)
DEFAULT_MESSAGE = "updating repo programatically (via surgen)"


class GitTarget(TargetBase):
    """
    Perform surgen operations against a git repository. The following
    arguments can be passed:

    * envvars: a dictionary of environment variables which will be used during git commands.
          this enables customizability of values such as GIT_AUTHOR_NAME, GIT_COMMITTER_NAME, etc.
    """

    def __init__(
        self,
        target,
        message=None,
        commit=True,
        branch=None,
        envvars: Dict[str, str] = None,
    ):
        super(GitTarget, self).__init__(target)
        self._message = message
        self._workspace = None
        self._commit = commit
        self._branch = branch
        self._envvars = envvars or {}

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
            self._commit_and_push(self._repo, self._branch, message)
        except Exception as e:
            LOG.exception("")
            print(e)
            self.log("unable to push to {0}".format(self._target))

    def _commit_and_push(self, repo, branch, message):
        if repo.is_dirty(untracked_files=True):
            self.log("committing changes to {0}".format(self._target))
            with repo.git.custom_environment(**self._envvars):
                repo.git.add(A=True)
                repo.git.commit(all=True, message=message)
        self._push(repo, branch)

    def _push(self, repo, branch):
        if branch:
            # this typically means the remote doesn't have the branch to rebase against
            try:
                repo.git.pull(self._repo.remotes[0].name, branch, rebase=True)
            except GitCommandError:
                pass
            repo.git.push(
                self._repo.remotes[0].name,
                "{0}:{1}".format(self._repo.active_branch.name, branch),
            )
        else:
            repo.git.pull(rebase=True)
            repo.git.push()

    def cleanup(self):
        shutil.rmtree(self._workspace)
