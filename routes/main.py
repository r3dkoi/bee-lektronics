from flask import Blueprint, render_template, request

# Blueprint groups all the "general site" pages together (not cart/orders/admin).
# The name 'main' here is what url_for() uses, e.g. url_for('main.home').
main = Blueprint('main', __name__)


@main.route('/')
def home():
    # Homepage — hero section + featured products carousel.
    # TODO: once models/product.py exists, fetch real featured products here
    # and pass them into the template, e.g. render_template('home.html', products=products)
    return render_template('home.html')


@main.route('/shop')
def shop():
    # Product listing page.
    # TODO: replace with real query, e.g. Product.query.all()
    page = request.args.get('page', 1, type=int)
    # category = request.args.get('category') #e.g 'phones' or None (Uncomment once TODO is done)
    # TODO: once real products exist, use Flask-SQLAlchemy's built-in pagination
    # TODO: Once category exists as foreign key thats part of Products table include for category route in shop.html
    total_pages = 2 #Placeholder until real pagination exists ^
    products = [
        {"id": 1, "name": "Arduino Uno", "price": 24.99, "category": "Computer", "image": "https://placehold.co/300x200.png", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
        {"id": 2, "name": "Raspberry Pi 4", "price": 59.99, "category": "Computer", "image": "https://placehold.co/300x200.png", "description": "Sed do eiusmod tempor incididunt ut labore et dolore magna."},
        {"id": 3, "name": "Oppo Reno 91", "price": 19.00, "category": "Phone", "image": "https://placehold.co/300x200.png", "description": "Ut enim ad minim veniam, quis nostrud exercitation ullamco."},
        {"id": 4, "name": "Samsung Galaxy S30", "price": 899.99, "category": "Phone", "image": "https://placehold.co/300x200.png", "description": "Duis aute irure dolor in reprehenderit in voluptate velit."},
        {"id": 5, "name": "iPhone 20", "price": 999.99, "category": "Phone", "image": "https://placehold.co/300x200.png", "description": "Excepteur sint occaecat cupidatat non proident, sunt in culpa."},
    ]
    return render_template('shop.html', products=products, page=page, total_pages=total_pages)


@main.route('/product/<int:product_id>')
def product_detail(product_id):
    #TODO: replace with real lookup, e.g. Product.query.get_or_404(product_id)
    #From product database list
    #Temporary hardcoded list for testing
    product = {"id": product_id, "name": "Arduino Uno", "price": 24.99, "category": "Phone", "image": "https://placehold.co/300x200.png"}
    return render_template('product_detail.html', product=product)


@main.route('/about')
def about_contact():
    # About / Contact info page — static content, no data needed.
    return render_template('about_contact.html')
