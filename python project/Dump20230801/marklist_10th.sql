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
-- Table structure for table `10th`
--

DROP TABLE IF EXISTS `10th`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `10th` (
  `Stu_Name` varchar(30) DEFAULT NULL,
  `Stu_Roll_Number` int NOT NULL,
  `Stu_Mother_Name` varchar(30) DEFAULT NULL,
  `Stu_Father_Or_Guardian_Name` varchar(30) DEFAULT NULL,
  `Stu_School_Name` varchar(30) DEFAULT NULL,
  `Stu_School_Code` int DEFAULT NULL,
  `Stu_English_Mark` int DEFAULT NULL,
  `Stu_Maths_Mark` int DEFAULT NULL,
  `Stu_Tamil_Or_Hindi_Mark` int DEFAULT NULL,
  `Stu_Science_Mark` int DEFAULT NULL,
  `Stu_Social_Science_Mark` int DEFAULT NULL,
  `me` int DEFAULT NULL,
  `mm` int DEFAULT NULL,
  `mth` int DEFAULT NULL,
  `ms` int DEFAULT NULL,
  `mss` int DEFAULT NULL,
  `Stu_Total_Mark` int DEFAULT NULL,
  `Stu_Result` varchar(20) NOT NULL,
  PRIMARY KEY (`Stu_Roll_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `10th`
--

LOCK TABLES `10th` WRITE;
/*!40000 ALTER TABLE `10th` DISABLE KEYS */;
INSERT INTO `10th` VALUES ('Ravi',1001,'Tharunika','Karan','Kendriya Vidyalaya',5101,60,56,59,61,42,80,76,79,81,62,378,'PASS'),('Tamil',1002,'Thango','Tharun','Vani Vidyalaya',5102,12,53,80,62,51,32,83,100,82,71,368,'FAIL'),('David',1003,'Vijaya','Ajith','Kendriya Vidyalaya',5101,42,49,61,59,34,62,69,81,79,54,345,'PASS'),('Willam',1004,'Rani','Ramsammy','Everwin',5103,10,24,28,31,22,30,44,48,51,42,215,'FAIL'),('Bhrath',1005,'Ruby','Manish','Kendriya Vidyalaya',5101,80,80,80,79,78,100,100,100,99,98,497,'PASS'),('Monish',1006,'Maha','Hari','Vani Vidyalaya',5102,8,14,21,23,19,28,34,41,43,39,185,'FAIL'),('Oviya',1007,'Mathi','Madhan','Kendriya Vidyalaya',5101,72,75,76,79,69,92,95,96,99,89,471,'PASS'),('Riya',1008,'Ammu','Saravana','Everwin',5103,56,64,56,10,12,76,84,76,30,32,298,'FAIL'),('Nivetha',1009,'Kavitha','Ravi','Kendriya Vidyalaya',5101,45,42,39,28,27,65,62,59,48,47,281,'PASS'),('Vivek',1010,'Srithal','Saravana','Vani Vidyalaya',5102,4,5,27,18,12,24,25,47,39,32,167,'FAIL');
/*!40000 ALTER TABLE `10th` ENABLE KEYS */;
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
