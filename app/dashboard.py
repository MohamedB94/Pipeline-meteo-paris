import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import config

from app.queries import (
    get_ajd_meteo, get_temp_delta, get_nb_jours, get_moy_dernier_7_jours,
    get_jour_plus_chaud, get_jour_plus_froid, get_30_derniers_jours,
    get_temps_par_jour, get_temps_par_semaine, get_temps_par_mois
)

# Titre
st.title("📊 Dashboard Météo - Paris")

# Filtres jour / semaine / mois
st.markdown("### 📅 Filtrer par période")
option = st.selectbox("Choisir la période :", ["Jour", "Semaine", "Mois"])

# Récupération des données selon la période sélectionnée 
if option == "Jour":
    df_filtres = get_temps_par_jour()
    
   
    
    if not df_filtres.empty:
        try:
            # Gestion des colonnes numériques (conversion manuelle) ou des colonnes nommées
            df_filtres = df_filtres.rename(columns={
                0: "Date", 
                1: "Température (°C)"
            } if 0 in df_filtres.columns else {
                "date": "Date", 
                "temperature": "Température (°C)"
            })
            
            # Conversion en type numérique avant arrondi
            df_filtres["Température (°C)"] = pd.to_numeric(df_filtres["Température (°C)"], errors='coerce')
            df_filtres["Température (°C)"] = df_filtres["Température (°C)"].round(1)
            st.dataframe(df_filtres, use_container_width=True)
        except Exception as e:
            st.error(f"Erreur lors du traitement des données: {str(e)}")
    else:
        st.warning("Aucune donnée disponible dans la base de données.")
elif option == "Semaine":
    df_filtres = get_temps_par_semaine()
    # Formatage des colonnes pour l'affichage
    df_filtres = df_filtres.rename(columns={"semaine": "Semaine", "temperature": "Température moyenne (°C)"})
    # Conversion en type numérique avant arrondi
    df_filtres["Température moyenne (°C)"] = pd.to_numeric(df_filtres["Température moyenne (°C)"], errors='coerce')
    df_filtres["Température moyenne (°C)"] = df_filtres["Température moyenne (°C)"].round(1)
    st.dataframe(df_filtres, use_container_width=True)
elif option == "Mois":
    df_filtres = get_temps_par_mois()
    # Formatage des colonnes pour l'affichage
    df_filtres = df_filtres.rename(columns={"mois": "Mois", "temperature": "Température moyenne (°C)"})
    # Conversion en type numérique avant arrondi
    df_filtres["Température moyenne (°C)"] = pd.to_numeric(df_filtres["Température moyenne (°C)"], errors='coerce')
    df_filtres["Température moyenne (°C)"] = df_filtres["Température moyenne (°C)"].round(1)
    st.dataframe(df_filtres, use_container_width=True)

# Métriques
col1, col2, col3 = st.columns(3)
col1.metric("Température actuelle", f"{get_ajd_meteo()} °C", f"{get_temp_delta()} °C depuis hier")
col2.metric("Jours collectés", get_nb_jours())
col3.metric("Moyenne des 7 derniers jours", f"{get_moy_dernier_7_jours()} °C")

# Infos supplémentaires
st.markdown("### Journée la plus chaude / froide de la semaine")
st.write(f"🔥 Plus chaud : {get_jour_plus_chaud()}")
st.write(f"❄️ Plus froid : {get_jour_plus_froid()}")

# Tableau des 30 derniers jours (au lieu du graphique)
st.markdown("### 📈 Températures des 30 derniers jours")
df_30j = get_30_derniers_jours()

if not df_30j.empty:
    try:
        # Gestion des colonnes numériques (conversion manuelle) ou des colonnes nommées
        df_30j = df_30j.rename(columns={
            0: "Date", 
            1: "Température (°C)"
        } if 0 in df_30j.columns else {
            "timestamp": "Date", 
            "temperature": "Température (°C)"
        })
        
        # Conversion en type numérique avant arrondi
        df_30j["Température (°C)"] = pd.to_numeric(df_30j["Température (°C)"], errors='coerce')
        df_30j["Température (°C)"] = df_30j["Température (°C)"].round(1)
        st.dataframe(df_30j, use_container_width=True)
    except Exception as e:
        st.error(f"Erreur lors du traitement des données sur 30 jours: {str(e)}")
else:
    st.warning("Aucune donnée météo disponible.")
