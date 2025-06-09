import requests
from datetime import datetime
from app.config import get_Connection

def fetch_donnees_meteo(city="Paris"):
    API_KEY = "96ab46c9fbce575b28061bfde7539c94"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=fr"

    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()

        # Extraction des données utiles
        donnees_meteo = {
            "ville": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidite": data["main"]["humidity"],
            "vent": data["wind"]["speed"],
            "timestamp": datetime.utcfromtimestamp(data["dt"]).strftime('%Y-%m-%d')
        }

        # Insertion dans la base de données
        conn = get_Connection()
        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = """
                    INSERT INTO meteo (timestamp, temperature, description, humidite, vent, ville)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(sql, (
                        donnees_meteo["timestamp"],
                        donnees_meteo["temperature"],
                        donnees_meteo["description"],
                        donnees_meteo["humidite"],
                        donnees_meteo["vent"],
                        donnees_meteo["ville"]
                    ))
                conn.commit()
            except Exception as e:
                print(f"Erreur lors de l'insertion dans la base de données : {e}")
            finally:
                conn.close()

        return donnees_meteo
    
    except Exception as e:
        print(f"Erreur lors de la récupération des données météo : {e}")
        return None