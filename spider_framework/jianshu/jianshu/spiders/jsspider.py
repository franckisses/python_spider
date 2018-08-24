# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import JianshuItem

class JsspiderSpider(CrawlSpider):
    name = 'jsspider'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )
    def parse_detail(self, response):
        title = response.xpath('//h1[@class="title"]/text()').get()
        avatar = response.xpath('//a[@class="avatar"]/img/@src').get()
        author = response.xpath('//span[@class="name"]/a/text()').get()
        pub_time = response.xpath('//span[@class="publish-time"]/text()').get()
        orginal_id = response.url
        article = (orginal_id.split("?")[0]).split("/")[-1]
        content = response.xpath("//div[@class='show-content-free']").get()
        word_count = response.xpath('//span[@class="wordage"]/text()').get().split(" ")[1]
        like_count = response.xpath('//span[@class="likes-count"]/text()').get().split(" ")[1]
        read_count = response.xpath("//span[@class='views-count']/text()").get().split(" ")[1]
        subject = ",".join(response.xpath('//div[@class="include-collection"]/a/div/text()').getall())
        # subject ="我爱中国"

        item = JianshuItem(
            title=title,
            avatar=avatar,
            author=author,
            pub_time=pub_time,
            orginal_id=orginal_id,
            article=article,
            content=content,
            word_count=word_count,
            like_count=like_count,
            read_count=read_count,
            subject=subject
        )
        yield item




