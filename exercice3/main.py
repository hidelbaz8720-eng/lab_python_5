
from csv_reader import (
    charger_csv,
    CsvException,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)

import logging

# Configuration du logger
logging.basicConfig(
    filename="erreurs.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():

    try:
        articles = charger_csv("C:\\Users\\ASUS\\Documents\\les_labs\\lab5_pyhton\\exercice3\\articles.csv")

        print("Importation réussie !")

        for article in articles:
            print(article)

    except FichierIntrouvableException as e:
        print("Erreur fichier :", e)
        logging.error(str(e))

    except LigneInvalideException as e:
        print("Erreur de ligne :", e)
        logging.error(str(e))

    except PrixNegatifException as e:
        print("Erreur de prix :", e)
        logging.error(str(e))

    except CsvException as e:
        print("Erreur CSV :", e)
        logging.error(str(e))


if __name__ == "__main__":
    main()
