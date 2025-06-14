import pytest
from exercice2_1 import calculer, calculate_1, calculate_2


# ==== Tests pour la fonction calculer ====
def test_calculer_addition():
    assert calculer(2, 3, '+') == 5

def test_calculer_division_par_zero():
    assert calculer(10, 0, '/') == "Erreur : division par zéro"

def test_calculer_operateur_invalide():
    assert calculer(4, 2, '%') == "Erreur : opérateur non reconnu"

def test_calculer_multiplication():
    assert calculer(3, 4, '*') == 12


# ==== Tests pour la fonction calculate_1 ====
def test_calculate_1_soustraction():
    assert calculate_1(7, 2, '-') == 5

def test_calculate_1_division_arrondie():
    assert calculate_1(10, 3, '/') == 3.33

def test_calculate_1_operateur_invalide():
    assert calculate_1(4, 2, '?') == "Erreur : opérateur invalide"

def test_calculate_1_division_par_zero():
    assert calculate_1(9, 0, '/') == "Erreur : division par zéro"


# ==== Tests pour la fonction calculate_2 ====
def test_calculate_2_addition():
    assert calculate_2(8, 7, '+') == 15

def test_calculate_2_verifie_entiers():
    assert calculate_2(4.5, 2, '+') == "Erreur : les deux valeurs doivent être des entiers"
    assert calculate_2("3", 2, '*') == "Erreur : les deux valeurs doivent être des entiers"

def test_calculate_2_division_arrondie():
    assert calculate_2(7, 3, '/') == 2.33

def test_calculate_2_operateur_invalide():
    assert calculate_2(3, 3, '^') == "Erreur : opérateur invalide"
