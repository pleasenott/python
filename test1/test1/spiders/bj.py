import scrapy

from test1.items import Test1Item  # 从items.py中引入MyItem对象


class LianjiaSpider(scrapy.Spider):
    name = 'bj'
    allowed_domains = ['bj.lianjia.com']
    zone_list_chinese=["东城","西城","朝阳","海淀","丰台","石景山","通州","昌平","大兴","亦庄开发区","顺义","房山","门头沟","平谷","怀柔","密云","延庆"]

    zone_list=["dongcheng","xicheng","chaoyang","haidian","fengtai","shijingshan","tongzhou","changping","daxing","yizhuangkaifaqu","shunyi","fangshan","mentougou","pinggu","huairou","miyun","yanqing"]
    # https://bj.lianjia.com/zufang/pg2/
    zone_list_number=[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
    base_url = 'https://bj.lianjia.com/zufang/'


    maxpage = 1000000

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.download_delay = 1
        with open("bj.txt", "r") as f:
            temp=f.read().split("\n")
            self.zone_index=int(temp[0])
            self.page_index =int (temp[1])

            self.start_urls = [self.base_url +self.zone_list[self.zone_index]+"/pg"  + str(self.page_index)]
            print(self.zone_index,self.page_index)
            f.close()

    #析构函数

    def parse(self, response, **kwargs):

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
            item["name_chinese"] = "北京"
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
            item["block"]=each.xpath("div/p[2]/a[2]/text()").extract_first()
            print(item["block"])
            # 获取面积
            # item["area"]=each.xpath("/div/p[2]/text()[2]").extract_first()

            # item["house_type"]=each.xpath("/div/p[2]/text()[7]").extract_first()
            # print(item)
            item["zone_name"] = response.xpath("/html/body/div[3]/div[1]/div[3]/h1/a/text()").extract_first().replace("租房","")
            if item['price'] and item['name'] and item['house_type'] and item['area'] and item['direct'] and item["block"]:
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

        for each in response.xpath("//*[@id='filter']/ul[4]/*"):    # 遍历可选的板块
            data_id = each.xpath("@data-id").extract_first()
            if data_id is None or data_id == "0":           # 板块选项的第一个是不限，跳过
                continue
            newblock = each.xpath("a/@href").extract_first()
            newblock=newblock.replace("/zufang/","").replace("/","")
            #print(newblock)
            if newblock not in self.zone_list:
                self.zone_list.append(newblock)
                self.zone_list_number.append(100)
                self.zone_list_chinese.append(each.xpath("a/text()").extract_first())
            # if self.block_visited.count(block_page) != 0:   # 已爬取过该板块，跳过
            #     continue
            # self.block_visited.append(block_page)           # 没有爬取过该板块，标识为已爬取
            # block_page = self.first_half + block_page       # 爬取板块的后半URL，拼接
            # yield scrapy.Request(block_page, callback=self.parse_block, dont_filter=True)
        if self.maxpage <= 0:
            with open("bj.txt", "w") as f:
                f.write(str(self.zone_index))
                f.write("\n")
                f.write(str(self.page_index))
                f.close()
            return
        if response.xpath("//*[@id='content']/div[1]/div[2]/@data-totalpage").extract_first() :
            self.zone_list_number[self.zone_index]=int(response.xpath("//*[@id='content']/div[1]/div[2]/@data-totalpage").extract_first())
            print("self.zone_list_number[self.zone_index]",self.zone_list_number[self.zone_index])
        self.page_index += 1
        if self.zone_index < len(self.zone_list):
            if self.page_index <= self.zone_list_number[self.zone_index]:
                url=self.base_url+self.zone_list[self.zone_index]+"/pg"+str(self.page_index)
            else:
                self.page_index = 1
                url = self.base_url + self.zone_list[self.zone_index]
                self.zone_index += 1
        else:
            with open("bj.txt", "w") as f:
                f.write(str(self.zone_index))
                f.write("\n")
                f.write(str(self.page_index))
                f.close()
            return
        self.maxpage -= 1
        yield scrapy.Request(url, callback=self.parse)

