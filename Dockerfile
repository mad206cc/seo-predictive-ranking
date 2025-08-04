# Utilise une image officielle de Python (ici la version 3.9 en version slim)
FROM python:3.9

# Définit le répertoire de travail dans le container (ici "app")
WORKDIR /predective_ranking

# Copie des fichiers du projet dans le container
COPY . /predective_ranking/

# Installe les dépendances définies dans requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install gunicorn

# Expose le port 8000 (celui utilisé par défaut par Django)
EXPOSE 8888
# Lance le serveur Gunicorn au lieu de runserver (beaucoup plus stable)
CMD ["gunicorn", "--bind", "0.0.0.0:8888", "SEO_Prediction_Project.wsgi:application"]