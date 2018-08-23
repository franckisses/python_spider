# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencenthire.items import TencenthireItem


class TenxunSpider(CrawlSpider):
    name = 'tenxun'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    rules = (
        Rule(LinkExtractor(allow=r'.+&start=\d+#a'),follow=True),
        Rule(LinkExtractor(allow=r'.+id=\d{5}&keywords=&tid=0&lid=0'),callback='parse_item',follow=False)
    )

    def parse_item(self, response):
        item = TencenthireItem()
        # 职位名称
        item['title'] = response.xpath("//*[@id='sharetitle']/text()").get()
        # 职位地点
        item['local'] = response.xpath('//tr[@class="c bottomline"]/td[1]/text()').get()
        # 职位类型
        item['position_type'] = response.xpath('//tr[@class="c bottomline"]/td[2]/text()').get()
        # 招聘人数
        item['position_num'] = response.xpath('//tr[@class="c bottomline"]/td[3]/text()').get()
        # 工作职责
        item['duty'] = "".join(response.xpath('//*[@id="position_detail"]/div/table//tr[3]/td/ul/li/child::node()').getall())
        # 工作要求
        item['request'] = "".join(response.xpath('//*[@id="position_detail"]/div/table//tr[4]/td/ul/li/child::node()').getall())
        # print(item['duty'])
        # print(item['request'])
        yield item




