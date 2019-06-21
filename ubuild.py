import os
import subprocess


def main(build):
    build.packages.install(".", develop=True)


def test(build):
    main(build)
    build.packages.install("jedi")
    build.packages.install("pytest")
    build.packages.install("pytest-cov")
    pytest = os.path.join(build.root, "bin", "py.test")
    subprocess.call(
        [pytest, "--cov", "surgen", "surgen/tests", "--cov-report", "term-missing"]
        + build.options.args
    )


def publish(build):
    """ publish the package itself """
    build.packages.install("wheel")
    build.packages.install("twine")
    build.executables.run(
        ["python", "setup.py", "sdist", "bdist_wheel", "--universal", "--release"]
    )
    build.executables.run(["twine", "upload", "dist/*"])


def stamp(build):
    """ after a distribution, stamp the current build. """
    build.packages.install("gitchangelog")
    changelog_text = subprocess.check_output(["gitchangelog"])
    with open(os.path.join(build.root, "CHANGELOG"), "wb+") as fh:
        fh.write(changelog_text)


def build_docs(build):
    build.packages.install("sphinx")
    return subprocess.call(["make", "html"], cwd=os.path.join(build.root, "docs"))
