# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/19 15:30
from pages.project_manager_page import ProjectManagementPageObj,starttime,endtime
from Lib.logger import LogAction
import allure     # pip install allure-pytest 来安装 allure库
import pytest

@allure.feature('项目管理模块')
class Test_project_management():
    @allure.story('新增项目')
    @allure.title('新增项目用例')
    # @pytest.mark.flaky(reruns=2)   # 装饰器，用例执行失败后会重新自动再执行2次
    def test_addproj(self):
        LogAction.printlog('DEBUG', '新增项目用例开始执行')
        # 项目名称
        projectName = '中国电信'
        #项目描述如下
        key_content = f"""该项目是一个{projectName}的项目，开始于{starttime}，结束与{endtime}，周期为一个月。
        项目要求为：xxxxxxxx。
        项目验收时间为：{endtime}日。
        """
        # 进入 项目管理  界面
        ProjectManagementPageObj.go_to_project_manager_page()
        with allure.step('步骤一、点击“新项目”按钮'):
            ProjectManagementPageObj.clickNewProjectButton()
        with allure.step('步骤二、填写项目名称'):
            ProjectManagementPageObj.InputProjectName(projectName)
        with allure.step('步骤三、填写项目别名'):
            ProjectManagementPageObj.InputProjectAlias(projectName)
        with allure.step('步骤四，填写开始日期'):
            ProjectManagementPageObj.InputStartTime()
        with allure.step('步骤五，填写结束日期'):
            ProjectManagementPageObj.InputEndTime()
        #项目描述是在 iframe框架里面，所以需要切入框架，然后再进行输入
        ProjectManagementPageObj.Pitching_in_iframe()
        with allure.step('步骤六、填写项目描述'):
            ProjectManagementPageObj.InputDescription(key_content)
        #现在需要切出框架，进行后面的点击提交按钮操作
        ProjectManagementPageObj.Punch_out_iframe()
        with allure.step('步骤七、点击提交按钮'):
            ProjectManagementPageObj.ClickSubmitButton()
        #点击新项目增加成功后弹出框中的"去设置管理"按钮
        ProjectManagementPageObj.ClickPrimaryButton()
        with allure.step('步骤八、判断项目是否增加成功'):
            try:
                assert f'test_{projectName}_{starttime}开始' in ProjectManagementPageObj.AcquireProNameList()
            except:
                ProjectManagementPageObj.getScreenshot()
                raise  #如果加try...except捕获异常后，此时所有的测试用例都是通过的，会影响测试结果。解决办法就是再把异常抛出来。

    @allure.story('搜索项目状态')
    @allure.title('搜索项目用例')
    def test_searchProjectStatus(self):
        LogAction.printlog('DEBUG', '搜索项目用例开始执行')
        # 进入 项目管理  界面
        ProjectManagementPageObj.go_to_project_manager_page()
        with allure.step('步骤一、选择项目状态为进行'):
            ProjectManagementPageObj.selectProjectStatusAction('进行')
        with allure.step('步骤二、输入要搜索的项目名称'):
            ProjectManagementPageObj.InputSearchContent('中国电信')
        with allure.step('步骤三、点击搜索按钮'):
            ProjectManagementPageObj.clickSearchButton()
        with allure.step('步骤四、判断搜索结果是否符合预期'):
            try:
                assert '中国电信' in ProjectManagementPageObj.AcquireProNameList()[0]
            except:
                ProjectManagementPageObj.getScreenshot()
                raise  #如果加try...except捕获异常后，此时所有的测试用例都是通过的，会影响测试结果。解决办法就是再把异常抛出来。


if __name__ == '__main__':
    Test_project_management().test_addproj()























