from app.config import get_Connection

def create_Table():
    print("📦 Tentative de création de la table meteo...")
    conn = get_Connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS meteo (
            id int auto_increment PRIMARY KEY,
            ville varchar(50),
            temperature float,
            description varchar(100),
            humidite int,
            vent float,
            timestamp date UNIQUE
            );
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_Meteo(data):
    conn = get_Connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO meteo (ville, temperature, description, humidite, vent, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s);
        """, (data['ville'], data['temperature'], data['description'],
              data['humidite'], data['vent'], data['timestamp']))
    conn.commit()
    cur.close()
    conn.close()
