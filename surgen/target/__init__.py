from .git_target import GitTarget
from .local_target import LocalTarget
from ..exceptions import TargetDriverNotFound


def target_from_str(driver, target):
    if driver == "local":
        return LocalTarget(target)
    elif driver == "git":
        return GitTarget(target)

    raise TargetDriverNotFound(driver)
