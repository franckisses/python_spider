# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class TencenthirePipeline(object):
    def process_item(self, item, spider):
        with open("tenxunhire.json", "a",encoding="utf-8") as f:
            f.write(json.dumps(dict(item), ensure_ascii=False) + "\n")
            return item





















    # def __init__(self):
    #     params ={
    #         'host':"127.0.0.1",
    #         'port':3306,
    #         'database':'newdatabase',
    #         'user':'root',
    #         'password':'123456',
    #         'charset':'utf8'
    #
    #     }
    #     self.conn = pymysql.connect(**params)
    #     self.cursor = self.conn.cursor()
    #     self._sql = None
    #
    # def process_item(self, item, spider):
    #     params = {item['title'],item['local'],item['position_type'],item['position_num'],item['duty'],item['request']}
    #     self.cursor.execute(self.sql,params)
    #     self.conn.commit()
    #     return item
    # @property
    # def sql(self):
    #     if not self._sql:
    #         self._sql = 'insert into newdatabase.tencenthire(title,local,position_type,position_num,duty,request) values (%s,%s,%s,%s,%s,%s)'
    #         return self._sql
    #     return self._sql
    #
    #
