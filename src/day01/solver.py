from utils.file import read_file
import math
from functools import reduce


def calc_fuel(m):
    return math.floor(m / 3) - 2


def recur_fuel_calc(m):
    result = calc_fuel(m)
    if result < 1:
        return 0
    else:
        return result + recur_fuel_calc(result)


def a(puzzle_input):
    return solve(calc_fuel, puzzle_input)


def b(puzzle_input):
    return solve(recur_fuel_calc, puzzle_input)


def solve(fn, puzzle_input):
    return reduce(lambda x, y: x + y, map(fn, [int(i) for i in puzzle_input.splitlines()]))


def main():
    i = read_file("day01/input.txt")
    print(a(i))
    print(b(i))


main()
