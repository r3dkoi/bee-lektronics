from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.database import get_connection
from routes.cart import get_cart_details

orders = Blueprint('orders', __name__)


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
