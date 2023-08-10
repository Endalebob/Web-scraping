import scrapy


class WorldpopulationSpider(scrapy.Spider):
    name = "worldpopulation"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        # title = response.xpath('//h1/text()').get()
        countries = response.xpath("//td/a")
        for country in countries:
            print(country)
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # absolute path
            # yield scrapy.Request(f'https://{self.allowed_domains[0]}{link}')
            # yield scrapy.Request(response.urljoin(link))

            # relative path
            yield response.follow(link,callback=self.country_content,meta={"country":country_name})
    def country_content(self,response):
        row = response.xpath('(//table[contains(@class,"table-striped")])[1]/tbody/tr')
        for ro in row:

            year = ro.xpath('.//td[1]/text()').get()
            population = ro.xpath('.//td[2]/strong/text()').get()
            country = response.request.meta["country"]
            yield {
                "country":country,
                "year":year,
                "population":population
            }
