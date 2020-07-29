# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/20 10:45
from Lib.findElement import BasePage
from config.globalparam import URL_OPMS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class CheckworkManagerPage(BasePage):
    def __init__(self, path = 'checkwork/manage'):
        # 执行父类的 构造方法
        super().__init__()
        # 进入 考勤管理页面的URL
        self.path = URL_OPMS + path
        # 以下是获取界面上每个元素的 定位表达式
        # 打卡状态 选择框 元素 表达式
        self.checkWorkStatusSelectorLocator = (By.CSS_SELECTOR, 'form.searchform > .form-control')
        # 搜索按钮 元素 表达式
        self.checkWorkSearchButtonLocator = (By.CSS_SELECTOR, 'form.searchform button.btn.btn-primary')
        # 列表中的打卡日期 元素 表达式
        self.checkWorkListDateLocator = (By.CSS_SELECTOR, 'tbody > tr >td:nth-child(1)')
        # 列表中 打完卡 的时间元素 表达式
        self.checkWorkListTimeLocator = (By.CSS_SELECTOR, 'tbody > tr >td:nth-child(2)')
        # 列表中 打卡状态 元素 表达式
        self.checkWorkListStatusLocator = (By.CSS_SELECTOR, 'tbody > tr >td:nth-child(3)')
        # 列表中 打卡IP 元素 表达式
        self.checkWorkListIPLocator = (By.CSS_SELECTOR, 'tbody > tr >td:nth-child(4)')
        # 饼图中 打卡 元素 表达式
        self.checkWorkLocator = (By.ID, 'js-clock')
        # 饼图中 打卡按钮上的时间 元素 表达式
        self.checkWorkTimeLocator = (By.CSS_SELECTOR, '#js-clock span')
         # 如果 某天已经打卡两次，再次打开会弹出 提示框，获取提示框中的 描述信息
        self.alertDescLocator = (By.CSS_SELECTOR, 'div.modal-body > p')
        # 弹出的提示框 右上角的 X 号
        self.alertCloseButtonLocator = (By.CSS_SELECTOR, 'button.close > span')

#  PO模式的  **对象层**
    # 打卡状态选择框 元素对象
    def checkWorkStatus(self):
        return self.find_element(self.checkWorkStatusSelectorLocator)
    # 搜索按钮 元素对象
    def checkWorkSearch(self):
        return self.find_element(self.checkWorkSearchButtonLocator)
    # 列表中 打卡日期 元素对象
    def checkWorkListDate(self):
        return self.find_elements(self.checkWorkListDateLocator)
    # 列表中 打完卡 的时间 元素对象
    def checkWorkListTime(self):
        return self.find_elements(self.checkWorkListTimeLocator)
    # 列表中 打卡状态 元素对象
    def checkWorkListStatus(self):
        return self.find_elements(self.checkWorkListStatusLocator)
    # 列表中 打卡IP 元素对象
    def checkWorkListIP(self):
        return self.find_elements(self.checkWorkListIPLocator)
    # 饼图中 打卡 元素对象
    def checkWork(self):
        return self.find_element(self.checkWorkLocator)
    # 饼图中 打卡按钮上的时间 元素对象
    def checkWorkTimeText(self):
        return self.find_element(self.checkWorkTimeLocator)
    #如果 某天已经打卡两次，再次打开会弹出 提示框，获取提示框中的 描述信息
    def alertDesc(self):
        return self.find_element(self.alertDescLocator)
    # 弹出提示框中 右上角 的 X 号
    def closeAlertPromptBox(self):
        return self.find_element(self.alertCloseButtonLocator)
    def go_to_checkwork_manager_page(self):
        '''
        访问考勤管理页面的网址，进入项目管理界面。方便后面进入该页面时调用。
        '''
        self.driver.get(self.path)

#  PO模式的  **操作层**
class CheckworkManagerPageAction(CheckworkManagerPage):
    def selectCheckWorkStatus(self, checkWork_status):
        '''选择打卡状态'''
        return Select(self.checkWorkStatus()).select_by_visible_text(checkWork_status)
    def clickCheckWorkSearch(self):
        ''' 点击 搜索 按钮'''
        return self.checkWorkSearch().click()
    def acquireCheckWorkList(self):
        ''' 获取 列表中的 打卡日期,并存入到列表中'''
        checkWorkDateList = []
        for date in self.checkWorkListDate():
            checkWorkDateList.append(date.text)
        return checkWorkDateList
    def acquireCheckWorkTimeList(self):
        ''' 获取 列表中的 打卡时间,并存入到列表中'''
        checkWorkTimeList = []
        for time in self.checkWorkListTime():
            checkWorkTimeList.append(time.text)
        return checkWorkTimeList
    def acquireCheckWorkStatusList(self):
        ''' 获取 列表中的 打卡状态,并存入到列表中'''
        checkWorkStatusList = []
        for status in self.checkWorkListStatus():
            checkWorkStatusList.append(status.text)
        return checkWorkStatusList
    def acquireCheckWorkIPList(self):
        ''' 获取 列表中的 打卡IP,并存入到列表中'''
        checkWorkIPList = []
        for ip in self.checkWorkListIP():
            checkWorkIPList.append(ip.text)
        return checkWorkIPList
    def clickCheckWork(self):
        '''点击 饼图 打卡'''
        return self.checkWork().click()
    def acquireCheckWorkTime(self):
        '''获取 点击打卡时的饼图上的时间'''
        return self.checkWorkTimeText().text
    def closeAlertFrame(self):
        '''关闭弹出框'''
        return self.closeAlertPromptBox().click()
    def acquireAlertDesc(self):
        '''如果 某天已经打卡两次，再次打开会弹出 提示框，获取提示框中的 描述信息'''
        return self.alertDesc().text
    def statisticsCheckwork(self):
        '''获取 打卡状态为 正常、迟到、早退、加班的次数'''
        normalStatusCnt = 0
        lateStatusCnt = 0
        leaveEarlyStatusCnt = 0
        overTimeStatusCnt = 0
        for status in self.acquireCheckWorkStatusList():
            if status == '正常':
                normalStatusCnt += 1
            elif status == '迟到':
                lateStatusCnt += 1
            elif status == '早退':
                leaveEarlyStatusCnt += 1
            elif status == '加班':
                overTimeStatusCnt += 1
        return [normalStatusCnt,lateStatusCnt,leaveEarlyStatusCnt,overTimeStatusCnt]


# 创建对象实例，其他模块引用此对象，可保持对象在内存中只有一个
CheckworkManagerPageObj = CheckworkManagerPageAction()












