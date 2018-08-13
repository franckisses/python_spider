import requests,re
from lxml import etree


url='https://www.gushiwen.org/'
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
}
resp=requests.get(url,headers=header)
text=resp.text
html=etree.HTML(text)
title=html.xpath("//b/text()")
dynasty=html.xpath('//p[@class="source"]/a[1]/text()')
auther=html.xpath('//p[@class="source"]/a[2]/text()')
poems=html.xpath('////div[@class="contson"]/text()')
print(poems)
poem=[]
for x in poems:
    print(x)
#     hah=x.strip()
#     print(hah)
#     poem.append(hah)
# print(poems)





