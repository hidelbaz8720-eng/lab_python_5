
class ReservationException(Exception):
    def __init__(self, message):
        super().__init__(message)


# 2. Exceptions filles
class CapaciteDepasseeException(ReservationException):
    pass


class NombreInvalideException(ReservationException):
    pass


class NomClientInvalideException(ReservationException):
    pass


class Evenement:

    def __init__(self, nom, capacite):
        self.nom = nom
        self.capacite = capacite
        self.places_reservees = 0

    def reserver(self, nom_client, nb_places):

        if not nom_client.strip():
            raise NomClientInvalideException(
                "Nom du client requis."
            )

        if nb_places <= 0:
            raise NombreInvalideException(
                "Nombre de places invalide."
            )

        if self.places_reservees + nb_places > self.capacite:
            raise CapaciteDepasseeException(
                "Capacite depassee."
            )

        self.places_reservees += nb_places

        print(
            f"Reservation confirmee pour {nom_client} "
            f"({nb_places} places)."
        )

    # Afficher les informations
    def afficher(self):
        print(f"evenement : {self.nom}")
        print(
            f"Places : {self.places_reservees}"
            f"/{self.capacite}"
        )



event = Evenement("Concert", 5)

try:
    event.reserver("Hamza", 2)
    event.reserver("Ali", 2)
    event.reserver("Sara", 2)

except ReservationException as e:
    print("Erreur :", e)

finally:
    print("\netat final :")
    event.afficher()
