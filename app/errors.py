import difflib
import sqlite3

from flask import render_template, request, jsonify


KNOWN_PATHS = ['/', '/shop', '/checkout', '/admin/login', '/admin/dashboard']


def wants_json():
    """True if the client asked for JSON (fetch/API call) rather than a browser page."""
    return request.path.startswith('/api/') or request.path.startswith('/cart/')


def register_error_handlers(app):
    """Attach app-wide handlers so bad URLs, bad requests, and DB errors never crash with a raw traceback."""

    @app.errorhandler(404)
    def not_found(e):
        
        matches = difflib.get_close_matches(request.path, KNOWN_PATHS, n=1, cutoff=0.6)
        suggestion = matches[0] if matches else None

        if wants_json():
            return jsonify({"error": "Not found", "suggestion": suggestion}), 404
        return render_template('errors/404.html', suggestion=suggestion), 404

    @app.errorhandler(400)
    def bad_request(e):
        if wants_json():
            return jsonify({"error": "Bad request"}), 400
        return render_template('errors/generic.html', code=400, message="Bad request"), 400

    @app.errorhandler(sqlite3.Error)
    def database_error(e):
      
        app.logger.error("Database error on %s: %s", request.path, e)
        if wants_json():
            return jsonify({"error": "Something went wrong, please try again"}), 500
        return render_template('errors/generic.html', code=500, message="Something went wrong, please try again"), 500

    @app.errorhandler(500)
    def server_error(e):
        app.logger.error("Server error on %s: %s", request.path, e)
        if wants_json():
            return jsonify({"error": "Something went wrong, please try again"}), 500
        return render_template('errors/generic.html', code=500, message="Something went wrong, please try again"), 500