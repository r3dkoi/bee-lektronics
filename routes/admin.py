from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from functools import wraps

from app.config import Config
from models.database import get_connection

# Blueprint groups the admin-only pages together.
# url_prefix means every route below lives under /admin, e.g. /admin/login
admin = Blueprint('admin', __name__, url_prefix='/admin')


def admin_required(view):
    # TODO: once a real User/Admin model exists, check something more robust
    # than a plain session flag (e.g. roles/permissions on the logged-in user).
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get('is_admin'):
            flash('Please log in to continue')
            return redirect(url_for('admin.login'))
        return view(*args, **kwargs)
    return wrapped


@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        # TODO: once models/admin exists, replace with a real lookup + hashed
        # password check instead of comparing against Config values.
        if username == Config.ADMIN_USERNAME and password == Config.ADMIN_PASSWORD:
            session['is_admin'] = True
            return redirect(url_for('admin.dashboard'))

        flash('Invalid username or password')

    return render_template('admin/login.html')


@admin.route('/logout')
def logout():
    session.pop('is_admin', None)
    return redirect(url_for('admin.login'))


@admin.route('/dashboard')
@admin_required
def dashboard():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT
            o.id AS order_id,
            o.email,
            o.phone,
            o.suburb,
            o.order_date,
            p.name AS product_name,
            oi.quantity,
            oi.unit_cost_price,
            oi.unit_price
        FROM order_items oi
        JOIN orders o ON oi.order_id = o.id
        JOIN products p ON oi.product_id = p.id
        ORDER BY o.order_date DESC, o.id DESC
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    # Each row is one product line within an order — the purchaser (email/phone/
    # suburb) repeats across every line of the same order, cost/sale price are
    # per-unit as recorded at sale time, so line totals are computed here.
    sales = []
    total_cost = 0
    total_sale = 0
    for row in rows:
        quantity = row['quantity']
        cost_price = float(row['unit_cost_price'])
        sale_price = float(row['unit_price'])
        line_cost = cost_price * quantity
        line_sale = sale_price * quantity
        total_cost += line_cost
        total_sale += line_sale
        sales.append({
            'order_id': row['order_id'],
            'email': row['email'],
            'phone': row['phone'],
            'suburb': row['suburb'],
            'order_date': row['order_date'],
            'product_name': row['product_name'],
            'quantity': quantity,
            'cost_price': cost_price,
            'sale_price': sale_price,
            'line_profit': line_sale - line_cost,
        })

    return render_template(
        'admin/sales_summary.html',
        sales=sales,
        total_cost=total_cost,
        total_sale=total_sale,
        total_profit=total_sale - total_cost,
    )
