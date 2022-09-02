import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from scraper.spiders.spider import MainSpider

settings = get_project_settings()

def runner():
    process = CrawlerProcess(settings)
    process.crawl(MainSpider)
    process.start()