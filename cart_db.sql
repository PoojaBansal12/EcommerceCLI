-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 02, 2020 at 08:50 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cart_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `cart_id` int(11) NOT NULL,
  `product` int(100) NOT NULL,
  `user` int(100) NOT NULL,
  `purchase_indicator` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cart`
--

INSERT INTO `cart` (`cart_id`, `product`, `user`, `purchase_indicator`) VALUES
(44, 6, 1, 'Purchased'),
(46, 7, 1, 'Purchased'),
(47, 6, 1, 'Purchased'),
(48, 6, 1, 'Purchased'),
(49, 6, 1, 'Purchased'),
(50, 6, 1, 'Purchased'),
(51, 15, 6, 'Purchased'),
(52, 7, 6, 'Purchased'),
(53, 15, 6, 'Purchased'),
(54, 7, 6, 'Purchased'),
(55, 15, 1, 'Purchased'),
(56, 7, 1, 'Purchased'),
(57, 15, 1, 'Purchased'),
(58, 7, 1, 'Purchased'),
(59, 6, 1, 'Purchased'),
(61, 15, 19, 'Purchased');

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `cat_id` int(11) NOT NULL,
  `category_name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`cat_id`, `category_name`) VALUES
(10, 'Beauty'),
(9, 'Home and Living'),
(2, 'Kids'),
(1, 'Men'),
(6, 'Women');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(100) NOT NULL,
  `product_name` varchar(200) NOT NULL,
  `category` int(11) NOT NULL,
  `prod_price` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `product_name`, `category`, `prod_price`) VALUES
(6, 'Shirt', 1, 1000),
(7, 'Toys', 2, 500),
(15, 'Laptops', 1, 10000),
(16, 'Lipstick', 10, 1500),
(17, 'Eyeliner', 10, 350),
(18, 'Moisturizer', 10, 300),
(19, 'BedSheet', 9, 1000),
(20, 'Photo Frame', 9, 800),
(21, 'Pillow covers', 9, 2000),
(22, 'Kurtas', 6, 1000),
(23, 'Tops', 6, 700),
(24, 'Jeans', 6, 1500);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(100) NOT NULL,
  `username` varchar(200) NOT NULL,
  `user_type` varchar(200) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `user_type`, `password`) VALUES
(1, 'pooja', 'customer', 'pvb'),
(3, 'admin', 'admin', 'admin'),
(6, 'abc', 'customer', 'abc'),
(7, 'User', 'customer', 'user'),
(9, 'John', 'customer', 'john'),
(10, 'xyz', 'customer', 'xyz'),
(11, 'wer', 'customer', 'wer'),
(12, 'Tom', 'customer', 'tom'),
(13, 'James', 'customer', 'james'),
(15, 'Jerry', 'customer', 'jerry'),
(19, 'Halley', 'customer', 'halley');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`cart_id`),
  ADD KEY `product` (`product`),
  ADD KEY `user` (`user`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`cat_id`),
  ADD UNIQUE KEY `category_name` (`category_name`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`),
  ADD KEY `category` (`category`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `cart_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `cat_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cart`
--
ALTER TABLE `cart`
  ADD CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`product`) REFERENCES `products` (`product_id`),
  ADD CONSTRAINT `cart_ibfk_2` FOREIGN KEY (`user`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `products_ibfk_1` FOREIGN KEY (`category`) REFERENCES `categories` (`cat_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
