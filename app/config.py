import os

from models.database import DB_PATH

# Reads values from .env (loaded by app/__init__.py) with fallback defaults
# so the app still runs even if .env is missing something.
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'bee-key-very-secure-l0l')

    # SQLite — a single file at instance/beelektronics.db (see models/database.py),
    # no separate server/host/credentials needed.
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # TODO: replace with a real Admin model + hashed passwords once one exists.
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin')
