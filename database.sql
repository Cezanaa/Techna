SET GLOBAL max_allowed_packet = 64 * 1024 * 1024;
SHOW VARIABLES LIKE 'max_allowed_packet';


DROP DATABASE IF EXISTS `app`;
CREATE DATABASE IF NOT EXISTS `app`;
USE `app`;

CREATE TABLE IF NOT EXISTS `user_data` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(30) NOT NULL,
  `Age` INT NOT NULL,
  `Gender` CHAR(1) NOT NULL,
  `Email` VARCHAR(50) NOT NULL, 
  PRIMARY KEY (`ID`)
) DEFAULT CHARSET=UTF8MB4;

CREATE TABLE IF NOT EXISTS `uporabniki` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Username` VARCHAR(30) NOT NULL,
  `Bio` VARCHAR(300) DEFAULT '',
  `Password` LONGBLOB NOT NULL,
  `Salt` LONGBLOB NOT NULL,
  `user_data_ID` INT NOT NULL,
  `profile_pic` VARCHAR(100) DEFAULT null ,
  `followers` INT DEFAULT 0,
  
  PRIMARY KEY (`ID`),
  FOREIGN KEY (`user_data_ID`) REFERENCES `user_data`(`ID`) ON DELETE CASCADE
) DEFAULT CHARSET=UTF8MB4;

CREATE TABLE IF NOT EXISTS `songs` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Title` VARCHAR(30) NOT NULL,
  `Audio` VARCHAR(100) NOT NULL, 
  `Cover_art` VARCHAR(100) NOT NULL,
  `Release_year` DATETIME DEFAULT NOW(),
  `Streams` INT DEFAULT 0,
  `Is_single` TINYINT(1) NOT NULL,
  `Artist_ID` INT NOT NULL, 
  PRIMARY KEY (`ID`),
  FOREIGN KEY (`Artist_ID`) REFERENCES `user_data`(`ID`) ON DELETE CASCADE
) DEFAULT CHARSET=UTF8MB4;

CREATE TABLE IF NOT EXISTS `Album` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Title` VARCHAR(30) NOT NULL,
  `Cover_art` LONGBLOB NOT NULL,
  `Artist_ID` INT NOT NULL, 
  `songs_ID` INT NOT NULL,
  PRIMARY KEY (`ID`),
  FOREIGN KEY (`songs_ID`) REFERENCES `songs`(`ID`) ON DELETE CASCADE,
  FOREIGN KEY (`Artist_ID`) REFERENCES `user_data`(`ID`) ON DELETE CASCADE
) DEFAULT CHARSET=UTF8MB4;

