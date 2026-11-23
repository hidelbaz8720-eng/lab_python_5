
import unittest
import tempfile
import os

from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)


class TestCSV(unittest.TestCase):

    def creer_fichier(self, contenu):
        fichier = tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="",
            suffix=".csv",
            delete=False
        )

        fichier.write(contenu)
        fichier.close()

        self.addCleanup(os.unlink, fichier.name)

        return fichier.name

    # Test 1 : CSV valide
    def test_csv_valide(self):
        chemin = self.creer_fichier(
            "id;nom;prix\n"
            "1;Clavier;150\n"
            "2;Souris;80\n"
        )

        resultat = charger_csv(chemin)

        self.assertEqual(len(resultat), 2)
        self.assertEqual(resultat[0]["nom"], "Clavier")
        self.assertEqual(resultat[0]["prix"], 150.0)

    # Test 2 : fichier absent
    def test_fichier_absent(self):
        with self.assertRaises(FichierIntrouvableException):
            charger_csv("fichier_inexistant.csv")

    # Test 3 : prix texte
    def test_prix_non_numerique(self):
        chemin = self.creer_fichier(
            "id;nom;prix\n1;Clavier;abc\n"
        )

        with self.assertRaises(LigneInvalideException):
            charger_csv(chemin)

    def test_prix_negatif(self):
        chemin = self.creer_fichier(
            "id;nom;prix\n1;Clavier;-50\n"
        )

        with self.assertRaises(PrixNegatifException):
            charger_csv(chemin)

    #   nombre de colonnes incorrect
    def test_colonne_manquante(self):
        chemin = self.creer_fichier(
            "id;nom;prix\n1;Clavier\n"
        )

        with self.assertRaises(LigneInvalideException):
            charger_csv(chemin)


if __name__ == "__main__":
    unittest.main()
