# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from scrpy.utils.project import get_project_settings

import logging

settings = get_project_settings()

class ScraperPipeline:
    def process_item(self, item, spider):
        return item

    def open_spider(self, spider):
        conn = MongoClient(settings["MONGODB_SETTINGS"])
        try:
            conn.admin.command('ping')
        except ConnectionFailure:
            logging.log("Connection failure from MongoClient.")

    def close_spider(self, spider):
        ...


