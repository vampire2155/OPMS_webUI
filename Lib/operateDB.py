# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/9 17:35
import pymysql   #  pymysql 就是一个封装好的客户端
import pymysql.cursors

#删除  aiopms.pms_projects 这张表中的数据
def delete_projects():
    #连接数据库  db 是库名，例如，这条SQL（ select * from aiopms.pms_projects;）的 aiopms  就是 db   。
    connect = pymysql.Connect(host = '127.0.0.1', port = 3306, user = 'root', password = '123456', db = 'aiopms', charset = 'utf8')
    #获取游标
    cursor = connect.cursor()   #  cursor 底层就是一个send操作
    #删除数据
    sql = 'DELETE FROM pms_projects where `name` like "test_%";'
    #执行SQL语句
    cursor.execute(sql)
    connect.commit()   # commit 告诉mysql真的要完成修改操作（如果不执行这个函数 修改不会生效） 。 查询不需要commit


if __name__ == '__main__':
    delete_projects()




