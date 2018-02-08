import scrapy
from seo_parsers.seo_parser.items import
import re
from scrapy.selector import Selector


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = SearchRequestGoogle.urlz

    def parse(self, response):
        title = response.xpath('//h3/a[not(contains(@class,"sla"))]').extract(),
        description = response.xpath('//span[@class="st"]').extract(),
        google_search_links_list = response.xpath('//div/h3/a[not(contains(@class,"sla"))]').extract(),
        links = response.xpath('//div[@class="kv"]//*').extract(),

        domain = 'https://www.knaw.nl/en/news/calendar/reading-wikipedia'
        i = 0
        for i in range(len(google_search_links_list[0])):
            if domain in google_search_links_list[0][i]:
               break
        index = i
        answer = re.sub(r'(?:<).*?(?:>)', '', title[0][index])
        desc = re.sub(r'(?:<).*?(?:>)', '', description[0][index])
        link = re.sub(r'(?:<).*?(?:>)', '', links[0][index])
        index += 1


        yield {
            'title': answer,
            'description': desc,
            'link': google_search_links_list,
            'lik':domain,
            'index': index

        }
