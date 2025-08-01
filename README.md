## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Error Monitoring and Logging

This project uses [Sentry](https://sentry.io/) for error monitoring and logging. Sentry is integrated via the `sentry-sdk` package and is configured in `oc_lettings_site/settings.py`.

### Sentry Setup

1. **Install dependencies:**
   Ensure `sentry-sdk` is installed (see `requirements.txt`).

2. **Set the Sentry DSN:**
   - Do **not** hardcode the DSN in the codebase.
   - Set the environment variable `SENTRY_DSN` with your Sentry project DSN:
     ```sh
     export SENTRY_DSN="https://<your-key>@sentry.io/<your-project>"
     ```
   - On Windows (cmd):
     ```cmd
     set SENTRY_DSN=https://<your-key>@sentry.io/<your-project>
     ```

3. **Deploy:**
   - When the app starts, Sentry will be initialized if the `SENTRY_DSN` environment variable is set.

### Logging

- Logging is configured in `settings.py` to output logs to the console.
- Logs are inserted in critical views and error handling blocks.
- You can adjust the logging level and handlers in the `LOGGING` configuration in `settings.py`.

### Security
- **Never commit your Sentry DSN or any sensitive credentials to the codebase.**
- Always use environment variables for secrets and sensitive configuration.

---

For more details, see the Sentry documentation: https://docs.sentry.io/platforms/python/guides/django/

## Déploiement

### Fonctionnement général

- Le pipeline CI/CD utilise GitHub Actions pour automatiser les tests, la construction de l'image Docker, le push sur Docker Hub, et le déploiement sur l'hébergeur cloud.
- Seules les modifications sur la branche `master` déclenchent la conteneurisation et le déploiement.
- Les autres branches déclenchent uniquement les tests et le linting.

### Configuration requise

- Secrets GitHub pour Docker Hub (`DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`).
- Secrets pour l'hébergeur cloud (ex: clé API Render, AWS, etc.).
- Un compte Docker Hub et un registre de conteneurs.
- Un compte sur l'hébergeur cloud choisi.

### Étapes de déploiement

1. **Configurer les secrets GitHub** dans les paramètres du repo.
2. **Pousser sur la branche `master`** pour déclencher le pipeline complet.
3. **L'image Docker est construite et poussée sur Docker Hub** avec le hash du commit.
4. **Le déploiement est déclenché automatiquement** sur l'hébergeur cloud.
5. **Pour lancer le site localement avec Docker :**
   ```sh
   docker pull <votre-utilisateur-docker>/oc-lettings-site:<hash-du-commit>
   docker run -e DJANGO_SECRET_KEY=... -e SENTRY_DSN=... -p 8000:8000 <votre-utilisateur-docker>/oc-lettings-site:<hash-du-commit>
   ```

---
