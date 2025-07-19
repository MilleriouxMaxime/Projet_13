Lettings
========

Le module **lettings** gère les annonces de locations immobilières.

Modèles
-------

- **Letting** : représente une location.
  - `title` : titre de la location
  - `address` : adresse associée (voir ci-dessous)

- **Address** : représente une adresse postale.
  - `number` : numéro de rue
  - `street` : nom de la rue
  - `city` : ville
  - `state` : état (code à 2 lettres)
  - `zip_code` : code postal
  - `country_iso_code` : code pays ISO (3 lettres)

Vues
----

- **Index** : liste toutes les locations disponibles.
- **Letting** : affiche le détail d'une location (titre, adresse).

Templates
---------

- `lettings/index.html` : liste des locations
- `lettings/letting.html` : détail d'une location

Exemple d'utilisation
--------------------

- Accéder à la liste des locations : `/lettings/`
- Accéder au détail d'une location : `/lettings/<letting_id>/` 