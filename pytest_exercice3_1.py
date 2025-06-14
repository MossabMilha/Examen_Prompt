import pytest
from exercice3_1 import calculate_average

def test_average_valid_integers():
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_average_valid_floats():
    assert calculate_average([1.0, 2.0, 3.0]) == 2.0

def test_average_mixed_numbers():
    assert calculate_average([1, 2.5, 3]) == pytest.approx(2.1666, 0.01)

def test_average_empty_list():
    with pytest.raises(ValueError, match="La liste est vide."):
        calculate_average([])

def test_average_with_string_element():
    with pytest.raises(ValueError, match="Élément non numérique trouvé"):
        calculate_average([1, 2, 'three', 4])

def test_average_with_all_invalid_elements():
    with pytest.raises(ValueError):
        calculate_average(['a', 'b'])

def test_average_with_negative_numbers():
    assert calculate_average([-1, -2, -3]) == -2.0

def test_average_with_zeroes():
    assert calculate_average([0, 0, 0]) == 0.0
