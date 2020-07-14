# -*- coding: UTF-8 -*- 
# @Time    : 2020/7/8 10:20
'''
登录51job，http://51job.com
输入搜索关键字“python”，地区选择“杭州”，（注意：如果所在地已经选中其他地区，要去掉）
搜索最新发布的职位，抓取页面信息，得到如下的格式化信息
python开发工程师 | 杭州纳帕科技有限公司|杭州|0.8-1.6万/月|04-27
'''
from config.globalparam import *
from time import sleep

class Test_51job():
    def test_get_jobsinfo_from_51job(self):
        driver.get('http://www.51job.com')
        driver.maximize_window()
        #点击高级搜索
        driver.find_element_by_css_selector('a.more').click()
        #输入搜索关键词 python
        driver.find_element_by_id('kwdselectid').send_keys('python')
        #地区选择 杭州
        driver.find_element_by_id('work_position_input').click()
        #删除默认 城市名 陕西省
        sleep(1)
        driver.find_element_by_id('work_position_click_multiple_selected_each_200000').click()
        #然后点击 H I 那一行
        driver.find_element_by_id('work_position_click_center_left_each_220200').click()
        #选择杭州
        driver.find_element_by_id('work_position_click_center_right_list_category_220200_080200').click()
        # 点击确定按钮
        driver.find_element_by_id('work_position_click_bottom_save').click()
        #在选择职能类别之前需要先在其他地方点击一下， 防止搜索框搜索出来的内容遮挡住 职能类别 的选择框
        driver.find_element_by_css_selector('div.d_lt.Fm > div:nth-child(3) > label').click()
        #职能类别 选 计算机软件 -> 高级软件工程师
        driver.find_element_by_id('funtype_click').click()
        #点击 后端开发
        driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()
        # 选择 高级软件工程师
        driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()
        driver.find_element_by_id('funtype_click_bottom_save').click()
        #公司性质选 外资 欧美
        driver.find_element_by_css_selector('#cottype_list span.ic.i_arrow').click()
        driver.find_element_by_css_selector('#cottype_list > div.ul > span:nth-child(3)').click()
        #工作年限选 1-3 年
        driver.find_element_by_css_selector('#workyear_list > span.ic.i_arrow').click()
        driver.find_element_by_css_selector('#workyear_list > div.ul > span:nth-child(3)').click()
        #点击 搜索按钮
        driver.find_element_by_css_selector('div.btnbox.p_sou > span.p_but').click()
        # 搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息
        #     Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
        #     Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27
        #     on开发工程师 | 杭州新思维计算机有限公司 | 杭州-西湖区 | 1-1.5万/月 | 04-27
        resultListEle = driver.find_elements_by_css_selector('#resultList div.el + .el')
        if not resultListEle:
            print ('对不起，没有找到符合你条件的职位！')
        else:
            for oneEle in resultListEle:
                Position = oneEle.find_elements_by_css_selector('p.t1 a')[0].get_attribute('title')
                # Position = oneEle.find_elements_by_css_selector('p.t1 a')[0].text
                company = oneEle.find_elements_by_css_selector('span.t2 > a')[0].get_attribute('title')
                address = oneEle.find_elements_by_css_selector('span.t3')[0].text
                salary = oneEle.find_elements_by_css_selector('span.t4')[0].text
                time = oneEle.find_elements_by_css_selector('span.t5')[0].text
                # print (f'{Position}|{company}|{address}|{salary}|{time}')
                print('|'.join(Position, company, address, salary, time))
        driver.quit()

