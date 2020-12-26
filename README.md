# Un projet Django

Un projet Django - création de posts et de critiques de livres

## Contenu du dossier

Un structure d'application Django ; le projet ``mylitreview`` contient le projet complet Django ; un projet y a été développé => ``mvplit``.

### "Matos" requis

- Tout est indiqué dans requirements.txt ; la commande ``pip install -r requirements.txt`` installera l'ensemble.

### Installation et démarrage (consignes adaptées pour utilisateurs/utilisatrices de Mac)

Etape 1: clonez le projet.

Etape 2: naviguez dans le dossier tout juste avec la commande ``cd litreview`` puis installez dans le répertoire un environnement virtuel (avec [pipenv](https://docs.python-guide.org/dev/virtualenvs/), ou avec [venv et pip](https://docs.python.org/fr/3/library/venv.html)).

Etape 3: activez l'environnement virtuel avec la commande appropriée. 

Etape 4 : installez Django sur votre machine avec la commande ``python -m pip install django``

Etpage 5 : accédez au répertoire ``mylitreview`` avec la commande ``cd mylitreview``, et installez les migrations avec la commande ``python manage.py makemigrations``puis ``python manage.py migrate``

## Executer le projet en local

Pour lancer le projet en local, cela se fait depuis le répertoire ``mylitreview`` avec ``cd mylitreview`` ; ensuite tapez la commande ``python manage.py runserver``
Vous pourrez accéder au projet en tapant l'adresse web ``localhost:8000``



## Auteur
* **Alexandre Kuzo**  [@alexandrekuzo](https://github.com/AlexandreKuzo)
