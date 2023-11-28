import scrapy
from test1.items import Test1Item #从items.py中引入MyItem对象
class mySpider(scrapy.spiders.Spider):
    name = "bupt" #爬虫的名字是bupt
    allowed_domains = ["bupt.edu.cn/"] #允许爬取的网站域名
    start_urls = ["https://www.bupt.edu.cn/yxjg1.htm"]
    #初始URL，即爬虫爬取的第一个URL
    def parse(self, response):  # 解析爬取的内容
        item = Test1Item()  # 生成一个在items.py中定义好的Myitem对象,用于接收爬取的
        for each in response.xpath("xxx"):
            item['school'] = each.xpath("text()").extract()  # 学院名称在text中
            item['link'] = each.xpath("@href").extract()  # 学院链接在href中
            if (item['school'] and item['link']):  # 去掉值为空的数据
                yield (item)  # 返回item数据给到pipelines模块