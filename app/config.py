import pymysql

def get_Connection():
    try:
        return pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='meteo_db',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.MySQLError as e:
        print(f"Erreur de connexion à la base de données : {e}")
        return None
    