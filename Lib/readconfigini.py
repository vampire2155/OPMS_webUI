# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/9 10:43
from configparser import ConfigParser
import os

father_path = os.path.dirname(os.path.realpath(__file__))  #这个是 当前文件readconfigini.py 的上一级目录的路径
proj_path = os.path.split(father_path)[0]  #获取的是工程的路径，即工程的根目录
configini_path = os.path.join(proj_path, 'config', 'config.ini')

class Readconfig():
    def __init__(self):
        # 实例化一个ConfigParser 对象
        self.cfg = ConfigParser()
        self.cfg.read(configini_path)   # read(filenames, encoding=None) read函数有两个参数。

    def get_userinfo(self,param):
        value = self.cfg.get('userinfo',param)  #参数 'userinfo'就是section（节） ，param传参为 ini文件中的参数。
        return value


if __name__ == '__main__':
    R = Readconfig()
    print (R.get_userinfo('username'))
    print(R.get_userinfo('password'))


