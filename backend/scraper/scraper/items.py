# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class ScraperItem(Item):
    title = Field()
    organization = Field()
    status = Field()
    url = Field()
    content = Field()