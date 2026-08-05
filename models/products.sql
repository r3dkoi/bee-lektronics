DROP TABLE IF EXISTS products;

CREATE TABLE products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name varchar(120) NOT NULL,
  price decimal(10,2) NOT NULL,
  cost_price decimal(10,2) NOT NULL DEFAULT '0.00',
  category varchar(50) NOT NULL,
  image varchar(255) NOT NULL,
  description text NOT NULL
);

INSERT INTO products VALUES (1,'MSI Modern',899.99,630.00,'Computer','images/computers/msi-modern.webp','27" Full HD (1920 x 1080) 75Hz display

Intel Core 5 - 120U 10 core processor (12MB cache, up to 5.0GHz)

1TB SSD storage with 16GB RAM

2 x HDMI ports

2 x USB-A 2.0 ports

Webcam

Bluetooth v5.3

Wi-Fi 6E (802.11 ax)

Wireless mouse & keyboard

Windows 11 Home OS');
INSERT INTO products VALUES (2,'Asus V470 AIO 27" Full HD All-in-One PC (Intel Core 5 - 210H)[512GB]',1999.00,1400.00,'Computer','images/computers/ASUS.webp','27" Full HD (1920 x 1080) 300 nits IPS display

Intel Core 5 - 210H 8 core processor (12MB cache, up to 4.8GHz)

512GB M.2 NVMe PCIe 4.0 SSD storage with 16GB RAM

Intel Graphics

1 x HDMI port

4 x USB-A ports

1 x USB-C port

Wi-Fi 6E (802.11 ax)

Bluetooth v5.4

Wireless mouse & keyboard (USB receiver)

Windows 11 Home');
INSERT INTO products VALUES (3,'HP OmniStudio 27" Full HD All-in-One Desktop PC (Ryzen 5)[512GB]',1849.00,1295.00,'Computer','images/computers/HP-Omnistudio.webp','The HP OmniStudio 27 inch All in One Desktop brings productivity and entertainment together in a sleek, space saving all in one PC design. Powered by an AMD Ryzen 5 processor, this powerful HP desktop computer delivers smooth multitasking, immersive visuals and everyday performance. Ideal for work, study and home use.');
INSERT INTO products VALUES (4,'Lenovo IdeaCentre AIO 27" QHD All-in-One PC (Intel Core 9)[1TB]',2899.00,2030.00,'Computer','images/computers/Lenovo.webp','27" QHD (2560 x 1440) IPS Touch display

Intel Core 9 - 270H 14 core processor (24MB cache, up to 5.8GHz)

1TB SSD storage with 32GB RAM

2 x HDMI ports

2 x USB-A 2.0 ports

2 x USB-A 3.2 ports

Bluetooth v 5.2

Wi-Fi 6 (802.11 ax)

Windows 11 Home OS');
INSERT INTO products VALUES (5,'HP AIO 24-cr1000a 23.8" FHD All-in-One PC (Intel Core Ultra 5)[512GB]',997.00,700.00,'Computer','images/computers/HP-AIO.webp','23.8" Full HD (1920 x 1080) IPS display

Intel Core Ultra 5 125H 14 core processor (1.2 - 4.5GHz)

512GB SSD storage with 16GB RAM

Intel Iris Xe graphics

1 x HDMI port

2 x USB 2.0 port

1 x USB-C port

HD webcam

Bluetooth v5.3

Wi-Fi 6 (802.11 ax)

Windows 11 Home');
INSERT INTO products VALUES (6,'Apple iPhone 17 Pro Max 256GB (Silver)',2079.00,1450.00,'Phone','images/phones/Apple.webp','iPhone 17 Pro Max. The most powerful iPhone ever. Brilliant 6.9-inch display1, aluminium unibody design, A19 Pro chip, all 48MP rear cameras and best-ever battery life.');
INSERT INTO products VALUES (7,'Samsung Galaxy S25 256GB (Navy)',1387.00,970.00,'Phone','images/phones/Samsung.webp','Shoot and share your best memories with a powerful 50MP camera, powered by an advanced AI engine, with upgraded Nightography and Portrait Modes2, for stunningly clear and natural images, day and night.');
INSERT INTO products VALUES (8,'Google Pixel 10a 5G 128GB (Obsidian)',849.00,590.00,'Phone','images/phones/Google.webp','All the essentials, priced just right.');
INSERT INTO products VALUES (9,'OPPO Reno15 Pro 5G 512GB (Dusk Black)',1399.00,980.00,'Phone','images/phones/OPPO.webp','Small in Size. Big on Stamina.
Compact, comfortable, and made for movement. The design fits naturally and effortlessly in your hand and pocket, while the long-lasting battery keeps you powered from morning to midnight');
INSERT INTO products VALUES (10,'HONOR Magic V6 5G 512GB (Red)',2999.00,2100.00,'Phone','images/phones/HONOR.webp','HONOR Nano-Crystal Shield Outer Screen
Advanced glass technology provides built-in, all-round protection to keep your display flawless.1 Enhanced clarity and durability, supported by international eye-care and performance certifications.');
INSERT INTO products VALUES (11,'Motorola Razr Fold 5G 256GB (PANTONE Blackened Blue)',2399.00,1680.00,'Phone','images/phones/Motorola.webp','Powered by the Snapdragon 8 Gen 5 and 12GB of RAM, the Razr Fold gives the best overall razr performance for everyday use and multitasking*. Laptop mode turns half the unfolded display into a trackpad, making it the best razr foldable phone for work and multitasking*, while the same chipset makes it just as capable for gaming on a big screen. Behind it all is a 6,000mAh silicon carbon battery, good for up to 43 hours of standard use, with 80W TurboPower wired charging, 50W wireless charging, and 5W reverse wireless charging to top up your other devices on the move.');
