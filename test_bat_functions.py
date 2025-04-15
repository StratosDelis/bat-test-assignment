# test_bat_functions.py

import pytest
import bat_functions
from bat_functions import calculate_bat_power
from bat_functions import signal_strength
from bat_functions import get_bat_vehicle

"""------------------------------Exercise 1------------------------------"""


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


"""------------------------------Exercise 2------------------------------"""

@pytest.fixture
def vehicle_dict():
    return {
        'Batmobile': {'speed': 200, 'armor': 80},
        'Batwing': {'speed': 300, 'armor': 60},
        'Batcycle': {'speed': 150, 'armor': 50}
    }

@pytest.mark.parametrize("vehicle",[
    'Batmobile',
    'Batwing',
    'Batcycle'
])

def test_get_bat_vehicle(vehicle, vehicle_dict):
    """
    Tests the validity of the get_bat_vehicle function for known bat vehicle names
    """
    assert get_bat_vehicle(vehicle) == vehicle_dict[vehicle]

def test_get_bat_vehicle_uk():
    """
    Tests the validity of the get_bat_vehicle function for unknown bat vehicle name
    """
    with pytest.raises(ValueError, match=(f"Unknown vehicle: Matiz")):
        get_bat_vehicle('Matiz')


"""------------------------------Exercise 3------------------------------"""

def test_fetch_joker_info(monkeypatch):
    def custom_dict():
        return {'mischief_level': 0, 'location': 'captured'}

    monkeypatch.setattr(bat_functions, 'fetch_joker_info', custom_dict)
    result = bat_functions.fetch_joker_info()
    assert result == {'mischief_level': 0, 'location': 'captured'}
