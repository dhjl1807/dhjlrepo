-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `lgw`
--

DROP TABLE IF EXISTS `lgw`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `lgw` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_name` varchar(200) DEFAULT NULL,
  `job_region` varchar(100) DEFAULT NULL,
  `job_format_time` varchar(50) DEFAULT NULL,
  `job_company` varchar(100) DEFAULT NULL,
  `job_company_type` varchar(50) DEFAULT NULL,
  `job_company_financ` varchar(30) DEFAULT NULL,
  `job_company_pernum` varchar(30) DEFAULT NULL,
  `job_salary` varchar(30) DEFAULT NULL,
  `job_exp` varchar(30) DEFAULT NULL,
  `job_edu` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lgw`
--

LOCK TABLES `lgw` WRITE;
/*!40000 ALTER TABLE `lgw` DISABLE KEYS */;
INSERT INTO `lgw` VALUES (1,'python研发工程师','朝阳区','2019-05-22 15:54:24','数美','企业服务,数据服务','B轮','150-500人','10k-20k','应届毕业生','本科'),(2,'Python开发工程师','朝阳区','2019-05-22 10:39:41','OYO','移动互联网','不需要融资','500-2000人','20k-30k','不限','本科'),(3,'python开发工程师（安全方向）','朝阳区','2019-05-21 11:10:40','罗辑思维','移动互联网,文化娱乐','D轮及以上','150-500人','25k-50k','3-5年','本科'),(4,'Django研发工程师','朝阳区','2019-05-22 10:15:11','爱特曼科技','移动互联网,数据服务','A轮','15-50人','15k-25k','1-3年','本科'),(5,'python开发工程师','朝阳区','2019-05-21 09:56:48','汇游科技','移动互联网,旅游','不需要融资','15-50人','15k-20k','3-5年','本科'),(6,'Python工程师','朝阳区','2019-05-22 18:54:00','亿欧','移动互联网,企业服务','B轮','150-500人','15k-25k','3-5年','本科'),(7,'Python中级工程师','朝阳区','2019-05-22 11:33:42','ZingFront智线','移动互联网,数据服务','A轮','50-150人','15k-25k','3-5年','本科'),(8,'python后端开发工程师','朝阳区','2019-05-21 17:28:32','北京超盟数据科技有限公司','数据服务,企业服务','A轮','50-150人','15k-25k','5-10年','本科'),(9,'python开发工程师','朝阳区','2019-05-22 17:04:15','北京智扬','移动互联网','不需要融资','50-150人','12k-18k','3-5年','本科'),(10,'Python开发工程师','朝阳区','2019-05-22 15:25:39','爱因互动','其他','A轮','15-50人','10k-20k','1-3年','本科'),(11,'Python中级工程师','海淀区','2019-05-22 12:53:01','石云科技','企业服务,金融','不需要融资','50-150人','13k-26k','1年以下','本科'),(12,'python开发工程师','海淀区','2019-05-21 15:39:22','小赢科技','金融','上市公司','500-2000人','20k-35k','5-10年','本科'),(13,'Django 开发工程师','大兴区','2019-05-20 16:41:30','富顺天牧','生活服务,企业服务','不需要融资','15-50人','10k-15k','5-10年','不限'),(14,'python后台开发工程师-阅读','海淀区','2019-05-22 11:10:12','小米','移动互联网','D轮及以上','2000人以上','15k-30k','1-3年','本科'),(15,'python开发实习生','海淀区','2019-05-21 12:05:05','Flow++','信息安全,数据服务','A轮','50-150人','4k-5k','应届毕业生','硕士'),(16,'Python中高级开发工程师','朝阳区','2019-05-21 13:49:14','乐飞天下','移动互联网,旅游','未融资','150-500人','15k-30k','5-10年','大专'),(17,'高级Python工程师','朝阳区','2019-05-21 15:39:28','ZingFront智线','移动互联网,数据服务','A轮','50-150人','15k-25k','3-5年','本科'),(18,'python策略开发工程师','东城区','2019-05-21 09:50:48','寻牛','金融','B轮','15-50人','10k-15k','1-3年','本科'),(19,'高级python开发工程师','海淀区','2019-05-22 19:24:35','达观数据','人工智能','B轮','150-500人','20k-30k','3-5年','本科'),(20,'11215N-Python开发工程师','朝阳区','2019-05-22 00:00:11','平安科技','金融','不需要融资','2000人以上','15k-30k','3-5年','本科'),(21,'Python','海淀区','2019-05-22 10:34:19','灵雀云','数据服务,企业服务','B轮','150-500人','13k-25k','不限','本科'),(22,'Python开发工程师','朝阳区','2019-05-22 11:50:04','中电广通','移动互联网','不需要融资','50-150人','10k-20k','3-5年','本科'),(23,'python工程师','大兴区','2019-05-21 23:54:29','生仝智能','移动互联网','天使轮','15-50人','14k-20k','不限','硕士'),(24,'Python开发工程师','海淀区','2019-05-22 19:12:37','合心科技','移动互联网,教育','B轮','50-150人','20k-35k','1-3年','本科'),(25,'python开发工程师（广告系统）','朝阳区','2019-05-22 18:45:07','流体网络','移动互联网','B轮','50-150人','20k-40k','3-5年','不限'),(26,'python开发工程师','海淀区','2019-05-22 14:59:54','金证优智','人工智能','A轮','15-50人','15k-25k','3-5年','本科'),(27,'python开发工程师','朝阳区','2019-05-22 10:49:08','奇虎360金融','移动互联网,金融','上市公司','500-2000人','20k-30k','5-10年','本科'),(28,'高级python开发工程师','海淀区','2019-05-21 18:14:46','旷视MEGVII','移动互联网,硬件','D轮及以上','500-2000人','25k-50k','1-3年','本科'),(29,'Python开发工程师（爬虫）','朝阳区','2019-05-22 19:27:46','博派通达','移动互联网,硬件','A轮','50-150人','12k-20k','1-3年','大专'),(30,'Python开发','海淀区','2019-05-22 16:26:28','北京智胜新格科技有限...','移动互联网,游戏','不需要融资','150-500人','15k-30k','1-3年','本科'),(31,'高级Java/PHP/Python工程师','朝阳区','2019-05-20 09:29:10','ZingFront智线','移动互联网,数据服务','A轮','50-150人','15k-25k','3-5年','本科'),(32,'python开发工程师','石景山区','2019-05-22 14:16:01','南京优玛软件科技有限公司','移动互联网','未融资','150-500人','12k-16k','3-5年','本科'),(33,'Python研发工程师','朝阳区','2019-05-22 09:27:25','逍遥志科技','移动互联网,金融','A轮','15-50人','18k-25k','3-5年','本科'),(34,'python开发工程师','海淀区','2019-05-21 10:00:07','茄子快传','移动互联网','B轮','150-500人','25k-50k','5-10年','本科'),(35,'python研发工程师（算法方向）','海淀区','2019-05-21 14:52:29','青藤云安全','数据服务','B轮','150-500人','25k-35k','3-5年','硕士'),(36,'python开发工程师(J10137)','海淀区','2019-05-22 17:17:26','AdMaster','数据服务','不需要融资','500-2000人','15k-25k','1-3年','不限'),(37,'python开发工程师','海淀区','2019-05-21 21:23:49','天眼查','数据服务','A轮','150-500人','15k-25k','不限','本科'),(38,'python 开发工程师','朝阳区','2019-05-22 19:27:46','博派通达','移动互联网,硬件','A轮','50-150人','15k-30k','1-3年','大专'),(39,'Python 研发工程师','朝阳区','2019-05-22 18:09:10','云杉智达科技','移动互联网,企业服务','不需要融资','15-50人','10k-20k','1-3年','本科'),(40,'Python开发工程师','海淀区','2019-05-22 11:37:47','Aibee','移动互联网,企业服务','A轮','150-500人','20k-40k','3-5年','本科'),(41,'python工程师（视觉产品创新中心）','朝阳区','2019-05-22 17:01:27','迈外迪','移动互联网,O2O','D轮及以上','150-500人','10k-20k','1-3年','本科'),(42,'python开发工程师','海淀区','2019-05-21 10:11:59','币信','移动互联网','不需要融资','50-150人','18k-35k','3-5年','本科'),(43,'python开发工程师','朝阳区','2019-05-21 10:06:11','摩尔妈妈','移动互联网','A轮','15-50人','15k-25k','1-3年','本科'),(44,'python开发工程师','海淀区','2019-05-21 10:59:20','香侬科技','企业服务,数据服务','A轮','50-150人','15k-20k','1-3年','本科'),(45,'python开发工程师','朝阳区','2019-05-21 15:19:28','流体网络','移动互联网','B轮','50-150人','15k-30k','3-5年','本科'),(46,'Python 中级工程师','朝阳区','2019-05-20 14:43:46','ZingFront智线','移动互联网,数据服务','A轮','50-150人','10k-18k','1-3年','本科'),(47,'python开发工程师','海淀区','2019-05-21 17:11:53','微步在线','信息安全','B轮','50-150人','15k-30k','1-3年','本科'),(48,'python开发工程师','朝阳区','2019-05-22 18:12:10','十牛科技','移动互联网','天使轮','15-50人','10k-20k','1-3年','大专'),(49,'python开发工程师','海淀区','2019-05-20 14:35:33','中寰卫星','移动互联网','不需要融资','500-2000人','15k-30k','3-5年','本科'),(50,'Django 研发工程师','朝阳区','2019-05-22 18:09:10','云杉智达科技','移动互联网,企业服务','不需要融资','15-50人','10k-20k','1-3年','本科'),(51,'python开发工程师','朝阳区','2019-05-22 11:31:11','钱方好近','金融','B轮','150-500人','13k-26k','3-5年','本科'),(52,'软件工程师-Python','朝阳区','2019-05-21 17:49:48','大地量子','数据服务','天使轮','15-50人','15k-28k','1-3年','本科'),(53,'python开发工程师','海淀区','2019-05-22 15:23:50','好未来','移动互联网,教育','上市公司','2000人以上','17k-30k','3-5年','不限'),(54,'python开发工程师','海淀区','2019-05-21 16:55:36','Flow++','信息安全,数据服务','A轮','50-150人','15k-25k','3-5年','本科'),(55,'python研发工程师','海淀区','2019-05-14 15:44:03','云孚科技','企业服务,移动互联网','不需要融资','15-50人','8k-16k','不限','本科'),(56,'PYTHON开发工程师 (MJ000126)','海淀区','2019-05-22 17:59:26','阿博茨科技','移动互联网','B轮','150-500人','15k-25k','1-3年','本科'),(57,'python开发工程师','海淀区','2019-05-22 09:44:37','中科物安','信息安全','未融资','15-50人','15k-25k','3-5年','本科'),(58,'高级python开发工程师','朝阳区','2019-05-22 14:00:47','V8实拍','移动互联网','B轮','150-500人','30k-60k','3-5年','本科'),(59,'资深Python工程师','海淀区','2019-05-22 10:44:54','RealAI','人工智能','天使轮','15-50人','18k-36k','不限','本科'),(60,'Python开发工程师','海淀区','2019-05-16 17:00:31','悦慧康','移动互联网','未融资','50-150人','12k-24k','1-3年','本科'),(61,'Python研发工程师','海淀区','2019-05-14 15:44:04','云孚科技','企业服务,移动互联网','不需要融资','15-50人','5k-10k','不限','本科'),(62,'实习-Python工程师','海淀区','2019-05-20 11:30:38','绿盟科技','信息安全','上市公司','500-2000人','2k-4k','1年以下','本科'),(63,'高级python开发工程师','朝阳区','2019-05-22 16:56:15','推想科技','医疗健康,数据服务','C轮','150-500人','20k-40k','5-10年','本科'),(64,'中级Python开发工程师（AK）','朝阳区','2019-05-21 13:49:14','乐飞天下','移动互联网,旅游','未融资','150-500人','15k-25k','5-10年','大专'),(65,'python开发工程师','朝阳区','2019-05-17 15:32:07','第三石科技','移动互联网,电子商务','B轮','50-150人','8k-16k','1-3年','本科'),(66,'高级python开发工程师','海淀区','2019-05-22 12:48:28','高鸿兴科','移动互联网,数据服务','不需要融资','50-150人','14k-17k','5-10年','本科'),(67,'python高级工程师/开发专家','朝阳区','2019-05-20 18:46:11','阿里巴巴-高德','移动互联网','上市公司','2000人以上','25k-50k','3-5年','本科'),(68,'Python/Golang开发工程师','朝阳区','2019-05-22 18:42:02','微壳','移动互联网,企业服务','不需要融资','150-500人','25k-40k','3-5年','本科'),(69,'python开发工程师','海淀区','2019-05-21 11:41:09','慧安金科','人工智能,数据服务','A轮','50-150人','25k-45k','3-5年','本科'),(70,'高级Python开发工程师','海淀区','2019-05-22 15:41:31','NewsJet','移动互联网','不需要融资','50-150人','25k-45k','3-5年','本科'),(71,'资深Python研发工程师','海淀区','2019-05-22 14:53:37','Gridsum 国双','数据服务,企业服务','上市公司','500-2000人','25k-40k','5-10年','本科'),(72,'Python','海淀区','2019-05-21 14:49:30','明日虫洞','移动互联网,数据服务','C轮','50-150人','15k-30k','1-3年','本科'),(73,'Python开发-北京','朝阳区','2019-05-22 17:16:29','优维科技','移动互联网,企业服务','B轮','50-150人','10k-20k','1-3年','本科'),(74,'高级Python研发工程师','朝阳区','2019-05-22 09:27:25','逍遥志科技','移动互联网,金融','A轮','15-50人','25k-50k','5-10年','本科'),(75,'中级python开发工程师','朝阳区','2019-05-21 17:28:32','北京超盟数据科技有限公司','数据服务,企业服务','A轮','50-150人','15k-25k','3-5年','本科');
/*!40000 ALTER TABLE `lgw` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-23 13:54:33
