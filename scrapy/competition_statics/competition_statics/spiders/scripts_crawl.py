from abc import ABC

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ScriptsCrawlSpider(CrawlSpider, ABC):
    name = "scripts_crawl"
    allowed_domains = ["subslikescript.com"]
    start_urls = ["http://subslikescript.com/"]

    rules = (Rule(LinkExtractor(deny=""), callback="parse_item", follow=True),)

    def parse_item(self, response):
        bre = '*'*50
        print(bre)
        print(bre)
        item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        return item
