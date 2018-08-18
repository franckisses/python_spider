from bs4 import BeautifulSoup

with open("lianjia.html","rb") as f:
    a = f.read().decode("utf-8")

soup = BeautifulSoup(a,"lxml")

# a = soup.find("div")
# print(type(a))

#获取注释字符串
p = soup.find("p")
print(p.contents)

#contents和 children
# 返回某个标签下的直接子元素,其中也包括字符串,他们两的区别是,
# contents返回的是一个列表,children返回的是一个迭代器