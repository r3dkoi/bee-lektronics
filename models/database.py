import os
import sqlite3

# All three .sql files (products, orders, order_items) get loaded into this
# single file on first run — see init_db() below.
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'instance', 'beelektronics.db')


def get_connection():
    # instance/ is gitignored, so a fresh clone (e.g. on first deploy) won't
    # have the .db file yet — seed it automatically instead of requiring a
    # separate manual setup step.
    if not os.path.exists(DB_PATH):
        init_db()

    conn = sqlite3.connect(DB_PATH)
    # row_factory makes each row behave like a dict (row['name']) as well as
    # a tuple (for product_id, cost_price in rows), which is what routes/*.py needs.
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys = ON')
    return conn


def init_db():
    # Rebuilds the database from the .sql dumps — safe to re-run any time
    # (each dump starts with DROP TABLE), e.g. to reset to seed data.
    sql_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    for filename in ('products.sql', 'orders.sql', 'order_items.sql'):
        with open(os.path.join(sql_dir, filename), encoding='utf-8') as f:
            conn.executescript(f.read())
    conn.commit()
    conn.close()


if __name__ == '__main__':
    init_db()
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    for row in cursor.fetchall():
        print(tuple(row))

    cursor.close()
    conn.close()
