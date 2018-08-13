import requests,re,json,random,time
from requests.exceptions import RequestException
from lxml import etree

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
    #####*****************importtant******************##############################
    pattern=re.compile('<p class="name">[\s\S]*?title="([\s\S]*?)"[\s\S]*?'  #匹配电影名字
                       '<p class="star">([\s\S]*?)</p>[\s\S]*?'               #匹配主演
                       '<p class="releasetime">([\s\S]*?)</p>[\s\S]*? ')    #匹配上映时间
    results=re.findall(pattern,html)
    for item in results:
        yield {
            "title":item[0].strip(),
            "stars":item[1].strip(),
            "releasetime":item[2].strip()
        }

def write2File(item):
    with open("maoyan_yield.txt","a",encoding="utf-8") as f:
        f.write(json.dumps(item,ensure_ascii=False)+"\n")

def crawlPage(num):
    url = "http://maoyan.com/board/4?offset={}".format(num)
    html=get_one_page(url)
    for item in deal_one_page(html):
        write2File(item)

if __name__=="__main__":
    for x in range(0,100,10):
        crawlPage(x)
    time.sleep(random.randint(1,5))
print("Finished")




