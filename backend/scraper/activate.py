from email.mime import base
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def activate_crawler(domain: str, name: str = "base"):
    process = CrawlerProcess(get_project_settings())

    process.crawl(name, domain=domain)
    process.start()

