# bee-lektronics
CST150 Project 3 E-Commerce Website (SAE)

## Project Structure

```
bee-lektronics/
├── app/            (backend)
├── models/         (backend)
├── routes/         (backend)
├── utils/          (backend)
├── instance/       (backend)
├── migrations/     (backend)
├── templates/      (frontend)
├── static/         (frontend)
├── run.py          (backend)
├── .env            (backend)
└── requirements.txt (backend)
```

Flask serves the HTML directly (Jinja2 templates) `templates/` and `static/` are the frontend; everything else is backend.

---

## Backend (Brent's section)

These folders are currently empty (aside from `.gitkeep` placeholders so git tracks them) — fill them in as the database/logic gets built.

### `app/`
Core Flask app setup.
- `__init__.py` — creates and configures the Flask app (the "app factory"); registers routes and extensions
- `config.py` — app settings (dev/prod config values, e.g. `SECRET_KEY`, `DATABASE_URL`)
- `extensions.py` — shared extensions like the database connection and session config

### `models/`
Database tables/schema — one file per table group.
- `product.py` — Product, Category tables
- `cart.py` — CartItem table (guest/session-based cart, no user login required)
- `order.py` — Order, OrderItem tables
- `admin.py` — Admin login table

### `routes/`
URL endpoints — the glue between `models/` and `templates/`. Each route fetches data and renders a template with it.
- `main.py` — Home, Shop, Product Detail, About/Contact pages
- `cart.py` — Cart view + add/remove item endpoints
- `orders.py` — Checkout + Order Confirmation pages
- `admin.py` — Admin login + Sales Summary page

### `utils/`
- `decorators.py` — helper functions, e.g. an `@admin_required` check to gate admin pages

### `instance/`
- `config.py` — local secrets/config (gitignored, never committed — each person creates their own copy locally)

### `migrations/`
Auto-generated database migration files (created by Flask-Migrate once the models are ready).

### Root-level backend files
- `run.py` — entry point that starts the Flask server
- `.env` — environment variables (`SECRET_KEY`, `DATABASE_URL`, etc.), gitignored
- `requirements.txt` — Python package dependencies

---

## Frontend (Koi's section)

### `templates/`
HTML pages (Jinja2), one per site-map page.
- `base.html` — shared layout: navbar, footer, page wrapper that every other page extends
- `home.html` — Home page
- `shop.html` — Product listing page
- `product_detail.html` — Single product page
- `cart.html` — Cart contents / shipping + payment info
- `checkout.html` — Checkout form
- `order_confirmation.html` — "Order complete" page
- `about_contact.html` — About/Contact info page
- `admin/login.html` — Admin login form
- `admin/sales_summary.html` — Admin-only sales data page

### `static/`
CSS, JS, and images served as-is (no build step needed).
- `css/base.css` — global/shared styles
- `css/shop.css`, `css/cart.css`, `css/admin.css` — page-specific styles
- `js/cart.js` — add/remove cart item behavior (talks to `routes/cart.py` endpoints)
- `js/checkout.js` — checkout form behavior
- `js/admin.js` — admin page behavior
- `images/` — product photos, logos, icons

IMAGE REFERENCES

https://openverse.org/image/7e29aa97-c842-48d3-a642-55c3de823815?q=bee+icon&p=5

https://openverse.org/image/1e62d106-4209-4e4c-8629-9e0bffeb3f28?q=honey+comb&p=25

GUIDES USED

https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow/Carousels