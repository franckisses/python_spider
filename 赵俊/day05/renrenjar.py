from http import cookiejar
from urllib import request

cookiej = cookiejar.CookieJar()
# 通过HTTPCookieProcessor来处理cookie
cookie_handler = request.HTTPCookieProcessor(cookiej)
# 构建一个opener
# 用一个新的可以处理cookie的handler取代原来的默认的http handler
# 从而加强http handler 的功能,实现其可以处理cookie
opener = request.build_opener(cookie_handler)

opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")]

url="http://www.renren.com"
data = {"email":"xxx","password":"yyy"}

data = bytes(parse.urlencode(data),encoding="utf-8")
req = request.Request(url,data=data,method="POST")
response=opener.open("sheide zhuye")
with open("myrenrenFormDATA.html","wb") as f:
    f.write(response)
