import streamlit as st
import pandas as pd
from app.queries import (
    get_ajd_meteo,
    get_temp_delta,
    get_nb_jours,
    get_moy_dernier_7_jours,
    get_jour_plus_chaud,
    get_jour_plus_froid,
    get_30_derniers_jours,
)

# Titre
st.title("Dashboard Météo")

# Données
col1, col2, col3 = st.columns(3)

col1.metric("Température actuelle", f"{get_ajd_meteo()} °C", f"{get_temp_delta()} °C depuis hier")
col2.metric("Jours collectés", get_nb_jours())
col3.metric("Moyenne des 7 derniers jours", f"{get_moy_dernier_7_jours()} °C")

# informations supplémentaires
st.markdown("### Journée la plus chaude / froide de la semaine")
st.write(f"Plus chaud : {get_jour_plus_chaud()}")
st.write(f"Plus froid : {get_jour_plus_froid()}")

# Graphique 
st.markdown("### Températures des 30 derniers jours")
df = get_30_derniers_jours()
st.line_chart(df.set_index("date")["temperature"])

