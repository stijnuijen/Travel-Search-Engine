import os 
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class TPSpider(CrawlSpider):
    name = 'travelpoint'

    custom_settings = {
        'ROBOTSTXT_OBEY': True,
        'DOWNLOAD_DELAY': 1.5,
        'USER_AGENT': 'bot',
        'CLOSESPIDER_PAGECOUNT': 1000}

    start_urls = [('https://www.travellerspoint.com/forum.cfm?start='+str(i)) for i in range(1,1000,50)]

    def parse(self, response):
        # follow links to question pages
        for href in response.xpath('//*[@id="all_threads"]//a/@href').getall():
            if '?thread' in href:
                href_stripped = href.split('#')[0]
                yield response.follow(href_stripped+'&start=1', self.parse_item)

    def parse_item(self, response):
        filename = response.url
        with open('url_list.txt','r+') as f:
            if filename not in f:
                f.write('{}\n'.format(filename))
