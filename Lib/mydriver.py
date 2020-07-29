# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/18 10:41
from selenium import webdriver
from config.globalparam import driverPath,URL_OPMS

class DriverClass():
    '''浏览器工具驱动类'''
    _driver = None  # 设置浏览器对象为空
    @classmethod   # 申明 get_driver是 **类方法**，类方法可以直接用   类名.类方法 进行调用  ，如：DriverClass.get_driver()
    def get_driver(cls, browser_type = 'Chrome'):
        # 如果判断浏览器驱动为空，则创建一个浏览器对象，如果不为空，则直接返回浏览器对象。
        # 这样做的好处是，执行多条用例时，不需要重复创建浏览器对象，重新打开浏览器
        if cls._driver is None:
            if browser_type == 'Chrome':
                cls._driver = webdriver.Chrome(driverPath['Chrome'])
            cls._driver.get(URL_OPMS)
            cls._driver.maximize_window()

            # 这个导入包操作必须放在这里，否则会报错，提示“循环导入”。
            from Lib.login_opms import LoginPageActionObj
            # 执行登录操作，只需要执行一次登录操作
            LoginPageActionObj.login()
        return cls._driver

#这里不用实例方法，是因为使用类方法 不用实例化对象就可以调用类方法，实例化对象会占用内存，而是用类方法则不用占用内存。


if __name__ == '__main__':
    DriverClass.get_driver()



