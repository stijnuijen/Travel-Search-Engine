import scrapy
import os 

class LonelySpider(scrapy.Spider):
    name = 'lonely'

    custom_settings = {
        'ROBOTSTXT_OBEY': True,
        'DOWNLOAD_DELAY': 1.5,
        'USER_AGENT': 'bot',
        'CLOSESPIDER_PAGECOUNT': 1000}
        
    start_urls = [('https://www.lonelyplanet.com/thorntree/forums/americas-south-america?page='+str(i)) for i in range(100)]
        
    def parse(self, response):
        # follow links to question pages
        for href in response.xpath('//a[@class="copy--h3"]/@href'):
            yield response.follow(href, self.parse_question)


    def parse_question(self, response):
        filename = response.url
        with open('url_list.txt','w') as f:
            if filename not in f:
                f.write('{}/n'.format(filename))