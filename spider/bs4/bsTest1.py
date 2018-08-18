from bs4 import BeautifulSoup

# CSS选择器的语法

with open("lianjia.html","rb") as f:
    a = f.read().decode("utf-8")

soup = BeautifulSoup(a,"lxml")

# 可以找到所有的div标签
# divs = soup.select("div")
# for div in divs:
#     print(div)

#找到第二个div标签
# div_2 = soup.select("div")[1]
# print(div_2)

# 获取所有的div的属性class为tag的标签
# tags = soup.select("div.tag")
# for tag in tags:
#     print(tag)

# tags = soup.select("div[class=tag]")
# for tag in tags:
#     print(tag)

# 获取标签的属性
# aList = soup.select("a")
# for a in aList:
#     href = a["href"]
    # print(href)

# 获取文本
divs = soup.select("div[class='info clear']")
for div in divs:
    print(div.get_text)
    # print(div.string)
    print(list(div.strings))   #这个也很爽
    # print(list(div.stripped_strings))   #这个方法太爽了吧
    break