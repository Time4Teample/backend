import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['slchld.com']
    start_urls = ['http://slchld.com/']

    def parse(self, response):
        pass
