from flask import Blueprint, render_template, request, jsonify, Response, url_for

from models.database import get_connection

# Blueprint groups all the "general site" pages together (not cart/orders/admin).
# The name 'main' here is what url_for() uses, e.g. url_for('main.home').
main = Blueprint('main', __name__)


@main.route('/')
def home():
    # Homepage — hero section + featured products carousel.
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, image FROM products")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('home.html', products=products)


@main.route('/api/products')
def api_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = [dict(row) for row in cursor.fetchall()]  # jsonify() can't serialise sqlite3.Row directly
    cursor.close()
    conn.close()
    return jsonify(products)

PRODUCTS_PER_PAGE = 6 #For pagination and grid showing display purposes

@main.route('/shop')
def shop():
    # Product listing page.
    page = request.args.get('page', 1, type=int)
    category = request.args.get('category') #e.g 'phones' or None

    conn = get_connection()
    cursor = conn.cursor()

    #Counts products per category across ALL products from products database
    #Sidebar count stays accurate even while category filter is active
    cursor.execute("SELECT category, COUNT(*) AS count FROM products GROUP BY category")
    category_counts = {row['category']: row['count'] for row in cursor.fetchall()}

    #Build WHERE clause only when category filter is requested
    where_clause = ""
    params = []
    if category:
        where_clause = "WHERE category = ?"
        params.append(category)

    #Total count drives how many pages exist
    cursor.execute(f"SELECT COUNT(*) AS total FROM products {where_clause}", params)
    total_products = cursor.fetchone()['total']
    total_pages = max(1, -(-total_products // PRODUCTS_PER_PAGE)) 

    #Clamp page into valid range so ?page=999 doesn't return an empty grid silently
    page = max(1, min(page, total_pages))
    offset = (page - 1) * PRODUCTS_PER_PAGE

    cursor.execute(
        f"SELECT * FROM products {where_clause} LIMIT ? OFFSET ?",
        params + [PRODUCTS_PER_PAGE, offset]
    )
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        'shop.html',
        products=products,
        page=page,
        total_pages=total_pages,
        category_counts=category_counts,
        selected_category=category)


@main.route('/product/<int:product_id>')
def product_detail(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()

    if product is None:
        return "Product not found", 404
    return render_template('product_detail.html', product=product)


@main.route('/robots.txt')
def robots_txt():
    lines = [
        "User-agent: *",
        "Disallow: /checkout",
        "Disallow: /cart",
        "Disallow: /admin",
        f"Sitemap: {request.url_root.rstrip('/')}{url_for('main.sitemap_xml')}",
    ]
    return Response("\n".join(lines), mimetype='text/plain')


@main.route('/sitemap.xml')
def sitemap_xml():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM products")
    products = cursor.fetchall()
    cursor.close()
    conn.close()

    static_urls = [url_for('main.home'), url_for('main.shop')]
    product_urls = [url_for('main.product_detail', product_id=p['id']) for p in products]

    root = request.url_root.rstrip('/')
    entries = "".join(
        f"<url><loc>{root}{path}</loc></url>"
        for path in static_urls + product_urls
    )
    xml = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{entries}</urlset>'
    return Response(xml, mimetype='application/xml')
