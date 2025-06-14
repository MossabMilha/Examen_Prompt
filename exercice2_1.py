

# Prompt Vague :
def calculer(nombre1, nombre2, operateur):
    if operateur == '+':
        return nombre1 + nombre2
    elif operateur == '-':
        return nombre1 - nombre2
    elif operateur == '*':
        return nombre1 * nombre2
    elif operateur == '/':
        if nombre2 != 0:
            return nombre1 / nombre2
        else:
            return "Erreur : division par zéro"
    else:
        return "Erreur : opérateur non reconnu"


#Prompt Spécifique
def calculate_1(a, b, op):
    """
    Effectue une opération mathématique entre deux entiers a et b selon l'opérateur fourni.

    Paramètres :
    - a (int) : Le premier nombre entier.
    - b (int) : Le second nombre entier.
    - op (str) : L'opération à effectuer, représentée par une chaîne de caractères.
                Doit être l'un des suivants : '+', '-', '*', '/'.

    Retours :
    - Le résultat de l’opération sous forme numérique.
      - Pour une division, le résultat est arrondi à deux décimales.
    - Une chaîne de message d'erreur si :
      - L'opérateur n'est pas reconnu.
      - Il y a une tentative de division par zéro.

    Exemples :
    >>> calculate(5, 3, '+')
    8
    >>> calculate(5, 0, '/')
    'Erreur : division par zéro'
    >>> calculate(10, 3, '/')
    3.33
    >>> calculate(4, 2, '?')
    'Erreur : opérateur invalide'
    """
    # Addition
    if op == '+':
        return a + b
    # Soustraction
    elif op == '-':
        return a - b
    # Multiplication
    elif op == '*':
        return a * b
    # Division avec gestion du zéro et arrondi
    elif op == '/':
        if b == 0:
            return "Erreur : division par zéro"
        else:
            return round(a / b, 2)
    # Si l'opérateur est invalide
    else:
        return "Erreur : opérateur invalide"

# Prompt avec Persona
def calculate_2(a, b, op):
    """
    Effectue une opération mathématique entre deux entiers.

    Paramètres :
        a (int) : Le premier entier.
        b (int) : Le second entier.
        op (str) : L'opérateur mathématique, attendu parmi : '+', '-', '*', '/'.

    Retourne :
        float|int : Le résultat de l'opération. Si l'opération est une division,
                    le résultat est arrondi à deux décimales.
        str : Un message d'erreur en cas d'opérateur invalide ou de division par zéro.

    Exemples :
        >>> calculate(10, 5, '+')
        15
        >>> calculate(10, 0, '/')
        'Erreur : division par zéro'
        >>> calculate(8, 2, '/')
        4.0
        >>> calculate(7, 3, '/')
        2.33
        >>> calculate(4, 2, '%')
        'Erreur : opérateur invalide'
    """
    # Vérifie que les entrées sont bien des entiers
    if not isinstance(a, int) or not isinstance(b, int):
        return "Erreur : les deux valeurs doivent être des entiers"

    # Effectue l'opération en fonction de l'opérateur fourni
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Erreur : division par zéro"
        return round(a / b, 2)
    else:
        return "Erreur : opérateur invalide"
