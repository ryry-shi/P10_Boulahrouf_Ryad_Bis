P10_Boulahrouf_Ryad

Description du programme:

-1 Créer l'environnement virtuel et le lancer:

    - Création de l'environnement virtuelle python -m venv venv
    - Lancement de l'environnement virtuelle venv/Scripts/activate
    - Installation des Prérequis avec pip et le fichier .Txt, pip install -r "requirements.txt"

-2 Importer les migrations, et lancer le serveur:

    - Importer les migrations, python manage.py migrate
    - Lancement du serveur, python manage.py runserver

-3 Création du superutilisateur et des utilisateurs:

    - Création de l'admin, python manage.py createsuperuser
    - User, http://127.0.0.1:8000/signup/ username, password
    - Project, 

-4 Création des objets(requis être connecter):

    - Création des projet, http://127.0.0.1:8000/project/:
        - read, update ou supprimer projet(besoin permission) http://127.0.0.1:8000/project/int/

    - Création des contributor, http://127.0.0.1:8000/project/int/user
        - read, update ou supprimer contributor(besoin permission) http://127.0.0.1:8000/project/int/contributor/int/

    - Création des issue, http://127.0.0.1:8000/project/int/issue
        - read, update ou supprimer issue(besoin permission) http://127.0.0.1:8000/project/int/issue/int/

    - Création des comment, http://127.0.0.1:8000/project/int/issue/int/comment
        - read, update ou supprimer comment(besoin permission) http://127.0.0.1:8000/project/int/issue/int/comment/int/

