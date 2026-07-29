import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', ''),
        database=os.environ.get('DB_NAME', 'beelektronics_db'),
    )

if __name__ == '__main__':
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()