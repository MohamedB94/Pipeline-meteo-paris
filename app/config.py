import pymysql

def get_Connection():
    try:
        return pymysql.connect(
            host='mysql',  # nom du service Docker
            user='root',
            password='root',
            database='meteo_db',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.MySQLError as e:
        print("❌ Erreur de connexion MySQL :", e)
        return None
