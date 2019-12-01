from day01.solver import calc_fuel, recur_fuel_calc


def test_calc_fuel():
    assert calc_fuel(12) == 2
    assert calc_fuel(14) == 2
    assert calc_fuel(1969) == 654
    assert calc_fuel(100756) == 33583


def test_rec_fuel_calc():
    assert recur_fuel_calc(14) == 2
    assert recur_fuel_calc(1969) == 966
    assert recur_fuel_calc(100756) == 50346
