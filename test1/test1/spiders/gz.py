import scrapy

from test1.items import Test1Item  # 从items.py中引入MyItem对象


class LianjiaSpider(scrapy.Spider):
    name = 'gz'
    allowed_domains = ['gz.lianjia.com']
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

    zone_list=["cencun" ,"chebei" ,"changxing1" ,"dongfengdong" ,"dashadi" ,"dongpu" ,"ershadao" ,"gaotang" ,"huajingxincheng" ,"huangpuqufu" ,"huangcun" ,"huijingxincheng" ,"huanshidong" ,"huanghuagang" ,"jinrongcheng1" ,"kexuecheng" ,"linhe" ,"longdong" ,"longkoudong" ,"longkouxi" ,"meihuayuan" ,"shipai1" ,"shuiyin" ,"shataibei" ,"shatainan" ,"shahe1" ,"tianhegongyuan" ,"tangxia1" ,"tianhenan" ,"tiyuzhongxin" ,"tianrunlu" ,"tianhekeyunzhan" ,"wuyangxincheng" ,"wushan" ,"yangji" ,"yuzhu" ,"yuancun" ,"yueken" ,"yantang" ,"zhihuicheng" ,"zhujiangxinchengdong" ,"zhujiangxinchengxi" ,"zhujiangxinchengzhong" ,"beijinglu" ,"dongfengxi" ,"dongfengdong" ,"donghu1" ,"dongchuanlu" ,"dongshankou" ,"ershadao" ,"guihuagang" ,"gongyuanqian" ,"huanshidong" ,"haizhuguangchang" ,"huanghuagang" ,"jichanglu" ,"jiefangbei" ,"jianshelu1" ,"jiefangnan" ,"longjin" ,"lujing" ,"liuhuazhanqian" ,"nongjiangsuo" ,"panfu" ,"renminlu" ,"renminbei1" ,"sanyuanli" ,"shuiyin" ,"shahe1" ,"tongdewei" ,"taojin" ,"wuyangxincheng" ,"xiaobei" ,"ximenkou" ,"xihualu" ,"yangji" ,"yuexiunan" ,"chenjiaci" ,"chajiao" ,"dongfengxi" ,"datansha" ,"donglang" ,"fenshui" ,"fangcun" ,"guanggangxincheng" ,"huangsha" ,"hepingxi" ,"hedong1" ,"huadiwan" ,"jushu" ,"jiaokou1" ,"kengkou" ,"longjin" ,"longxi1" ,"liuhuazhanqian" ,"nananlu" ,"renminlu" ,"renminbei1" ,"sanyuanli" ,"shamian" ,"xiguan" ,"xicun" ,"xichang" ,"ximenkou" ,"xilang" ,"xihualu" ,"zhongshanba1" ,"zhoumen" ,"baogang" ,"binjiangzhong" ,"binjiangxi" ,"binjiangdong" ,"chigang" ,"changgang1" ,"dongxiaonan" ,"dongxiaolu" ,"gongyedadaozhong" ,"gongyedadaonan" ,"gongyedadaobei" ,"guangzhoudadaonan" ,"guanzhou" ,"hongde" ,"huangpucun" ,"huazhou" ,"jiangnandadaozhong" ,"jiangnanxi" ,"jiangyanlu" ,"jinbi" ,"kecun" ,"lijiao" ,"modiesha" ,"nanzhou" ,"pazhouxi" ,"pazhoudong" ,"pazhouzhong" ,"qianjinlu" ,"shayuan" ,"tongfu" ,"wanshengwei" ,"xingangxi" ,"yingzhou1" ,"zhongda" ,"changzhoudao1" ,"dashi" ,"dongyixinqu" ,"daxuecheng" ,"fuhaoshanzhuang" ,"guojichuangxincheng" ,"guangzhounanzhan" ,"guanzhou" ,"hualong" ,"huijiang" ,"hanxichanglong" ,"huananxincheng" ,"huananbiguiyuan" ,"jinshangu" ,"lianhuashan" ,"lanhezhen" ,"luoxi" ,"nancun" ,"nanpu" ,"panyukeyunzhan" ,"panyuguangchang" ,"qiaonan4" ,"qifuxincun" ,"shiqiaobei" ,"shiqiao1" ,"shiqi1" ,"shilou" ,"shiqiaodong" ,"shajiao" ,"shawan1" ,"shundebiguiyuan" ,"wanbo" ,"xinghewan" ,"yayundadaozhong" ,"yajule1" ,"yayuncheng" ,"zhongcun" ,"baiyundadaonan" ,"dongping1" ,"dajinzhonglu" ,"guihuagang" ,"huangbian" ,"huadongzhen" ,"huangshi" ,"jinshazhou" ,"jingtai" ,"jiangxia1" ,"jichanglu" ,"jingxi1" ,"jinghudadao" ,"jiahewanggang" ,"jianggaozhen" ,"luochongwei" ,"longgui" ,"lujing" ,"liangtianzhen" ,"longdong" ,"mawu" ,"meihuayuan" ,"nanhu5" ,"renhe1" ,"shijing" ,"sanyuanli" ,"shenshanzhen" ,"shataibei" ,"shatainan" ,"shahe1" ,"tongdewei" ,"taihe" ,"tonghe1" ,"taipingzhen" ,"tieluxi" ,"tanbu" ,"tianhekeyunzhan" ,"xinshi" ,"xicun" ,"xiamao" ,"yongtai" ,"yuanxiatian" ,"zhishicheng" ,"zhongluotan" ,"aotouzhen" ,"beixingzhen" ,"chicao" ,"hebinbeilu" ,"jiangpujie" ,"jiuchengqu" ,"liangkouzhen" ,"shengangzhen" ,"taipingzhen" ,"wenquanzhen" ,"wangchengpianqu" ,"xinchengpianqu" ,"baijiang" ,"fenghuangcheng" ,"fuhezhen" ,"huangpuyonghe" ,"jiangpujie" ,"kaifadongqu" ,"lichengzhongqu" ,"lichengfupeng" ,"lichengxiqu" ,"lichengzengjiang" ,"nangang1" ,"paitanzhen" ,"shacun" ,"shitanzhen" ,"xintangnan" ,"xiaolouzhen" ,"xintangbei" ,"xiangxue" ,"yongning1" ,"zengchengbiguiyuan" ,"zengchengqufu" ,"zhishicheng" ,"zhucun" ,"zhongxinzhen" ,"zhengguozhen" ,"dagangzhen" ,"dongyong" ,"hengli" ,"huangge" ,"jingangdadao" ,"jinzhou2" ,"lanhezhen" ,"mingzhuwan" ,"nanshaqufu" ,"nanshawan" ,"nanshagang" ,"wanqingsha" ,"yuwotou"]
    # https://bj.lianjia.com/zufang/pg2/
    #为每个zone_list设置最大页数为3
    zone_list_number=[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
    base_url = 'https://gz.lianjia.com/zufang/'


    maxpage = 500

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.download_delay = 1
        with open("gz.txt", "r") as f:
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
            item["name_chinese"] = "广州"
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
            with open("gz.txt", "w") as f:
                f.write(str(self.zone_index))
                f.write("\n")
                f.write(str(self.page_index))
                f.close()
            return
        if self.maxpage%10==0:
            with open("gz.txt", "w") as f:
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
            with open("gz.txt", "w") as f:
                f.write(str(self.zone_index))
                f.write("\n")
                f.write(str(self.page_index))
                f.close()
            return
        self.maxpage -= 1
        yield scrapy.Request(url, callback=self.parse)

