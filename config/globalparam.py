# -*- coding: UTF-8 -*-
# @author  ：vampire
# @Time    : 2020/7/8 15:44
from selenium import webdriver
import os
from configparser import ConfigParser   #该类 是用来读取操作（读和写）配置文件（.ini）文件的库。 这里没有用到。

#创建driver对象，用于操作浏览器
driver = webdriver.Chrome(r'G:\Selenium_java\chromedriver.exe')

#opms系统的登录用户名和密码
username = 'libai'
password = 'opmsopms123'

#获取当前脚本文件的上一层目录的路径
cur_path = os.path.dirname(os.path.realpath(__file__))   # G:\Python_webUI\config
#获取项目所在的根目录的路径
project_path = os.path.split(cur_path)[0]   #打印结果是 G:\Python_webUI

# 日志路径
log_path = os.path.join(project_path,'report','log')

# 截图文件路径
screenshot_path = os.path.join(project_path, 'report', 'screenshot')

# 测试报告路径
report_path = os.path.join(project_path, 'report', 'report')

# 默认浏览器
browser = 'firefox'

# 测试数据路径
data_path = os.path.join(project_path, 'data')

#数据库信息
host = '127.0.0.1'
port = 3306   #端口需要是 %d  即需要传入一个数字，而不是字符串
user = 'root'
psd = '123456'
db = 'python'
charset = 'utf8'

