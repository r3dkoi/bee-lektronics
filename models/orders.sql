DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email varchar(255) NOT NULL,
  phone varchar(20) NOT NULL,
  suburb varchar(50) NOT NULL,
  order_date datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  total_sale_price decimal(10,2) NOT NULL
);

INSERT INTO orders VALUES (1,'j.smith@gmail.com','0412345678','Parramatta','2026-07-15 10:32:00',899.99);
