from bs4 import BeautifulSoup

#使用find方法提取

with open("lianjia.html", "rb") as f:
    a = f.read().decode("utf-8")

bs = BeautifulSoup(a, "lxml")
# 美化显示网页
# print(bs.prettify)

# 找到网页中所有的a标签
# all_li = bs.find_all("a",)
# for all in all_li:
#     print("*" * 30)
#     print(all)

#找到网页中li标签中的第二个标签 limit 一共显示几个
# all_li = bs.find_all("a",limit=2)
# a = all_li[1]
# print(a)

# <span class="positionIcon">
# 获取有属性的标签
# all_span = bs.find_all("span",class_="positionIcon")
# print(all_span)

# 指定属性
# all_span = bs.find_all("span",attrs={"class":"positionIcon"})
# print(all_span)

# 将满足两个条件的属性的标签提取出来 attrs 也可以
# all_span = bs.find_all("span",class_="positionIcon",id="text")
# print(all_span)

# 获取a标签的href属性
# hrefs = bs.find_all("a")
# for a in hrefs:
    # 通过下标的方式获取
    # link = a['href']
    # print(link)
    #通过attrs方式获取
    # href = a.attrs['href']
    # print(href)

div = bs.find_all("li",class_="clear LOGCLICKDATA")
for x in div:
    title = x.find_all("div")[1].get_text()
    print(title)
# string 获取某个标签下的非标签字符串,返回的是一个字符串
# strings 获取某个标签下的子孙非标签字符串,返回来的是个生成器
# stripped_strings 获取某个标签下的子孙非标签字符串,去掉空白字符,返回一个生成器
# get_text() 获取某个标签下的子孙非标签字符串 ,不是以列表的形式返回,是以普通字符串返回










