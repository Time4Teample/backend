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
    def __init__(self):
        conn = MongoClient(host="mongodb://mongo", port=27017, username='root',password='root')
        db = conn["city"]
        self.collection = db["programs"]


    def process_item(self, item, spider):
        self.collection.insert_one(ItemAdapter(item).asdict())
        return item

    def open_spider(self, spider):
        ...

    def close_spider(self, spider):
        self.conn.close()

