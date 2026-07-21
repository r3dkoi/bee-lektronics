from flask import Blueprint, render_template, session, redirect, url_for

# Blueprint for everything cart-related.
# url_for('cart.view_cart') etc. will map to the functions below.
cart = Blueprint('cart', __name__)


@cart.route('/cart')
def view_cart():
    # Cart is guest/session-based — no login required.
    # session.get('cart', []) reads whatever's stored in the visitor's session,
    # or returns an empty list if they haven't added anything yet.
    cart_items = session.get('cart', [])
    return render_template('cart.html', cart_items=cart_items)


@cart.route('/cart/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # Adds a product id to the session cart.
    # TODO: once models exist, store real product details (name/price) not just the id.
    cart_items = session.get('cart', [])
    cart_items.append(product_id)
    session['cart'] = cart_items
    return redirect(url_for('cart.view_cart'))


@cart.route('/cart/remove/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    # Removes one matching product id from the session cart, if present.
    cart_items = session.get('cart', [])
    if product_id in cart_items:
        cart_items.remove(product_id)
    session['cart'] = cart_items
    return redirect(url_for('cart.view_cart'))
