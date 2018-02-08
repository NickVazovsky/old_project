# coding: utf8
import scrapy
from scrapy.spider import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re
from scrapy.http import Request
class PublicationSpider(CrawlSpider):
    name = "Publication"
    start_urls = ["https://habrahabr.ru/users/alonecoder/"]
    rules = (
        Rule(LinkExtractor(allow=('https://habrahabr.ru/users/bekbulatov/*')), callback='parse'),
    )
    def parse(self, response):
        title = response.xpath('//h2[@class="post__title"]/a/text()').extract(),
        keyword = response.xpath('//ul[@class="post__hubs inline-list"]/li[1]/a/text()').extract(),
        description = response.xpath('//div[@class="post__text post__text-html js-mediator-article"]').extract()
        descri = ''
        st =''

        for i in range(len(description)):
            re.sub(r'(?:<).*?(?:>)', '', description[i])

        tit = str(title).encode(encoding="utf-8",errors='ignore')
        key = str(keyword).encode(encoding='utf-8',errors='ignore')
        desc = str(description).encode(encoding='utf-8',errors='ignore')
        filename = 'answer42.json'
        with open(filename, 'wt') as f:
            f.write(str(tit))
            f.write(str(key))
            f.write(str(desc))

    start_urls.append(start_urls[0]+'posts')
