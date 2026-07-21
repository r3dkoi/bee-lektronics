from app import create_app

app = create_app()

if __name__ == '__main__':
    # debug=True auto-reloads on file changes and shows detailed error pages — dev only.
    app.run(debug=True)
