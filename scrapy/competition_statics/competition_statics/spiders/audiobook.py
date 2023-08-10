import scrapy


class AudiobookSpider(scrapy.Spider):
    name = "audiobook"
    allowed_domains = ["www.audible.com"]
    start_urls = ["https://www.audible.com/search"]

    def parse(self, response, **kwargs):
        all_list = response.xpath('//ul')
        for lis in all_list:
            h3 = lis.xpath('.//h3/a/text()').get()
            author = lis.xpath('.//li[contains(@class,"authorLabel")]/span/a/text()').getall()
            length = lis.xpath('.//li[contains(@class,"runtimeLabel")]/span/text()').get()

            yield {
                "title": h3,
                "author": author,
                "length": length
            }

        x_path = '//ul[contains(@class,"pagingElements")]/li/span[contains(@class,"nextButton")]/a'
        a_tag = response.xpath(x_path)
        link = a_tag.xpath(".//@href").get()
        yield response.follow(link, callback=self.parse)

    # def parse(self, response):
    #
    #     pagination = response.xpath('//ul[contains(@class,"pagingElement")]/li/a/text()').getall()
    #     n = int(pagination[-1])
    #     for i in range(1,n+1):
    #         yield scrapy.Request(f'{self.start_urls[0]}?page={i}',callback=self.pagination)
    #
    #
    #
    #
    #
    # def pagination(self,response):
    #     def contents(content):
    #         print(
    #             "------------------------------------------------------------------------------------------------------")
    #         for par in content:
    #             title = par.xpath('.//h3/a/text()').get()
    #             author = par.xpath('.//li[contains(@class, "authorLabel")]/span/a/text()').getall()
    #             length = par.xpath('.//li[contains(@class, "runtimeLabel")]/span/text()').get()
    #
    #             yield {
    #                 "title": title,
    #                 "author": author,
    #                 "length": length.split(':')[-1]
    #             }
    #
    #     content = response.xpath('//div[@class="adbl-impression-container "]/div/span/ul/li')
    #     print('############################################################################')
    #     for con in contents(content):
    #         yield con
