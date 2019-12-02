from day02.solver import add, mul, run


def test_add():
    actual = [0, 2, 3]
    add([1, 2, 0], actual)
    assert actual == [5, 2, 3]


def test_mul():
    actual = [0, 2, 3]
    mul([1, 2, 0], actual)
    assert actual == [6, 2, 3]


def test_run():
    assert run([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert run([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert run([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert run([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

