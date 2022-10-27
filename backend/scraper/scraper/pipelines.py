# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from scrapy.utils.project import get_project_settings

import logging

settings = get_project_settings()

class ScraperPipeline:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=settings["MONGODB_SETTINGS"],
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def process_item(self, item, spider):
        self.collection.insert_one(item)
        return item

    def open_spider(self, spider):
        # conn = MongoClient()
        self.conn = MongoClient(self.mongo_uri)
        self.db = self.conn[self.mongo_db]
        try:
            conn.admin.command('ping')
            self.database = conn["city"]
            self.collection = conn["courses"]
        except ConnectionFailure:
            logging.log("Connection failure from MongoClient.")



    def close_spider(self, spider):
        self.conn.close()

