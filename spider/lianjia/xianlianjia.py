"""
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 18:57
# @Author  : franck
# @Email   : franck_gxu@outlook.com
"""
import time,random
import requests
from UserAgentPool import UserAgent
from lxml import etree
from MysqlHelper import DbHelper

def request_page(url):
    headers = {
        "User-Agent": UserAgent().user_agent(),
        "Cookie": 'lianjia_uuid=9aed2e91-8eef-43ac-b5be-96b9ef415950; lianjia_ssid=f8cfe29b-60fa-430a-9441-b6085cafe548; UM_distinctid=16541b6d9601166-0630781662e2c-323b5b03-1fa400-16541b6d961371; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1534405828; _smt_uid=5b752cc8.1e7a73f9; _ga=GA1.2.1913783529.1534405835; _gid=GA1.2.498042162.1534405835; select_city=610100; all-lj=26155dc0ee17bc7dec4aa8e464d36efd; TY_SESSION_ID=59631a28-f9ed-44ca-b6b3-3c4dd295379d; CNZZDATA1255849580=1634441359-1534405146-https%253A%252F%252Fbj.lianjia.com%252F%7C1534405146; CNZZDATA1254525948=1126850249-1534403892-https%253A%252F%252Fbj.lianjia.com%252F%7C1534403892; CNZZDATA1255633284=1921619603-1534405129-https%253A%252F%252Fbj.lianjia.com%252F%7C1534405129; CNZZDATA1255604082=1854788469-1534404856-https%253A%252F%252Fbj.lianjia.com%252F%7C1534404856; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1534406544; _gat=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1'
    }
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    # 标题
    title = html.xpath('//*[@id="house-lst"]/li/div[2]/h2/a/text()')
    # 小区
    department = html.xpath('//*[@id="house-lst"]/li/div[2]/div[1]/div[1]/span[1]/text()')
    # 户型
    type = html.xpath('//*[@id="house-lst"]/li/div[2]/div[1]/div[1]/span[2]/span/text()')
    # 面积
    area = html.xpath('//*[@id="house-lst"]/li/div[2]/div[1]/div[1]/span[3]/text()')
    # 走向
    towards = html.xpath('//*[@id="house-lst"]/li/div[2]/div[1]/div[1]/span[4]/text()')
    # 行政区域
    district = html.xpath('//*[@id="house-lst"]/li/div[2]/div[1]/div[2]/div/a/text()')
    # 楼层
    floor = html.xpath('//*[@id="house-lst"]/li/div[2]/div[1]/div[2]/div/text()[1]')
    # 楼层特点
    build_type = html.xpath('//*[@id="house-lst"]/li/div[2]/div[1]/div[2]/div/text()[2]')
    # 月租
    rent_rate = html.xpath('//*[@id="house-lst"]/li/div[2]/div[2]/div[1]/span/text()')
    # 更新时间
    update_time = html.xpath('//*[@id="house-lst"]/li/div[2]/div[2]/div[2]/text()')
    # print(title,"\n",department,"\n",type,"\n",area,"\n",towards,"\n",district,"\n",floor,"\n",build_type,"\n",rent_rate,"\n",update_time)
    item = []
    # "".join(a.split())
    for x in range(0,30):
        info = {
            "title" : title[x],
            "department" : "".join(department[x].split()),
            "type" : "".join(type[x].split()),
            "area" : "".join(area[x].split()),
            "towards" : towards[x],
            "district" : district[x],
            "floor": floor[x],
            "bulid_type": build_type[x],
            "rent_rate":rent_rate[x],
            "update_time":update_time[x].split(" ")[0]
        }
        item.append(info)
    return  write2sql(item)

def write2sql(item):
    dbhelper = DbHelper()
    for x in item:
        title = x["title"]
        department = x["department"]
        type = x["type"]
        area =  x["area"]
        towards = x["towards"]
        district = x["district"]
        floor = x["floor"]
        build_type = x["bulid_type"]
        rent_rate = x["rent_rate"]
        update_time = x["update_time"]
        sql = "INSERT INTO newdatabase.lianjia(title,department,type,area,towards,district,floor,build_type,rent_rate,update_time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params = (title,department,type,area,towards,district,floor,build_type,rent_rate,update_time)
        result = dbhelper.execute(sql, params)
        if result == True:
            print("插入成功")
        else:
            print("插入失败",params)



def main():
    for x in range(2, 101):
        url = "https://xa.lianjia.com/zufang/pg{}/".format(x)
        request_page(url)
        time.sleep(random.randint(10,20))



if __name__ == "__main__":
    main()


