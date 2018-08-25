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
        # 获取文章的标题
        title = response.xpath('//h1[@class="title"]/text()').get()
        # 获取文章作者的头像地址
        avatar = response.xpath('//a[@class="avatar"]/img/@src').get()
        # 获取文章作者
        author = response.xpath('//span[@class="name"]/a/text()').get()
        # 获取文章的发表时间
        pub_time = response.xpath('//span[@class="publish-time"]/text()').get()
        # 文章的存储地址
        orginal_id = response.url
        article = (orginal_id.split("?")[0]).split("/")[-1]
        # 文章的内容部分
        content = response.xpath("//div[@class='show-content-free']").get()
        # 文章的字数
        word_count = response.xpath('//span[@class="wordage"]/text()').get().split(" ")[1]
        # 喜欢的人数
        like_count = response.xpath('//span[@class="likes-count"]/text()').get().split(" ")[1]
        # 阅读的数量
        read_count = response.xpath("//span[@class='views-count']/text()").get().split(" ")[1]
        # 属于的专题
        subject = ",".join(response.xpath('//div[@class="include-collection"]/a/div/text()').getall())

        # 将文章的所有的信息,返回到item中
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




