# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
#要求将课程名称、老师、所属学校和选课人数信息，保存到一个csv文件中。
import json
import csv
class Test1Pipeline:

    def open_spider(self, spider):
        try:
            self.file = open('gz2.csv', "a", encoding="utf-8-sig", newline='')
            self.writer = csv.writer(self.file)
        except Exception as err:
            print(err)

    def process_item(self, item, spider):
        list_item = [item['name_chinese'],item["zone_name"],item['house_type'], item['direct'], item['area'], item['price']]
        self.writer.writerow(list_item)
        return item
    def close_spider(self, spider):
            self.file.close() #关闭文件