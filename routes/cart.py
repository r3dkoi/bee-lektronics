from flask import Blueprint, jsonify, request, session
from routes.main import PRODUCTS

# Blueprint for everything cart-related.
cart = Blueprint('cart', __name__)


def get_cart_details():
    # Reads the session cart ({product_id_str: quantity}) and looks up
    # each product's real details from the mock PRODUCTS list.
    # TODO: once models exist, replace PRODUCTS lookup with Product.query.get(id)
    cart_dict = session.get('cart', {})
    items = []
    subtotal = 0
    for product_id_str, quantity in cart_dict.items():
        product = next((p for p in PRODUCTS if p["id"] == int(product_id_str)), None)
        if product:
            subtotal += product["price"] * quantity
            items.append({
                "id": product["id"],
                "name": product["name"],
                "price": product["price"],
                "image": product["image"],
                "quantity": quantity,
            })
    return items, subtotal


@cart.route('/cart/data')
def cart_data():
    # Fetched by main.js to populate the minicart overlay.
    items, subtotal = get_cart_details()
    return jsonify({"items": items, "subtotal": subtotal})


@cart.route('/cart/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    cart_dict = session.get('cart', {})
    key = str(product_id)
    cart_dict[key] = cart_dict.get(key, 0) + 1
    session['cart'] = cart_dict
    items, subtotal = get_cart_details()
    return jsonify({"items": items, "subtotal": subtotal})


@cart.route('/cart/update/<int:product_id>', methods=['POST'])
def update_quantity(product_id):
    # Used by the minicart's +/- buttons to set an exact quantity.
    quantity = request.json.get('quantity', 1)
    cart_dict = session.get('cart', {})
    key = str(product_id)
    if quantity > 0:
        cart_dict[key] = quantity
    elif key in cart_dict:
        del cart_dict[key]
    session['cart'] = cart_dict
    items, subtotal = get_cart_details()
    return jsonify({"items": items, "subtotal": subtotal})


@cart.route('/cart/remove/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    cart_dict = session.get('cart', {})
    key = str(product_id)
    if key in cart_dict:
        del cart_dict[key]
    session['cart'] = cart_dict
    items, subtotal = get_cart_details()
    return jsonify({"items": items, "subtotal": subtotal})
