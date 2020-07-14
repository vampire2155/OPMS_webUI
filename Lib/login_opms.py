# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/9 10:19
from config.globalparam import *
import time
from Lib.readconfigini import *

class Login_class():
    def login_userinfo_from_ini(self):
        driver.get('http://127.0.0.1:8088/')
        driver.maximize_window()
        # 两种方法获取opms系统的登录用户名和密码
        # 方法一：通过读取config.ini文件获取
        username = Readconfig().get_userinfo('username')
        password = Readconfig().get_userinfo('password')
        #输入用户名，用户名username是 从 globalparam.py 获取
        driver.find_element_by_name('username').send_keys(username)
        #输入密码，password 从 globalparam.py 获取
        driver.find_element_by_name('password').send_keys(password)
        #点击登录按钮
        driver.find_element_by_class_name('btn-login').click()
        #因为登录完成以后会弹出一个登录成功的提示框，等待3s后会自动消失，所以，这里强制等待3s秒钟
        time.sleep(4)

    def login(self):
        # 方法二：通过import globalparam.py 获取
        driver.get('http://127.0.0.1:8088/')
        driver.maximize_window()
        #输入用户名，用户名username是 从 globalparam.py 获取
        # driver.find_element_by_name('username').send_keys(username)
        driver.find_element_by_xpath('//*[@id="login-form"]/div[2]/input[1]').send_keys(username)
        #输入密码，password 从 globalparam.py 获取
        driver.find_element_by_name('password').send_keys(password)
        #点击登录按钮
        driver.find_element_by_class_name('btn-login').click()
        #因为登录完成以后会弹出一个登录成功的提示框，等待3s后会自动消失，所以，这里强制等待3s秒钟
        time.sleep(4)

if __name__ == '__main__':
    Login_class().login()

    # Login_class().login_userinfo_from_ini()

