# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/9 11:40
from Lib.findElement import BasePage
from selenium.webdriver.common.by import By
from config.globalparam import URL_OPMS
from dateutil.relativedelta import relativedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import datetime

class ProjectManagementPage(BasePage):
    def __init__(self, path = 'project/manage'):
        '''
        子类构造方法的作用：进一步抽离出元素定位的方法，这里只封装寻找元素的方法，不会真的找元素
        '''
        self.path = URL_OPMS + path
        # 主动执行父类的构造方法，因为子类也有构造方法，如果此时不主动执行父类的构造方法，则父类的构造方法不会自动执行。
        # （子类有构造方法时不会执行父类的构造方法）
        super().__init__()

        # 项目状态 元素
        self.projectStatusLocator = (By.CSS_SELECTOR, 'select.form-control')
        # 搜索内容 元素
        self.searchContentLocator = (By.CSS_SELECTOR, '.searchform input')
        # 搜索按钮 元素
        self.searchButtonLocator = (By.CSS_SELECTOR, '.searchform button.btn.btn-primary')
        # 项目管理 元素
        self.proManagementLocator = (By.CLASS_NAME, 'fa-book')
        #新项目元素
        self.newProjectButtonLocator = (By.CLASS_NAME, 'btn-success')
        # 项目名称 元素
        self.projectNameInputLocator = (By.CSS_SELECTOR, '#project-form >div:nth-child(1) input')
        # 项目别名 元素
        self.projectAliasInputLocator = (By.NAME, 'aliasname')
        # 开始日期 元素
        self.startTimeLocator = (By.NAME, 'started')
        #结束日期 元素
        self.endTimeLocator = (By.NAME, 'ended')
        # iframe框架 元素，描述是在一个iframe框架中，需要先进行切换
        self.iframeLocator = (By.CLASS_NAME, 'ke-edit-iframe')
        #描述元素  描述是在另外一个 iframe中
        self.descLocator = (By.CLASS_NAME, 'ke-content')
        # 提交按钮 元素
        self.submitButtonLocator = (By.CSS_SELECTOR, 'button.btn-primary')
        # 新项目增加成功后弹出框中的"去设置管理"按钮 元素
        self.primaryButtonLocator = (By.CSS_SELECTOR, 'a.btn.btn-primary')
        # 新增项目 名称元素列表
        self.proNameListLocator = (By.CSS_SELECTOR, '#project-form-list > table>tbody>tr>td:nth-child(1)')

    #  选择项目状态 函数
    def selectProjectStatus(self):
        return self.find_element(self.projectStatusLocator)
    # 搜索内容 函数
    def searchContent(self):
        return self.find_element(self.searchContentLocator)
    #  搜索按钮 函数
    def searchButton(self):
        return self.find_element(self.searchButtonLocator)
    # 点击 项目管理 函数
    def clickProManage(self):
        return self.find_element(self.proManagementLocator)
    #   新项目元素 函数
    def newProjectButton(self):
        return self.find_element(self.newProjectButtonLocator)
    # 项目名称 函数
    def projectName(self):
        return self.find_element(self.projectNameInputLocator)
    # 项目别名 函数
    def projectAlias(self):
        return self.find_element(self.projectAliasInputLocator)
    # 开始日期 函数
    def startTime(self):
        return self.find_element(self.startTimeLocator)
    # 结束日期 函数
    def endTime(self):
        return self.find_element(self.endTimeLocator)
    #iframe框架函数
    def iframe(self):
        return self.find_element(self.iframeLocator)
    # 描述  函数
    def description(self):
        return self.find_element(self.descLocator)
    # 提交按钮 函数
    def submitButton(self):
        return self.find_element(self.submitButtonLocator)
    # 新项目增加成功后弹出框中的"去设置管理"按钮
    def primaryButton(self):
        return self.find_element(self.primaryButtonLocator)
    # 新增项目 名称列表 函数
    def proNameList(self):
        return self.find_elements(self.proNameListLocator)

    # def go_to_project_manager_page(self):
    #     '''
    #     点击 项目管理  并进入该页面。也可以使用 self.driver.get(self.path)进入该界面。
    #     :return: 没有返回值
    #     '''
    #     self.clickProManage().click()

    def go_to_project_manager_page(self):
        '''
        访问项目管理页面的网址，进入项目管理界面。方便后面进入该页面时调用。
        '''
        self.driver.get(self.path)

#  输入项目名称时 加上项目开始时间，并且开始时间和结束时间需要用到这两个参数。
starttime = datetime.date.today()
endtime = starttime + relativedelta(months=+1)

class ProjectManagementPageAction(ProjectManagementPage):
    def selectProjectStatusAction(self, project_status):
        '''选择项目状态'''
        return Select(self.selectProjectStatus()).select_by_visible_text(project_status)
    def InputSearchContent(self, search_content):
        '''输入搜索内容'''
        return self.searchContent().send_keys(search_content)
    def clickSearchButton(self):
        '''点击搜索按钮'''
        return self.searchButton().click()
    def clickNewProjectButton(self):
        '''点击 新项目  按钮'''
        return self.newProjectButton().click()
    def InputProjectName(self, projectName):
        '''输入项目名称'''
        return self.projectName().send_keys(f'test_{projectName}_{starttime}开始')
    def InputProjectAlias(self, projectName):
        '''输入项目别名'''
        return self.projectAlias().send_keys(f'test_{projectName}_{starttime}开始')
    def InputStartTime(self):
        '''输入开始时间，不需要有返回值'''
        self.startTime().send_keys(Keys.CONTROL, 'a')
        self.startTime().send_keys(Keys.BACKSPACE)  # 鼠标事件   即相当于手动点了键盘上的 BackSpace键
        self.startTime().send_keys(f'{starttime}')  # 输入开始时间
    def InputEndTime(self):
        '''输入结束时间，不需要有返回值'''
        self.endTime().send_keys(Keys.CONTROL, 'a')
        self.endTime().send_keys(Keys.BACKSPACE)  # 鼠标事件   即相当于手动点了键盘上的 BackSpace键
        self.endTime().send_keys(f'{endtime}')  # 输入结束时间
    def Pitching_in_iframe(self):
        '''切入iframe框架'''
        self.driver.switch_to.frame(self.iframe())
    def Punch_out_iframe(self):
        '''切出 iframe框架'''
        self.driver.switch_to.default_content()
    def InputDescription(self, pro_description):
        '''输入项目描述'''
        return self.description().send_keys(pro_description)
    def ClickSubmitButton(self):
        '''点击提交按钮'''
        return self.submitButton().click()
    def ClickPrimaryButton(self):
        '''点击 新项目增加成功后弹出框中的"去设置管理"按钮'''
        return self.primaryButton().click()
    def AcquireProNameList(self):
        '''获取 所有的项目名称'''
        nameEles = self.proNameList()
        namelist = []
        for ele in nameEles:
            namelist.append(ele.text)
        return namelist

# 创建对象实例，其他模块引用此对象，可保持对象在内存中只有一个
ProjectManagementPageObj = ProjectManagementPageAction()