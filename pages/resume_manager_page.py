# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/20 17:48
from Lib.findElement import BasePage
from config.globalparam import URL_OPMS
from selenium.webdriver.common.by import By

class ResumeMangerPage(BasePage):
    def __init__(self, path = 'resume/manage'):
        # 进入  简历管理  界面的URL
        self.path = URL_OPMS + path
        # 如果子类 和 父类 都有构造函数，当继承父类时，此时父类的 构造方法不会自动执行，需要手动调用
        # 执行 父类的构造方法
        super().__init__()
        # 简历状态 元素表达式
        self.resumeStatusSelectLocator = (By.CSS_SELECTOR, 'select.form-control')
        # 输入名称 搜索框 元素表达式
        self.searchInputBoxLocator = (By.CSS_SELECTOR, 'input[name="keywords"]')
        #搜索按钮 元素 表达式
        self.searchButtonLocator = (By.CSS_SELECTOR, 'input[name="keywords"] + button.btn')








