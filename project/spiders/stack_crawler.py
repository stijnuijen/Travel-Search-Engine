import scrapy
import os 

class StackSpider(scrapy.Spider):
    name = 'stack'
    max_pages = 20000

    custom_settings = {
        'ROBOTSTXT_OBEY': True,
        'DOWNLOAD_DELAY': 1.5,
        'USER_AGENT': 'bot'}

    start_urls = ['https://stackoverflow.com/questions/tagged/python+pandas?sort=votes&page=1&pagesize=50']

    def parse(self, response):
        page_n = response.url.split('&')[-1]
        if page_n == 'page=2':
            exit()

        # follow links to question pages
        for href in response.xpath('//a[@class="question-hyperlink"]/@href'):
            yield response.follow(href, self.parse_question)

        # follow pagination links
        for href in response.xpath('//a[@rel="next"]/@href'):
            yield response.follow(href, self.parse)

    def parse_question(self, response):
        # write question html file to folder
        question_id = response.url.split('/')[-2]

        with open('pages/' + question_id + '.html', 'wb') as f:
            f.write(response.body)
