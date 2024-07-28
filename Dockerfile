# Utilisez une image Python de base comme point de départ
FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y nodejs

# Définissez le répertoire de travail dans le container
WORKDIR /app

# Copiez les fichiers de l'application
COPY requirements.txt requirements.txt
COPY . .

# Installez les dépendances Python
RUN pip install -r requirements.txt

# Copiez le script JavaScript
#COPY script.js script.js

# Exposez le port si nécessaire (ajuster selon votre application)
#EXPOSE 8080

# Commande pour lancer l'application Python
CMD ["python", "discordApp.py"]