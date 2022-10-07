import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from .scraper.spiders.spider import BaseSpider

settings = get_project_settings()

def runner():
    # import sys    
    # if "twisted.internet.reactor" in sys.modules:
    #     del sys.modules["twisted.internet.reactor"]
    process = CrawlerProcess(settings)
    process.crawl(BaseSpider)
    process.start()