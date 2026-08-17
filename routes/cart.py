from flask import Blueprint, jsonify, request, session
from models.database import get_connection

# Blueprint for everything cart-related.
cart = Blueprint('cart', __name__)


def get_cart_details():
    """Resolve the session cart's product IDs/quantities into full item details and a subtotal."""
    # Reads the session cart ({product_id_str: quantity}) and looks up
    # each product's real details from the database.
    cart_dict = session.get('cart', {})
    items = []
    subtotal = 0

    if not cart_dict:
        return items, subtotal

    conn = get_connection()
    cursor = conn.cursor()
    product_ids = [int(product_id_str) for product_id_str in cart_dict]
    placeholders = ', '.join(['?'] * len(product_ids))
    cursor.execute(f"SELECT * FROM products WHERE id IN ({placeholders})", product_ids)
    products_by_id = {row["id"]: row for row in cursor.fetchall()}
    cursor.close()
    conn.close()

    for product_id_str, quantity in cart_dict.items():
        product = products_by_id.get(int(product_id_str))
        if product:
            price = float(product["price"])
            line_total = price * quantity
            subtotal += line_total
            items.append({
                "id": product["id"],
                "name": product["name"],
                "price": price,
                "image": product["image"],
                "quantity": quantity,
                "line_total": line_total,
            })
    return items, subtotal

def product_exists(product_id):
    """Check whether a product ID is real, so cart routes can 404 cleanly instead of silently no-opping."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM products WHERE id = ?", (product_id,))
    exists = cursor.fetchone() is not None
    cursor.close()
    conn.close()
    return exists

@cart.route('/cart/data')
def cart_data():
    """Return the current cart's items and subtotal as JSON (fetched by main.js for the minicart)."""
    items, subtotal = get_cart_details()
    return jsonify({"items": items, "subtotal": subtotal})


@cart.route('/cart/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    """Add a quantity of the given product to the session cart."""
    if not product_exists(product_id):
        return jsonify({"error": f"Product {product_id} not found"}), 404

    # product_detail.html's quantity selector; shop.html's grid form sends
    # no body at all, so this defaults to adding a single unit.
    quantity = (request.get_json(silent=True) or {}).get('quantity', 1)
    if not isinstance(quantity, int) or quantity < 1:
        return jsonify({"error": "Quantity must be a positive whole number"}), 400

    cart_dict = session.get('cart', {})
    key = str(product_id)
    cart_dict[key] = cart_dict.get(key, 0) + quantity
    session['cart'] = cart_dict
    items, subtotal = get_cart_details()
    return jsonify({"items": items, "subtotal": subtotal})


@cart.route('/cart/update/<int:product_id>', methods=['POST'])
def update_quantity(product_id):
    """Set a product's exact quantity in the cart, removing it if set to zero or below."""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    quantity = data.get('quantity', 1)
    if not isinstance(quantity, int):
        return jsonify({"error": "Quantity must be a whole number"}), 400

    cart_dict = session.get('cart', {})
    key = str(product_id)
    if quantity > 0:
        if not product_exists(product_id):
            return jsonify({"error": f"Product {product_id} not found"}), 404
        cart_dict[key] = quantity
    elif key in cart_dict:
        del cart_dict[key]
    session['cart'] = cart_dict
    items, subtotal = get_cart_details()
    return jsonify({"items": items, "subtotal": subtotal})


@cart.route('/cart/remove/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    """Remove a product from the session cart entirely."""
    cart_dict = session.get('cart', {})
    key = str(product_id)
    if key in cart_dict:
        del cart_dict[key]
    session['cart'] = cart_dict
    items, subtotal = get_cart_details()
    return jsonify({"items": items, "subtotal": subtotal})
