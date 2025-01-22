
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer un port si nécessaire (généralement pas nécessaire pour un bot Discord)
# EXPOSE 8080

# Commande pour exécuter le bot
CMD ["python", "discordApp.py"]