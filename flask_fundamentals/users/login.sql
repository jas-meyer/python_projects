-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: login
-- ------------------------------------------------------
-- Server version	5.7.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `salt` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES (11,'jimjockamo@gmail.com','asdfjkl;','Jason','Meyer',NULL,'2018-02-15 11:33:13','2018-02-15 11:33:13'),(12,'jimjockamo@gmail.com','22d7fe8c185003c98f97e5d6ced420c7','Jason','Meyer',NULL,'2018-02-15 11:37:45','2018-02-15 11:37:45'),(13,'dog@gmail.com','31f98cbff061a579f690855824d3b4f7','drop','drop',NULL,'2018-02-15 12:29:31','2018-02-15 12:29:31'),(14,'dog@gmail.com','95d300421321cb42839ae8047e289dbb','dog','dog',NULL,'2018-02-15 12:30:48','2018-02-15 12:30:48'),(15,'apple@apple.org','d66d0c18d08103b4012243e2f3780338','richard','richard',NULL,'2018-02-15 13:52:51','2018-02-15 13:52:51'),(16,'bugsbunny@gmail.com','d0c0b6fda58a6270b508922998f2d6fe','Bugs','Bunny',NULL,'2018-02-15 13:58:51','2018-02-15 13:58:51'),(17,'realdog@bowow.net','adf56e00b2ae891707add766c5669b09','real','dog','dda14b010a75dd87e855da68f3e53b','2018-02-15 14:17:36','2018-02-15 14:17:36'),(18,'asfdas@sadf.com','52c88b3659079f7c7082fbdb5654377a','asdf','asdf','25825af3ba72ca47c8550988bd4d99','2018-02-15 14:21:27','2018-02-15 14:21:27'),(19,'jimjockamo@gmail.com','07046e33ca26c89c1ef73bc60edbd4ad','asdfasfd','asdfasfd','481354326146995b2f2928db5772fc','2018-02-15 14:21:52','2018-02-15 14:21:52'),(20,'jimjockamo@gmail.com','2e12a8300bae928d6adcac14f94b3efe','asdfasfd','asdfasfd','1b53d5227b06e13acd98f2586bd30c','2018-02-15 14:22:56','2018-02-15 14:22:56');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-02-15 14:33:57
