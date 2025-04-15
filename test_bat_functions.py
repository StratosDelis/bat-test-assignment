# test_bat_functions.py

import pytest
from bat_functions import calculate_bat_power

@pytest.mark.parametrize("a, expected",[
    (0, 0),
    (1, 42),
    (2, 84),
    (3, 126)
])

def test_calc_bat_power(a, expected):
    assert calculate_bat_power(a) == expected
