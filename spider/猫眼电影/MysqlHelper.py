"""
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 9:33
# @Author  : franck
# @Email   : franck_gxu@outlook.com
"""
import pymysql


class DbHelper:
    """
    完成所有对mysql数据库的处理
    """
    def __init__(self, host="localhost", port=3306, user="root",
                 password="123456", database="newdatabase", charset="utf8"):
        self.host = host
        self.port = port
        self.password = password
        self.user = user
        self.db = database
        self.charset = charset
        self.conn = None
        self.cur = None

    def connectData(self):
        try:
            self.conn = pymysql.connect(host=self.host,
                                        user=self.user,
                                        port=self.port,
                                        passwd=self.password,
                                        database=self.db,
                                        charset=self.charset
                                        )
        except:
            print("conn error")
            return False
        self.cur = self.conn.cursor()
        return True

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        return True

    def execute(self,sql,params = None):
        if self.connectData() == False:
            return False
        try:
            if self.conn and self.cur:
                self.cur.execute(sql,params)
                self.conn.commit()
        except:
            print("execute:"+sql+"error")
            return False
        return True

# if __name__ == "__main__":
#     dbhelper = DbHelper()
#     title = "英雄本色"
#     actor = "周润发"
#     time = "2010-08-17"
#     sql = "INSERT INTO newdatabase.maoyan(title,actor,time) VALUES(%s,%s,%s)"
#     params = (title, actor, time)
#     result = dbhelper.execute(sql, params)
#     if (result == True):
#         print("Insert Ok")
#     else:
#         print("Insert Failed")
#     print(dbhelper.close())
