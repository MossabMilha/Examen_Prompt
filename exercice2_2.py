def format_product_code_1(product_id):
    """
    Formate un identifiant de produit en insérant des tirets.

    L'identifiant doit être une chaîne alphanumérique exactement composée de 10 caractères.
    Le format retourné sera : XXX-XXXX-XXX

    Paramètre :
        product_id (str) : L'identifiant du produit à formater.

    Retourne :
        str : L'identifiant formaté avec des tirets (après le 3e et 7e caractère).

    Lève :
        ValueError : Si la chaîne ne fait pas 10 caractères ou contient des caractères non alphanumériques.

    Exemple :
        >>> format_product_code("A1B2C3D4E5")
        'A1B-2C3D-E5'
    """
    # Vérifie la longueur et le contenu
    if not isinstance(product_id, str) or len(product_id) != 10:
        raise ValueError("L'identifiant doit contenir exactement 10 caractères.")

    if not product_id.isalnum():
        raise ValueError("L'identifiant doit être uniquement alphanumérique.")

    # Insère les tirets
    return f"{product_id[:3]}-{product_id[3:7]}-{product_id[7:]}"


def format_product_code_2(product_id):
    """
    Formate un identifiant de produit en insérant des tirets.

    Le code produit doit être une chaîne de 10 caractères alphanumériques.
    Le format retourné est : XXX-XXX-XXXX

    Paramètre :
        product_id (str) : Chaîne représentant le code produit à formater.

    Retourne :
        str : Le code produit formaté, par exemple : 'ABC-123-DEF4'.

    Lève :
        ValueError : Si l'entrée n'est pas une chaîne de 10 caractères alphanumériques.

    Exemple :
        >>> format_product_code("ABC123DEF4")
        'ABC-123-DEF4'
    """
    # Vérification du type, de la longueur et du contenu alphanumérique
    if not isinstance(product_id, str):
        raise ValueError("Le code produit doit être une chaîne de caractères.")

    if len(product_id) != 10:
        raise ValueError("Le code produit doit contenir exactement 10 caractères.")

    if not product_id.isalnum():
        raise ValueError("Le code produit doit être alphanumérique uniquement.")

    # Formatage avec des tirets : XXX-XXX-XXXX
    return f"{product_id[:3]}-{product_id[3:6]}-{product_id[6:]}"

def format_product_code_3(product_id):
    """
    Formate un identifiant de produit de 10 caractères alphanumériques au format 'XXX-XXX-XXXX'.

    Paramètre :
        product_id (str) : Code produit à formater.

    Retourne :
        str : Le code produit formaté avec des tirets, par exemple 'ABC-123-DEF4'.

    Lève :
        ValueError :
            - Si le code n'est pas une chaîne de 10 caractères.
            - Si le code contient des caractères non alphanumériques.

    Exemples :
        >>> format_product_code("ABC123DEF4")
        'ABC-123-DEF4'
        >>> format_product_code("XYZ987GHIJ")
        'XYZ-987-GHIJ'
        >>> format_product_code("SHORT")
        ValueError: Le code produit doit contenir exactement 10 caractères alphanumériques.
    """
    if not isinstance(product_id, str):
        raise ValueError("Le code produit doit être une chaîne de caractères.")

    if len(product_id) != 10 or not product_id.isalnum():
        raise ValueError("Le code produit doit contenir exactement 10 caractères alphanumériques.")

    return f"{product_id[:3]}-{product_id[3:6]}-{product_id[6:]}"
