
# TP 5 – Gestion des Exceptions en Python

## Informations générales

- **Module :** Programmation Orientée Objet (POO)
- **Langage :** Python
- **TP :** 5 – Exceptions
- **Plateforme :** MLIAEdu
- **Étudiant :** Hamza ID EL BAZ

---

##  Objectif du TP

Ce TP a pour objectif de maîtriser la gestion des erreurs en Python à travers les exceptions natives et personnalisées.

Les compétences développées :

- Créer des exceptions personnalisées.
- Utiliser l'héritage entre exceptions.
- Comprendre `try`, `except`, `finally` et `raise`.
- Valider les données avant leur traitement.
- Gérer les erreurs liées aux fichiers.
- Utiliser le module `logging`.
- Réaliser des tests unitaires avec `unittest`.

---

##  Exercice 1 – Compte bancaire

### Objectif
Créer une exception personnalisée pour gérer les retraits avec un solde insuffisant.

### Concepts utilisés
- Héritage de la classe `Exception`.
- Création d'une exception `SoldeInsuffisantException`.
- Utilisation de `raise`.
- Gestion des erreurs avec `try / except`.

### Exemple de résultat

```text
Compte: Alice, Solde: 100€
Erreur: Solde insuffisant pour ce retrait.
```

---
<img width="1920" height="1080" alt="ex1" src="https://github.com/user-attachments/assets/4f403012-238c-4059-a349-624949002e5f" />

##  Exercice 2 – Système de réservation

### Objectif
Développer un système de réservation avec plusieurs exceptions personnalisées.


### Validations réalisées

- Vérifier que le nom du client n'est pas vide.
- Vérifier que le nombre de places est positif.
- Vérifier que la capacité maximale n'est pas dépassée.

### Exemple de résultat

```text
Erreur: Nom du client requis.
```

---
<img width="1920" height="1080" alt="ex2" src="https://github.com/user-attachments/assets/1a704645-73d0-4fde-b6bf-43aef829e175" />

##  Exercice 3 – Import CSV sécurisé

### Objectif
Développer un système d'importation CSV sécurisé permettant de lire et de valider les informations des articles.

### Format du fichier CSV

```csv
id;nom;prix
1;Clavier;150
2;Souris;80
3;Ecran;1200
```

<img width="1920" height="1080" alt="ex3" src="https://github.com/user-attachments/assets/ebe4e742-79f4-463e-8829-984b779b0a47" />

### Fonctionnalités

- Vérification de l'existence du fichier.
- Lecture du fichier CSV avec `csv.reader`.
- Vérification du nombre de colonnes.
- Ignorer les lignes vides.
- Vérification des données obligatoires.
- Conversion du prix en `float`.
- Refus des prix nuls ou négatifs.
- Journalisation des erreurs avec `logging`.
- Tests unitaires avec `unittest`.








##  Notions essentielles retenues

| Instruction | Rôle |
|---|---|
| `try` | Tester un bloc de code |
| `except` | Capturer une exception |
| `finally` | Exécuter un bloc dans tous les cas |
| `raise` | Déclencher une exception |
| `Exception` | Classe mère des exceptions |
| `super()` | Appeler la classe mère |
| `with open()` | Ouvrir et fermer automatiquement un fichier |
| `assertRaises()` | Vérifier qu'une exception est déclenchée |

---

##  Conclusion

Ce TP m'a permis de renforcer mes connaissances en programmation orientée objet avec Python, notamment dans la création et la gestion des exceptions personnalisées.

J'ai également appris à organiser un projet en plusieurs fichiers, à sécuriser l'importation de données CSV et à vérifier le bon fonctionnement du programme à l'aide de tests unitaires.

---

**Réalisé par : Hamza ID EL BAZ**
