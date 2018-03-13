# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LotteryspiderItem(scrapy.Item):
    date = scrapy.Field()
    issue = scrapy.Field()
    number1 = scrapy.Field()
    number2 = scrapy.Field()
    number3 = scrapy.Field()
    number4 = scrapy.Field()
    number5 = scrapy.Field()
    number6 = scrapy.Field()
    numberEx = scrapy.Field()
    sales = scrapy.Field()
    first_prize = scrapy.Field()
    second_prize = scrapy.Field()
    place = scrapy.Field()
