import os

# Reads values from .env (loaded by app/__init__.py) with fallback defaults
# so the app still runs even if .env is missing something.
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'bee-key-very-secure-l0l')

    # Admin credentials now live in the admins table (models/admins.sql), as a username + hashed password
