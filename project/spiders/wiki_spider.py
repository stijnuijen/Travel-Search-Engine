import scrapy, os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class WikiSpider(scrapy.Spider):
    name = 'wiki'

    custom_settings = {
        'ROBOTSTXT_OBEY': True,
        'DOWNLOAD_DELAY': .5,
        'USER_AGENT': 'bot'}

    start_urls = ['https://en.wikipedia.org/wiki/List_of_sovereign_states']
    blacklist = ['#', 'Category:', 'File:', 'Wikipedia:', 'Index', 'List', 'Template', 'User', 'Book:']
    allowed_domains = ['en.wikipedia.org']

    count = 0
    max_count = 1050

    def parse(self, response):

        # follow links to country pages
        for href in response.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody//a/@href'):
            for forbidden_tag in self.blacklist:
                if forbidden_tag not in href.get():
                    yield response.follow(href, self.parse_page)


    def parse_page(self, response):

        if self.count < self.max_count:

            # write url to file
            page_url = response.url

            for forbidden_tag in self.blacklist:
                if forbidden_tag in page_url:
                    return
            
            with open('url_list.txt', 'a+') as f:
                if page_url not in f.read():
                    f.write('{}\n'.format(page_url))
                    self.count += 1

                # follow all links on the page and parse until itemcount is reached
                for href in response.xpath('//*[@id="bodyContent"]//a/@href'):
                    yield response.follow(href, self.parse_page)
            
        else:
            raise CloseSpider('Limit reached.')
