from app.database import create_Table, insert_Meteo
from app.fetch_api import fetch_donnees_meteo

def main():
    print("Création de la table...")
    create_Table()  

    print("Récupération des données météo...")
    data = fetch_donnees_meteo()

    if data:
        print("Insertion dans la base...")
        insert_Meteo(data)
        print("✅ Données insérées avec succès.")
    else:
        print("❌ Aucune donnée récupérée.")

if __name__ == "__main__":
    main()
