# test_bat_functions.py

import pytest
from bat_functions import calculate_bat_power
from bat_functions import signal_strength

@pytest.mark.parametrize("p, expectedPower",[
    (0, 0),
    (1, 42),
    (2, 84),
    (3, 126)
])

def test_calc_bat_power(p, expectedPower):
    """
    Tests Batman's power for different levels (0, 1, 2, 3)
    """
    assert calculate_bat_power(p) == expectedPower

@pytest.mark.parametrize("d, expectedSignal",[
    (0, 100.0),
    (5, 50.0),
    (10, 0),
    (12, 0)
])

def test_signal_strength(d, expectedSignal):
    """
    Tests the signal strength for different distances (0km, 5km, 10km, 12km)
    """
    assert signal_strength(d) == expectedSignal
