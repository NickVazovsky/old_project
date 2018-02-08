import scrapy


class BookSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://google.ru/']

    def parse(self, response):
        for quote in response.css('html'):

            yield {
                'a': quote.css('a::attr(href)').extract(),
                 }
