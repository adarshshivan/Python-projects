# tests/test_helpers.py
from number_guess import get_max_attempts, get_range_by_difficulty

def test_get_max_attempts():
    assert get_max_attempts(1) == 10
    assert get_max_attempts(2) == 6
    assert get_max_attempts(3) == 4

def test_get_range_by_difficulty():
    assert get_range_by_difficulty(1) == 50
    assert get_range_by_difficulty(2) == 100
    assert get_range_by_difficulty(3) == 200
