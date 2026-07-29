from flask import Blueprint, jsonify, request, session
from models.database import get_connection

# Blueprint for everything cart-related.
cart = Blueprint('cart', __name__)


def get_cart_details():
    # Reads the session cart ({product_id_str: quantity}) and looks up
    # each product's real details from the database.
    cart_dict = session.get('cart', {})
    items = []
    subtotal = 0

    if not cart_dict:
        return items, subtotal

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    product_ids = [int(product_id_str) for product_id_str in cart_dict]
    placeholders = ', '.join(['%s'] * len(product_ids))
    cursor.execute(f"SELECT * FROM products WHERE id IN ({placeholders})", product_ids)
    products_by_id = {row["id"]: row for row in cursor.fetchall()}
    cursor.close()
    conn.close()

    for product_id_str, quantity in cart_dict.items():
        product = products_by_id.get(int(product_id_str))
        if product:
            line_total = product["price"] * quantity
            subtotal += line_total
            items.append({
                "id": product["id"],
                "name": product["name"],
                "price": product["price"],
                "image": product["image"],
                "quantity": quantity,
                "line_total": line_total,
            })
    return items, subtotal


@cart.route('/cart/data')
def cart_data():
    # Fetched by main.js to populate the minicart overlay.
    items, subtotal = get_cart_details()
    return jsonify({"items": items, "subtotal": subtotal})


@cart.route('/cart/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # product_detail.html's quantity selector; shop.html's grid form sends
    # no body at all, so this defaults to adding a single unit.
    quantity = (request.get_json(silent=True) or {}).get('quantity', 1)
    cart_dict = session.get('cart', {})
    key = str(product_id)
    cart_dict[key] = cart_dict.get(key, 0) + quantity
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
