# bee-lektronics
CST150 Project 3 E-Commerce Website (SAE)

## Project Structure

```
bee-lektronics/
├── app/            (backend)
├── models/         (backend)
├── routes/         (backend)
├── instance/       (backend)
├── templates/      (frontend)
├── static/         (frontend)
├── run.py          (backend)
├── .env            (backend)
└── requirements.txt (backend)
```

Flask serves the HTML directly (Jinja2 templates) `templates/` and `static/` are the frontend; everything else is backend.

---

## Backend 

### `app/`
Core Flask app setup.
- `__init__.py` — creates and configures the Flask app (the "app factory"); registers routes 
- `config.py` — app settings (`SECRET_KEY`, `ADMIN_USERNAME`, `ADMIN_PASSWORD`)

### `models/`
NO ORM (Object-Relational Mapping) models, just raw SQL. In order to host a site for free, needed to move from MySQL to SQLite. Still the data layer.
- `database.py` opens a SQLite connection (`instance/beelektronics.db`) with `row_factory = sqlite3.Row` so rows can be accessed like dicts; `init_db()` seeds DB from the `.sql` files below
- `products.sql` - Contains products table; the digital stock
- `orders.sql` - Contains orders table; customer details saved from delivery form
- `order_items.sql` - Joined with orders.sql and contains actual product order details (quantity ordered), the product's price and the product's cost for us ordering it's stock


### `routes/`
URL endpoints — the glue between `models/` and `templates/`. Each route fetches data and renders a template with it.
- `main.py` — Home, Shop, Product Detail pages, plus `robots.txt` and `sitemap.xml`
- `cart.py` — Cart view + add/remove item endpoints
- `orders.py` — Checkout page + server-side delivery details validation + order submission which redirecits back top /shop.
- `admin.py` — Admin login + Sales Summary page

### `instance/`
- `config.py` — local secrets/config (gitignored, never committed — each person creates their own copy locally)


### Root-level backend files
- `run.py` — entry point that starts the Flask server (`gunicorn run:app` for Render production, `python run.py` for local dev)
- `.env` — environment variables (`SECRET_KEY`, `ADMIN_USERNAME`, `ADMIN_PASSWORD`, etc.), gitignored
- `requirements.txt` — Python package dependencies

---

## Frontend 

### `templates/`
HTML pages (Jinja2), one per site-map page.
- `base.html` — shared layout: navbar (sticky, hamburger menu on mobile, cart item-count badge), footer, page wrapper that every other page extends
- `home.html` — Home page
- `shop.html` — Product listing page
- `product_detail.html` — Single product page
- `checkout.html` — Cart review + shipping info + order submission
- `admin/login.html` — Admin login form
- `admin/sales_summary.html` — Admin-only sales data page

### `static/`
CSS, JS, and images served as-is (no build step needed).
- `css/base.css` — global/shared styles (navbar, footer, hero, featured/carousel sections)
- `css/shop.css`, `css/product_detail.css`, `css/checkout.css`, `css/minicart.css`, `css/admin.css` — page-specific styles
- `js/main.js` — hamburger nav toggle + home page carousel
- `js/minicart.js` — minicart overlay (open/close, render cart, add/update/remove, cart badge count)
- `js/shop.js`, `js/product_detail.js`, `js/checkout.js`, `js/admin.js` — page-specific behavior
- `images/` — product photos, logos, icons


SQLITE3 NOTES
1. To run SQLITE3 in terminal
    python -m sqlite3 instance/bee.db

IMAGE REFERENCES

https://openverse.org/image/7e29aa97-c842-48d3-a642-55c3de823815?q=bee+icon&p=5

https://openverse.org/image/1e62d106-4209-4e4c-8629-9e0bffeb3f28?q=honey+comb&p=25

GUIDES USED

https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow/Carousels

https://hype4.academy/tools/glassmorphism-generator

RESOURCES USED

https://fonts.google.com/specimen/Sulphur+Point?preview.script=Latn