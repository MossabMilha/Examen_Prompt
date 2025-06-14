import pytest
from exercice2_2 import format_product_code_1, format_product_code_2, format_product_code_3


# ===== Tests pour format_product_code_1 =====
def test_format_product_code_1_valide():
    assert format_product_code_1("A1B2C3D4E5") == "A1B-2C3D-E5"

def test_format_product_code_1_longueur_invalide():
    with pytest.raises(ValueError):
        format_product_code_1("A1B2C3D4")  # 9 caractères

def test_format_product_code_1_caracteres_invalides():
    with pytest.raises(ValueError):
        format_product_code_1("A1B2C3D4E#")  # caractère non alphanumérique


# ===== Tests pour format_product_code_2 =====
def test_format_product_code_2_valide():
    assert format_product_code_2("ABC123DEF4") == "ABC-123-DEF4"

def test_format_product_code_2_type_invalide():
    with pytest.raises(ValueError):
        format_product_code_2(1234567890)  # pas une chaîne

def test_format_product_code_2_longueur_invalide():
    with pytest.raises(ValueError):
        format_product_code_2("ABC123DEF")  # 9 caractères

def test_format_product_code_2_caracteres_invalides():
    with pytest.raises(ValueError):
        format_product_code_2("ABC123DE#4")  # caractère non alphanumérique


# ===== Tests pour format_product_code_3 =====
def test_format_product_code_3_valide():
    assert format_product_code_3("ABC123DEF4") == "ABC-123-DEF4"
    assert format_product_code_3("XYZ987GHIJ") == "XYZ-987-GHIJ"

def test_format_product_code_3_type_invalide():
    with pytest.raises(ValueError):
        format_product_code_3(None)

def test_format_product_code_3_longueur_ou_caracteres_invalides():
    with pytest.raises(ValueError):
        format_product_code_3("SHORT")
    with pytest.raises(ValueError):
        format_product_code_3("ABC123DE#4")
