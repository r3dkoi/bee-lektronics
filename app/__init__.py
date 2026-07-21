from flask import Flask
from dotenv import load_dotenv

from app.config import Config
from routes.main import main
from routes.cart import cart
# from routes.orders import orders   # TODO: uncomment once routes/orders.py exists
# from routes.admin import admin     # TODO: uncomment once routes/admin.py exists


def create_app():
    # Load variables from .env into the environment (SECRET_KEY, etc.)
    load_dotenv()

    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)

    # session (used by cart.py) requires SECRET_KEY to be set — comes from Config above.

    # Register each blueprint so their routes/url_for() names become available.
    app.register_blueprint(main)
    app.register_blueprint(cart)
    # app.register_blueprint(orders)
    # app.register_blueprint(admin)

    return app
