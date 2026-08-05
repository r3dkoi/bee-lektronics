import os

# Reads values from .env (loaded by app/__init__.py) with fallback defaults
# so the app still runs even if .env is missing something.
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'bee-key-very-secure-l0l')

    # TODO: replace with a real Admin model + hashed passwords once one exists.
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin')
