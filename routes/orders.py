import re

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.database import get_connection
from routes.cart import get_cart_details

orders = Blueprint('orders', __name__)

# Mirrors the pattern/minlength/maxlength attributes on checkout.html's inputs —
# those are enforced by the browser only, so the same rules are re-checked here
# since a form can always be bypassed (devtools, disabled JS, a raw POST request).

# Something, then @, then something, then a literal dot, then something —
# not a full RFC 5322 email validator, just enough to catch obvious garbage.
EMAIL_RE = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')

# Digits only, with an optional leading + for country codes (e.g. +61),
# 8-20 characters total (matches the input's pattern="\+?[0-9]+" plus its
# minlength/maxlength).
PHONE_RE = re.compile(r'^\+?[0-9]{8,20}$')

# Letters, spaces, apostrophes, hyphens only, 2-50 characters total
# (matches the input's pattern="[A-Za-z\s'-]+" plus its minlength/maxlength).
SUBURB_RE = re.compile(r"^[A-Za-z\s'-]{2,50}$")


def validate_delivery_details(email, phone, suburb):
    # Returns an error message for the first failing field, or None if all three pass.
    if not email or len(email) > 255 or not EMAIL_RE.match(email):
        return 'Please enter a valid email address'
    if not PHONE_RE.match(phone):
        return 'Phone must be 8-20 digits, with an optional leading + for country codes. E.g: 04830559011'
    if not SUBURB_RE.match(suburb):
        return "Suburb must be 2-50 letters only (spaces, apostrophes, and hyphens allowed). E.g: Kellyville"
    return None


@orders.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart_items, subtotal = get_cart_details()

    if request.method == 'POST':
        if not cart_items:
            flash('Your cart is empty')
            return redirect(url_for('main.shop'))

        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        suburb = request.form.get('suburb', '').strip()

        error = validate_delivery_details(email, phone, suburb)
        if error:
            flash(error)
            return render_template('checkout.html', cart_items=cart_items, subtotal=subtotal)

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO orders (email, phone, suburb, total_sale_price) VALUES (%s, %s, %s, %s)",
            (email, phone, suburb, subtotal)
        )
        order_id = cursor.lastrowid

        product_ids = [item['id'] for item in cart_items]
        placeholders = ', '.join(['%s'] * len(product_ids))
        cursor.execute(f"SELECT id, cost_price FROM products WHERE id IN ({placeholders})", product_ids)
        cost_price_by_id = {product_id: cost_price for product_id, cost_price in cursor.fetchall()}

        order_items = [
            (order_id, item['id'], item['quantity'], item['price'], cost_price_by_id[item['id']])
            for item in cart_items
        ]
        cursor.executemany(
            "INSERT INTO order_items (order_id, product_id, quantity, unit_price, unit_cost_price) "
            "VALUES (%s, %s, %s, %s, %s)",
            order_items
        )

        conn.commit()
        cursor.close()
        conn.close()

        session['cart'] = {}  # empty the cart now that the order's placed
        flash('Order Confirmed')
        return redirect(url_for('main.shop'))

    return render_template('checkout.html', cart_items=cart_items, subtotal=subtotal)
