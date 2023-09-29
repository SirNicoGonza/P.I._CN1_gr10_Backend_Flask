-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: mensajeria
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
-- Table structure for table `canales`
--
CREATE SCHEMA IF NOT EXISTS mensajeria;

--
--

DROP TABLE IF EXISTS `canales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `canales` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `id_servidor` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_servidor` (`id_servidor`),
  CONSTRAINT `canales_ibfk_1` FOREIGN KEY (`id_servidor`) REFERENCES `servidores` (`id`)
  ON DELETE cascade
  ON UPDATE cascade
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `canales`
--

LOCK TABLES `canales` WRITE;
/*!40000 ALTER TABLE `canales` DISABLE KEYS */;
/*!40000 ALTER TABLE `canales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mensajes`
--

DROP TABLE IF EXISTS `mensajes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mensajes` (
	`id_mensaje` int NOT NULL auto_increment primary key,
  `contenido` text NOT NULL,
  `fecha_hora` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `id_canal` int NOT NULL,
  `id_usuario` int DEFAULT NULL,
  KEY `id_canal` (`id_canal`),
  CONSTRAINT `mensajes_ibfk_1` FOREIGN KEY (`id_canal`) REFERENCES `canales` (`id`),
  CONSTRAINT fk_mensajes_usuario FOREIGN KEY (id_usuario) REFERENCES mensajeria.usuarios(id)
  ON DELETE cascade
  ON UPDATE cascade  
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mensajes`
--

LOCK TABLES `mensajes` WRITE;
/*!40000 ALTER TABLE `mensajes` DISABLE KEYS */;
/*!40000 ALTER TABLE `mensajes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nexo`
--

DROP TABLE IF EXISTS `nexo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nexo` (
  `id_usuario` int NOT NULL,
  `id_servidor` int NOT NULL,
  KEY `id_usuario` (`id_usuario`),
  KEY `id_servidor` (`id_servidor`),
  CONSTRAINT `membresia_usuario_servidor_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`)
  ON DELETE cascade
  ON UPDATE cascade,
  CONSTRAINT `membresia_usuario_servidor_ibfk_2` FOREIGN KEY (`id_servidor`) REFERENCES `servidores` (`id`)
  ON DELETE cascade
  ON UPDATE cascade
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nexo`
--

LOCK TABLES `nexo` WRITE;
/*!40000 ALTER TABLE `nexo` DISABLE KEYS */;
/*!40000 ALTER TABLE `nexo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servidores`
--

DROP TABLE IF EXISTS `servidores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servidores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `descripcion` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servidores`
--

LOCK TABLES `servidores` WRITE;
/*!40000 ALTER TABLE `servidores` DISABLE KEYS */;
/*!40000 ALTER TABLE `servidores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre_usuario` varchar(255) NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  `correo_electronico` varchar(255) NOT NULL,
  `imagen_perfil` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre_usuario` (`nombre_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-25 18:06:59
