# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencenthireItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    local = scrapy.Field()
    position_type = scrapy.Field()
    position_num = scrapy.Field()
    duty = scrapy.Field()
    request = scrapy.Field()
