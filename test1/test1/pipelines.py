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
        try: #打开json文件
            self.file = open('MyData.json', "w", encoding="utf-8")
        except Exception as err:
            print(err)
        try:
            #以utf-8 bom 打开
            self.file2 = open('MyData.csv', "w", encoding="utf-8-sig", newline='')
            self.writer = csv.writer(self.file2)
            #self.writer.writerow(['课程名称', '老师', '所属学校', '选课人数'])
        except Exception as err:
            print(err)

    def process_item(self, item, spider):
        dict_item = dict(item) #生成字典对象
        json_str = json.dumps(dict_item, ensure_ascii=False) + "\n" #生成json串
        self.file.write(json_str) #将json串写入到文件中
        self.writer.writerow([item['class_name'], item['teacher'], item['school_name'], item['student_num']])
        print([item['class_name'], item['teacher'], item['school_name'], item['student_num']])
        return item
    def close_spider(self, spider):
            self.file.close() #关闭文件