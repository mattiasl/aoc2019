from itertools import groupby


def has_at_least_two_equal_adjacent_digits(pw):
    return 1 in [1 for i in range(len(pw) - 1) if int(pw[i]) == int(pw[i + 1])]


def has_exactly_two_equal_adjacent_digits(pw):
    return 2 in [len(list(g)) for _, g in groupby([int(i) for i in list(pw)])]


def is_ascending_from_left_to_right(pw):
    return ''.join(sorted(pw)) == pw


def is_accepted(pw):
    return has_at_least_two_equal_adjacent_digits(pw) and is_ascending_from_left_to_right(pw)


def a():
    return [int(candidate) for candidate in range(272091, 815432 + 1) if is_accepted(str(candidate))]


def b(candidates):
    return [int(c) for c in candidates if has_exactly_two_equal_adjacent_digits(str(c))]


def main():
    passwords = a()
    print(len(passwords))
    print(len(b(passwords)))


main()
