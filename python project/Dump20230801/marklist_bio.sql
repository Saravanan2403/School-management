-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: marklist
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bio`
--

DROP TABLE IF EXISTS `bio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bio` (
  `Stu_Name` varchar(30) DEFAULT NULL,
  `Stu_Roll_Number` int NOT NULL,
  `Stu_Mother_Name` varchar(30) DEFAULT NULL,
  `Stu_Father_Or_Guardian_Name` varchar(30) DEFAULT NULL,
  `Stu_School_Name` varchar(30) DEFAULT NULL,
  `Stu_School_Code` int DEFAULT NULL,
  `Stu_English_Mark` int DEFAULT NULL,
  `Stu_Maths_Mark` int DEFAULT NULL,
  `Stu_Bio_Mark` int DEFAULT NULL,
  `Stu_Phy_Mark` int DEFAULT NULL,
  `Stu_Chem_Mark` int DEFAULT NULL,
  `me` int DEFAULT NULL,
  `mm` int DEFAULT NULL,
  `mb` int DEFAULT NULL,
  `mp` int DEFAULT NULL,
  `mc` int DEFAULT NULL,
  `Stu_Total_Mark` int DEFAULT NULL,
  `Stu_Result` varchar(20) NOT NULL,
  PRIMARY KEY (`Stu_Roll_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bio`
--

LOCK TABLES `bio` WRITE;
/*!40000 ALTER TABLE `bio` DISABLE KEYS */;
INSERT INTO `bio` VALUES ('Sriram',1201,'Seema Vani','Ranjith Kumar','Kendriya Vidyalaya',5101,39,44,23,32,31,59,64,53,62,61,299,'PASS'),('Seema',1202,'Vani','Kumar','Vani Vidyalaya',5102,64,56,43,57,61,84,76,73,87,91,411,'PASS'),('Devi',1203,'Rani','Ravi','Vani Vidyalaya',5102,23,53,25,30,18,43,73,55,60,48,279,'FAIL'),('Pavi',1204,'Riya','Siva','Everwin',5103,54,52,50,56,58,74,72,80,86,88,400,'PASS'),('Dharun',1205,'vashathi','peramguru','Kendriya Vidyalaya',5101,38,43,23,31,30,58,63,53,61,60,295,'PASS'),('kavin',1206,'Devi','Tarun','Kendriya Vidyalaya',5101,24,20,22,21,28,44,40,52,51,58,245,'FAIL'),('Ramu',1207,'Raniamma','Tarun','Everwin',5103,23,22,24,27,21,43,42,54,57,51,247,'FAIL'),('Ranjith',1208,'Rani','Rajasammy','Vani Vidyalaya',5102,40,50,49,51,38,60,70,79,81,68,358,'PASS'),('Srithu',1209,'Seetha','Ram','Everwin',5103,22,21,22,19,10,42,41,52,49,39,223,'FAIL'),('Priyanka',1210,'Kaviya','Kavin','Kendriya Vidyalaya',5102,23,21,18,7,11,43,41,48,37,41,210,'FAIL');
/*!40000 ALTER TABLE `bio` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-01 18:08:59
