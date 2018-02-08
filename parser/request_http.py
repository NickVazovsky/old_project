# -*- coding: UTF-8 -*-
from link_spider import LinksSpider
from universal_spider import QuotesSpider
import urllib.request
import urllib
from xml.dom.minidom import *
from scrapy.crawler import CrawlerProcess

starts_url =[]
try:
  man = urllib.request.urlopen("http://kuznetsovskyfarfor.ru/sitemap.xml")
except Exception as e:# Обработать urlerror установив urllib2 через виртуальную среду urllib2.URLError
    process = CrawlerProcess()
    spider = LinksSpider()
    spider.start_spider()
    print(spider.crawledLinks)


else:
    xml = parse(man)
    name = xml.getElementsByTagName('loc')
    for node in name:
       starts_url.append(node.childNodes[0].nodeValue)

       #print (node.childNodes[0].nodeValue)

class SearchRequestGoogle(object):
    urlz = []
    i = 0
    while i<1:
        urlz.append('https://www.google.com/search?q=wikipedia reading&start=' + str(i))
        i+=10

class SearchRequestYandex(object):
    urlc = []
    i = 0
    while i< 2:
        urlc.append('https://yandex.ru/search/?text=красивые туфли&p=' + str(i))
        i+=1
