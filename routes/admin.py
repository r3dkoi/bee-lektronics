from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from functools import wraps

from app.config import Config

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
    # TODO: pass real sales data once models/orders exist
    return render_template('admin/sales_summary.html')
