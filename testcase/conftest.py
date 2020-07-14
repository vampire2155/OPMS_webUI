# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/8 15:42

#用例初始化模块   包括  用例执行前数据初始化  以及   用例执行完成以后的数据清除。
import pytest
from Lib.operateDB import delete_projects

@pytest.fixture(scope='module',autouse=True)
#环境初始化 、数据清除
def setup(request):
    #连接数据库删除数据
    delete_projects()

    # 环境、数据清除----teardown
    def fin():  #为什么要命名为 fin() 函数，因为 fixture.html 文档中是这样写的。 其他名称应该也是可以的。
        delete_projects()
    request.addfinalizer(fin)  #函数名作为实参进行传递

