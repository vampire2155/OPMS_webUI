# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/20 14:24
from pages.checkwork_manager_page import CheckworkManagerPageObj
from collections import Counter
import allure
import datetime

@allure.feature('考勤管理模块')
class Test_checkwork_management():
    def test_search_checkwork(self):
        # 进入考勤管理界面
        CheckworkManagerPageObj.go_to_checkwork_manager_page()
        # 这个统计打卡状态不知道要测试什么，后面有思路了再写。
        assert CheckworkManagerPageObj.statisticsCheckwork()[1] >= 0

    def test_checkwork(self):
        # 进入考勤管理界面
        CheckworkManagerPageObj.go_to_checkwork_manager_page()
        # 获取列表中的打卡日期
        Cdate = CheckworkManagerPageObj.acquireCheckWorkList()
        if Counter(Cdate)[f'{datetime.date.today()}'] == 2:
            # 点击 饼图 进行打卡
            CheckworkManagerPageObj.clickCheckWork()
            try:
                assert CheckworkManagerPageObj.acquireAlertDesc() == '你今天打卡次数超过了2次'
            except:
                CheckworkManagerPageObj.getScreenshot()
                raise  #如果加try...except捕获异常后，此时所有的测试用例都是通过的，会影响测试结果。解决办法就是再把异常抛出来。
        elif Counter(Cdate)[f'{datetime.date.today()}'] < 2:
            # 点击 饼图 进行打卡
            CheckworkManagerPageObj.clickCheckWork()
            # 获取饼图上的时间
            time = CheckworkManagerPageObj.acquireCheckWorkTime()
            # 关闭弹出框
            CheckworkManagerPageObj.closeAlertFrame()
            # 点击 搜索按钮
            CheckworkManagerPageObj.clickCheckWorkSearch()
             # 获取打卡 列表中的时间
            checkworkTime = CheckworkManagerPageObj.acquireCheckWorkTimeList()
            # 判断打卡时间是否 包含在 时间列表中
            try:
                assert time in checkworkTime
            except:
                CheckworkManagerPageObj.getScreenshot()
                raise  # 如果加try...except捕获异常后，此时所有的测试用例都是通过的，会影响测试结果。解决办法就是再把异常抛出来。


if __name__ == '__main__':
    Test_checkwork_management().test_checkwork()











