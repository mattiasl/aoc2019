from day03.solver import create_wire, a, b


def test_a():
    wire = [create_wire("test/1.in"), create_wire("test/2.in")]
    assert a(wire[0]) == 159
    assert a(wire[1]) == 135


def test_b():
    wire = [create_wire("test/1.in"), create_wire("test/2.in")]
    assert b(wire[0]) == 610
    assert b(wire[1]) == 410

