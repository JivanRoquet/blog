Admin section
=============

# Fichiers et arborescence

* Renommer app/views.py en app/blog.py et from app import blog, admin dans app/__init__.py
* Créer app/admin.py

# Fonctions et routes

* Créer route @app.route('/admin/login') dans admin.py (+ template)
* Créer décorateur @admin renvoyant vers le login si non connecté en tant qu'administrateur
* Créer route @app.route('/admin') dans admin.py (+ template)
* Créer route @app.route('/admin/posts') pour répertorier les posts existants (+ template)
* Créer route @app.route('/admin/post/<post_id>') pour éditer un post (+ template)
* Créer route @app.route('/admin/post/create') pour créer un nouveau post (+ template)
* Créer form WTF d'édition/création de post (le même) avec post_id (hidden) renseigné si édition et vide si nouveau post

# Support de Markdown

* Implémenter Markdown pour l'édition/création de posts
* Dans formulaire édition/création, implémenter import/export du post_body en fichier .md
