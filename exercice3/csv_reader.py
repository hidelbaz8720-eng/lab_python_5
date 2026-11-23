
import csv
import os


# 1. Exception mère
class CsvException(Exception):
    pass


# 2. Exceptions personnalisées
class FichierIntrouvableException(CsvException):
    pass


class LigneInvalideException(CsvException):
    pass


class PrixNegatifException(CsvException):
    pass


# 3. Fonction de lecture CSV
def charger_csv(chemin):

    # Vérifier l'existence du fichier
    if not os.path.isfile(chemin):
        raise FichierIntrouvableException(
            "Le fichier CSV est introuvable."
        )

    articles = []

    try:
        with open(chemin, "r", encoding="utf-8", newline="") as fichier:

            lecteur = csv.reader(fichier, delimiter=";")

            # Lire l'en-tête
            entete = next(lecteur, None)

            if entete != ["id", "nom", "prix"]:
                raise LigneInvalideException(
                    "En-tête CSV incorrect."
                )

            # Lire les lignes suivantes
            for numero, ligne in enumerate(lecteur, start=2):

                # Ignorer les lignes vides
                if not ligne or all(
                    valeur.strip() == "" for valeur in ligne
                ):
                    continue

                # Vérifier le nombre de colonnes
                if len(ligne) != 3:
                    raise LigneInvalideException(
                        f"Ligne {numero} : 3 colonnes attendues."
                    )

                identifiant, nom, prix = [
                    valeur.strip() for valeur in ligne
                ]

                # Vérifier les champs obligatoires
                if not identifiant or not nom:
                    raise LigneInvalideException(
                        f"Ligne {numero} : ID ou nom manquant."
                    )

                # Vérifier le prix numérique
                try:
                    prix = float(prix)
                except ValueError:
                    raise LigneInvalideException(
                        f"Ligne {numero} : prix non numérique."
                    )

                # Vérifier le prix positif
                if prix <= 0:
                    raise PrixNegatifException(
                        f"Ligne {numero} : prix doit être positif."
                    )

                # Ajouter l'article
                article = {
                    "id": identifiant,
                    "nom": nom,
                    "prix": prix
                }

                articles.append(article)

    except UnicodeDecodeError:
        raise LigneInvalideException(
            "Le fichier n'est pas encodé correctement."
        )

    return articles
