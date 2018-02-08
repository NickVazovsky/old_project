"""from bs4 import BeautifulSoup
import requests

check = "http://redkie.ru"
url = 'http://www.google.com/search?q='
page = requests.get(url + 'кузнецовский фарфор')
index2=1
for index in range(1):
    soup = BeautifulSoup(page.text)
    next_page = soup.find("a", class_="fl")
    next_link = ("https://www.google.com" + next_page["href"])
    print(next_link)
    h3 = soup.find_all("h3", class_="r")
    for elem in h3:
        elem = elem.contents[0]
        print(elem)
    page = requests.get(next_link)

"""
import scrapy
from request_http import SearchRequestGoogle
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
        page = response.xpath('span[@class="csb"]/b/text()').extract()

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

            'page': page,

        }







