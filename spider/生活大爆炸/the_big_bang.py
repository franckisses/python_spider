import requests,re
from lxml import etree
from bs4 import BeautifulSoup

resp=requests.get("http://www.hao6v.com/mj/2009-09-23/8674.html")
html=resp.content.decode("gbk")
soup=BeautifulSoup(html,features="lxml")
s=soup.select("tr p")
for x in s:
    content=re.findall("<p>.*<br>([\s\S]*?)</p>",x)
    print(content)
