# Utilise une image de base Python
FROM python:3.9-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /home/jka/Documents/VS_Code/Secret_Santa/

# Copie le fichier Python dans le conteneur
COPY secret_santa.py .

# Installe les dépendances (si ton projet en a dans un requirements.txt)
# Si tu n'as pas de dépendances, tu peux ignorer cette étape
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# Définit la commande de démarrage du conteneur
CMD ["python", "secret_santa.py"]


