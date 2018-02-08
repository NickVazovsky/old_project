import scrapy
from request_http import starts_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
""""class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response): 
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)"""""


class QuotesSpider(CrawlSpider,scrapy.Spider):
    name = "quotes"
    allowed_domain = starts_url
    if starts_url:
        start_urls = starts_url
        rules = (
            # Надо динамически вносить домен в allow
            Rule(LinkExtractor(allow=('http://mospolytech.ru/',)), callback='parse',follow=True),
        )



    def parse(self, response):
        process = CrawlerProcess()
        process.crawl(self)
        process.stop()
        process.start()
        for quote in response.css('html'):
            yield {
                'title': quote.css('title::text').extract_first(),
                'keywords': quote.css('meta[name*=Keywords]::attr(content), meta[name*=keywords]::attr(content)').extract(),
                'description': quote.css('meta[name*=description]::attr(content), meta[name*=Description]::attr(content)').extract(),
                'h1': quote.css('h1::text').extract(),
                'h2': quote.css('h2::text, H2::text').extract(),
                'text': quote.css('p::text, span::text').extract(),
            }
