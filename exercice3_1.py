def calculate_average(numbers_list):
    """
    Calcule la moyenne des nombres dans une liste.
    Lève une ValueError si la liste contient un élément non numérique.
    """
    total = 0
    count = 0
    for num in numbers_list:
        if not isinstance(num, (int, float)):
            raise ValueError(f"Élément non numérique trouvé : {num}")
        total += num
        count += 1
    if count == 0:
        raise ValueError("La liste est vide.")
    return total / count

# Exemple d'utilisation
my_nums = [1, 2, 3, 4]  # Corrigé : remplacer 'three' par 3
try:
    avg = calculate_average(my_nums)
    print(f"Moyenne : {avg}")
except ValueError as e:
    print(f"Erreur : {e}")
