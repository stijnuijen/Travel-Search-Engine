import os 
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider

class TPSpider(CrawlSpider):
    name = 'travelpoint'

    custom_settings = {
        'ROBOTSTXT_OBEY': True,
        'DOWNLOAD_DELAY': .5,
        'USER_AGENT': 'bot'}

    count = 0
    max_count = 10050

    start_urls = [('https://www.travellerspoint.com/forum.cfm?start='+str(i)) for i in range(1,100000,50)]

    def parse(self, response):
        # follow links to question pages
        for href in response.xpath('//*[@id="all_threads"]//a/@href').getall():
            if '?thread' in href:
                href_stripped = href.split('&')[0]
                yield response.follow(href_stripped+'&start=1', self.parse_item)

    def parse_item(self, response):
        if self.count < self.max_count:
            page_url = response.url
            with open('url_list_large.txt','a+') as f:
                if page_url not in f.read():
                    f.write('{}\n'.format(page_url))
                    self.count += 1
        else:
            raise CloseSpider('Limit reached.')

