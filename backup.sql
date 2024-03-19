-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: profile
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

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
-- Table structure for table `user`
--
CREATE Database `profile`;
USE profile;
DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password_hash` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Ariel','$2b$12$f9KjeOuDB4a4pGczfXkqcOVq/Ewg8.bnwjcFahU9Oqz3fZ2C0qS.W'),(3,'AriDel','$2b$12$q5btu4/4X8a2Lv8IvJk8gurmakTes5/Qc/Evxcy0Xh19S3gUjWvt.'),(5,'Oriel','$2b$12$wj7aZnJRpxxg8Pe0P7R39upfvcfcngIhFD4DPwtYbWkRfqxJiMTHu'),(7,'Uriel','$2b$10$YKgyFI8S2D4Cggkx5cMOV.556dECzxEHqcslByUSLLSgchzzDiTRu'),(12,'ABriel','$2b$10$vSTnjdbPvriLBy68qFA70OGDIZgpZP17TLAQhLDOI9eTNRBLZCb.m'),(14,'ABriel1','$2b$10$p2y7pMPJ/qEZptDIlqJcYOl./eZZuMLNr0r.wU37cxhuYsiTfRWsq'),(15,'Flask','$2b$10$U3td7vF6cLfX0djAwQ7VXugkwt.MPc/MdD0kMtSIJg4WM4SC32L2e'),(16,'Flask8','$2b$10$b/CE4ZeGTuh6JL0O4XLPCeR2jX0NTKHcc7O1fDagPPAdcWY05TZly'),(18,'Flask85','$2b$10$bKl8ijK.1iV7WsLW0Rd66eWTjJHKboyKK0qlTdSvv4q4GWO/fIGYC'),(20,'Flask1','$2b$10$mkX9sB7WRHqZ1LEX1TLhSer72SzzDG6/hJuKm9L8j0d711KxVQ2N6'),(22,'Flask2','$2b$10$BOqLUSkxr5dDZsFqsNwANeEbgsq1kahmNRno0Rbu9sW2RbW7/bxcm'),(23,'Flask3','$2b$10$VN4vKQXmXMnRYLoUtroI2etEFnjYFWAbdptwOCZOTB4EIvJRPGKK6'),(25,'Flask4','$2b$10$ZRtlnb2C0MZ0giLkne5Pn.7A4L2dmHZ9S9hJNJ6Ai5tNU1PFYjQMi'),(28,'Flask5','$2b$10$S52eBIBcituNtXBDhkd/D.rpKZvfP9qEU4P9dfjd..cy55c32ULMm'),(29,'Flask6','$2b$10$mwRTzHa4Bnwf7g2yQ7Mz/ONLcbcojw9YdXEz8VHP5yLq3kB1l8uau'),(33,'Flask10','$2b$10$SMyQZnEDELV3ZxEA0bcHkuFUXO3FchYKnF85zwBcBP1mjRpQmS.Kq'),(34,'Flask11','$2b$10$cgpV.UKWDpLQlfgB7MaU7eHEdDXlXvyeWKT2HU7CYnH9pANuD4dbG'),(37,'Flask12','$2b$10$0pkomWBeuRXn8R1cFLzAVOPzSJQWrWwhRHoVGcYPTfUZ.5HBnSdMS'),(39,'Flask15','$2b$10$NbExfd9SJwiPC3vFICflVex.Q/enrnZbG0s3gvWfvKsXH65VM7jse'),(41,'Flask18','$2b$10$iYWRETUvpC.1dS3YN.0cb.EWuhQ6aihxkisaP47dhzJIEaEySCHZy'),(44,'Flask20','$2b$10$MKHMAKVwgmtE0AA2hxBRY.3xlz5aE4/UghpxAgQERuWka9aE6mYIC'),(46,'Flask22','$2b$10$DRUD9h63EOIpm8paP3.2q.mf6hO0up2URhiknqou5GdiVJzgXG1Ke'),(50,'Flask23','$2b$10$UaESANgK9/TXihC4ulGKu.qWfoBYwrKIESYPQEeuevSfY5IJESiTO'),(52,'Flask25','$2b$10$APIFkYuGIFJuzGZfmIKJpOBx/hli9iqKfnFMlctqn9KoU9F677qPu'),(54,'Flask26','$2b$10$2fZnzx4.9yzcNXp9j5QrceGfFaC7PDQ7JaAV4i51XSMFYThxqWsuO'),(55,'Flask29','$2b$10$zryIHYH2W5MvecnDQxRKe.GfzPiJOhQ4VNd2zZvS9mEggRcPot2nC'),(57,'Flask30','$2b$10$ndRqHUiPFqSe.pZXY31y..szcJM8HaybLLQuzBcG76liqO9Md9vlO'),(58,'Flask32','$2b$10$lC./xmkUcSlz/CZUaI4QxeWqLs/zqL.9mH9Zxqt4y0weT35j9sDja'),(60,'Flask33','$2b$10$odS9uGqXnlkPW4C7eSd6su2JA1i1roYpCuVaHH1ayyRQvE1S4yIsC'),(65,'Flask34','$2b$10$F1C43..w//yJ5fmTXFDnWO7XS8ymK8gUeVNoWrc.8Sm6FsQP9Hxvi');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-19 17:38:11
