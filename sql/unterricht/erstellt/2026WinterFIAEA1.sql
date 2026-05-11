Enter password: -- MariaDB dump 10.19  Distrib 10.4.28-MariaDB, for osx10.10 (x86_64)
--
-- Host: localhost    Database: 2026WinterFIAEA1
-- ------------------------------------------------------
-- Server version	10.4.28-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bueroklammern`
--

DROP TABLE IF EXISTS `bueroklammern`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bueroklammern` (
  `Farbe` varchar(4) DEFAULT NULL,
  `groesse` varchar(6) DEFAULT NULL,
  `Hersteller` varchar(7) DEFAULT NULL,
  `Datum` int(4) DEFAULT NULL,
  `Anzahl` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bueroklammern`
--

LOCK TABLES `bueroklammern` WRITE;
/*!40000 ALTER TABLE `bueroklammern` DISABLE KEYS */;
INSERT INTO `bueroklammern` VALUES ('rot','klein','Leitz',2016,48),('blau','mittel','Durable',2015,20),('gelb','groß','Herlitz',2014,12),('grün','klein','no name',2013,36),('weiß','mittel','Leitz',2012,24),('rot','groß','Durable',2011,6),('blau','klein','Herlitz',2010,50),('gelb','mittel','no name',2016,100),('grün','groß','Leitz',2015,18),('weiß','klein','Durable',2014,72),('rot','mittel','Herlitz',2013,48),('blau','groß','no name',2012,20),('gelb','klein','Leitz',2011,12),('grün','mittel','Durable',2010,36),('weiß','groß','Herlitz',2016,24),('rot','klein','no name',2015,6),('blau','mittel','Leitz',2014,50),('gelb','groß','Durable',2013,100),('grün','klein','Herlitz',2012,18),('weiß','mittel','no name',2011,72),('rot','groß','Leitz',2010,48),('blau','klein','Durable',2016,20),('gelb','mittel','Herlitz',2015,12),('grün','groß','no name',2014,36),('weiß','klein','Leitz',2013,24),('rot','mittel','Durable',2012,6),('blau','groß','Herlitz',2011,50),('gelb','klein','no name',2010,100),('grün','mittel','Leitz',2016,18),('weiß','groß','Durable',2015,72),('rot','klein','Herlitz',2014,48),('blau','mittel','no name',2013,20),('gelb','groß','Leitz',2012,12),('grün','klein','Durable',2011,36),('weiß','mittel','Herlitz',2010,24),('rot','groß','no name',2016,6),('blau','klein','Leitz',2015,50),('gelb','mittel','Durable',2014,100),('grün','groß','Herlitz',2013,18),('weiß','klein','no name',2012,72),('rot','mittel','Leitz',2011,48),('blau','groß','Durable',2010,20),('gelb','klein','Herlitz',2016,12),('grün','mittel','no name',2015,36),('weiß','groß','Leitz',2014,24),('rot','klein','Durable',2013,6),('rot','mittel','Herlitz',2012,50),('blau','groß','no name',2011,100),('gelb','klein','Leitz',2010,18),('grün','mittel','Durable',2016,72),('weiß','groß','Herlitz',2015,48),('rot','klein','no name',2014,20),('blau','mittel','Leitz',2013,12),('rot','groß','Leitz',2012,36),('blau','klein','Durable',2011,24),('gelb','mittel','Herlitz',2010,6),('grün','groß','no name',2016,50),('weiß','klein','Leitz',2015,100),('rot','mittel','Durable',2014,18),('blau','groß','Herlitz',2013,72),('rot','klein','no name',2012,48),('blau','mittel','Leitz',2011,20),('gelb','groß','Durable',2010,12),('grün','klein','Herlitz',2016,36),('weiß','mittel','no name',2015,24),('rot','groß','Leitz',2014,6),('blau','klein','Durable',2013,50),('rot','mittel','Herlitz',2012,100),('blau','groß','no name',2011,18),('gelb','klein','Leitz',2010,72),('grün','mittel','Durable',2016,48),('weiß','groß','Herlitz',2015,20),('rot','klein','no name',2014,12),('blau','mittel','Leitz',2013,36),('rot','groß','Durable',2012,24),('blau','klein','Herlitz',2011,6),('gelb','mittel','no name',2010,50),('grün','groß','Leitz',2016,100),('weiß','klein','Durable',2015,18),('rot','mittel','Herlitz',2014,72),('blau','groß','no name',2013,48),('rot','klein','Leitz',2012,20),('blau','mittel','Durable',2011,12),('gelb','groß','Herlitz',2010,36),('grün','klein','no name',2016,24),('weiß','mittel','Leitz',2015,6),('rot','groß','Durable',2014,50),('blau','klein','Herlitz',2013,100),('rot','mittel','no name',2012,18),('blau','groß','Leitz',2011,72),('gelb','klein','Durable',2010,48),('grün','mittel','Herlitz',2016,20),('weiß','groß','no name',2015,12),('rot','klein','Leitz',2014,36),('blau','mittel','Durable',2013,24),('rot','groß','Herlitz',2012,6),('blau','klein','no name',2011,50),('gelb','mittel','Leitz',2010,100),('grün','groß','Durable',2016,18),('weiß','klein','Herlitz',2015,72),('rot','mittel','no name',2014,48),('blau','groß','Leitz',2013,20),('rot','klein','Durable',2012,12),('blau','mittel','Herlitz',2011,36),('gelb','groß','no name',2010,24),('grün','klein','Leitz',2016,6),('weiß','mittel','Leitz',2015,50),('rot','groß','Durable',2014,100),('blau','klein','Herlitz',2013,18),('rot','mittel','no name',2012,72),('blau','groß','Leitz',2011,48),('gelb','klein','Durable',2010,20),('grün','mittel','Herlitz',2016,12),('weiß','groß','no name',2015,36),('rot','klein','Leitz',2014,24),('blau','mittel','Durable',2013,6),('rot','groß','Herlitz',2012,50),('blau','klein','no name',2011,100),('gelb','mittel','Leitz',2010,18),('grün','groß','Durable',2016,72),('weiß','klein','Herlitz',2015,48),('rot','mittel','no name',2014,20),('blau','groß','Leitz',2013,12),('rot','klein','Durable',2012,36),('blau','mittel','Herlitz',2011,24),('gelb','groß','no name',2010,6),('grün','klein','Leitz',2016,50),('weiß','mittel','Durable',2015,100),('rot','groß','Herlitz',2014,18),('blau','klein','no name',2013,72),('rot','mittel','Leitz',2012,48),('blau','groß','Durable',2011,20),('gelb','klein','Herlitz',2010,12),('grün','mittel','no name',2016,36),('weiß','groß','Leitz',2015,24),('rot','klein','Durable',2014,6),('blau','mittel','Herlitz',2013,50),('rot','groß','Leitz',2012,100),('blau','klein','Durable',2011,18),('gelb','mittel','Herlitz',2010,72),('grün','groß','no name',2016,48),('weiß','klein','Leitz',2015,20),('rot','mittel','Durable',2014,12),('blau','groß','Herlitz',2013,36),('rot','klein','no name',2012,24),('blau','mittel','Leitz',2011,6),('gelb','groß','Durable',2010,50),('grün','klein','Herlitz',2016,100),('weiß','mittel','no name',2015,18),('rot','groß','Leitz',2014,72),('blau','klein','Durable',2013,48),('rot','mittel','Herlitz',2012,20),('blau','groß','no name',2011,12),('gelb','klein','Leitz',2010,36),('grün','mittel','Durable',2016,24),('weiß','groß','Herlitz',2015,6),('rot','klein','no name',2014,50),('blau','mittel','Leitz',2013,100),('rot','groß','Durable',2012,18),('blau','klein','Herlitz',2011,72),('gelb','mittel','no name',2010,48),('grün','groß','Leitz',2016,20),('weiß','klein','Durable',2015,12),('rot','mittel','Herlitz',2014,36),('blau','groß','no name',2013,24),('rot','klein','Leitz',2012,6),('blau','mittel','Durable',2011,50),('gelb','groß','Herlitz',2010,100),('grün','klein','no name',2016,18),('weiß','mittel','Leitz',2015,72),('rot','groß','Durable',2014,48),('blau','klein','Herlitz',2013,20),('rot','mittel','no name',2012,12),('blau','groß','Leitz',2011,36),('gelb','klein','Durable',2010,24),('grün','mittel','Herlitz',2016,6),('weiß','groß','no name',2015,50),('rot','klein','Leitz',2014,100),('blau','mittel','Durable',2013,18),('rot','groß','Herlitz',2012,72),('blau','klein','no name',2011,48),('gelb','mittel','Leitz',2010,20),('grün','groß','Durable',2016,12),('weiß','klein','Herlitz',2015,36),('rot','mittel','no name',2014,24),('blau','groß','Leitz',2013,6),('rot','klein','Durable',2012,50),('blau','mittel','Herlitz',2011,100),('gelb','groß','no name',2010,18),('grün','klein','Leitz',2016,72),('weiß','mittel','Leitz',2015,48),('rot','groß','Durable',2014,20),('blau','klein','Herlitz',2013,12),('rot','mittel','no name',2012,36),('blau','groß','Leitz',2011,24),('gelb','klein','Durable',2010,6),('grün','mittel','Herlitz',2016,50),('weiß','groß','no name',2015,100),('rot','klein','Leitz',2014,18),('blau','mittel','Durable',2013,72);
/*!40000 ALTER TABLE `bueroklammern` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `klassen`
--

DROP TABLE IF EXISTS `klassen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `klassen` (
  `Klasse` char(3) NOT NULL,
  `klassenlehrer` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Klasse`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `klassen`
--

LOCK TABLES `klassen` WRITE;
/*!40000 ALTER TABLE `klassen` DISABLE KEYS */;
INSERT INTO `klassen` VALUES ('11a','Lempel'),('11b','Sommer'),('12a','Breier');
/*!40000 ALTER TABLE `klassen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lernangebote`
--

DROP TABLE IF EXISTS `lernangebote`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lernangebote` (
  `LernangebotsNr` int(11) NOT NULL AUTO_INCREMENT,
  `Beschreibung` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`LernangebotsNr`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lernangebote`
--

LOCK TABLES `lernangebote` WRITE;
/*!40000 ALTER TABLE `lernangebote` DISABLE KEYS */;
INSERT INTO `lernangebote` VALUES (1,'Elektronik'),(2,'Tanz'),(3,'Chor');
/*!40000 ALTER TABLE `lernangebote` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lernangebotsnutzungen`
--

DROP TABLE IF EXISTS `lernangebotsnutzungen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lernangebotsnutzungen` (
  `SchuelerNr` int(11) DEFAULT NULL,
  `LernangebotsNr` int(11) DEFAULT NULL,
  `Zeit_in_h` int(11) DEFAULT NULL,
  KEY `SchuelerNr` (`SchuelerNr`),
  KEY `LernangebotsNr` (`LernangebotsNr`),
  CONSTRAINT `lernangebotsnutzungen_ibfk_1` FOREIGN KEY (`SchuelerNr`) REFERENCES `schueler` (`SchuelerNr`),
  CONSTRAINT `lernangebotsnutzungen_ibfk_2` FOREIGN KEY (`LernangebotsNr`) REFERENCES `lernangebote` (`LernangebotsNr`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lernangebotsnutzungen`
--

LOCK TABLES `lernangebotsnutzungen` WRITE;
/*!40000 ALTER TABLE `lernangebotsnutzungen` DISABLE KEYS */;
INSERT INTO `lernangebotsnutzungen` VALUES (1,2,12),(2,3,22),(3,1,15),(3,2,12),(3,3,2),(4,2,5),(5,1,23);
/*!40000 ALTER TABLE `lernangebotsnutzungen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personen`
--

DROP TABLE IF EXISTS `personen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vorname` varchar(50) NOT NULL,
  `nachname` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personen`
--

LOCK TABLES `personen` WRITE;
/*!40000 ALTER TABLE `personen` DISABLE KEYS */;
INSERT INTO `personen` VALUES (1,'Clara','Corn'),(2,'Karlheinz',''),(3,'','Koslowski'),(4,'Karl-Theodor','Guttenberg'),(5,'Otto','Hahn'),(6,'Nils','Bohr'),(10,'Marie','Curie'),(11,'Sir Isaac','Newton'),(12,'Frauke','Fleissig');
/*!40000 ALTER TABLE `personen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schueler`
--

DROP TABLE IF EXISTS `schueler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schueler` (
  `SchuelerNr` int(11) NOT NULL AUTO_INCREMENT,
  `Nachname` varchar(30) DEFAULT NULL,
  `Vorname` varchar(30) DEFAULT NULL,
  `Klasse` char(3) DEFAULT NULL,
  PRIMARY KEY (`SchuelerNr`),
  KEY `fk_klasse_schueler` (`Klasse`),
  CONSTRAINT `fk_klasse_schueler` FOREIGN KEY (`Klasse`) REFERENCES `klassen` (`Klasse`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schueler`
--

LOCK TABLES `schueler` WRITE;
/*!40000 ALTER TABLE `schueler` DISABLE KEYS */;
INSERT INTO `schueler` VALUES (1,'Jürgens','Ina','11a'),(2,'Schmidt','Tom','12a'),(3,'Jäger','Franz','11a'),(4,'Olsen','Ina','11b'),(5,'Jürgens','Paula','12a');
/*!40000 ALTER TABLE `schueler` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zahlen`
--

DROP TABLE IF EXISTS `zahlen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zahlen` (
  `zahl` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`zahl`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zahlen`
--

LOCK TABLES `zahlen` WRITE;
/*!40000 ALTER TABLE `zahlen` DISABLE KEYS */;
/*!40000 ALTER TABLE `zahlen` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-02 23:47:37
