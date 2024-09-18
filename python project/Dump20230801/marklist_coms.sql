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
-- Table structure for table `coms`
--

DROP TABLE IF EXISTS `coms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coms` (
  `Stu_Name` varchar(30) DEFAULT NULL,
  `Stu_Roll_Number` int NOT NULL,
  `Stu_Mother_Name` varchar(30) DEFAULT NULL,
  `Stu_Father_Or_Guardian_Name` varchar(30) DEFAULT NULL,
  `Stu_School_Name` varchar(30) DEFAULT NULL,
  `Stu_School_Code` int DEFAULT NULL,
  `Stu_English_Mark` int DEFAULT NULL,
  `Stu_Maths_Mark` int DEFAULT NULL,
  `Stu_Coms_Mark` int DEFAULT NULL,
  `Stu_Bis_Mark` int DEFAULT NULL,
  `Stu_Eco_Mark` int DEFAULT NULL,
  `me` int DEFAULT NULL,
  `mm` int DEFAULT NULL,
  `mc` int DEFAULT NULL,
  `mb` int DEFAULT NULL,
  `meo` int DEFAULT NULL,
  `Stu_Total_Mark` int DEFAULT NULL,
  `Stu_Result` varchar(20) NOT NULL,
  PRIMARY KEY (`Stu_Roll_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coms`
--

LOCK TABLES `coms` WRITE;
/*!40000 ALTER TABLE `coms` DISABLE KEYS */;
INSERT INTO `coms` VALUES ('Ramesh',1221,'Rani','Raja','Kendriya Vidyalaya',5101,70,79,80,70,74,90,99,100,90,94,473,'PASS'),('Hainee',1222,'Nithya','Kumar','Kendriya Vidyalaya',5101,56,76,46,54,57,76,86,66,74,77,379,'PASS'),('Dharni',1223,'Divya','Ravi','Vani Vidyalaya',5102,18,34,43,51,31,38,54,63,71,51,177,'FAIL'),('Dharun',1224,'Swetha','Arun','Vani Vidyalaya',5102,56,59,51,49,47,76,79,71,69,67,362,'PASS'),('Parthi',1225,'Kumari','Anand','Everwin',5103,12,35,64,23,29,32,55,86,43,49,265,'FAIL'),('Thavashika',1226,'Sriram','Sriram','Kendriya Vidyalaya',5101,80,80,80,80,80,100,100,100,100,100,500,'PASS'),('Pavi',1227,'Pattumami','perama','Kendriya Vidyalaya',5101,56,58,53,46,18,76,78,73,66,38,331,'FAIL'),('Ravi',1228,'Ammu','Ramasammy','Vani Vidyalaya',5102,4,13,9,10,11,24,33,29,30,31,147,'FAIL'),('Vemal',1229,'Sumathi','Periyasamy','Everwin',5103,12,15,36,52,43,32,35,56,72,63,258,'FAIL'),('Somiya',1230,'Fathima','Aquil','Everwin',5103,45,54,35,65,49,65,74,55,85,69,348,'PASS');
/*!40000 ALTER TABLE `coms` ENABLE KEYS */;
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
