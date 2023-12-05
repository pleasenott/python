# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Test1Item(scrapy.Item):
    # define the fields for your item here like:
    school = scrapy.Field()
    link = scrapy.Field()

    # lianjia
    zone_name = scrapy.Field()
    building_names = scrapy.Field()
    area = scrapy.Field()
    price_per_area = scrapy.Field()
    houseInfo = scrapy.Field()
    total_price = scrapy.Field()


    followInfo = scrapy.Field()
    totalPrice_totalPrice2= scrapy.Field()
    unitPrice = scrapy.Field()
    positionInfo = scrapy.Field()

    # xuetang
    class_name = scrapy.Field()
    teacher = scrapy.Field()
    school_name = scrapy.Field()
    student_num = scrapy.Field()

    # loupan
    name = scrapy.Field()
    location_district = scrapy.Field()
    location_place = scrapy.Field()
    location_detail = scrapy.Field()
    room_type = scrapy.Field()
    room_area = scrapy.Field()
    average_price = scrapy.Field()