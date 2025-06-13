# 💡 TP — Prompt Engineering  
**Auteur : Oumayma Mesbahi**

Ce projet explore le rôle du **Prompt Engineering** dans l’utilisation de l’IA générative appliquée au développement logiciel. À travers plusieurs exercices, nous analysons comment différents types de prompts influencent la **qualité**, la **robustesse** et la **structuration** du code généré.

---

## 🧠 Partie 1 — Choix de la Solution d’IA Générative

### ✅ 1. Outil Sélectionné
> **Gemini (anciennement Bard)** : un LLM avancé développé par Google, accessible via une interface de type chatbot.

### 📌 2. Définition Synthétique
IA générative capable de produire et comprendre du **langage naturel** et du **code source**, utilisée notamment pour :
- Génération de code
- Débogage
- Documentation
- Refactoring

### ⚙️ 3. Avantages
- 🚀 **Prototypage rapide** : création rapide de structures ou scripts de base.
- 🛠️ **Aide au débogage** : analyse d’erreurs, suggestions d’améliorations.
- 📄 **Documentation & tests** : génération automatisée de docstrings, README, tests unitaires.

### ⚠️ 4. Limites Identifiées
- 🎭 **Hallucinations** : production de code incorrect ou inexistant.
- 🔍 **Sensibilité au prompt** : résultats très dépendants de la clarté de la requête.
- 📅 **Obsolescence potentielle** : absence de mises à jour implicites sans contexte explicite.

### 🧰 5. Cas d’usage pertinents
- Refactoring
- Traduction inter-langages
- Apprentissage assisté (concepts, bibliothèques, exemples)

---

## 🧪 Partie 2 — Expérimentation : Génération de Code

### 🔍 Exercice 2.1 — Comparaison de Prompts

#### ⚫ Prompt Vague
- Génère une fonction `effectuer_operation`
- Prise en charge de +, -, *, /
- Gestion basique des erreurs (division par zéro, opérateur inconnu)
- Présence de docstrings et commentaires

#### ⚫ Prompt Spécifique
- Amélioration de la **lisibilité** et de la **documentation**
- Respect des contraintes : nom `calculate`, arrondi à deux décimales
- Gestion d’erreurs toujours perfectible (`return` au lieu de `raise`)

#### ⚫ Prompt avec Persona
- Résultat plus **professionnel** :
  - Typage (`type hinting`)
  - Bloc `if __name__ == "__main__"`
  - Docstring intégrant des **doctests**
- Bonne structuration, mais erreur récurrente : retour de chaînes au lieu d’exceptions

#### ✅ Synthèse
- Le **prompt spécifique** offre le meilleur compromis en termes de fonctionnalité.
- Le **persona** améliore nettement le **style et la structure**.
- Faiblesse persistante : mauvaise gestion des erreurs dans tous les cas.

---

### 🔧 Exercice 2.2 — Approches Zero-shot, One-shot, Few-shot

#### ⚫ Zero-shot
- Interprétation ambiguë de la règle de formatage
- Gestion des erreurs correcte via `raise`
- Fonctionne, mais comporte des risques logiques

#### ⚫ One-shot
- Exemple explicite qui lève l’ambiguïté
- Résultat conforme aux attentes métier
- La logique devient plus précise

#### ⚫ Few-shot
- Ajout de plusieurs exemples
- Renforce la robustesse et prévient les mauvaises interprétations
- Peu ou pas de changement si le modèle est déjà bien orienté

#### ✅ Analyse
- Les exemples améliorent :
  - La compréhension de la règle métier
  - La qualité des résultats générés
- Le **few-shot** est très efficace pour :
  - Cas limites
  - Règles complexes
  - Reproduction d’un style spécifique

---

## 🧮 Comparaison : Calculatrice Simple vs Calculatrice Avancée

| **Critère**             | **Calculatrice Simple**            | **Calculatrice Avancée**                            |
|------------------------|------------------------------------|-----------------------------------------------------|
| 🎨 **Design**           | Minimaliste, thème clair           | Moderne, thème sombre, ergonomie améliorée          |
| 🧱 **Structure du code**| Boutons liés directement au texte  | Utilisation de `data-action`, gestion d’état propre |
| 🔒 **Robustesse**       | Failles lors d’utilisations intensives | Gestion soignée des erreurs et cas particuliers |

> ✅ **Conclusion** : La version avancée est plus **professionnelle, maintenable et fiable**.

---

## 🧹 Partie 3 — Débogage et Refactoring avec l’IA

### 🧼 Refactoring (Exercice 3.2)
**Code de départ** :
- Tri à bulles rudimentaire
- Faible lisibilité (noms de variables ambigus)
- Aucune fonction, pas de commentaires

**Améliorations apportées par l’IA** :
- Encapsulation dans des fonctions
- Ajout de docstrings et commentaires
- Clarification du nommage

---

### 📚 Documentation Automatisée (Exercice 3.3)

#### Fonction : `get_user_permissions(user_id, system_context)`
Détermine les permissions attribuées à un utilisateur selon son rôle.

##### 📥 Paramètres
- `user_id` : int ou str
- `system_context` : dictionnaire contenant :
```python
{
  'admins': {101, 105},
  'editors': {202, 304}
}
```

##### 📤 Retour
- Liste des permissions (ex. : `['read', 'write']`)

##### ✅ Exemple d’appel :
```python
permissions_admin = get_user_permissions(101, system_roles)
# Résultat : ['read', 'write', 'delete', 'admin']
```

---

## ✅ Conclusion Générale

- Un **prompt bien formulé** améliore significativement la qualité du code généré.
- Le **few-shot prompting** est un levier puissant pour réduire les ambiguïtés et renforcer la cohérence.
- Malgré l’avancée des IA génératives, la **formulation du prompt reste déterminante** dans la qualité du résultat obtenu.
