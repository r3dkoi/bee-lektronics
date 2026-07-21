from flask import Blueprint, render_template

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
    return render_template('shop.html', products=products)


@main.route('/product/<int:product_id>')
def product_detail(product_id):
     #TODO: replace with real lookup, e.g. Product.query.get_or_404(product_id)
     #From product database list
    return render_template('product_detail.html', product=product)


@main.route('/about')
def about_contact():
    # About / Contact info page — static content, no data needed.
    return render_template('about_contact.html')
