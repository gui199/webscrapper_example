# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TeleshopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nome = scrapy.Field()
    image = scrapy.Field()
    preço = scrapy.Field()
