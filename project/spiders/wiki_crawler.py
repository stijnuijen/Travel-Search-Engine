import scrapy, os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Spider(scrapy.Spider):
    name = 'wiki'

    custom_settings = {
        'ROBOTSTXT_OBEY': True,
        'DOWNLOAD_DELAY': 1.5,
        'USER_AGENT': 'bot',
        'CLOSESPIDER_ITEMCOUNT': 1000}

    start_urls = ['https://en.wikipedia.org/wiki/List_of_sovereign_states']

    def parse(self, response):

        # follow links to country pages
        for href in response.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody//a/@href'):
            for forbidden_tag in blacklist:
                if forbidden_tag not in href:
                    yield response.follow(href, self.parse_page)

    def parse_page(self, response):

        # write url to file
        page_url = response.url
        with open('urls.txt', 'r+') as f:
            if page_url not in f:
                f.write(page_url+'\n')

        # follow all links on the page and parse until itemcount is reached
        for href in response.xpath('//*[@id="bodyContent"]//a/@href'):
            yield response.follow(href, self.parse_page)
