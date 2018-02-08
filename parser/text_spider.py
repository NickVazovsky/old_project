import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.http import FormRequest

class TextSpider(scrapy.Spider):
    name = "TextSpider"
    start_urls = ['https://text.ru/antiplagiat/unauthorized']
    def parse(self, response):
        frmdata = {'user-text': 'За 20 лет работы «Кузнецовский фарфор» зарекомендовал истории'},
        url = "https://text.ru/antiplagiat/unauthorized"
        yield FormRequest(url, callback=self.after_text, formdata=frmdata)

    def after_text(self,response):
        unic = response.xpath(".//div[@class='section text unique']/strong/span[@class='unique hight']/text()")
        yield {
            'unic':unic

        }