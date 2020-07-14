# -*- coding: UTF-8 -*-
from config.globalparam import *
from time import sleep
from win32com import client
import pytest,allure

@allure.feature('文件上传')
class Test_uploadfile():
    @allure.story('文件上传UI自动化')
    @allure.title('文件上传UI自动化用例')
    def test_uploadfile(self):
        with allure.step('第一步、在浏览器中输入网址'):
            driver.get('https://tinypng.com/')
        with allure.step('第二步、最大化窗口'):
            driver.maximize_window()
        with allure.step('第三步、点击上传文件按钮'):
            driver.find_element_by_css_selector("figure.icon").click()
        #因为弹出文件选择框需要时间，所以需要强制等待3秒钟。  time.sleep() 表示强制等待 ，还有隐式等待和显式等待。
        sleep(3)  #为什么这里需要使用强制等待，而不是隐式等待和显式等待，因为上传文件的弹出框不是web界面的。
        with allure.step('第四步、创建一个敲击键盘所需要用到的对象'):
            sh = client.Dispatch('WScript.shell')
        #因为 光标 会自动  定位到 弹出的选择框中的文件名 输入框中，所以可以通过输入 路径 + 文件名 + \n  的方式来上传文件.
        # 需要上传的文件，如果需要上传多个文件，可以手动选中多个文件，查看一个文件名输入框中的格式是怎么样的。
        # 文件路径不能有中文   而且文件路径必须要用 反斜杠 \ ，否则会提示找不到文件。同时上传多个文件时，文件路径必须相同。 因为手动操作时，也无法同时上传多个路径不同的文件。

        # 同时上传多个文件的操作
        # files =""" "G:\Python_scripts\\UITest\\a.png" "G:\Python_scripts\\UITest\\aa.png\n" """
        # sh.Sendkeys(files)

        #多次上传文件
        with allure.step('第五步、上传第一个文件'):
            file1 = "G:\Python_scripts\\UITest\\a.png\n"
            sh.Sendkeys(file1)
        #上传多个文件之间需要强制等待，否则界面会来不及操作
        sleep(3)
        with allure.step('第六步、上传第二个文件'):
            driver.find_element_by_css_selector("figure.icon").click()
            sleep(3)
            file2 = "G:\Python_scripts\\aa.png\n"
            sh.Sendkeys(file2)
        #文件上传以后 获取  文件名 所在的元素
        ele = driver.find_elements_by_css_selector('div.before')
        #把获取到的文件名放置在一个列表中，然后进行判断
        nameList = []
        for sonEle in ele:
            nameList.append(sonEle.get_attribute('title'))
        with allure.step('第七步、判断文件是否上传成功'):
            assert "a.png" in nameList
            assert "aa.png" in nameList
        driver.quit()


if __name__ == '__main__':
    pytest.main(['-s'])