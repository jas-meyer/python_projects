-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: wall
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
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `idcomments` int(11) NOT NULL AUTO_INCREMENT,
  `message_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `comment` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`idcomments`),
  KEY `fk_comments_messages1_idx` (`message_id`),
  KEY `fk_comments_users1_idx` (`user_id`),
  CONSTRAINT `fk_comments_messages1` FOREIGN KEY (`message_id`) REFERENCES `messages` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (2,1,2,'asdf\r\nasfd','2018-02-15 19:18:18','2018-02-15 19:18:18'),(3,1,2,'\r\n123','2018-02-15 19:18:20','2018-02-15 19:18:20'),(4,3,2,'\r\nasdf','2018-02-15 20:17:37','2018-02-15 20:17:37'),(6,1,2,'asdf\r\n','2018-02-15 20:54:24','2018-02-15 20:54:24'),(7,1,2,'\r\napples\r\n','2018-02-15 20:57:18','2018-02-15 20:57:18'),(8,1,2,'apples\r\n','2018-02-15 20:57:58','2018-02-15 20:57:58'),(9,1,2,'nope\r\n','2018-02-15 20:58:28','2018-02-15 20:58:28'),(10,1,2,'ok\r\n','2018-02-15 20:59:07','2018-02-15 20:59:07'),(11,1,2,'\r\nunicorns','2018-02-15 21:00:23','2018-02-15 21:00:23'),(12,1,2,'what\r\n','2018-02-15 21:00:42','2018-02-15 21:00:42'),(13,2,2,'nope\r\n','2018-02-15 21:00:46','2018-02-15 21:00:46'),(14,3,2,'help\r\n','2018-02-15 21:00:51','2018-02-15 21:00:51'),(15,1,1,'whats up doc\r\n','2018-02-15 22:10:24','2018-02-15 22:10:24'),(16,6,1,'Daffy has taken over your profile\r\n','2018-02-15 22:27:24','2018-02-15 22:27:24'),(17,6,1,'Daffy has taken over your profile\r\n','2018-02-15 22:28:23','2018-02-15 22:28:23'),(18,7,1,'\r\nwhat?','2018-02-15 22:29:10','2018-02-15 22:29:10'),(19,7,1,'\r\nwhat?','2018-02-15 22:30:11','2018-02-15 22:30:11'),(20,10,1,'\r\nhello','2018-02-15 22:30:52','2018-02-15 22:30:52'),(21,13,2,'\r\n','2018-02-15 22:43:41','2018-02-15 22:43:41'),(22,1,2,'\r\n','2018-02-15 22:45:26','2018-02-15 22:45:26'),(23,14,2,'\r\n','2018-02-15 22:46:05','2018-02-15 22:46:05'),(24,15,2,'\r\nwhy is this a blank message?','2018-02-16 08:13:59','2018-02-16 08:13:59');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users_idx` (`user_id`),
  CONSTRAINT `fk_messages_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,1,'hello\r\n','2018-02-15 16:54:13','2018-02-15 16:54:13'),(2,1,'Don\'t log me out\r\n','2018-02-15 16:55:31','2018-02-15 16:55:31'),(3,1,'\r\ndasf','2018-02-15 17:10:52','2018-02-15 17:10:52'),(4,2,'different user\r\n','2018-02-15 17:40:28','2018-02-15 17:40:28'),(5,1,'\r\nasdf','2018-02-15 18:35:01','2018-02-15 18:35:01'),(6,1,'\r\n','2018-02-15 18:35:08','2018-02-15 18:35:08'),(7,1,'\r\n','2018-02-15 18:37:23','2018-02-15 18:37:23'),(8,1,'\r\n','2018-02-15 18:39:25','2018-02-15 18:39:25'),(9,1,'\r\n','2018-02-15 18:41:28','2018-02-15 18:41:28'),(10,1,'\r\nNew message','2018-02-15 18:46:51','2018-02-15 18:46:51'),(11,1,'\r\nDoes this work?','2018-02-15 22:37:23','2018-02-15 22:37:23'),(12,1,'\r\n','2018-02-15 22:37:25','2018-02-15 22:37:25'),(13,1,'\r\n','2018-02-15 22:38:41','2018-02-15 22:38:41'),(14,2,'\r\n','2018-02-15 22:41:11','2018-02-15 22:41:11'),(15,2,'\r\n','2018-02-15 22:46:01','2018-02-15 22:46:01');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `salt` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Bugs','Bunny','bugsbunny@gmail.com','318ace41b216c3549af52bd4b9ae3d00','6fa3fc54d3d6802c516324ec11b117','2018-02-15 16:02:12','2018-02-15 16:02:12'),(2,'steve','jobs','apple@apple.org','4a782552caca929fb5096a5909227715','b7988d81b352fb905037e9825b9760','2018-02-15 17:19:47','2018-02-15 17:19:47');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-02-16  8:18:16
