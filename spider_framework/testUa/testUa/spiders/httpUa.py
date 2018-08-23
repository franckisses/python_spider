# -*- coding: utf-8 -*-
import scrapy
import json

class HttpuaSpider(scrapy.Spider):
    name = 'httpUa'
    allowed_domains = ['http://httpbin.org/']
    start_urls = ['http://httpbin.org/user-agent']

    def parse(self, response):
        print(response.text)
        yield  scrapy.Request(self.start_urls[0])
