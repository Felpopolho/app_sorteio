-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 22-Nov-2023 às 20:13
-- Versão do servidor: 10.4.28-MariaDB
-- versão do PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `app_sorteio`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `participante`
--

CREATE TABLE `participante` (
  `numero` int(3) NOT NULL,
  `nome` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Extraindo dados da tabela `participante`
--

INSERT INTO `participante` (`numero`, `nome`) VALUES
(1, 'Danilo Moura'),
(2, 'Gracinha'),
(3, 'Danilo Moura'),
(4, 'Carlos EI21'),
(5, 'Angelo Aurich'),
(6, 'Criscielli'),
(7, 'Maria Luiza'),
(8, 'Maria Berião'),
(9, 'Maiana Paiva'),
(10, 'João EMA'),
(11, 'Maiana Paiva'),
(12, 'Maiana Paiva'),
(13, 'Polianna Aurich'),
(14, 'Cyntia '),
(15, 'Marlécia'),
(16, 'Daniel Moura'),
(17, 'Polianna Aurich'),
(18, 'Keyla Rabêllo'),
(19, 'Maiana Paiva'),
(20, 'Gracinha'),
(21, 'Miguel Lopes'),
(22, 'Julia Raquel'),
(23, 'Aline'),
(24, 'Milenka'),
(25, 'Fabiana Rodrigues'),
(26, 'Jhon Abner'),
(27, 'Gracinha'),
(28, 'Chrislayne'),
(29, 'Ana Carla'),
(30, 'Chrislayne'),
(31, 'Rosicler'),
(32, 'Chrislayne'),
(33, 'Carol ED31'),
(34, 'Lincoln'),
(35, 'Ruan ED11'),
(36, 'Danilo Moura'),
(37, 'Adenilson'),
(38, 'Mateus Lisboa'),
(39, 'Chrislayne'),
(40, 'Gustavo Gobbi'),
(41, 'Chrislayne'),
(42, 'Pai de Jennifer'),
(43, 'Julinha CAENS'),
(44, 'Adenilson'),
(45, 'Luis CORES'),
(46, 'Lincoln'),
(47, 'Caroline'),
(48, 'Bete Tigre'),
(49, 'Dilo'),
(50, 'Polianna Aurich'),
(51, 'Bete Tigre'),
(52, 'Herveton Nascimento'),
(53, 'Danilo Moura'),
(54, 'Valdirene Aurich'),
(55, 'Tarcísio ED11'),
(56, 'Lara Bolsanelo'),
(57, 'Peuzin'),
(58, 'Cássio'),
(59, 'Ian Rocha'),
(60, 'Daniel Lopes'),
(61, 'Kalebe ED31'),
(62, 'Aline EMA41'),
(63, 'Gerusa'),
(64, 'Rosicler'),
(65, 'Valdirente Aurich'),
(66, 'Marlécia'),
(67, 'Erineuza/Nadia'),
(68, 'Cássia'),
(69, 'Tigre'),
(70, 'Cedraz'),
(71, 'Ian Rocha'),
(72, 'Roberto'),
(73, 'Peuzin'),
(74, 'Bete Tigre'),
(75, 'Bete Tigre'),
(76, 'Bete Tigre'),
(77, 'Ithauan'),
(78, 'Dajuda'),
(79, 'Aldo'),
(80, 'Dajuda'),
(81, 'Jucelma Araujo'),
(82, 'Cássio'),
(83, 'Aline'),
(84, 'Flavão'),
(85, 'Gerusa'),
(86, 'Fabiana Rodrigues'),
(87, 'Miguel Lopes'),
(88, 'Samir'),
(89, 'Bete Tigre'),
(90, 'Erineuza/Nadia'),
(91, 'Peuzin'),
(92, 'Hannah'),
(93, 'Aline'),
(94, 'Polianna Aurich'),
(95, 'Dudao'),
(96, 'Bete Tigre'),
(97, 'Marlécia'),
(98, 'Tavares'),
(99, 'Thamiris DEPAE'),
(100, 'Maiana Paiva');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
