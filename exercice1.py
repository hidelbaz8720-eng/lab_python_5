
class SoldeInsuffisantException(Exception):
    def __init__(self, message):
        super().__init__(message)


class CompteBancaire:
    def __init__(self, nom, solde=0):
        self.nom = nom
        self.solde = solde

    def deposer(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")

        self.solde += montant
        print("Dépôt effectué !")

    def retirer(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")

        if montant > self.solde:
            raise SoldeInsuffisantException(
                "Solde insuffisant pour ce retrait."
            )

        self.solde -= montant
        print("Retrait effectué !")

    def afficher(self):
        print(f"Compte : {self.nom}")
        print(f"Solde : {self.solde} €")


# Programme principal
compte = CompteBancaire("Hamza", 100)

try:
    compte.afficher()
    compte.retirer(150)

except SoldeInsuffisantException as e:
    print("Erreur :", e)

except ValueError as e:
    print("Montant invalide :", e)

finally:
    print("Fin de l'opération.")
    compte.afficher()
