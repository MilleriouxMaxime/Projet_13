.. oc_lettings_site documentation master file, created by
   sphinx-quickstart on Sat Jul 19 13:35:59 2025.
   Vous pouvez adapter ce fichier à votre convenance, mais il doit au moins
   contenir la directive racine `toctree`.

Documentation du projet oc_lettings_site
========================================

Bienvenue dans la documentation du projet **oc_lettings_site**.
Ce site web, développé avec Django, permet de gérer des profils utilisateurs et des locations immobilières (lettings).

.. contents:: Table des matières
   :depth: 2

Présentation
-----------
Le projet **oc_lettings_site** est une application web permettant :
- de consulter et gérer des profils utilisateurs,
- de consulter et gérer des annonces de locations immobilières.

Installation
------------

Prérequis :
- Python 3.6 ou supérieur
- Git
- SQLite3

Étapes d'installation :

.. code-block:: bash

   git clone <url-du-repo>
   cd <nom-du-repo>
   python -m venv venv
   source venv/bin/activate  # (ou .\venv\Scripts\Activate.ps1 sous Windows)
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver

Accédez ensuite à http://localhost:8000 dans votre navigateur.

Modules principaux
------------------

Lettings
~~~~~~~~
- Modèle : Letting (titre, adresse)
- Vue : liste des locations, détail d'une location

Profiles
~~~~~~~~
- Modèle : Profile (utilisateur, ville préférée)
- Vue : liste des profils, détail d'un profil

Configuration
-------------
- Les paramètres principaux se trouvent dans ``oc_lettings_site/settings.py``.
- Les variables sensibles (clé secrète, DSN Sentry) doivent être passées via les variables d'environnement.

Tests
-----
- Les tests unitaires sont situés dans les dossiers ``lettings/tests.py`` et ``profiles/tests.py``.
- Lancer tous les tests :

.. code-block:: bash

   pytest

Déploiement
-----------
- Le projet utilise Docker et un pipeline CI/CD (GitHub Actions).
- Voir le README pour les détails sur la configuration des secrets et le déploiement automatique.

Supervision et journalisation des erreurs
----------------------------------------
- Sentry est utilisé pour la supervision des erreurs (voir ``oc_lettings_site/settings.py``).
- Les logs sont configurés pour s'afficher dans la console.

.. toctree::
   :maxdepth: 2
   :caption: Contenu détaillé :

   lettings
   profiles

