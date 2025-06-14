def get_user_permissions(user_id, system_context):
    """Récupère les permissions d’un utilisateur en fonction de son rôle dans le système.

    Cette fonction examine le rôle d'un utilisateur à partir du dictionnaire `system_context`
    et retourne une liste de permissions associée à ce rôle. Trois types de rôles sont pris en compte :
    "admins", "editors", et les autres utilisateurs, avec des niveaux de permission décroissants.

    Args:
        user_id (str): L'identifiant unique de l'utilisateur.
        system_context (dict): Un dictionnaire contenant les rôles d'utilisateurs,
            avec des clés telles que 'admins', 'editors', etc., chacune associée à une liste d'identifiants.

    Returns:
        list[str]: Une liste de chaînes représentant les permissions de l'utilisateur.
            - ['read', 'write', 'delete', 'admin'] si l'utilisateur est un admin
            - ['read', 'write'] s’il est éditeur
            - ['read'] sinon

    Example:
        >>> system_context = {
        ...     'admins': ['user1', 'user2'],
        ...     'editors': ['user3']
        ... }
        >>> get_user_permissions('user1', system_context)
        ['read', 'write', 'delete', 'admin']

        >>> get_user_permissions('user3', system_context)
        ['read', 'write']

        >>> get_user_permissions('user5', system_context)
        ['read']
    """
    if user_id in system_context['admins']:
        return ['read', 'write', 'delete', 'admin']
    elif user_id in system_context['editors']:
        return ['read', 'write']
    else:
        return ['read']
