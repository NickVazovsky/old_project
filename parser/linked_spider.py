import scrapy


class LinkedSpider(scrapy.Spider):
    name = 'LinkedSpider'
    start_urls = ['http://www.linkpad.ru/?search=kuznetsovskyfarfor.ru#/default.aspx?r=3&i=kuznetsovskyfarfor.ru']

    def parse(self, response):
        spanius = response.xpath('.//span[@class="M3 M3-0"]/text()').extract()
        yield {
            'span':spanius
        }
