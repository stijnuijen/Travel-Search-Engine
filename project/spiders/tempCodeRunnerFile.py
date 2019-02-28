import scrapy
import os
from scrapy.exceptions import CloseSpider

class FodorsSpider(scrapy.Spider):
    name = 'fodors'

    custom_settings = {
        'ROBOTSTXT_OBEY': True,
        'DOWNLOAD_DELAY': .5,
        'USER_AGENT': 'bot'}

    count = 0
    max_count = 10050

    start_urls = [('https://www.fodors.com/community/asia/page'+str(i)) for i in range(100000)]
        
    def parse(self, response):
        # follow links to question pages
        for href in response.xpath('//*[@id="td_threadtitle_1664163"]//a/@href'):
            print(href)
            yield response.follow(href, self.parse_question)
            

    def parse_question(self, response):
        if self.count < self.max_count:
            page_url = response.url
            with open('url_list_large.txt','a+') as f:
                if page_url not in f.read():
                    f.write('{}\n'.format(page_url))
                    self.count += 1
        else:
            raise CloseSpider('Limit reached.')