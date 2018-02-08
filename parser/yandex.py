import scrapy
from request_http import SearchRequestYandex
import re


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = SearchRequestYandex.urlc

    def parse(self, response):
            title = response.xpath('//li[contains(@class, "t-construct-adapter__legacy")]/div/h2/a').extract(),
            yasearchlink= response.xpath('//li[contains(@class, "t-construct-adapter__legacy")]/div/h2/a/@href').extract()
            desc = response.xpath('//li[contains(@class, "t-construct-adapter__legacy")]/div/div[2]').extract(),
            domain = 'http://wlooks.ru/'
            page = response.xpath('//span[@class="pager__item pager__item_current_yes pager__item_kind_page"]/text()').extract()
            i = 0

            for i in range(len(title[0])):
                if domain in title[0][i]:
                    break

            if domain in title[0][i]:

                index = i
                links = yasearchlink[index]
                tit = re.sub(r'(?:<).*?(?:>)', '', str(title[0][index]))
                descr = re.sub(r'(?:<).*?(?:>)', '', str(desc[0][index]))
                index += 1

                yield {
                    'title': tit,
                    'link':links,
                    'desk': descr,
                    'index':index,
                    'page':page,
                    #'index': yasearchlink,
                }


