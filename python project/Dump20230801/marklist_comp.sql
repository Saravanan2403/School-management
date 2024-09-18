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
-- Table structure for table `comp`
--

DROP TABLE IF EXISTS `comp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comp` (
  `Stu_Name` varchar(30) DEFAULT NULL,
  `Stu_Roll_Number` int NOT NULL,
  `Stu_Mother_Name` varchar(30) DEFAULT NULL,
  `Stu_Father_Or_Guardian_Name` varchar(30) DEFAULT NULL,
  `Stu_School_Name` varchar(30) DEFAULT NULL,
  `Stu_School_Code` int DEFAULT NULL,
  `Stu_English_Mark` int DEFAULT NULL,
  `Stu_Maths_Mark` int DEFAULT NULL,
  `Stu_Comp_Mark` int DEFAULT NULL,
  `Stu_Phy_Mark` int DEFAULT NULL,
  `Stu_Chem_Mark` int DEFAULT NULL,
  `me` int DEFAULT NULL,
  `mm` int DEFAULT NULL,
  `mco` int DEFAULT NULL,
  `mp` int DEFAULT NULL,
  `mc` int DEFAULT NULL,
  `Stu_Total_Mark` int DEFAULT NULL,
  `Stu_Result` varchar(20) NOT NULL,
  PRIMARY KEY (`Stu_Roll_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comp`
--

LOCK TABLES `comp` WRITE;
/*!40000 ALTER TABLE `comp` DISABLE KEYS */;
INSERT INTO `comp` VALUES ('Durga',1211,'Kalai','Srinath','Kendriya Vidyalaya',5101,56,65,54,52,59,76,85,84,82,89,416,'PASS'),('Dharsini',1212,'Gayathri','Venkat','Kendriya Vidyalaya',5101,25,24,18,12,32,45,44,48,42,62,241,'FAIL'),('Kavin',1213,'Vanilla','Surya','Kendriya Vidyalaya',5101,69,61,57,53,59,89,81,87,83,89,429,'PASS'),('Deva',1214,'Bala','Murugan','Kendriya Vidyalaya',5101,24,18,22,29,12,44,38,42,49,32,205,'FAIL'),('Devi',1215,'Amutha','Raj','Vani Vidyalaya',5102,80,79,68,69,65,100,99,98,99,95,491,'PASS'),('Tarun',1216,'Lajitha','Vikram','Vani Vidyalaya',5102,14,21,19,12,8,34,41,39,32,38,184,'FAIL'),('Karan',1217,'Meenakshi','Mani','Vani Vidyalaya',5102,32,39,41,43,41,52,59,71,73,71,326,'PASS'),('Dharun',1218,'Savitha','Ashok','Everwin',5103,11,16,24,34,10,31,36,54,64,40,225,'FAIL'),('Siva',1219,'Riddhi','Saravana','Everwin',5103,46,56,43,46,51,66,76,73,76,81,372,'PASS'),('Tharunika',1220,'Kavitha','Aryan','Everwin',5103,23,16,19,20,8,43,36,49,50,38,216,'FAIL');
/*!40000 ALTER TABLE `comp` ENABLE KEYS */;
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
