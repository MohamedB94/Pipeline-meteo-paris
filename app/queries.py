from app.config import get_Connection
import pandas as pd

def get_ajd_meteo():
    conn = get_Connection()
    cur = conn.cursor()
    cur.execute("SELECT temperature FROM meteo WHERE timestamp = CURDATE();")
    resultat = cur.fetchone()
    cur.close()
    conn.close()
    return round(resultat['temperature'], 1) if resultat else "N/A"

def get_temp_delta():
    conn = get_Connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT temperature
        FROM meteo
        WHERE timestamp IN (CURDATE(), CURDATE() - INTERVAL 1 DAY)
        ORDER BY timestamp;
    """)
    resultats = cur.fetchall()
    cur.close()
    conn.close()

    if len(resultats) == 2:
        return round(resultats[1]['temperature'] - resultats[0]['temperature'], 1)
    return "N/A"

def get_nb_jours():
    conn = get_Connection()
    cur = conn.cursor()
    cur.execute("sELECT COUNT(*) AS count FROM meteo;")
    resultat = cur.fetchone()
    cur.close()
    conn.close()
    return resultat['count']

def get_moy_dernier_7_jours():
    conn = get_Connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT AVG(temperature) AS moy_temp
        FROM meteo
        WHERE timestamp >= CURDATE() - INTERVAL 7 DAY;
    """)
    resultat = cur.fetchone()
    cur.close()
    conn.close()
    return round(resultat['moy_temp'], 1) if resultat ['moy_temp'] else "N/A"

def get_jour_plus_chaud():
    conn = get_Connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT timestamp, temperature
        FROM meteo
        WHERE timestamp >= CURDATE() - INTERVAL 7 DAY
        ORDER BY temperature DESC
        LIMIT 1;
    """)
    resultat = cur.fetchone()
    cur.close()
    conn.close()
    return f"{resultat['timestamp']} ({resultat['temperature']} °C)" if resultat else "N/A"

def get_jour_plus_froid():
    conn = get_Connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT timestamp, temperature
        FROM meteo
        WHERE timestamp >= CURDATE() - INTERVAL 7 DAY
        ORDER BY temperature ASC
        LIMIT 1;
    """)
    resultat = cur.fetchone()
    cur.close()
    conn.close()
    return f"{resultat['timestamp']} ({resultat['temperature']} °C)" if resultat else "N/A"

def get_30_derniers_jours():
    conn = get_Connection()
    # Return timestamp directly instead of formatting in MySQL
    df = pd.read_sql_query("""
        SELECT timestamp, temperature
        FROM meteo
        WHERE timestamp >= CURDATE() - INTERVAL 30 DAY
        ORDER BY timestamp ASC;
    """, conn)
    conn.close()
    return df

def get_temps_par_jour():
    conn = get_Connection()
    df = pd.read_sql_query("""
        SELECT timestamp AS date, temperature
        FROM meteo
        ORDER BY timestamp ASC;
    """, conn)
    conn.close()
    return df

def get_temps_par_semaine():
    conn = get_Connection()
    df = pd.read_sql_query("""
        SELECT DATE_FORMAT(timestamp, '%%Y-%%u') AS semaine, AVG(temperature) AS temperature
        FROM meteo
        GROUP BY semaine
        ORDER BY semaine ASC;
    """, conn)
    conn.close()
    return df

def get_temps_par_mois():
    conn = get_Connection()
    df = pd.read_sql_query("""
        SELECT DATE_FORMAT(timestamp, '%%Y-%%m') AS mois, AVG(temperature) AS temperature
        FROM meteo
        GROUP BY mois
        ORDER BY mois ASC;
    """, conn)
    conn.close()
    return df
