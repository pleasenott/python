import scrapy

from test1.items import Test1Item  # 从items.py中引入MyItem对象


class LianjiaSpider(scrapy.Spider):
    name = 'sz'
    allowed_domains = ['sz.lianjia.com']
    """
天河
越秀
荔湾
海珠
番禺
白云
黄埔
从化
增城
花都
南沙
"""

    zone_list=["buxin","baishida","cuizhu","chunfenglu","dongmen","diwang","honghu","huangbeiling","huangmugang","liantang","luohukouan","luoling","qingshuihe","sungang","wanxiangcheng","xinxiu","yinhu","bagualing","baihua","chegongmiao","chiwei","futianbaoshuiqu","futianzhongxin","huanggang","huaqiangbei","huaqiangnan","jingtian","lianhua","meilin","shixia","shangxiasha","shawei","shangbu","xiangmihu","xiangmeibei","xinzhou1","yuanling","zhuzilin","baishizhou","daxuecheng3","hongshuwan","houhai","huaqiaocheng1","kejiyuan","nanshanzhongxin","nantou","qianhai","shekou","shenzhenwan","xili1","meisha","shatoujiao","yantiangang","baoanzhongxin","bihai1","fanshen","fuyong","songgang","shajing","shiyan","taoyuanju","xinan","xicheng1","xixiang","bujiguan","bujidafen","bujishuijing","bujishiyaling","bantian","bujijie","bujinanling","danzhutou","dayunxincheng","henggang","longgangshuanglong","longgangzhongxincheng","longgangbaohe","minzhi","pingdi","pinghu","guanlan","hongshan6","longhuazhongxin","longhuaxinqu","meilinguan","shangtang","gongming","guangming1","pingshan","dapengbandao"]
    #为每个zone_list设置最大页数为3
    zone_list_number=[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
    base_url = 'https://sz.lianjia.com/zufang/'


    maxpage = 500

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.download_delay = 1
        with open("sz.txt", "r") as f:
            temp=f.read().split("\n")
            self.zone_index=int(temp[0])
            self.page_index =int (temp[1])

            self.start_urls = [self.base_url +self.zone_list[self.zone_index]+"/pg"  + str(self.page_index)]
            print(self.zone_index,self.page_index)
            f.close()

    #析构函数

    def parse(self, response, **kwargs):
        sign=False
        for each in response.xpath("//*[@id='content']/div[1]/div[1]/*"):
            item = Test1Item()
            item['price'] = each.xpath("div/span/em/text()").extract_first()
            if '-' in item['price']:
                temp = item['price'].split("-")
                item['price'] = (float(temp[0]) + float(temp[1])) / 2
            temp = each.xpath("div/p[1]/a/text()").extract_first()
            # 从temp中提取数据
            temp = temp.split(" ")
            item['name'] = temp[0]
            item["house_type"] = ""
            item["area"] = ""
            item["direct"] = ""
            item["name_chinese"] = "深圳"
            for i in temp:
                if '室' in i or '厅' in i or '卫' in i:
                    item['house_type'] = i
                if '东' in i or '南' in i or '西' in i or '北' in i:
                    if len(i) < 5:
                        item['direct'] = i
            temp = each.xpath("div/p[2]/text()").extract()
            for i in temp:
                if '㎡' in i:
                    i = i.replace("㎡", "").replace(" ", "").replace("\n", "")
                    if "-" in i:
                        temp = i.split("-")
                        item['area'] = (float(temp[0]) + float(temp[1])) / 2
                    else:
                        item['area'] = i

            # 获取面积
            # item["area"]=each.xpath("/div/p[2]/text()[2]").extract_first()

            # item["house_type"]=each.xpath("/div/p[2]/text()[7]").extract_first()
            # print(item)
            #item["zone_name"] = self.zone_list_chinese[self.zone_index]
            item["zone_name"] = response.xpath("/html/body/div[3]/div[1]/div[3]/h1/a/text()").extract_first().replace(
                "租房", "")
            if item['price'] and item['name'] and item['house_type'] and item['area'] and item['direct']:
                sign=True
                yield item

            # if item['building_names'] and item['total_price'] and item['area'] and item['price_per_area']:
            #     yield item

        # self.page_index += 1
        # if self.zone_index < len(self.zones):
        #     if self.page_index <= 2:
        #         url = self.base_url + self.zones[self.zone_index] +self.mem+ 'pg' + str(self.page_index)
        #     else:
        #         self.page_index = 1
        #         url = self.base_url + self.zones[self.zone_index] + self.mem+"pg"
        #         self.zone_index += 1
        # else:
        # self.page_index += 1
        # print("adasdasdsd",response.xpath('//*[@id="content"]/div[1]/div[2]/*[@class="next"]/text()').extract_first() )
        # if response.xpath('//*[@id="content"]/div[1]/div[2]/*[@class="next"]') is None:
        #     self.page_index=0
        #     self.zone_index+=1
        #     if self.zone_index>=len(self.zone_list):
        #         return
        # url=self.base_url+self.zone_list[self.zone_index]+"/pg"+str(self.page_index)
        #
        # print(url)
        # yield scrapy.Request(url, callback=self.parse)
        if self.maxpage <= 0:
            with open("sz.txt", "w") as f:
                f.write(str(self.zone_index))
                f.write("\n")
                f.write(str(self.page_index))
                f.close()
            return
        if self.maxpage%10==0:
            with open("sz.txt", "w") as f:
                f.write(str(self.zone_index))
                f.write("\n")
                f.write(str(self.page_index))
                f.close()
        if response.xpath("//*[@id='content']/div[1]/div[2]/@data-totalpage").extract_first() :
            self.zone_list_number[self.zone_index]=int(response.xpath("//*[@id='content']/div[1]/div[2]/@data-totalpage").extract_first())
            print("self.zone_list_number[self.zone_index]",self.zone_list_number[self.zone_index])
        self.page_index += 1
        if self.zone_index < len(self.zone_list):
            if self.page_index <= self.zone_list_number[self.zone_index] and sign:
                url=self.base_url+self.zone_list[self.zone_index]+"/pg"+str(self.page_index)
            else:
                self.page_index = 1
                url = self.base_url + self.zone_list[self.zone_index]
                self.zone_index += 1
        else:
            with open("sz.txt", "w") as f:
                f.write(str(self.zone_index))
                f.write("\n")
                f.write(str(self.page_index))
                f.close()
            return
        self.maxpage -= 1
        yield scrapy.Request(url, callback=self.parse)

