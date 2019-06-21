from surgen.utils.string import replace, remove, insert


def test_replace():
    contents = """
a
b
c
d
    """.strip()

    subs = [("a", "foo"), ("b\n", "bar")]

    output = replace(subs, contents)

    assert (
        output
        == """
foo
barc
d
    """.strip()
    )


def test_remove():
    assert remove(["abc", "def"], "abcdefg") == "g"


def test_insert():
    assert insert(["c", "b", "a"], "") == "cba"
