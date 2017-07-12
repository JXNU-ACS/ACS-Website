
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stu_id` bigint(20) DEFAULT NULL,
  `name` varchar(16) DEFAULT NULL,
  `stu_class` varchar(64) DEFAULT NULL,
  `qq` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `stu_id` (`stu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
