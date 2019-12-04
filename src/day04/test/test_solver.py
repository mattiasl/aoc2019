from day04.solver import has_at_least_two_equal_adjacent_digits, has_exactly_two_equal_adjacent_digits, \
    is_ascending_from_left_to_right


def test_is_ascending_from_left_to_right():
    assert is_ascending_from_left_to_right(str(111111)) is True
    assert is_ascending_from_left_to_right(str(223450)) is False
    assert is_ascending_from_left_to_right(str(123789)) is True


def test_has_at_least_two_equal_adjacent_digits():
    assert has_at_least_two_equal_adjacent_digits(str(111111)) is True
    assert has_at_least_two_equal_adjacent_digits(str(223450)) is True
    assert has_at_least_two_equal_adjacent_digits(str(123789)) is False


def test_has_exactly_two_equal_adjacent_digits():
    assert has_exactly_two_equal_adjacent_digits(str(112233)) is True
    assert has_exactly_two_equal_adjacent_digits(str(123444)) is False
    assert has_exactly_two_equal_adjacent_digits(str(111122)) is True
