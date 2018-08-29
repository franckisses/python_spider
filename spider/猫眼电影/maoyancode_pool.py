"""
爬取猫眼电影的榜单前一百
"""

import requests,re,json,random,time
from requests.exceptions import RequestException
from multiprocessing import Pool
from multiprocessing import Manager
import functools
import MysqlHelper

useragentlist = [
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)',
'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 1073) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
'Mozilla/5.0 (X11; U; Linux x8664; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10126) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
]
def get_one_page(url):
    headers={
        "User-Agent":random.choice(useragentlist)
    }
    try:
        response=requests.get(url,headers=headers)
        if response.status_code ==200:
            return response.text
        return None
    except RequestException:
        return None

def deal_one_page(html):
    pattern=re.compile('<p class="name">[\s\S]*?title="([\s\S]*?)"[\s\S]*?'  #匹配电影名字
                       '<p class="star">([\s\S]*?)</p>[\s\S]*?'               #匹配主演
                       '<p class="releasetime">([\s\S]*?)</p>[\s\S]*? ')    #匹配上映时间
    results=re.findall(pattern,html)
    resultsL=[]
    for item in results:
        resultsL.append({
            "title":item[0].strip(),
            "stars":item[1].strip(),
            "releasetime":item[2].strip()
        })
    return resultsL

def write2File(item):
    with open("maoyan_pool.txt","a",encoding="utf-8") as f:
        f.write(json.dumps(item,ensure_ascii=False)+"\n")

def write2SQL(item):
    """
    将返回的数据插入到数据库中
    :param item:
    :return:
    """
    dbhelper = MysqlHelper.DbHelper()
    title = item['title']
    actor = item['stars'].split("：")[1]
    time = item['releasetime'].split("：")[1]
    sql = "INSERT INTO newdatabase.maoyan(title,actor,time) VALUES(%s,%s,%s)"
    params = (title, actor, time)
    result = dbhelper.execute(sql, params)
    if result == True:
        print("插入成功")
    else:
        print("插入失败")


def crawlPage(lock,num):
    url = "http://maoyan.com/board/4?offset={}".format(num)
    html=get_one_page(url)
    for item in deal_one_page(html):
        # print(item)
        lock.acquire()
        write2File(item)
        write2SQL(item)
        lock.release()
        
def anaylysiscount():
    dbhelper = MysqlHelper.DbHelper()
    total = dbhelper.fetchCount("select count(*) from maoyan")
    am = dbhelper.fetchCount("select count(*) from 'newdatabase'.'maoyan'where time like '%美国%'")
    china = dbhelper.fetchCount("select count(*) from 'newdatabase'.'maoyan'where time like '%中国%'")
    japan = dbhelper.fetchCount("select count(*) from 'newdatabase'.'maoyan'where time like '%日本%'")
    print(total,am,japan,china)




if __name__=="__main__":
    anaylysiscount()
    # for x in range(0,100,10):
    #     crawlPage(x)
    # time.sleep(random.randint(1,5))
    # manager=Manager()
    # lock=manager.Lock()
    # 使用函数包装器
    # pcrawlPage=functools.partial(crawlPage,lock)
    # pool=Pool()
    # pool.map(pcrawlPage,[x for x in range(0,100,10)]) #分配给进程池 任务序列
    # pool.close()
    # pool.join()
    #
    # print("Finished")




