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

if option == "Jour":
    df_filtres = get_temps_par_jour()
    st.line_chart(df_filtres.set_index("date")["temperature"])
elif option == "Semaine":
    df_filtres = get_temps_par_semaine()
    st.line_chart(df_filtres.set_index("semaine")["temperature"])
elif option == "Mois":
    df_filtres = get_temps_par_mois()
    st.line_chart(df_filtres.set_index("mois")["temperature"])

# Métriques
col1, col2, col3 = st.columns(3)
col1.metric("Température actuelle", f"{get_ajd_meteo()} °C", f"{get_temp_delta()} °C depuis hier")
col2.metric("Jours collectés", get_nb_jours())
col3.metric("Moyenne des 7 derniers jours", f"{get_moy_dernier_7_jours()} °C")

# Infos supplémentaires
st.markdown("### Journée la plus chaude / froide de la semaine")
st.write(f"🔥 Plus chaud : {get_jour_plus_chaud()}")
st.write(f"❄️ Plus froid : {get_jour_plus_froid()}")

# Graphique des 30 derniers jours
st.markdown("### 📈 Températures des 30 derniers jours")
df_30j = get_30_derniers_jours()

if not df_30j.empty:
    df_30j = df_30j.sort_values("timestamp")
    st.line_chart(df_30j.set_index("timestamp")["temperature"])
else:
    st.warning("Aucune donnée météo disponible.")
