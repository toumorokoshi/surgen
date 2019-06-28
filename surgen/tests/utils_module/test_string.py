from surgen.utils.string import replace, insert, remove


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


def test_insert():
    contents = "abc"
    assert insert(["a", "d", "e"], contents) == "a\nd\ne\n" + contents


def test_remove():
    contents = "and a one and a two and a"
    assert remove(["one"], contents) == "and a  and a two and a"

