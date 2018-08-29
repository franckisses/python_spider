"""
# -*- coding: utf-8 -*-
# @Time    : 2018/8/20 14:43
# @Author  : franck
# @Email   : franck_gxu@outlook.com
"""
import asyncio,requests,time,json
from UserAgentPool import  UserAgent
from lxml import etree

async def get(url):
    headers ={
        "User-Agent" : UserAgent().user_agent()
    }
    return requests.get(url,headers=headers)

async def request(_):
    url = 'https://www.dankegongyu.com/room/sh?page={}'.format(_)
    # 返回请求的响应
    response = await get(url)
    text = response.text
    html = etree.HTML(text)
    house_url = html.xpath("//div[3]/div/div[6]/div[2]/div[1]/div/div[1]/div[1]/a/@href")
    title = html.xpath("//div[3]/div/div[6]/div[2]/div[1]/div/div[1]/div[1]/a/@title")
    image_url = html.xpath("//div[3]/div/div[6]/div[2]/div[1]/div/a/img/@src")
    distance2subway =html.xpath('//div[3]/div/div[6]/div[2]/div[1]/div/div[1]/div[1]/div[1]/text()')
    details = html.xpath("/html/body/div[3]/div/div[6]/div[2]/div[1]/div/div[1]/div[2]/text()")
    temp_detail =[]
    #面积
    area = []
    # 楼层
    floor = []
    # 类型
    house_type = []
    # 房间走向
    towards = []
    for x in details:
        temp_detail.append(x.strip())
    while "" in temp_detail:
        temp_detail.remove("")
    # 去掉了所有的换行符之后
    for x in temp_detail:
        detail = x.split()
        area.append(detail[0])
        floor.append(detail[2])
        house_type.append(detail[4])
        towards.append(detail[6])
    tags = html.xpath('//div[3]/div/div[6]/div[2]/div[1]/div/div[1]/div[3]')
    tag_add=[]
    for tag in tags:
        tag_detail = ""
        if tag.xpath("./span[1]/text()"):
            tag_detail+=tag.xpath("./span[1]/text()")[0]
        else:
            pass
        if tag.xpath("./span[2]/text()"):
            tag_detail += tag.xpath("./span[2]/text()")[0]
        else:
            pass
        if tag.xpath("./span[3]/text()"):
            tag_detail += tag.xpath("./span[3]/text()")[0]
        else:
            pass
        tag_add.append(tag_detail)
    total_money = html.xpath("//span[@class='ty_b']/text()")
    for x in range(20):
        item = {
            "title": title[x],
            "image_url": image_url[x],
            "house_url": house_url[x],
            "distance2subway": distance2subway[x].strip(),
            "area": area[x],
            "floor": floor[x],
            "tag_add":tag_add[x],
            "house_type": house_type[x],
            "total_money": int(total_money[x].strip())  ,
        }
        with open("dankeSH.json","a",encoding="utf-8") as f:
            f.write(json.dumps(item,ensure_ascii=False)+"\n")

def main():
    tasks = [asyncio.ensure_future(request(_)) for _ in range(159,162)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print(tasks)

if __name__ =="__main__":
    main()


