from flask import Blueprint, render_template, request, jsonify

from models.database import get_connection

# Blueprint groups all the "general site" pages together (not cart/orders/admin).
# The name 'main' here is what url_for() uses, e.g. url_for('main.home').
main = Blueprint('main', __name__)


@main.route('/')
def home():
    # Homepage — hero section + featured products carousel.
    # TODO: fetch real featured products here and pass them into the template,
    # e.g. render_template('home.html', products=products)
    return render_template('home.html')


@main.route('/api/products')
def api_products():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(products)


@main.route('/shop')
def shop():
    # Product listing page.
    page = request.args.get('page', 1, type=int)
    # category = request.args.get('category') #e.g 'phones' or None

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    conn.close()

    # TODO: once real pagination/category filtering is needed, apply it via
    # SQL (LIMIT/OFFSET, WHERE category = %s) instead of fetching everything.
    total_pages = 2  # Placeholder until real pagination exists
    return render_template('shop.html', products=products, page=page, total_pages=total_pages)


@main.route('/product/<int:product_id>')
def product_detail(product_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()

    if product is None:
        return "Product not found", 404
    return render_template('product_detail.html', product=product)
