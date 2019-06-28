from uranium import current_build, task_requires
import os
import time

current_build.packages.install("uranium-plus[vscode]")
import uranium_plus

current_build.config.update(
    {
        "uranium-plus": {
            "module": "surgen",
            "publish": {"additional_args": ["--release"]},
            "test": {"packages": [""]},
        }
    }
)

uranium_plus.bootstrap(current_build)
