import os

# Reads values from .env (loaded by app/__init__.py) with fallback defaults
# so the app still runs even if .env is missing something.
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'bee-key-very-secure-l0l')

    # MySQL connection — each person points this at their own local server via
    # .env (never commit real credentials). Defaults assume a local MySQL
    # instance with a database named 'bee_lektronics' already created.
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '3306')
    DB_NAME = os.environ.get('DB_NAME', 'bee_lektronics')

    SQLALCHEMY_DATABASE_URI = (
        f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # TODO: replace with a real Admin model + hashed passwords once one exists.
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin')
