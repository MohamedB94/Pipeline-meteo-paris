from app.fetch_api import fetch_donnees_meteo
from app.database import create_Table , insert_Meteo

def main():
    print("Initialisation de la base...")
    create_Table()

    print("Récupération des données météo...")
    data = fetch_donnees_meteo()

    if data: 
        print("Insertion des données dans la base...")
        insert_Meteo(data)
        print("Données insérées avec succès.")
    else:
        print("Aucune donnée à insérer.")
if __name__ == "__main__":
    main()
