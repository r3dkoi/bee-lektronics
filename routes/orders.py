from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from routes.cart import get_cart_details

orders = Blueprint('orders', __name__)


@orders.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # TODO: once models exist, create a real Order/OrderItem in the database
        # using request.form.get('first_name'), etc.
        session['cart'] = {}  # empty the cart now that the order's placed
        flash('Order Confirmed')
        return redirect(url_for('main.shop'))

    cart_items, subtotal = get_cart_details()
    return render_template('checkout.html', cart_items=cart_items, subtotal=subtotal)
