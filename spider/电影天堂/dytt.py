# http://www.dytt8.net/html/gndy/dyzz/index.html

import requests
from lxml import etree

url="http://www.dytt8.net/html/gndy/dyzz/index.html"
header={
"Cookie": "td_cookie=18446744070634153048; td_cookie=18446744070634105235",
"Host": "www.dytt8.net",
"Referer": "http://www.dytt8.net/html/gndy/dyzz/index.html",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
}
resp=requests.get(url,headers=header)
print(resp.text)