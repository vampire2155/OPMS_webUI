# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/9 10:19
from Lib.findElement import BasePage
from config.globalparam import USERNAME,PASSWORD
from Lib.readconfigini import *
from selenium.webdriver.common.by import By

class LoginPageClass(BasePage):
    def __init__(self):
        '''子类构造方法的作用：进一步抽离出元素定位的方法，这里只封装寻找元素的方法，不会真的找元素'''

        # 主动执行父类的构造方法，因为子类也有构造方法，如果此时不主动执行父类的构造方法，则父类的构造方法不会自动执行。
        # （子类有构造方法时不会执行父类的构造方法）
        super().__init__()

        #用户名输入框元素
        self.userNameLocator = (By.NAME, 'username')
        #密码输入框元素
        self.passwordLocator = (By.NAME, 'password')
        #登录按钮元素
        self.loginButtonLocator = (By.CSS_SELECTOR, 'button')
    #用户名输入框 函数
    def userNameInputBox(self):
        return self.find_element(self.userNameLocator)

    # 密码输入框 函数
    def passwordInputBox(self):
        return self.find_element(self.passwordLocator)

    # 登录按钮 函数
    def loginButton(self):
        return self.find_element(self.loginButtonLocator)

class LoginPageAction(LoginPageClass):
    def login_userinfo_from_ini(self):
        # 两种方法获取opms系统的登录用户名和密码
        # 方法一：通过读取config.ini文件获取
        username = Readconfig().get_userinfo('username')
        password = Readconfig().get_userinfo('password')
        #输入用户名，用户名username是 从 config.ini 中获取
        self.userNameInputBox().send_keys(username)
        #输入密码，password 从 config.ini中 获取
        self.passwordInputBox().send_keys(password)
        #点击登录按钮
        self.loginButton().click()
        #因为登录完成以后会弹出一个登录成功的提示框，等待3s后会自动消失，所以，这里强制等待3s秒钟

    def login(self):
        # 方法二：通过import globalparam.py 获取
        #如果 同时调用这两个登录函数的话，因为上一个函数已经退出浏览器了，所以如果不再创建一个 driver的话，直接driver.get 就会报错。
        #输入用户名，用户名username是 从 globalparam.py 获取
        # driver.find_element_by_name('username').send_keys(username)
        self.userNameInputBox().send_keys(USERNAME)
        #输入密码，password 从 globalparam.py 获取
        self.passwordInputBox().send_keys(PASSWORD)
        #点击登录按钮
        self.loginButton().click()
        #因为登录完成以后会弹出一个登录成功的提示框，等待3s后会自动消失，所以，这里强制等待3s秒钟

# 创建对象实例，其他模块引用此对象，可保持对象在内存中只有一个
LoginPageActionObj = LoginPageAction()


if __name__ == '__main__':
    # LoginPageAction().login_userinfo_from_ini()
    LoginPageAction().login()


