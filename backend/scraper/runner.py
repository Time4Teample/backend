import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from scraper.scraper.spiders.spider import BaseSpider
from scraper.scraper import settings
import sys
import os


class Scraper:
    def __init__(self):
        # settings_file_path = 'scraper.scraper.settings' # The path seen from root, ie. from main.py
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings.__name__)
        # os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        self.process = CrawlerProcess(get_project_settings())
        self.spider = BaseSpider # The spider you want to crawl



    def run_spiders(self):
        self.process.crawl(self.spider)
        self.process.start()
