# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/9 17:35
import pymysql
import pymysql.cursors

#删除  aiopms.pms_projects 这张表中的数据
def delete_projects():
    #连接数据库  db 是库名，例如，这条SQL（ select * from aiopms.pms_projects;）的 aiopms  就是 db   。
    connect = pymysql.Connect(host = '127.0.0.1',port = 3306,user = 'root',password = '123456',db = 'aiopms',charset = 'utf8')
    #获取游标
    cursor = connect.cursor()
    #删除数据
    sql = 'DELETE FROM pms_projects where `name` like "test_%";'
    #执行SQL语句
    cursor.execute(sql)
    connect.commit()


if __name__ == '__main__':
    delete_projects()




