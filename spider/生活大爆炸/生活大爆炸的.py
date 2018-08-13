import requests
from lxml import etree

url='http://www.hao6v.com/mj/2016-09-20/27800.html'
response=requests.get(url)
text=response.content.decode('gbk')
html=etree.HTML(text)
url_list=html.xpath('//tbody//td/a//@href')
url_name=html.xpath("//tbody//td/a/text()")
big_bang=[]
for url in url_list:
    for name in url_name:
        with open("the_big_bang_theory.txt",'a',encoding="utf-8") as f:
            f.write(url+"\n"+name+"\n\n")

