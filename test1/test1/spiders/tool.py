import scrapy

from test1.items import Test1Item  # 从items.py中引入MyItem对象


class LianjiaSpider(scrapy.Spider):
    name = 'tool'
    allowed_domains = ['zz.lianjia.com']
    """
二七区
中原区
管城回族区
惠济区
金水区
郑东新区
荥阳市
新郑市
上街区
巩义市
新密市
登封市
中牟县
郑州经济技术开发区
郑州高新技术产业开发区
航空港区

"""
    zone_list_chinese = ["二七区", "中原区", "管城回族区", "惠济区", "金水区", "郑东新区", "荥阳市", "新郑市", "上街区",
                         "巩义市", "新密市", "登封市", "中牟县", "郑州经济技术开发区", "郑州高新技术产业开发区",
                         "航空港区"]

    zone_list = ["erqiqu", "zhongyuanqu", "guanchengqu", "huijiqu", "jinshuiqu", "zhengdongxinqu", "xingyangshi",
                 "xinzhengshi", "shangjiequ", "gongyishi", "xinmishi", "dengfengshi", "zhongmuxian",
                 "zhengzhoujingjijishukaifaqu", "zhengzhougaoxinjishuchanyekaifaqu", "hangkonggangqu"]
    # https://bj.lianjia.com/zufang/pg2/
    zone_list_number = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    base_url = 'https://zz.lianjia.com/zufang/'
    out_list=[]
    num=1
    def __init__(self):
        super().__init__()
        self.download_delay = 1
        self.start_urls = [self.base_url +self.zone_list[0]+"/pg1"]
        print(self.zone_list[0])




    #析构函数

    def parse(self, response, **kwargs):

        filename="tool.txt"
        with open(filename, "a") as f:
            for each in response.xpath("//*[@id='filter']/ul[4]/*"):  # 遍历可选的板块
                data_id = each.xpath("@data-id").extract_first()
                if data_id is None or data_id == "0":  # 板块选项的第一个是不限，跳过
                    continue
                newblock = each.xpath("a/@href").extract_first()
                newblock = newblock.replace("/zufang/", "").replace("/", "")
                if newblock not in self.out_list:
                    self.out_list.append(newblock)
                    f.write("\""+newblock +"\",")
            if self.num<len(self.zone_list):
                url = self.base_url + self.zone_list[self.num] + "/pg1"
                self.num=self.num+1
                yield scrapy.Request(url, callback=self.parse)

