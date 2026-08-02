-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: beelektronics_db
-- ------------------------------------------------------
-- Server version	8.0.46

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `cost_price` decimal(10,2) NOT NULL DEFAULT '0.00',
  `category` varchar(50) NOT NULL,
  `image` varchar(255) NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'MSI Modern',899.99,630.00,'Computer','images/computers/msi-modern.webp','27\" Full HD (1920 x 1080) 75Hz display\n\nIntel Core 5 - 120U 10 core processor (12MB cache, up to 5.0GHz)\n\n1TB SSD storage with 16GB RAM\n\n2 x HDMI ports\n\n2 x USB-A 2.0 ports\n\nWebcam\n\nBluetooth v5.3\n\nWi-Fi 6E (802.11 ax)\n\nWireless mouse & keyboard\n\nWindows 11 Home OS');
INSERT INTO `products` VALUES (2,'Asus V470 AIO 27\" Full HD All-in-One PC (Intel Core 5 - 210H)[512GB]',1999.00,1400.00,'Computer','images/computers/ASUS.webp','27\" Full HD (1920 x 1080) 300 nits IPS display\n\nIntel Core 5 - 210H 8 core processor (12MB cache, up to 4.8GHz)\n\n512GB M.2 NVMe PCIe 4.0 SSD storage with 16GB RAM\n\nIntel Graphics\n\n1 x HDMI port\n\n4 x USB-A ports\n\n1 x USB-C port\n\nWi?Fi 6E (802.11 ax)\n\nBluetooth v5.4\n\nWireless mouse & keyboard (USB receiver)\n\nWindows 11 Home');
INSERT INTO `products` VALUES (3,'HP OmniStudio 27\" Full HD All-in-One Desktop PC (Ryzen 5)[512GB]',1849.00,1295.00,'Computer','images/computers/HP-Omnistudio.webp','The HP OmniStudio 27 inch All in One Desktop brings productivity and entertainment together in a sleek, space saving all in one PC design. Powered by an AMD Ryzen 5 processor, this powerful HP desktop computer delivers smooth multitasking, immersive visuals and everyday performance. Ideal for work, study and home use.');
INSERT INTO `products` VALUES (4,'Lenovo IdeaCentre AIO 27\" QHD All-in-One PC (Intel Core 9)[1TB]',2899.00,2030.00,'Computer','images/computers/Lenovo.webp','27\" QHD (2560 x 1440) IPS Touch display\n\nIntel Core 9 - 270H 14 core processor (24MB cache, up to 5.8GHz)\n\n1TB SSD storage with 32GB RAM\n\n2 x HDMI ports\n\n2 x USB-A 2.0 ports\n\n2 x USB-A 3.2 ports\n\nBluetooth v 5.2\n\nWi-Fi 6 (802.11 ax)\n\nWindows 11 Home OS');
INSERT INTO `products` VALUES (5,'HP AIO 24-cr1000a 23.8\" FHD All-in-One PC (Intel Core Ultra 5)[512GB]',997.00,700.00,'Computer','images/computers/HP-AIO.webp','23.8\" Full HD (1920 x 1080) IPS display\n\nIntel Core Ultra 5 125H 14 core processor (1.2 - 4.5GHz)\n\n512GB SSD storage with 16GB RAM\n\nIntel Iris Xe graphics\n\n1 x HDMI port\n\n2 x USB 2.0 port\n\n1 x USB-C port\n\nHD webcam\n\nBluetooth v5.3\n\nWi-Fi 6 (802.11 ax)\n\nWindows 11 Home');
INSERT INTO `products` VALUES (6,'Apple iPhone 17 Pro Max 256GB (Silver)',2079.00,1450.00,'Phone','images/phones/Apple.webp','iPhone 17 Pro Max. The most powerful iPhone ever. Brilliant 6.9-inch display1, aluminium unibody design, A19 Pro chip, all 48MP rear cameras and best-ever battery life.');
INSERT INTO `products` VALUES (7,'Samsung Galaxy S25 256GB (Navy)',1387.00,970.00,'Phone','images/phones/Samsung.webp','Shoot and share your best memories with a powerful 50MP camera, powered by an advanced AI engine, with upgraded Nightography and Portrait Modes2, for stunningly clear and natural images, day and night.');
INSERT INTO `products` VALUES (8,'Google Pixel 10a 5G 128GB (Obsidian)',849.00,590.00,'Phone','images/phones/Google.webp','All the essentials, priced just right.');
INSERT INTO `products` VALUES (9,'OPPO Reno15 Pro 5G 512GB (Dusk Black)',1399.00,980.00,'Phone','images/phones/OPPO.webp','Small in Size. Big on Stamina.\nCompact, comfortable, and made for movement. The design fits naturally and effortlessly in your hand and pocket, while the long-lasting battery keeps you powered from morning to midnight');
INSERT INTO `products` VALUES (10,'HONOR Magic V6 5G 512GB (Red)',2999.00,2100.00,'Phone','images/phones/HONOR.webp','HONOR Nano-Crystal Shield Outer Screen\nAdvanced glass technology provides built-in, all-round protection to keep your display flawless.1 Enhanced clarity and durability, supported by international eye-care and performance certifications.');
INSERT INTO `products` VALUES (11,'Motorola Razr Fold 5G 256GB (PANTONE Blackened Blue)',2399.00,1680.00,'Phone','images/phones/Motorola.webp','Powered by the Snapdragon 8 Gen 5 and 12GB of RAM, the Razr Fold gives the best overall razr performance for everyday use and multitasking*. Laptop mode turns half the unfolded display into a trackpad, making it the best razr foldable phone for work and multitasking*, while the same chipset makes it just as capable for gaming on a big screen. Behind it all is a 6,000mAh silicon carbon battery, good for up to 43 hours of standard use, with 80W TurboPower wired charging, 50W wireless charging, and 5W reverse wireless charging to top up your other devices on the move.');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-07-29 16:20:56
