import scrapy


class MainSpider(scrapy.Spider):
    name = 'main'

    def __init__(self, start_urls=None, *args, **kwargs):
        super(MainSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'{start_urls}']

    def start_requests(self):
        yield scrapy.Request(self.start_urls)

    def parse(self, response):
        pass
