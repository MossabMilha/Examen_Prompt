# 🚀 Prompt Engineering & IA Générative – Projet Claude (Anthropic)

Ce projet explore l'utilisation de l'IA générative, en particulier **Claude d'Anthropic**, dans le cadre du développement logiciel : génération de code, débogage, documentation et refactoring via le *prompt engineering*.

---

## 🧠 Partie 1 – Choix de la Solution IA

### ✅ Solution choisie

**Claude (Anthropic)**

### 📌 Définition

Claude est un assistant IA développé par Anthropic, conçu pour comprendre, générer, commenter et améliorer du code dans de multiples langages. Il se distingue par son approche conversationnelle et pédagogique.

### 👍 Avantages

- Explication claire et didactique du code
- Support multi-langage (Python, JS, Java, C++, etc.)
- Dialogue itératif pour affiner les résultats
- Débogage et refactoring assisté
- Génération automatique de documentation

### 🙎 Limites

- Pas d'exécution de code en temps réel
- Connaissance figée à une date limite (cutoff)
- Pas d'intégration directe avec IDEs
- Code parfois générique ou hors contexte métier
- Nécessite une connexion internet

### 🛠️ Cas d’usage

- Apprentissage & formation
- Prototypage rapide
- Débogage automatisé
- Refactoring
- Génération de tests unitaires & documentation

---

## 💻 Partie 2 – Génération de Code

### 🔍 Comparaison entre deux versions de `calculatrice()`

#### 🔐 Robustesse

| Critère               | Version 1                                      | Version 2                             |
| --------------------- | ---------------------------------------------- | ------------------------------------- |
| Opérations supportées | 7 (+, -, \*, /, //, %, \*\*)                   | 4                                     |
| Types acceptés        | `int`, `float`, `str`                          | `int` uniquement                      |
| Gestion d’erreurs     | `ValueError`, `ZeroDivisionError`, `TypeError` | Validation stricte via `isinstance()` |
| Architecture          | Dictionnaire + lambdas                         | If/elif explicites                    |

🌟 **Conclusion :** *La première version est plus robuste et flexible.*

#### 📖 Lisibilité

| Critère    | Version 1                       | Version 2                |
| ---------- | ------------------------------- | ------------------------ |
| Structure  | Modulaire, fonctions abstraites | Linéaire, claire         |
| Docstring  | Complète                        | Présente                 |
| Lisibilité | Moyenne (abstraction)           | Excellente (pédagogique) |

🌟 **Conclusion :** *La seconde version est plus lisible.*

---

### 🌟 Prompt Engineering – Types

#### ✅ Prompt Spécifique

Permet de générer un code plus précis, conforme à la demande initiale (ex : PEP8, annotations types, etc.).

#### ✅ Prompt avec Persona

Ajout d’un style professionnel :

- Respect des standards Python (PEP8, docstrings)
- Architecture modulaire
- Séparation des responsabilités

#### ✅ Prompt basé sur la Règle (Zero-Shot)

- Fonction valide, gestion d’erreurs robuste
- Formatage correct : `XXX-XXXX-XXX`
- Vérification du type et contenu alphanumérique

#### ✅ Prompt avec Exemple (One-Shot)

- L’exemple fourni a **révélé une contradiction** dans les spécifications (XXX-XXXX-XXX vs XXX-XXX-XXXX)
- A aidé à clarifier l’intention et éviter des erreurs de logique

#### ✅ Prompt avec Exemples Multiples (Few-Shot)

- Pas d'amélioration technique de la robustesse
- Meilleure documentation
- Utile dans les cas complexes ou ambigus

---

## 🛠️ Partie 3 – Débogage et Refactoring

### 🐞 Exercice 3.1 – Débogage assisté

**Erreur rencontrée :**

```python
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
```

**Cause :** mélange de types dans `my_nums = [1, 2, 'three', 4]`

👉 **Correction proposée :**

- Validation des types
- Gestion des listes vides
- Exceptions explicites

🧪 **Tests Pytest :**

- Listes valides/invalide
- Types incorrects (None, str)
- Cas limites

---

### ♻️ Exercice 3.2 – Refactoring

**Objectif :** améliorer un algorithme de tri

### Problèmes initiaux :

- Variables peu explicites (`a`, `tmp`, etc.)
- Pas de structure ni de commentaires
- Manque de validation

👉 **Contraintes pour refactoring :**

- Respect PEP8
- Noms explicites
- Fonctions modulaires
- Docstring conforme
- Bloc `if __name__ == '__main__'`

---

### 📒 Exercice 3.3 – Génération de Documentation

#### 🐾 Exemple de docstring :

```python
def get_user_permissions(user_id: str, system_context: dict) -> list:
    """
    Récupère les permissions d’un utilisateur selon son rôle.

    Args:
        user_id (str): Identifiant de l’utilisateur
        system_context (dict): Dictionnaire contenant les rôles

    Returns:
        list: Liste de permissions associées

    Example:
        >>> get_user_permissions('admin1', {'admins': ['admin1'], 'editors': []})
        ['read', 'write', 'delete', 'admin']
    """
```

#### 📘 Section README générée

````markdown
## 🔐 Gestion des Permissions

Permet d’attribuer dynamiquement les droits aux utilisateurs en fonction de leur rôle.

### Exemple d'utilisation :

```python
from permissions import get_user_permissions

system_context = {
    'admins': ['admin1', 'admin2'],
    'editors': ['editor1']
}

permissions = get_user_permissions('admin1', system_context)
print(permissions)  # ['read', 'write', 'delete', 'admin']
````

### Prérequis :

- `system_context` est un dictionnaire avec les clés `'admins'` et `'editors'`
- `user_id` est une chaîne non vide

```

---

## ✅ Conclusion

Ce projet a permis de démontrer l’impact des types de prompts sur la qualité du code généré par l’IA, et les bonnes pratiques pour intégrer des outils IA comme Claude dans un flux de développement :

- 🔹 Les prompts spécifiques réduisent le nombre d’itérations
- 🔹 Les exemples permettent d’éviter les erreurs d’interprétation
- 🔹 L’IA peut produire une documentation conforme aux standards
- 🔹 Un prompt bien conçu permet d’avoir un code **robuste, lisible et professionnel**

```
