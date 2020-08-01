"""
    @author: franck
    @datetime: 2020-08-01 14:00
"""

import redis    
# cant import leveldb 

class UrlDB:
    '''Use LevelDB to store URLs what have been done(succeed or faile)
    '''
    status_failure = b'0'
    status_success = b'1'

    def __init__(self):
        self.db = redis.Redis(host='localhost', port=6379, db=0)

    def set_success(self, url):
        if isinstance(url, str):
            url = url.encode('utf8')
        try:
            self.db.set(url, self.status_success)
            s = True
        except:
            s = False
        return s

    def set_failure(self, url):
        if isinstance(url, str):
            url = url.encode('utf8')
        try:
            print(url)
            self.db.set(url, self.status_failure)
            s = True
        except:
            s = False
        return s

    def has(self, url):
        if isinstance(url, str):
            url = url.encode('utf8')
        try:
            attr = self.db.get(url)
            return attr
        except:
            pass
        return False

if __name__ == "__main__":
    mytest = UrlDB()
    a = mytest.set_success('http://baidu.com')
    b = mytest.set_failure('http://weibo.com')
    c = mytest.has('http://baidu.com')
    print(a)
    print(b)
    print(c)