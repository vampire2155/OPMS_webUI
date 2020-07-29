# -*- coding: UTF-8 -*-
# @author  ：vampire
# @Time    : 2020/7/8 15:44

import os
from configparser import ConfigParser   #该类 是用来读取操作（读和写）配置文件（.ini）文件的库。 这里没有用到。

#driver路径，通过字典配置不通过浏览器的driver路径
driverPath = {
    'Chrome':r'G:\Selenium_java\chromedriver.exe'
}

# OPMS系统的WEB页面的 HOST
URL_OPMS = 'http://127.0.0.1:8088/'

# 显式等待的参数(单位：秒)
# 超时时间
TIMEOUT = 10
#轮询时间
POLL_FREQUENCY = 0.5

#opms系统的登录用户名和密码
USERNAME = 'libai'
PASSWORD = 'opmsopms123'

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

# 测试数据路径
data_path = os.path.join(project_path, 'data')

# OPMS系统的数据库信息
HOST = '127.0.0.1'
PORT = 3306   #端口需要是 %d  即需要传入一个数字，而不是字符串
USER_DB = 'root'
PSD_DB = '123456'
DB = 'python'
CHARSET = 'UTF8'

