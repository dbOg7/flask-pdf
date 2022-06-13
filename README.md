# flask-pdf

# a savoir

 - le projet contient un template
 
 - python-dotenv est installé pour un environnment de développement

# Objectif du projet

- Générer un pdf d'une page html dynamiquement

- *dynamique : Le pdf ne doit pas etre généré ni stocké dans le projet !

- le pdf doit être télécharger lors d'un clic.

# installation des modules

    - créer un environnement virtuel (venv) puis l'activer

    - pip install -r requirements.txt

    - créer un fichier .env à la racine du dossier git

    - coller dedans :
    
        DEBUG = True
        
        FLASK_APP=app.py

        FLASK_ENV=development

# démarrer le projet 

    - cd app 

    - flask run

