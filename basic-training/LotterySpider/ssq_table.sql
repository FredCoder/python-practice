-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 2018-03-22 12:44:28
-- 服务器版本： 10.1.29-MariaDB
-- PHP Version: 7.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lottery_spider`
--

-- --------------------------------------------------------

--
-- 表的结构 `ssq`
--

CREATE TABLE `ssq` (
  `id` int(20) NOT NULL,
  `date` varchar(10) NOT NULL,
  `issue` varchar(10) NOT NULL,
  `number1` int(2) NOT NULL,
  `number2` int(2) NOT NULL,
  `number3` int(2) NOT NULL,
  `number4` int(2) NOT NULL,
  `number5` int(2) NOT NULL,
  `number6` int(2) NOT NULL,
  `numberEx` int(2) NOT NULL,
  `sales` varchar(20) NOT NULL,
  `first_prize` int(5) NOT NULL,
  `second_prize` int(10) NOT NULL,
  `place` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ssq`
--
ALTER TABLE `ssq`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `ssq`
--
ALTER TABLE `ssq`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
