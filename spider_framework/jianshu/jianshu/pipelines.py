# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors


# 将ajax加载的内容异步步插入数据库
class JianshuPipeline(object):
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
        title = item["title"]
        avatar = item['avatar']
        author = item['author']
        pub_time = item['pub_time']
        orginal_id = item['orginal_id']
        article = item['article']
        content = item['content']
        read_count = item['read_count']
        like_count = item['like_count']
        word_count = item['word_count']
        subject = item['subject']


        sql = "INSERT INTO jianshu(title,avatar,author,pub_time,orginal_id,article,content,read_count,like_count,word_count,subject) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params = (title,avatar,author,pub_time,orginal_id,article,content,read_count,like_count,word_count,subject)
        result = self.execute(sql,params)
        if result == True:
            print("插入成功")
        else:
            print("插入失败", params)

# 将返回的数据同步插入到数据库
class JsInsertMysql(object):
    def __init__(self):
        dbparams ={
            'host':"localhost",
            'port': 3306,
            'user':"root",
            'password':"123456",
            'database': "newdatabase",
            'charset': "utf8",
            'cursorclass':cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql',**dbparams)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = "INSERT INTO jianshu(title,avatar,author,pub_time,orginal_id,article,content) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            return self._sql
        return self._sql

    def process_item(self,item,spider):
        defer = self.dbpool.runInteraction(self.insert_item,item)
        # 错误处理函数
        defer.addErrback(self.handle_error,item,spider)

    def insert_item(self,cursor,item):
        cursor.execute(self.sql,(item["title"],item['avatar'],item['author'],item['pub_time'],item['orginal_id'],item['article'],item['content']))

    def handle_error(self,error,item,spider):
        print("="*10+"error"+"="*10)
        print(error)
        print("=" * 10 + "error" +"="*10)


# 未获取ajax加载的内容
class ToMysqlTwistedPipeline(object):
    # 初始化函数
    def __init__(self, db_pool):
        self.db_pool = db_pool

    # 从settings配置文件中读取参数
    @classmethod
    def from_settings(cls, settings):
        # 用一个db_params接收连接数据库的参数
        db_params = dict(
            host='localhost',
            user='root',
            password='123456',
            port=3306,
            database='newdatabase',
            charset='utf8',
            use_unicode=True,
            # 设置游标类型
            cursorclass=cursors.DictCursor
        )
        # 创建连接池
        db_pool = adbapi.ConnectionPool('pymysql', **db_params)

        # 返回一个pipeline对象
        return cls(db_pool)

    # 处理item函数
    def process_item(self, item, spider):
        # 把要执行的sql放入连接池
        query = self.db_pool.runInteraction(self.insert_into, item)
        # 如果sql执行发送错误,自动回调addErrBack()函数
        query.addErrback(self.handle_error, item, spider)

        # 返回Item
        return item

    # 处理sql函数
    def insert_into(self, cursor, item):
        # 创建sql语句
        sql = "INSERT INTO jianshu(title,avatar,author,pub_time,orginal_id,article,content) VALUES ('%s','%s','%s','%s','%s','%s','%s')"%(
            item["title"],item['avatar'],item['author'],item['pub_time'],item['orginal_id'],item['article'],
            item['content'])
        # 执行sql语句
        cursor.execute(sql)
        # 错误函数

    def handle_error(self, failure, item, spider):
        # #输出错误信息
        print(failure)





