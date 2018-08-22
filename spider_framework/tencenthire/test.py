"""
# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 11:59
# @Author  : franck
# @Email   : franck_gxu@outlook.com
"""

from lxml import etree
with open("HUH.html","r",encoding="utf-8") as f:
    a = f.read()

a = etree.HTML(a)
local = a.xpath('//tr[@class="c bottomline"]/td[1]/text()')
pos_type =  a.xpath('//tr[@class="c bottomline"]/td[2]/text()')
pos_num =  a.xpath('//tr[@class="c bottomline"]/td[3]/text()')
duty = a.xpath('//div[@class="box wcont_a"]/table[@class="tablelist textl"]/tr[3]/td/ul/li[1]/text()')
require = a.xpath('//table[@class="tablelist textl"]/tr[4]/ul/li/text()')

print(duty)