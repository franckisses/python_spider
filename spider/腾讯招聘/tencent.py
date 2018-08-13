# https://hr.tencent.com/position.php?&start=0#a
# https://hr.tencent.com/position.php?&start=10#a
# https://hr.tencent.com/position.php?&start=20#a
# https://hr.tencent.com/position.php?&start=30#a

import requests
from lxml import etree
headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
        "Cookie":"_ga=GA1.2.1391731176.1529458040; pgv_pvi=1731241984; PHPSESSID=4emqq60nm111kslja2206b7uh3; pgv_si=s2937956352",
        "Host":"hr.tencent.com",
        "Upgrade-Insecure-Requests":"1",
    }
resp=requests.get('https://hr.tencent.com/position.php?&start=10',headers=headers)
print(resp.text)



# def save_info(url):
#     headers={
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0\
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#         "Cookie":"_ga=GA1.2.1391731176.1529458040; pgv_pvi=1731241984; PHPSESSID=mk4r7k9eu77ingt9l5nmtfc5k7; pgv_si=s9881389056",
#         "Host":"hr.tencent.com",
#         "Upgrade-Insecure-Requests":"1",
#     }
#     resp=requests.get(url,headers=headers)
#     print(resp.text)
#     html=etree.HTML(resp.text)
#     print(type(html))
#     # title=html.xpath('//td[@class="l square"]/text')
#     # print(title)
#
#
#
# def built_url():
#     url="https://hr.tencent.com/position.php?&start={}#a"
#     for x in range(0,1,10):
#         new_url=url.format(x)
#         save_info(new_url)
#     save_info(url)
#
#
# built_url()