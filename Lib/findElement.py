# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/18 11:05
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Lib.mydriver import DriverClass
from config.globalparam import TIMEOUT, POLL_FREQUENCY,screenshot_path
import time


class BasePage():
    def __init__(self):
        # 因为每个界面都会用到 driver对象，所以把driver定义在 构造方法中。
        self.driver = DriverClass.get_driver()  # 因为get_driver()是类方法，所以可以直接用类名进行调用，而不用通过创建实例化对象进行调用。

    def find_element(self, locator):
        '''
        (显示等待)根据表达式匹配单个元素，并返回元素对象
        :param locator: 传参（元组），第0个元素表示定位方法，第1个元素表示元素定位表达式
        :return: 返回元素对象
        '''
        WebDriverWait(driver=self.driver, timeout=TIMEOUT, poll_frequency=POLL_FREQUENCY).until(
            EC.visibility_of_element_located(locator))
        #寻找元素的表达式 driver.find_element(By.ID, 'id')  ,返回的是元素对象
        return self.driver.find_element(*locator)   # * 表示要对传入的元组进行解包

    def find_elements(self, locator):
        '''
        (显示等待)根据表达式匹配多个元素，并返回元素对象列表
        :param locator: 传参（元组），第0个元素表示定位方法，第1个元素表示元素定位表达式
        :return: 返回元素对象列表
        '''
        WebDriverWait(driver=self.driver, timeout=TIMEOUT, poll_frequency=POLL_FREQUENCY).until(
            EC.visibility_of_element_located(locator))
        #寻找元素的表达式 driver.find_elements(By.ID, 'id')  ,返回的是元素对象列表
        return self.driver.find_elements(*locator)   # * 表示要对传入的参数 locator （元组类型） 进行解包

    # 定义截图函数
    def getScreenshot(self):
        # screenshot_path 的值为 G:\Python_webUI\report\screenshot
        # 文件名中不能存在 ：冒号，所以用 . 点代替
        fileName = time.strftime('%Y-%m-%d %H.%M.%S',time.localtime(time.time()))
        pngpath = screenshot_path + f'\\{fileName}.png'
        self.driver.get_screenshot_as_file(pngpath)