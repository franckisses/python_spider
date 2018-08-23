# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class TencenthirePipeline(object):
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

    def execute(self, sql, params=None):
        if self.connectData() == False:
            return False
        try:
            if self.conn and self.cur:
                self.cur.execute(sql, params)
                self.conn.commit()
        except:
            print("execute:" + sql + "error")
            return False
        return True

    def process_item(self, item, spider):
        dbhelper = self.connectData()
        title = item["title"]
        local = item['local']
        duty = item['duty']
        position_type = item['position_type']
        position_num = item['position_num']
        request = item['request']

        sql = "INSERT INTO newdatabase.tencenthire(title,local,position_type,position_num,duty,request) VALUES(%s,%s,%s,%s,%s,%s)"
        params = (title, local, position_type, position_num,duty,request)
        result = self.execute(sql, params)
        if result == True:
            print("插入成功")
        else:
            print("插入失败", params)





