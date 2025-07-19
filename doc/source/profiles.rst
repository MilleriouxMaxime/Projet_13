Profiles
========

Le module **profiles** gère les profils utilisateurs du site.

Modèle
------

- **Profile** :
  - `user` : lien vers l'utilisateur Django
  - `favorite_city` : ville préférée de l'utilisateur

Vues
----

- **Index** : liste tous les profils utilisateurs.
- **Profile** : affiche le détail d'un profil (nom d'utilisateur, ville préférée).

Templates
---------

- `profiles/index.html` : liste des profils
- `profiles/profile.html` : détail d'un profil

Exemple d'utilisation
--------------------

- Accéder à la liste des profils : `/profiles/`
- Accéder au détail d'un profil : `/profiles/<username>/` 