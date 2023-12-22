import scrapy

from test1.items import Test1Item  # 从items.py中引入MyItem对象


class LianjiaSpider(scrapy.Spider):
    name = 'sh'
    allowed_domains = ['sh.lianjia.com']
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

    zone_list=["beiwaitan","buyecheng","caojiadu","daning","jingansi","jiangninglu","nanjingxilu","pengpu","suhewan","xizangbeilu","yonghe","yangcheng","zhabeigongyuan","changqiao","caohejing","huajing","huadongligong","hengshanlu","jianguoxilu","jinhui","kangjian","longhua","shanghainanzhan","tianlin","wantiguan","xuhuibinjiang","xujiahui","xietulu","zhiwuyuan","dapuqiao","dongjiadu","huangpubinjiang","huaihaizhonglu","laoximen","nanjingdonglu","penglaigongyuan","renminguangchang","shibobinjiang","wuliqiao","xintiandi","yuyuan","beixinjing","gubei","hongqiao1","hanghua","tianshan","xijiao","xinhualu","xianxia","zhenninglu","zhongshangongyuan","changfeng1","changshoulu","caoyang","changzheng","guangxin","ganquanyichuan","taopu","wanli","wuning","zhenguang","zhongyuanliangwancheng","zhenru","beicai","biyun","caolu","chuansha","datuanzhen","geqing","gaohang","gaodong","huamu","hangtou","huinan","jinqiao","jinyang","kangqiao","lujiazui","laogangzhen","lingangxincheng","lianyang","meiyuan1","nichengzhen","nanmatou","sanlin","shibo","shuyuanzhen","tangqiao","tangzhen","waigaoqiao","wanxiangzhen","weifang","xuanqiao","xinchang","yuqiao1","yangsiqiantan","yangdong","yuanshen","yangjing","zhangjiang","zhuqiao","zhoupu","dahua","dachangzhen","gongfu","gongkang","gucun","gaojing","luojing","luodian","songbao","songnan","shangda","tonghe","yuepu","yanghang","zhangmiao","jiangwanzhen","luxungongyuan","liangcheng","linpinglu","quyang","sichuanbeilu","anshan","dongwaitan","huangxinggongyuan","kongjianglu","wujiaochang","xinjiangwancheng","zhoujiazuilu","zhongyuan1","chunshen","gumei","huacao","jinhongqiao","jinganxincheng","longbai","laominhang","minpu","maqiao","meilong","pujiang1","qibao","shenminbieshu","wujing","xinzhuangnanguangchang","xinzhuangbeiguangchang","zhuanqiao","jinshanxincheng","jiaxing","shanghaizhoubian2","anting","fengzhuang","huating","jiadinglaocheng","jiadingxincheng","juyuanxinqu","jiangqiao","malu","nanxiang","taicang212","waigang","xinchenglu1","xuxing","baozhen","changxingdao21211","chenjiazhen","chongmingxincheng","chongmingqita","hengshadao","qidong1","fengxianjinhui","fengcheng","haiwan","nanqiao","qingcun","situan","xidu","zhelin","zhuanghang","chedun","dongjing2","jiuting","maogang","shihudang","songjiangxincheng","sheshan","songjiangdaxuecheng","sijing","songjianglaocheng","xinqiao","xiaokunshan","xinbang","yexie","baihe","chonggu","huaxin","jinze","kunshan1","liantang1","xiayang","xujing","xianghuaqiao","yingpu","zhaoxiang","zhujiajiao"]

    #为每个zone_list设置最大页数为3
    zone_list_number=[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
    base_url = 'https://sh.lianjia.com/zufang/'


    maxpage = 5000

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.download_delay = 1
        with open("sh.txt", "r") as f:
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
            item["name_chinese"] = "上海"
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
            with open("sh.txt", "w") as f:
                f.write(str(self.zone_index))
                f.write("\n")
                f.write(str(self.page_index))
                f.close()
            return
        if self.maxpage%10==0:
            with open("sh.txt", "w") as f:
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
            with open("sh.txt", "w") as f:
                f.write(str(self.zone_index))
                f.write("\n")
                f.write(str(self.page_index))
                f.close()
            return
        self.maxpage -= 1
        yield scrapy.Request(url, callback=self.parse)

