import requests
from lxml import etree
import random
from urllib import request
import os,re

# 创建一个ua池
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

def parse_page(url):
    header = {
        "User-Agent":random.choice(useragentlist)
    }
    # 发送get请求
    response =requests.get(url,headers=header)
    # 将返回的页面进行转码
    text = response.text
    # 创建一个xpath对象
    html = etree.HTML(text)
    # 用xpath进行对图片进行匹配
    images = html.xpath('//div[@class="page-content text-center"]//img[@class != "gif"]')
    # 遍历每一个列表
    for img in images:
        # 拿到表情包的链接
        img_url = img.get("data-original")
        # 拿到表情包的名称
        alt = img.get("alt")
        # 将表情包的名称中的一些特殊符号用正则替换
        alt=re.sub(r"[\？\?！!，,\.:~\d\\]","",alt)
        # 将拿到的链接进行分割,并且拿到图片的后缀
        suffix = os.path.splitext(img_url)[-1]
        # 拼接表情包的名字
        fullname = alt+suffix
        # 将下载的表情缓存到文件夹里边[urlretrieve(url, filename=None, reporthook=None, data=None)]
        request.urlretrieve(img_url,"imges/"+fullname)

def main():
    for x in range(1,101):
        url = "http://www.doutula.com/photo/list/?page={}".format(x)
        parse_page(url)

if __name__ == "__main__":
    main()