from flask_sqlalchemy import SQLAlchemy

# Shared SQLAlchemy instance — imported by app/__init__.py (init_app) and by
# models/*.py (db.Model, db.Column, etc.) once those exist.
db = SQLAlchemy()
