Partie 1 : Choix de la Solution d'IA Générative

**1. Solution choisie :** 

ChatGPT (OpenAI)

**2. Définition brève de la solution :** 

ChatGPT est un modèle d'intelligence artificielle développé par OpenAI, capable de comprendre et de générer du langage naturel. Il est utilisé comme assistant de codage pour générer, corriger, expliquer ou améliorer du code dans plusieurs langages de programmation.

**3. Avantages perçus de cette solution pour le développement de code :**

- 💬 **Multifonctionnel** : peut expliquer du code, le commenter, le corriger ou générer de nouvelles fonctionnalités à partir d’une simple description.
- 🌍 **Polyglotte** : prend en charge une large variété de langages de programmation (Python, JavaScript, C, HTML, etc.).
- ⏱ **Gain de productivité** : permet d'accélérer le prototypage, la recherche d'erreurs ou l'exploration de solutions alternatives rapidement.

**4. Inconvénients ou limites perçues de cette solution :**

- ❌ **Pas toujours précis** : peut générer du code incorrect ou inefficace, nécessitant une vérification attentive.
- 📎 **Dépendance possible** : risque de limiter l’apprentissage actif chez certains étudiants ou développeurs débutants.
- 🔒 **Pas d’accès direct au projet ou aux fichiers** : contrairement à certains IDE intégrés, il ne voit pas directement votre arborescence de projet.

**5. Cas d'utilisation typiques :**

- 🚀 Génération rapide de fonctions ou d’algorithmes à partir d’une description en langage naturel.
- 🧪 Débogage ou explication de code complexe.
- 📖 Aide à l'apprentissage de nouveaux langages ou frameworks.
- 📝 Génération de documentation, commentaires ou tests unitaires.

Partie 2 – Génération de code avec IA

Exercice 2.1 :

**• Analyse Critique**

**1) Différences observées entre les codes :**

|**Aspect**|**Code 1**|**Code 2 (milieu)**|**Code 3 (final)**|
| :-: | :-: | :-: | :-: |
|**Nom de la fonction**|calculer|calculate|calculate|
|**Langue**|Français|Français pour le docstring, noms anglais pour la fonction/variables|Même chose que le deuxième|
|**Robustesse**|Faible : pas de vérification d’opérateur|Moyenne : gestion d’erreur basique mais claire, arrondi de division|Élevée : vérifie l’opérateur d'abord, gestion d’erreurs plus rigoureuse|
|**Clarté du code**|Très simple, peu de commentaires|Docstring bien structuré, mais logique perfectible|Docstring enrichi, logique plus robuste|
|**Conformité PEP8**|Non garantie|Meilleure, mais pas parfaite|Respecte mieux les conventions (docstring structuré, noms clairs, logique propre)|
|**Gestion des erreurs**|Division par zéro uniquement|Division par zéro + opérateur non reconnu (avec messages clairs)|Idem, mais avec vérification anticipée et docstring plus professionnelle|
|**Affichage du résultat**|Retour brut (int ou str)|Retour avec arrondi (2 décimales) pour division|Idem|
|**Documentation / Docstring**|Aucune|Moyenne : description simple + exemples|Excellente : structuration en sections (Paramètres, Retours, Exemples)|


**2) Principe de Prompt Engineering le plus impactant :**

**→ Le principe ayant le plus d’impact est *la spécificité*.**

- Dans le premier code, le prompt était probablement vague : résultat = code fonctionnel mais basique, sans docstring, ni robustesse.
- Dans les codes suivants, les prompts demandaient :
  - une **fonction robuste**,
  - avec une **documentation complète**,
  - et une **gestion des erreurs précises**.
- Cette **spécificité** du prompt a orienté l’IA vers des standards plus professionnels (PEP8, docstring détaillée, bonnes pratiques).

**3) Erreurs ou comportements inattendus :**

- Non, **aucune erreur manifeste** dans les trois codes. Toutefois :
- **Code 1** :
  - L’absence de vérification de l’opérateur (+, -, etc.) laisse une faille (retourne une erreur générique).
- **Code 2** :
  - La vérification de division par zéro est correcte mais **placée après** l’identification de l’opérateur. Cela peut être inefficace si l’opérateur est invalide.
- **Code 3** :
  - Pas d’erreur, au contraire : **logique améliorée** (on vérifie l’opérateur **avant** d’entrer dans la logique opérationnelle).
- Donc, l’IA a **progressivement corrigé ses propres faiblesses** au fur et à mesure que les prompts devenaient plus précis.


**4) Coût prompt vague vs. spécifique :**

|**Type de prompt**|**Résultat**|**Temps / effort estimé**|
| :-: | :-: | :-: |
|**Prompt vague**|Code fonctionnel mais peu robuste|Faible temps, mais demande des itérations manuelles ensuite|
|**Prompt spécifique**|Code robuste, documenté|Temps de formulation du prompt plus long, mais **moins d’effort après**|

Conclusion : Un prompt spécifique **réduit le nombre d’itérations** nécessaires. Il demande un peu plus d’effort initial, mais **économise beaucoup de temps globalement** en produisant un code plus professionnel dès le départ.

Exercice 2.1 :
#### ***1) Analyse sur l’impact des exemples :***
L’ajout d’exemples a **significativement amélioré la compréhension de l’IA**, notamment :

- La **structure précise du format de sortie** (positions des tirets).
- La gestion des **valeurs invalides** (longueur, caractères).
- La **cohérence** dans la levée des erreurs.

Sans exemple, l’IA pourrait deviner un mauvais format. Avec un seul exemple, elle applique correctement **le même schéma**. Avec plusieurs, elle **généralise mieux** et gère les erreurs.

#### ***2) Quand le Few-Shot Prompting est-il particulièrement utile ?***
- Lorsqu’il faut suivre **des formats très précis** (ex. : codes produits, numéros de série).
- Quand la **règle métier est implicite ou ambigüe**.
- Pour gérer des cas limites (ValueError, format partiel, mauvaise longueur…).
- Utile aussi pour former l’IA à **différents scénarios** : bon format, mauvais format, cas d’erreur, etc.

#### ***3) Y a-t-il des limites aux exemples (nombre, qualité) ?***
✅ **OUI** – deux grandes limites :

- **Qualité des exemples :** Un mauvais exemple peut induire l’IA en erreur, surtout si la logique décrite n’est pas claire.
- **Nombre d’exemples :** Trop d’exemples peuvent rendre le prompt confus ou ralentir la réponse. Il vaut mieux **2-3 exemples bien choisis** que 6 similaires.

Partie 3 – Débogage et Amélioration du Code  

Exercice 3.1 Débogage assisté :
### **1) Exécution du code et observation de l'erreur**
- Type : TypeError
- Message : unsupported operand type(s) for +=: 'int' and 'str'
- Localisation : Ligne total += num
- Contexte : Tentative de sommation d'un entier avec la chaîne 'three' dans la liste my\_nums = [1, 2, 'three', 4].
### **2) Message d'erreur complet et identification de la cause**
- Correctifs appliqués :
- Validation des types avant calcul
- Gestion des listes vides (évitement de DivisionByZero)
- Messages d'erreur contextualisés
- Ajout de documentation fonctionnelle
### **3) Tests unitaires avec pytest**
- **Cas nominaux** :
  - Listes homogènes (entiers/décimaux)
  - Listes mixtes (entiers + décimaux)
  - Singleton numérique
- **Cas d'erreur** :
  - Liste vide
  - Éléments non numériques
  - Valeurs None
- **Tests d'exceptions** : Vérification du relèvement d'exceptions spécifiques.

Exercice 3.2 Refactoring avec l’IA :
### **1) Analyse du code fourni**
- **Algorithme identifié** : Tri par sélection (à corriger depuis "tri à bulles")
- **Problématiques relevées** :
  - **Lisibilité** : Variables obscures (a, i, j, tmp)
  - **Structure** : Code monolothique, non modulaire
  - **Documentation** : Absence de docstrings/commentaires
  - **Robustesse** : Aucune validation des inputs
### **2) Prompt de refactoring clair**
Refactorisez ce code de tri en implémentant les bonnes pratiques suivantes

**3) Ajouter des contraintes**

Refactorisez ce code de tri en implémentant les bonnes pratiques suivantes

- **PEP8** : Conformité stricte (nommage, espaces, longueur ligne ≤79 caractères)
- **Documentation** : Docstrings complètes (paramètres, retour, exemples)
- **Modularité** : Découpage en fonctions SRP (*Single Responsibility Principle*)
- **Sémantique** : Renommage des variables (array au lieu de a, index au lieu de i, etc.)
- **Exécution contrôlée** : Bloc if \_\_name\_\_ == '\_\_main\_\_': pour usage modularisable

## 🧹 Partie 3 – Débogage et Refactoring avec l’IA

### 🧼 Exercice 3.2 – Refactoring Assisté par IA

#### 🔧 **Code initial** :
- Implémentation basique du tri à bulles.
- Noms de variables peu explicites (`a`, `i`, `j`, etc.).
- Absence de structure fonctionnelle et de commentaires.

#### 💡 **Refactoring réalisé par l’IA** :
- Encapsulation du tri dans une fonction nommée (`bubble_sort`).
- Respect des conventions **PEP8** (indentation, nommage, longueur des lignes).
- Introduction de **docstrings** structurées (Paramètres, Retour, Exemples).
- Renommage des variables pour améliorer la clarté (`array`, `index`, etc.).
- Ajout d’un bloc `if __name__ == "__main__":` pour faciliter la réutilisation du code.

---

### 📚 Exercice 3.3 – Documentation Automatisée

#### 🧠 **Fonction générée** : `get_user_permissions(user_id, system_context)`

Cette fonction détermine dynamiquement les permissions associées à un utilisateur, en fonction de son rôle défini dans le contexte du système.

##### 🔢 **Paramètres**
- `user_id` *(int ou str)* : identifiant de l'utilisateur à analyser.
- `system_context` *(dict)* : dictionnaire des rôles du système, par exemple :
```python
{
  'admins': {101, 105},
  'editors': {202, 304}
}
```

##### 📤 **Retour**
- Liste des permissions attribuées à l'utilisateur (ex. : `['read', 'write']`).

##### ✅ **Exemple d’appel**
```python
system_roles = {
  'admins': {101, 105},
  'editors': {202, 304}
}

permissions_admin = get_user_permissions(101, system_roles)
# Résultat : ['read', 'write', 'delete', 'admin']
```

> 🔎 Cette documentation a été générée automatiquement grâce à un prompt bien conçu, démontrant la capacité de l’IA à comprendre l’intention métier et à la traduire en interface fonctionnelle documentée.

---

## ✅ Conclusion Générale

- 🧠 Un **prompt précis, structuré et contextuel** améliore considérablement la qualité, la robustesse et la lisibilité du code généré.
- 📌 Le **few-shot prompting** (ajout d’exemples dans le prompt) permet à l’IA de mieux généraliser et de gérer les cas limites efficacement.
- 🧰 L’IA ne remplace pas la compréhension humaine, mais **augmente la productivité** et permet de se concentrer sur les aspects complexes du développement.
- ✍️ En résumé : **la qualité du résultat dépend directement de la qualité de la formulation**.
