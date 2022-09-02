import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def activate_crawler(name: str, domain: str):
    process = CrawlerProcess(get_project_settings())

    process.crawl(name, domain=domain)
    process.start()

