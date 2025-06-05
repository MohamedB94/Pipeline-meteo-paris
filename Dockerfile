# Étape 1 : image de base avec Python
FROM python:3.11-slim

# Étape 2 : définition du dossier de travail dans le conteneur
WORKDIR /app

# Étape 3 : copier les fichiers locaux dans le conteneur
COPY . /app

# Étape 4 : installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : exposer le port utilisé par Streamlit
EXPOSE 8501

# Étape 6 : lancer Streamlit au démarrage
CMD ["streamlit", "run", "app/dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
