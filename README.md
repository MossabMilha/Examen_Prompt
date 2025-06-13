# 💡 TP Prompt Engineering — Oumayma Mesbahi

Ce projet explore le rôle du **Prompt Engineering** dans l'utilisation d'IA générative pour le développement logiciel. À travers une série d'exercices, nous évaluons l’impact de différents types de prompts sur la qualité, la robustesse, et la professionnalisation du code généré.

---

## 🧠 Partie 1 : Choix de la Solution d'IA Générative

### ✅ 1. Solution Choisie
> **Gemini (anciennement Bard)** — modèle LLM avancé de Google, utilisé via une interface de chat.

### 📌 2. Définition Brève
IA générative capable de comprendre et produire du **langage naturel** et du **code**. Elle fonctionne comme un assistant conversationnel polyvalent pour :
- Génération de code
- Débogage
- Documentation
- Refactoring

### ⚙️ 3. Avantages
- **Prototypage rapide** : Génère des structures de code ou des applications simples.
- **Assistance au débogage** : Analyse d’erreurs (tracebacks), suggestions d’algorithmes.
- **Documentation et tests automatisés** : Rédaction de docstrings, README, et tests unitaires.

### ⚠️ 4. Inconvénients
- **Hallucinations** : Code inventé ou logiquement erroné.
- **Sensibilité au contexte** : Les réponses dépendent de la clarté du prompt.
- **Obsolescence** : Non informée des mises à jour récentes sans contexte explicite.

### 🧰 5. Cas d’Usage Typiques
- Refactoring
- Traduction de code entre langages
- Apprentissage (explication de concepts, bibliothèques, etc.)

---

## 🧪 Partie 2 : Génération de Code avec l'IA

### 🔍 Exercice 2.1 — Vague vs. Spécifique vs. Persona

#### ⚫ Prompt Vague
- Fonction générée : `effectuer_operation`
- Opérations : +, -, *, /
- Gestion d’erreurs basique (ex : division par zéro, opérateur invalide)
- Bon docstring et commentaires

#### ⚫ Prompt Spécifique
- Meilleure **lisibilité** et **documentation**
- Respect des exigences : nom `calculate`, arrondi à 2 décimales
- Toujours même défaut de gestion d’erreurs (retour de str au lieu de `raise`)

#### ⚫ Prompt Persona
- Apparence très professionnelle
  - Type hinting
  - Bloc `if __name__ == "__main__"`
  - Doctest dans le docstring
- Structure soignée mais **même erreur critique** (str au lieu d’exception)

#### 🔎 Synthèse de l’Exercice
- **Spécificité** : Meilleur impact fonctionnel
- **Persona** : Meilleur style et structure
- **Failles persistantes** : Mauvaise gestion des erreurs dans toutes les versions

---

### 🔧 Exercice 2.2 — Zero-shot vs One-shot vs Few-shot

#### ⚫ Zero-Shot
- Interprétation ambigüe : mauvaise règle d’insertion de tirets
- Très bonne gestion des erreurs (`raise ValueError`)
- Fonctionnel mais possiblement incorrect

#### ⚫ One-Shot (avec exemple)
- Ambiguïté levée
- Résultat conforme aux attentes
- L’exemple simplifie et **oriente correctement la logique métier**

#### ⚫ Few-Shot (avec multiples exemples)
- Renforce la robustesse de la génération
- Ne change pas le code final (déjà robuste)
- Réduit les risques d’interprétation incorrecte

#### 🔎 Analyse Critique
- L’ajout d’exemples :
  - Clarifie les règles complexes
  - Renforce les bonnes pratiques
- Le **Few-Shot** est particulièrement utile pour :
  - Cas limites
  - Règles complexes
  - Reproduire un style spécifique

---

## 🧮 Comparaison : Calculatrice Simple vs Avancée

| Critère                 | Calculatrice Simple                | Calculatrice Avancée                          |
|------------------------|------------------------------------|-----------------------------------------------|
| **Design**             | Basique, thème clair               | Moderne, thème sombre, ergonomie soignée      |
| **Structure du Code**  | Directe, dépend du texte des boutons | Professionnelle, usage de `data-action`, état centralisé |
| **Robustesse**         | Limitée, erreurs si clics répétés  | Meilleure gestion des cas limites             |

**Conclusion** : La calculatrice avancée est plus **professionnelle, maintenable et fiable**.

---

## 🧹 Partie 3 : Débogage et Refactoring

### 🧼 Exercice 3.2 — Refactoring avec l'IA
**Code initial** :
- Algorithme : tri à bulles
- Problèmes :
  - Variables non explicites (`a, i, j`)
  - Aucune fonction
  - Pas de commentaire, code peu réutilisable

**IA a permis de** :
- Structurer le code avec fonctions
- Ajouter docstrings et lisibilité

---

### 📚 Exercice 3.3 — Documentation Générée

#### Fonction : `get_user_permissions(user_id, system_context)`
Détermine les permissions utilisateur selon leur rôle (Admin > Éditeur > Utilisateur).

##### 📥 Paramètres
- `user_id` : int ou str
- `system_context` : dict avec :
```python
{
    'admins': {101, 105},
    'editors': {202, 304}
}
```

##### 📤 Retour
- Liste des permissions (ex : `['read', 'write']`)

##### 📘 Exemple :
```python
permissions_admin = get_user_permissions(101, system_roles)
# Résultat : ['read', 'write', 'delete', 'admin']
```

---

## ✅ Conclusion Générale

- Un bon **prompt spécifique** améliore considérablement le code produit.
- Le **prompting par exemple (Few-Shot)** est crucial pour éviter les erreurs subtiles.
- Même avec une IA puissante, l’interprétation d’un prompt reste **sensible** : la formulation est clé.
