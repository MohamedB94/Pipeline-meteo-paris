# 🌤️ pipeline-meteo-paris

Ce projet collecte automatiquement les données météorologiques de Paris via l'API **OpenWeatherMap**, les stocke dans une base **MySQL (XAMPP)**, et les affiche dans un **dashboard interactif Streamlit**.

## ⚙️ Fonctionnement

1. Appel de l'API météo 1x/jour (`main.py`)
2. Insertion des données dans la base MySQL
3. Affichage dynamique via Streamlit (`dashboard.py`)

## 📊 Fonctionnalités du dashboard

- 🌡 Température actuelle vs hier
- 📅 Nombre de jours de données collectées
- 📈 Moyenne des 7 derniers jours
- 🔥 Jour le plus chaud / ❄️ le plus froid de la semaine
- 📉 Graphique des températures des 30 derniers jours

## 📂 Architecture du projet

```bash
pipeline-meteo-paris/
│
├── app/
│   ├── fetch_api.py
│   ├── config.py
│   ├── database.py
│   ├── queries.py
│   └── dashboard.py
├── main.py
├── requirements.txt
└── screenshots/

## 🖼️ Capture du Dashboard

![Dashboard](screenshots/Dashboard.png)
```
