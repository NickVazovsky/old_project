import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor


class LinksSpider(CrawlSpider):
    name = 'link_spider'
    #start_url=["http://mospolytech.ru/"]
    allowed_domains = ["http://mospolytech.ru/"]
    crawledLinks = []
    crawledLinks.append("http://mospolytech.ru/")
    start_urls = crawledLinks
    rules = (
        # Надо динамически вносить домен в allow
        Rule(LinkExtractor(allow=('http://mospolytech.ru/\w+/d+$',)), follow=True),
        Rule(LinkExtractor(allow=('http://mospolytech.ru/\w+/d+$',)), callback='parse'),
    )


    def parse(self, response):
        links = response.xpath('//a/@href').extract()


        for link in links:
            if link not in self.crawledLinks:
                if 'http' in link:
                    if link not in self.crawledLinks and '#' not in link:
                        self.crawledLinks.append(link)
                        self.start_urls.append(link)
                else:
                    link = 'http://mospolytech.ru/' + link
                    if link not in self.crawledLinks and '#' not in link:

                        self.crawledLinks.append(link)
                        self.start_urls.append(link)

                yield self.crawledLinks





   # def start_spider(self):
     #   process = CrawlerProcess({
    #        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
      #  })

#        process.crawl(self)
 #       process.start()

