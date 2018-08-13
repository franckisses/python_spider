# https://www.qiushibaike.com/
import requests,re

from lxml import etree

resp = requests.get("https://www.qiushibaike.com/")
response = resp.text
# print(type(response))
root = etree.HTML(response)
user_name = root.xpath("//div/div[1]/a[2]/h2/text()")
users=[]
for user_1 in user_name:
    user=user_1.strip()
    users.append(user)
print(len(users))
jokers=root.xpath("//div[@class='content']/span/text()")
print(jokers)
print(len(jokers))
joker=[]
for x in jokers:
    a =""
    print(x[1],x[-1])
    if x[1]=="\n" and x[-1]=="\n":
        joker.append(x)
    else:
        a+=x
        joker.append(a)
    # elif x[0]=="\n":
    #     a=x
    # elif x[1]!="\n" and x[-1]!="\n":
    #     a+=x
    # elif x[-1]=='\n':
    #     a+=x
    #     joker.append(a)

# jokers=re.findall(r'<div class="content"><span>(.+?)</span>',response,re.DOTALL)
print(len(jokers))
print(joker)





