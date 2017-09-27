/*
Navicat MySQL Data Transfer

Source Server         : aaa
Source Server Version : 50624
Source Host           : localhost:3306
Source Database       : acs

Target Server Type    : MYSQL
Target Server Version : 50624
File Encoding         : 65001

Date: 2017-09-27 17:19:39
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for picturewall
-- ----------------------------
DROP TABLE IF EXISTS `picturewall`;
CREATE TABLE `picturewall` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  `pic_url` varchar(128) DEFAULT NULL,
  `info` text,
  `remote_url` varchar(128) DEFAULT NULL,
  `add_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of picturewall
-- ----------------------------
INSERT INTO `picturewall` VALUES ('1', '1', null, '2008年11月，江西师范大学ACM竞赛队第一次进入亚洲区域赛ACM-ICPC现场赛', 'http://otiryjpu9.bkt.clouddn.com/static/images/zp1.jpg', '2017-09-27 16:20:53');
INSERT INTO `picturewall` VALUES ('2', '2', null, '2013年3月20号，江西师范大学ACM协会正式成立，其前身为江西师范大学ACM竞赛队', 'http://otiryjpu9.bkt.clouddn.com/static/images/zp2.png', '2017-09-27 16:30:34');
INSERT INTO `picturewall` VALUES ('3', '3', null, '2013年7月11日，算法组成员在北京大学参加第四届“蓝桥杯”决赛', 'http://otiryjpu9.bkt.clouddn.com/static/images/zp3.jpg', '2017-09-27 16:31:51');
INSERT INTO `picturewall` VALUES ('4', '4', null, '2013年9月13日，协会举办第一次算法组招新宣传会', 'http://otiryjpu9.bkt.clouddn.com/static/images/zp4.jpg', '2017-09-27 16:32:25');
INSERT INTO `picturewall` VALUES ('5', '5', null, '2013年11月，江西师范大学ACM协会更名为“计算机科学协会”（Assocation of Computer Science）,ACM竞赛队改为协会算法组。', 'http://otiryjpu9.bkt.clouddn.com/static/images/zp5.jpg', '2017-09-27 16:34:16');
INSERT INTO `picturewall` VALUES ('6', '6', null, '2014年4月25日，协会正式加入“CSDN”高校俱乐部', 'http://otiryjpu9.bkt.clouddn.com/static/images/zp6.jpg', '2017-09-27 16:50:18');
INSERT INTO `picturewall` VALUES ('7', '7', null, '2014年5月25日，算法组成员参加第39届ACM-ICPC国际大学生程序设计竞赛亚洲区西安邀请赛', 'http://otiryjpu9.bkt.clouddn.com/static/images/zp12.jpg', '2017-09-27 16:50:54');
INSERT INTO `picturewall` VALUES ('8', '8', null, '2014年5月31日，算法组成员前往北京参加“蓝桥杯”决赛', 'http://otiryjpu9.bkt.clouddn.com/static/images/zp8.jpg', '2017-09-27 16:52:26');
INSERT INTO `picturewall` VALUES ('9', '9', null, '2014年10月12日，协会举办计算机信息工程学院首届网页设计大赛', 'http://otiryjpu9.bkt.clouddn.com/static/images/zp10.jpg', '2017-09-27 16:53:11');
INSERT INTO `picturewall` VALUES ('10', '10', null, '2015年5月16日，协会组织同学参加江西省第六届计算机作品大赛', 'http://otiryjpu9.bkt.clouddn.com/static/images/zp13.jpg', '2017-09-27 16:54:54');
INSERT INTO `picturewall` VALUES ('11', '11', null, '2015年5月16日，协会组织同学参加江西省第六届计算机作品大赛', 'http://otiryjpu9.bkt.clouddn.com/static/images/zp15.jpg', '2017-09-27 16:57:56');
INSERT INTO `picturewall` VALUES ('12', '12', null, '2015年8月，协会组织算法组，网站组，机器人竞赛暑假集训', 'http://otiryjpu9.bkt.clouddn.com/static/images/zp17.png', '2017-09-27 16:59:06');
INSERT INTO `picturewall` VALUES ('13', '13', null, '2015年9月，协会举办15级新生ACM宣传会', 'http://otiryjpu9.bkt.clouddn.com/static/images/zp18.jpg', '2017-09-27 16:59:44');
INSERT INTO `picturewall` VALUES ('14', '14', null, '2015年11月，组织参加江西省第三届软件服务外包大赛，江西省第六届智能机器人大赛', 'http://otiryjpu9.bkt.clouddn.com/static/images/zp19.jpg', '2017-09-27 17:00:29');
INSERT INTO `picturewall` VALUES ('15', '15', null, '2015年11月，算法组成员参加第40届ACM-ICPC国际大学生程序设计竞赛北京赛区现场赛', 'http://otiryjpu9.bkt.clouddn.com/static/images/zp20.jpg', '2017-09-27 17:00:57');
INSERT INTO `picturewall` VALUES ('16', '16', null, '2016年3月，举办春季联合招新宣传会，并对参加的同学进行专业技能培训', 'http://otiryjpu9.bkt.clouddn.com/static/images/zp21.png', '2017-09-27 17:01:24');
INSERT INTO `picturewall` VALUES ('17', '17', null, '2016年5月24日,协会举办江西师范大学2016校ACM程序设计竞赛', 'http://otiryjpu9.bkt.clouddn.com/static/images/zp22.jpg', '2017-09-27 17:01:46');
INSERT INTO `picturewall` VALUES ('18', '18', null, '2016年6月4日，协会组织同学参加江西省第十一届计算机作品大赛', 'http://otiryjpu9.bkt.clouddn.com/static/images/zp23.jpg', '2017-09-27 17:02:09');
