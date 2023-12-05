import scrapy

from test1.items import Test1Item #从items.py中引入MyItem对象

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['bj.lianjia.com']
    base_url = 'https://bj.lianjia.com/ershoufang/'
    zones = ['dongcheng/', 'xicheng/', 'chaoyang/', 'haidian/']
    zones_chinese = ['东城', '西城', '朝阳', '海淀']
    page_index = 1  # 页面计数
    zone_index = 1  # 地区计数
    start_urls = [base_url + zones[0]]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.download_delay = 5

    def parse(self, response, **kwargs):
        item = Test1Item()

        info_list = response.xpath('//div[@class="info clear"]')
        for info in info_list:
            # item['zone_name'] = self.zones_chinese[self.zone_index - 1]
            # item['building_names'] = info.xpath('./div[@class="flood"]/div[@class="positionInfo"]/a[1]/text()').get()+"-"+info.xpath('./div[@class="flood"]/div[@class="positionInfo"]/a[1]/text()').get()
            # # print(item['building_names'])
            # # item['total_price'] = ''.join(info.xpath(
            # #     './div[@class="priceInfo"]/div[@class="totalPrice totalPrice2"]/span/text()').getall() + info.xpath(
            # #     './div[@class="priceInfo"]/div[@class="totalPrice totalPrice2"]/text()').getall())
            #
            # # print(item['total_price'])
            # item['area'] = info.xpath(
            #     './div[@class="address"]/div[@class="houseInfo"]/text()').get().split('|')[1].strip()
            # item["houseInfo"]=info.xpath('./div[@class="address"]/div[@class="houseInfo"]/text()').get()
            # item["followInfo"]=info.xpath('./div[@class="followInfo"]/text()').get()
            # item["positionInfo"]=info.xpath('./div[@class="flood"]/div[@class="positionInfo"]/a[2]/text()').get()
            #
            #
            # # print(item['area'])
            # item['unitPrice'] = info.xpath(
            #     './div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()').get()
            # item['totalPrice_totalPrice2']= info.xpath(
            #     './div[@class="priceInfo"]/div[@class="totalPrice totalPrice2"]/span/text()').get()
            # # print(item['price_per_area'])

            item['zone_name'] = self.zones_chinese[self.zone_index - 1]
            item['building_names'] = info.xpath('./div[@class="flood"]/div[@class="positionInfo"]/a[1]/text()').get()
            # print(item['building_names'])
            item['total_price'] = ''.join(info.xpath(
                './div[@class="priceInfo"]/div[@class="totalPrice totalPrice2"]/span/text()').getall() + info.xpath(
                './div[@class="priceInfo"]/div[@class="totalPrice totalPrice2"]/text()').getall())
            # print(item['total_price'])
            item['area'] = info.xpath(
                './div[@class="address"]/div[@class="houseInfo"]/text()').get().split('|')[1].strip()
            # print(item['area'])
            item['price_per_area'] = info.xpath(
                './div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()').get()
            # print(item['price_per_area'])
            item['houseInfo']=info.xpath('./div[@class="address"]/div[@class="houseInfo"]/text()').get()

            if item['building_names'] and item['total_price'] and item['area'] and item['price_per_area']:
                yield item

        self.page_index += 1
        if self.zone_index < len(self.zones):
            if self.page_index <= 5:
                url = self.base_url + self.zones[self.zone_index] + 'pg' + str(self.page_index)
            else:
                self.page_index = 1
                url = self.base_url + self.zones[self.zone_index]
                self.zone_index += 1
        else:
            return
        yield scrapy.Request(url, callback=self.parse)


"""
</script>
<ul class="sellListContent" log-mod="list">
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="0" data-lj_action_fb_expo_id='782020333212327936'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027377435"
        data-lj_action_housedel_id="101121958292"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121958292.html" target="_blank" data-log_index="1"
            data-el="ershoufang" data-housecode="101121958292" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/c63a695d-a564-4247-a08a-4a0a1ac2d2ec_1000.jpg.296x216.jpg"
                alt="北京东城地安门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121958292.html" target="_blank"
                    data-log_index="1" data-el="ershoufang" data-housecode="101121958292" data-is_focus=""
                    data-sl="">安定门京香福苑南北通带车位有钥匙</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027377435/" target="_blank" data-log_index="1"
                        data-el="region">京香福苑 </a> - <a href="https://bj.lianjia.com/ershoufang/dianmen/"
                        target="_blank">地安门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>3室1厅 | 119.76平米 | 西 南 北 | 精装 | 中楼层(共6层) | 板楼</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>11人关注 / 11天以前发布</div>
            <div class="tag"><span class="vr">VR房源</span><span class="taxfree">房本满五年</span><span
                    class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">1580</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121958292" data-rid="1111027377435" data-price="131931">
                    <span>131,931元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121958292"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121958292" log-mod="101121958292" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="1" data-lj_action_fb_expo_id='782020333212327937'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027380567"
        data-lj_action_housedel_id="101122011479"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101122011479.html" target="_blank" data-log_index="2"
            data-el="ershoufang" data-housecode="101122011479" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrgold.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/pc1_azcMfWfIK_1.jpg.296x216.jpg"
                alt="北京东城永定门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101122011479.html" target="_blank"
                    data-log_index="2" data-el="ershoufang" data-housecode="101122011479" data-is_focus=""
                    data-sl="">新奥洋房 近地铁 满五唯一东西通透两居</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027380567/" target="_blank" data-log_index="2"
                        data-el="region">新奥洋房 </a> - <a href="https://bj.lianjia.com/ershoufang/yongdingmen/"
                        target="_blank">永定门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>2室2厅 | 92.08平米 | 东 西 北 | 精装 | 6层 | 板塔结合</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>3人关注 / 5天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="isVrFutureHome">VR看装修</span><span
                    class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">828</span><i>万</i></div>
                <div class="unitPrice" data-hid="101122011479" data-rid="1111027380567" data-price="89922">
                    <span>89,922元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101122011479"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101122011479" log-mod="101122011479" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="2" data-lj_action_fb_expo_id='782020333212327938'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027375475"
        data-lj_action_housedel_id="101122021175"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101122021175.html" target="_blank" data-log_index="3"
            data-el="ershoufang" data-housecode="101122021175" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/44afd754-1d24-43a9-87d4-a5da44d22c2c_1000.jpg.296x216.jpg"
                alt="北京东城东直门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101122021175.html" target="_blank"
                    data-log_index="3" data-el="ershoufang" data-housecode="101122021175" data-is_focus=""
                    data-sl="">央产房南北三居带客厅 采光充足 交通便利 随时看</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027375475/" target="_blank" data-log_index="3"
                        data-el="region">后永康胡同2号院4号院 </a> - <a href="https://bj.lianjia.com/ershoufang/dongzhimen/"
                        target="_blank">东直门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>3室1厅 | 72.03平米 | 南 北 | 精装 | 高楼层(共6层) | 板楼</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>13人关注 / 6天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span
                    class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">680</span><i>万</i></div>
                <div class="unitPrice" data-hid="101122021175" data-rid="1111027375475" data-price="94406">
                    <span>94,406元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101122021175"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101122021175" log-mod="101122021175" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="3" data-lj_action_fb_expo_id='782020333212327939'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027382286"
        data-lj_action_housedel_id="101121784981"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121784981.html" target="_blank" data-log_index="4"
            data-el="ershoufang" data-housecode="101121784981" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/7fb2a2f3-68ab-463f-9b9d-38ec19cac2db_1000.jpg.296x216.jpg"
                alt="北京东城左安门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121784981.html" target="_blank"
                    data-log_index="4" data-el="ershoufang" data-housecode="101121784981" data-is_focus=""
                    data-sl="">左安漪园2005年商品房社区，满五年唯一的南北通透</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027382286/" target="_blank" data-log_index="4"
                        data-el="region">左安漪园 </a> - <a href="https://bj.lianjia.com/ershoufang/zuoanmen1/"
                        target="_blank">左安门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>3室1厅 | 133.04平米 | 南 北 | 简装 | 中楼层(共10层) | 板塔结合
                </div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>18人关注 / 23天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span
                    class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">1400</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121784981" data-rid="1111027382286" data-price="105232">
                    <span>105,232元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121784981"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121784981" log-mod="101121784981" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="4" data-lj_action_fb_expo_id='782020333212327940'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027378107"
        data-lj_action_housedel_id="101121831488"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121831488.html" target="_blank" data-log_index="5"
            data-el="ershoufang" data-housecode="101121831488" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/2af37cd7-94e7-404f-ae85-f79a137b4d27_1000.jpg.296x216.jpg"
                alt="北京东城左安门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121831488.html" target="_blank"
                    data-log_index="5" data-el="ershoufang" data-housecode="101121831488" data-is_focus=""
                    data-sl="">龙潭西里-中间楼层-临湖-满五唯一-精装修</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027378107/" target="_blank" data-log_index="5"
                        data-el="region">龙潭西里 </a> - <a href="https://bj.lianjia.com/ershoufang/zuoanmen1/"
                        target="_blank">左安门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>1室1厅 | 46.98平米 | 东 西 | 精装 | 6层 | 2000年 | 板楼</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>11人关注 / 21天以前发布</div>
            <div class="tag"><span class="vr">VR房源</span><span class="taxfree">房本满五年</span><span
                    class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">495</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121831488" data-rid="1111027378107" data-price="105364">
                    <span>105,364元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121831488"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121831488" log-mod="101121831488" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="5" data-lj_action_fb_expo_id='782020333212327941'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027375663"
        data-lj_action_housedel_id="101121967820"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121967820.html" target="_blank" data-log_index="6"
            data-el="ershoufang" data-housecode="101121967820" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/6de7fbfb-8fea-4b18-8156-7eaf65c88b34_1000.jpg.296x216.jpg"
                alt="北京东城和平里"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121967820.html" target="_blank"
                    data-log_index="6" data-el="ershoufang" data-housecode="101121967820" data-is_focus=""
                    data-sl="">南北通透四居室 明厨明卫 满五年唯一</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027375663/" target="_blank" data-log_index="6"
                        data-el="region">安外花园 </a> - <a href="https://bj.lianjia.com/ershoufang/hepingli/"
                        target="_blank">和平里</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>4室1厅 | 88.67平米 | 南 北 | 简装 | 底层(共5层) | 板楼</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>13人关注 / 11天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span
                    class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">1110</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121967820" data-rid="1111027375663" data-price="125184">
                    <span>125,184元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121967820"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121967820" log-mod="101121967820" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="6" data-lj_action_fb_expo_id='782020333212327942'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027377501"
        data-lj_action_housedel_id="101121947378"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121947378.html" target="_blank" data-log_index="7"
            data-el="ershoufang" data-housecode="101121947378" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/9af3ad18-b3ad-42e9-931d-576ad3cc2f69_1000.jpg.296x216.jpg"
                alt="北京东城天坛"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121947378.html" target="_blank"
                    data-log_index="7" data-el="ershoufang" data-housecode="101121947378" data-is_focus=""
                    data-sl="">东城区二环内 天坛北门 桥湾地铁站 金鱼池西区南北2居</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027377501/" target="_blank" data-log_index="7"
                        data-el="region">金鱼池西区 </a> - <a href="https://bj.lianjia.com/ershoufang/tiantan/"
                        target="_blank">天坛</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>2室1厅 | 61.85平米 | 南 北 | 精装 | 中楼层(共5层) | 2002年 | 板楼
                </div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>13人关注 / 12天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span
                    class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">620</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121947378" data-rid="1111027377501" data-price="100243">
                    <span>100,243元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121947378"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121947378" log-mod="101121947378" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="7" data-lj_action_fb_expo_id='782020333212327943'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027374078"
        data-lj_action_housedel_id="101122056807"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101122056807.html" target="_blank" data-log_index="8"
            data-el="ershoufang" data-housecode="101122056807" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrgold.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/758fee5f-e244-45cb-9e57-07afcb365dad_1000.jpg.296x216.jpg"
                alt="北京东城东直门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101122056807.html" target="_blank"
                    data-log_index="8" data-el="ershoufang" data-housecode="101122056807" data-is_focus=""
                    data-sl="">北小街8号院 高楼层 南北三居 无遮挡 精装修</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027374078/" target="_blank" data-log_index="8"
                        data-el="region">东直门内北小街8号院 </a> - <a href="https://bj.lianjia.com/ershoufang/dongzhimen/"
                        target="_blank">东直门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>3室1厅 | 90.76平米 | 南 北 | 精装 | 中楼层(共13层) | 板塔结合</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>16人关注 / 4天以前发布</div>
            <div class="tag"><span class="isVrFutureHome">VR看装修</span><span class="five">房本满两年</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">910</span><i>万</i></div>
                <div class="unitPrice" data-hid="101122056807" data-rid="1111027374078" data-price="100265">
                    <span>100,265元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101122056807"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101122056807" log-mod="101122056807" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="8" data-lj_action_fb_expo_id='782020333212327944'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027376748"
        data-lj_action_housedel_id="101122031981"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101122031981.html" target="_blank" data-log_index="9"
            data-el="ershoufang" data-housecode="101122031981" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/0240fe62-3ae5-431b-856f-da36b3fc043e_1000.jpg.296x216.jpg"
                alt="北京东城朝阳门内"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101122031981.html" target="_blank"
                    data-log_index="9" data-el="ershoufang" data-housecode="101122031981" data-is_focus=""
                    data-sl="">豆瓣胡同 精装修两居 商品房满五年唯一住房 采光好</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027376748/" target="_blank" data-log_index="9"
                        data-el="region">豆瓣胡同 </a> - <a href="https://bj.lianjia.com/ershoufang/chaoyangmennei1/"
                        target="_blank">朝阳门内</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>2室1厅 | 71.64平米 | 西南 | 精装 | 中楼层(共11层) | 2003年 |
                    板塔结合</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>10人关注 / 6天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span
                    class="taxfree">房本满五年</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">878</span><i>万</i></div>
                <div class="unitPrice" data-hid="101122031981" data-rid="1111027376748" data-price="122558">
                    <span>122,558元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101122031981"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101122031981" log-mod="101122031981" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="9" data-lj_action_fb_expo_id='782020333212327945'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027374239"
        data-lj_action_housedel_id="101121798951"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121798951.html" target="_blank" data-log_index="10"
            data-el="ershoufang" data-housecode="101121798951" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrgold.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/pc1_bFHEpRkSp_1.jpg.296x216.jpg"
                alt="北京东城崇文门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121798951.html" target="_blank"
                    data-log_index="10" data-el="ershoufang" data-housecode="101121798951" data-is_focus=""
                    data-sl="">法华南里 南北通透精装两居 采光好诚心出售</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027374239/" target="_blank" data-log_index="10"
                        data-el="region">法华南里 </a> - <a href="https://bj.lianjia.com/ershoufang/chongwenmen/"
                        target="_blank">崇文门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>2室2厅 | 81.68平米 | 南 北 | 精装 | 高楼层(共6层) | 1995年 | 板楼
                </div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>17人关注 / 23天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="isVrFutureHome">VR看装修</span><span
                    class="five">房本满两年</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">799</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121798951" data-rid="1111027374239" data-price="97821">
                    <span>97,821元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121798951"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121798951" log-mod="101121798951" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="10" data-lj_action_fb_expo_id='782020333212327946'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027375114"
        data-lj_action_housedel_id="101121647575"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121647575.html" target="_blank" data-log_index="11"
            data-el="ershoufang" data-housecode="101121647575" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrgold.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/edc7bc1e-0235-416d-80d2-ddd7ca510917_1000.jpg.296x216.jpg"
                alt="北京东城东直门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121647575.html" target="_blank"
                    data-log_index="11" data-el="ershoufang" data-housecode="101121647575" data-is_focus=""
                    data-sl="">东直门外 胡家园 西南朝向2居室 满五年唯一</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027375114/" target="_blank" data-log_index="11"
                        data-el="region">胡家园小区 </a> - <a href="https://bj.lianjia.com/ershoufang/dongzhimen/"
                        target="_blank">东直门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>2室1厅 | 83.36平米 | 西南 | 精装 | 中楼层(共10层) | 2000年 |
                    板塔结合</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>12人关注 / 1个月以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="isVrFutureHome">VR看装修</span><span
                    class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">920</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121647575" data-rid="1111027375114" data-price="110365">
                    <span>110,365元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121647575"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121647575" log-mod="101121647575" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="11" data-lj_action_fb_expo_id='782020333212327947'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027374680"
        data-lj_action_housedel_id="101121692049"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121692049.html" target="_blank" data-log_index="12"
            data-el="ershoufang" data-housecode="101121692049" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrgold.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/pc1_dMQBTrtRV_1.jpg.296x216.jpg"
                alt="北京东城广渠门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121692049.html" target="_blank"
                    data-log_index="12" data-el="ershoufang" data-housecode="101121692049" data-is_focus=""
                    data-sl="">东城区 东二环 商品房本 满五唯一 有地铁 诚心出售</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027374680/" target="_blank" data-log_index="12"
                        data-el="region">广渠家园 </a> - <a href="https://bj.lianjia.com/ershoufang/guangqumen/"
                        target="_blank">广渠门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>2室2厅 | 71.43平米 | 东 | 精装 | 高楼层(共29层) | 2009年 | 板塔结合
                </div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>16人关注 / 26天以前发布</div>
            <div class="tag"><span class="isVrFutureHome">VR看装修</span><span class="taxfree">房本满五年</span><span
                    class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">690</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121692049" data-rid="1111027374680" data-price="96599">
                    <span>96,599元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121692049"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121692049" log-mod="101121692049" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="12" data-lj_action_fb_expo_id='782020333212327948'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027382345"
        data-lj_action_housedel_id="101121755008"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121755008.html" target="_blank" data-log_index="13"
            data-el="ershoufang" data-housecode="101121755008" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/pc1_Trqr8RIJC.jpg.296x216.jpg"
                alt="北京东城东直门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121755008.html" target="_blank"
                    data-log_index="13" data-el="ershoufang" data-housecode="101121755008" data-is_focus=""
                    data-sl="">正东国际大厦七十年产权，东城区房本</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027382345/" target="_blank" data-log_index="13"
                        data-el="region">正东国际大厦 </a> - <a href="https://bj.lianjia.com/ershoufang/dongzhimen/"
                        target="_blank">东直门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>1室1厅 | 146.93平米 | 东 | 简装 | 中楼层(共10层) | 2004年 | 塔楼
                </div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>12人关注 / 24天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span
                    class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">458</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121755008" data-rid="1111027382345" data-price="31172">
                    <span>31,172元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121755008"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121755008" log-mod="101121755008" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="13" data-lj_action_fb_expo_id='782020333212327949'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027376862"
        data-lj_action_housedel_id="101121819811"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121819811.html" target="_blank" data-log_index="14"
            data-el="ershoufang" data-housecode="101121819811" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/pc1_ukUv2chHs_2.jpg.296x216.jpg"
                alt="北京东城东直门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121819811.html" target="_blank"
                    data-log_index="14" data-el="ershoufang" data-housecode="101121819811" data-is_focus=""
                    data-sl="">东城 东直门东方银座 一居室 户型方正</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027376862/" target="_blank" data-log_index="14"
                        data-el="region">东方银座 </a> - <a href="https://bj.lianjia.com/ershoufang/dongzhimen/"
                        target="_blank">东直门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>1室1厅 | 77.74平米 | 东 | 简装 | 高楼层(共26层) | 2003年 | 塔楼
                </div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>2人关注 / 8天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span
                    class="five">房本满两年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">639</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121819811" data-rid="1111027376862" data-price="82198">
                    <span>82,198元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121819811"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121819811" log-mod="101121819811" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="14" data-lj_action_fb_expo_id='782020333212327950'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027374965"
        data-lj_action_housedel_id="101121731683"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121731683.html" target="_blank" data-log_index="15"
            data-el="ershoufang" data-housecode="101121731683" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/64b6799a-b53f-4d61-88fa-a28f85de4239_1000.jpg.296x216.jpg"
                alt="北京东城金宝街"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121731683.html" target="_blank"
                    data-log_index="15" data-el="ershoufang" data-housecode="101121731683" data-is_focus=""
                    data-sl="">禾风相府 花园式小区 人车分流</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027374965/" target="_blank" data-log_index="15"
                        data-el="region">禾风相府 </a> - <a href="https://bj.lianjia.com/ershoufang/jinbaojie/"
                        target="_blank">金宝街</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>2室1厅 | 96.26平米 | 东 | 精装 | 低楼层(共14层) | 2004年 | 板楼
                </div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>5人关注 / 27天以前发布</div>
            <div class="tag"><span class="vr">VR房源</span><span class="taxfree">房本满五年</span><span
                    class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">1250</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121731683" data-rid="1111027374965" data-price="129857">
                    <span>129,857元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121731683"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121731683" log-mod="101121731683" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="15" data-lj_action_fb_expo_id='782020333212327951'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027378448"
        data-lj_action_housedel_id="101121859654"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121859654.html" target="_blank" data-log_index="16"
            data-el="ershoufang" data-housecode="101121859654" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrgold.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/4f21fe40-b87e-43e5-ba94-be0122042621_1000.jpg.296x216.jpg"
                alt="北京东城东单"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121859654.html" target="_blank"
                    data-log_index="16" data-el="ershoufang" data-housecode="101121859654" data-is_focus=""
                    data-sl="">煤渣胡同小区 灯市口 南北通透</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027378448/" target="_blank" data-log_index="16"
                        data-el="region">煤渣胡同 </a> - <a href="https://bj.lianjia.com/ershoufang/dongdan/"
                        target="_blank">东单</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>1室1厅 | 52.7平米 | 南 北 | 简装 | 低楼层(共9层) | 板塔结合</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>14人关注 / 19天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="isVrFutureHome">VR看装修</span><span
                    class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">590</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121859654" data-rid="1111027378448" data-price="111955">
                    <span>111,955元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121859654"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121859654" log-mod="101121859654" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="16" data-lj_action_fb_expo_id='782020333212327952'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027382662"
        data-lj_action_housedel_id="101121836522"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121836522.html" target="_blank" data-log_index="17"
            data-el="ershoufang" data-housecode="101121836522" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrgold.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/4ce04429-c1ff-4510-b5de-6d2fb28243ef_1000.jpg.296x216.jpg"
                alt="北京东城安定门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121836522.html" target="_blank"
                    data-log_index="17" data-el="ershoufang" data-housecode="101121836522" data-is_focus=""
                    data-sl="">中绦胡同甲2号院 正规两居 中间楼层 采光好</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027382662/" target="_blank" data-log_index="17"
                        data-el="region">中绦胡同甲2号院 </a> - <a href="https://bj.lianjia.com/ershoufang/andingmen/"
                        target="_blank">安定门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>2室1厅 | 59.15平米 | 南 北 | 精装 | 中楼层(共6层) | 板楼</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>5人关注 / 21天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="isVrFutureHome">VR看装修</span><span
                    class="five">房本满两年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">750</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121836522" data-rid="1111027382662" data-price="126797">
                    <span>126,797元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121836522"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121836522" log-mod="101121836522" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="17" data-lj_action_fb_expo_id='782020333212327953'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027378417"
        data-lj_action_housedel_id="101121858398"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121858398.html" target="_blank" data-log_index="18"
            data-el="ershoufang" data-housecode="101121858398" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrgold.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/64dcbbf3-9387-4a6b-87d9-ab326fc50845_1000.jpg.296x216.jpg"
                alt="北京东城和平里"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121858398.html" target="_blank"
                    data-log_index="18" data-el="ershoufang" data-housecode="101121858398" data-is_focus=""
                    data-sl="">航空部大院 民旺园明厨明卫客厅带窗两居室 业主诚售</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027378417/" target="_blank" data-log_index="18"
                        data-el="region">民旺园 </a> - <a href="https://bj.lianjia.com/ershoufang/hepingli/"
                        target="_blank">和平里</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>2室1厅 | 60.05平米 | 东 西 | 简装 | 中楼层(共6层) | 板楼</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>7人关注 / 13天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="isVrFutureHome">VR看装修</span><span
                    class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">730</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121858398" data-rid="1111027378417" data-price="121566">
                    <span>121,566元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121858398"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121858398" log-mod="101121858398" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="18" data-lj_action_fb_expo_id='782020333212327954'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027376532"
        data-lj_action_housedel_id="101121719972"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121719972.html" target="_blank" data-log_index="19"
            data-el="ershoufang" data-housecode="101121719972" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/pc1_0l9k27Ygi_1.jpg.296x216.jpg"
                alt="北京东城左安门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121719972.html" target="_blank"
                    data-log_index="19" data-el="ershoufang" data-housecode="101121719972" data-is_focus=""
                    data-sl="">1995年东城区二环内龙体单价7万小三居中间楼层精装</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027376532/" target="_blank" data-log_index="19"
                        data-el="region">长青园 </a> - <a href="https://bj.lianjia.com/ershoufang/zuoanmen1/"
                        target="_blank">左安门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>2室1厅 | 64.24平米 | 南 北 | 精装 | 高楼层(共6层) | 1995年 | 板楼
                </div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>13人关注 / 29天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span
                    class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">459</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121719972" data-rid="1111027376532" data-price="71451">
                    <span>71,451元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121719972"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121719972" log-mod="101121719972" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="19" data-lj_action_fb_expo_id='782020333212327955'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027374081"
        data-lj_action_housedel_id="101121827336"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121827336.html" target="_blank" data-log_index="20"
            data-el="ershoufang" data-housecode="101121827336" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/cd137945-7ba9-405f-9151-ac3160bf50f5_1000.jpg.296x216.jpg"
                alt="北京东城东直门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121827336.html" target="_blank"
                    data-log_index="20" data-el="ershoufang" data-housecode="101121827336" data-is_focus=""
                    data-sl="">东直门南大街满五唯一高层电梯直达南向三居室诚意出售</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027374081/" target="_blank" data-log_index="20"
                        data-el="region">东直门南大街 </a> - <a href="https://bj.lianjia.com/ershoufang/dongzhimen/"
                        target="_blank">东直门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>3室1厅 | 89.39平米 | 西南 | 精装 | 高楼层(共18层) | 板塔结合</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>12人关注 / 21天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span
                    class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">836</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121827336" data-rid="1111027374081" data-price="93523">
                    <span>93,523元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121827336"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121827336" log-mod="101121827336" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="20" data-lj_action_fb_expo_id='782020333212327956'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027382048"
        data-lj_action_housedel_id="101121873126"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121873126.html" target="_blank" data-log_index="21"
            data-el="ershoufang" data-housecode="101121873126" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrgold.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/pc1_GJFXJ1Glk.jpg.296x216.jpg"
                alt="北京东城东直门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121873126.html" target="_blank"
                    data-log_index="21" data-el="ershoufang" data-housecode="101121873126" data-is_focus=""
                    data-sl="">此房格局方正，南北通透户型方正，双朝南阳台不算面积</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027382048/" target="_blank" data-log_index="21"
                        data-el="region">育树四条 </a> - <a href="https://bj.lianjia.com/ershoufang/dongzhimen/"
                        target="_blank">东直门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>3室1厅 | 77.54平米 | 南 北 | 简装 | 底层(共6层) | 板楼</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>15人关注 / 18天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="isVrFutureHome">VR看装修</span><span
                    class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">730</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121873126" data-rid="1111027382048" data-price="94145">
                    <span>94,145元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121873126"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121873126" log-mod="101121873126" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="21" data-lj_action_fb_expo_id='782020333212327957'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027375202"
        data-lj_action_housedel_id="101120210801"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101120210801.html" target="_blank" data-log_index="22"
            data-el="ershoufang" data-housecode="101120210801" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrgold.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/3b832f35-d367-4d36-b1f3-775b513bfbdc_1000.jpg.296x216.jpg"
                alt="北京东城和平里"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101120210801.html" target="_blank"
                    data-log_index="22" data-el="ershoufang" data-housecode="101120210801" data-is_focus=""
                    data-sl="">和平里六区3居室 小区品质高 楼层高 视眼好 采光好</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027375202/" target="_blank" data-log_index="22"
                        data-el="region">和平里六区 </a> - <a href="https://bj.lianjia.com/ershoufang/hepingli/"
                        target="_blank">和平里</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>3室1厅 | 121.73平米 | 东 南 北 | 简装 | 高楼层(共17层) | 塔楼
                </div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>34人关注 / 4个月以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="isVrFutureHome">VR看装修</span><span
                    class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">1399</span><i>万</i></div>
                <div class="unitPrice" data-hid="101120210801" data-rid="1111027375202" data-price="114927">
                    <span>114,927元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101120210801"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101120210801" log-mod="101120210801" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="22" data-lj_action_fb_expo_id='782020333212327958'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111043316752"
        data-lj_action_housedel_id="101118571918"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101118571918.html" target="_blank" data-log_index="23"
            data-el="ershoufang" data-housecode="101118571918" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrgold.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/aaf94a98-5a72-4367-93f0-08372cd75f25_1000.jpg.296x216.jpg"
                alt="北京东城东花市"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101118571918.html" target="_blank"
                    data-log_index="23" data-el="ershoufang" data-housecode="101118571918" data-is_focus=""
                    data-sl="">花市枣苑 南北通透大三居 前后花园 诚心卖</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111043316752/" target="_blank" data-log_index="23"
                        data-el="region">花市枣苑三期 </a> - <a href="https://bj.lianjia.com/ershoufang/donghuashi/"
                        target="_blank">东花市</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>3室1厅 | 140.33平米 | 南 北 | 精装 | 低楼层(共18层) | 2005年 |
                    塔楼</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>55人关注 / 7个月以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="isVrFutureHome">VR看装修</span><span
                    class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">1728</span><i>万</i></div>
                <div class="unitPrice" data-hid="101118571918" data-rid="1111043316752" data-price="123139">
                    <span>123,139元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101118571918"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101118571918" log-mod="101118571918" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="23" data-lj_action_fb_expo_id='782020333212327959'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111043316752"
        data-lj_action_housedel_id="101116660228"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101116660228.html" target="_blank" data-log_index="24"
            data-el="ershoufang" data-housecode="101116660228" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrgold.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/76ef3c6d-f232-4983-94a4-4c21ea67750b_1000.jpg.296x216.jpg"
                alt="北京东城东花市"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101116660228.html" target="_blank"
                    data-log_index="24" data-el="ershoufang" data-housecode="101116660228" data-is_focus=""
                    data-sl="">花市枣苑三期 东向 双卫两居 采光好</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111043316752/" target="_blank" data-log_index="24"
                        data-el="region">花市枣苑三期 </a> - <a href="https://bj.lianjia.com/ershoufang/donghuashi/"
                        target="_blank">东花市</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>2室2厅 | 113.23平米 | 东 南 | 精装 | 低楼层(共18层) | 2005年 |
                    塔楼</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>36人关注 / 一年前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="isVrFutureHome">VR看装修</span><span
                    class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">1260</span><i>万</i></div>
                <div class="unitPrice" data-hid="101116660228" data-rid="1111043316752" data-price="111278">
                    <span>111,278元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101116660228"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101116660228" log-mod="101116660228" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="24" data-lj_action_fb_expo_id='782020333212327960'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027374300"
        data-lj_action_housedel_id="101119840856"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101119840856.html" target="_blank" data-log_index="25"
            data-el="ershoufang" data-housecode="101119840856" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrgold.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/pc1_3WsMZkHeW_2.jpg.296x216.jpg"
                alt="北京东城永定门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101119840856.html" target="_blank"
                    data-log_index="25" data-el="ershoufang" data-housecode="101119840856" data-is_focus=""
                    data-sl="">富莱茵花园 正规大三居 中间楼层采光好</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027374300/" target="_blank" data-log_index="25"
                        data-el="region">富莱茵花园 </a> - <a href="https://bj.lianjia.com/ershoufang/yongdingmen/"
                        target="_blank">永定门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>3室1厅 | 148.63平米 | 西南 | 精装 | 中楼层(共21层) | 2001年 | 塔楼
                </div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>105人关注 / 5个月以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="isVrFutureHome">VR看装修</span><span
                    class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">930</span><i>万</i></div>
                <div class="unitPrice" data-hid="101119840856" data-rid="1111027374300" data-price="62572">
                    <span>62,572元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101119840856"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101119840856" log-mod="101119840856" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="25" data-lj_action_fb_expo_id='782020333212327961'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027379254"
        data-lj_action_housedel_id="101120330660"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101120330660.html" target="_blank" data-log_index="26"
            data-el="ershoufang" data-housecode="101120330660" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrgold.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/58f869f6-fe19-4f0d-a72d-b90de99eae9c_1000.jpg.296x216.jpg"
                alt="北京东城安贞"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101120330660.html" target="_blank"
                    data-log_index="26" data-el="ershoufang" data-housecode="101120330660" data-is_focus=""
                    data-sl="">东城和平里区域 精装修大三居 层高2.7米</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027379254/" target="_blank" data-log_index="26"
                        data-el="region">胜古中路1号院 </a> - <a href="https://bj.lianjia.com/ershoufang/anzhen1/"
                        target="_blank">安贞</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>3室2厅 | 148.9平米 | 东 西 | 精装 | 中楼层(共14层) | 板楼</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>49人关注 / 3个月以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="isVrFutureHome">VR看装修</span><span
                    class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">1060</span><i>万</i></div>
                <div class="unitPrice" data-hid="101120330660" data-rid="1111027379254" data-price="71189">
                    <span>71,189元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101120330660"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101120330660" log-mod="101120330660" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="26" data-lj_action_fb_expo_id='782020333212327962'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027378868"
        data-lj_action_housedel_id="101121878626"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121878626.html" target="_blank" data-log_index="27"
            data-el="ershoufang" data-housecode="101121878626" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrgold.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/pc1_dJhltYLDL.jpg.296x216.jpg"
                alt="北京东城前门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121878626.html" target="_blank"
                    data-log_index="27" data-el="ershoufang" data-housecode="101121878626" data-is_focus=""
                    data-sl="">前门东大街 诚意出售 电梯直达 东北向大2居</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027378868/" target="_blank" data-log_index="27"
                        data-el="region">前门东大街 </a> - <a href="https://bj.lianjia.com/ershoufang/qianmen/"
                        target="_blank">前门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>2室1厅 | 59.19平米 | 东 北 | 简装 | 低楼层(共16层) | 板楼</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>11人关注 / 11天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="isVrFutureHome">VR看装修</span><span
                    class="five">房本满两年</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">510</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121878626" data-rid="1111027378868" data-price="86164">
                    <span>86,164元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121878626"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121878626" log-mod="101121878626" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="27" data-lj_action_fb_expo_id='782020333212327963'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027374239"
        data-lj_action_housedel_id="101121963214"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121963214.html" target="_blank" data-log_index="28"
            data-el="ershoufang" data-housecode="101121963214" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrgold.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/pc1_gqOm1aDx8_1.jpg.296x216.jpg"
                alt="北京东城崇文门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121963214.html" target="_blank"
                    data-log_index="28" data-el="ershoufang" data-housecode="101121963214" data-is_focus=""
                    data-sl="">法华南里 485万的三层一居室 94年楼 不临街</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027374239/" target="_blank" data-log_index="28"
                        data-el="region">法华南里 </a> - <a href="https://bj.lianjia.com/ershoufang/chongwenmen/"
                        target="_blank">崇文门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>1室1厅 | 47.56平米 | 西 | 简装 | 中楼层(共6层) | 1994年 | 板楼
                </div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>2人关注 / 11天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="isVrFutureHome">VR看装修</span><span
                    class="five">房本满两年</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">485</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121963214" data-rid="1111027374239" data-price="101977">
                    <span>101,977元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121963214"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121963214" log-mod="101121963214" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="28" data-lj_action_fb_expo_id='782020333212327964'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027376532"
        data-lj_action_housedel_id="101121926322"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121926322.html" target="_blank" data-log_index="29"
            data-el="ershoufang" data-housecode="101121926322" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrgold.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/25b276da-d340-4a22-9c04-01c9d0893765_1000.jpg.296x216.jpg"
                alt="北京东城左安门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121926322.html" target="_blank"
                    data-log_index="29" data-el="ershoufang" data-housecode="101121926322" data-is_focus=""
                    data-sl="">东城二环内 龙潭西湖边 长青园 南北两居室</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027376532/" target="_blank" data-log_index="29"
                        data-el="region">长青园 </a> - <a href="https://bj.lianjia.com/ershoufang/zuoanmen1/"
                        target="_blank">左安门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>2室1厅 | 57.99平米 | 南 北 | 简装 | 中楼层(共5层) | 塔楼</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>64人关注 / 13天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="isVrFutureHome">VR看装修</span><span
                    class="taxfree">房本满五年</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">455</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121926322" data-rid="1111027376532" data-price="78462">
                    <span>78,462元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121926322"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121926322" log-mod="101121926322" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
    <li class="clear LOGVIEWDATA LOGCLICKDATA" data-lj_view_evtid="21625" data-lj_evtid="21624"
        data-lj_view_event="ItemExpo" data-lj_click_event="SearchClick" data-lj_action_source_type="链家_PC_二手列表页卡片"
        data-lj_action_click_position="29" data-lj_action_fb_expo_id='782020333212327965'
        data-lj_action_fb_query_id='782020333019389952' data-lj_action_resblock_id="1111027380488"
        data-lj_action_housedel_id="101121958886"><a class="noresultRecommend img LOGCLICKDATA"
            href="https://bj.lianjia.com/ershoufang/101121958886.html" target="_blank" data-log_index="30"
            data-el="ershoufang" data-housecode="101121958886" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img
                src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2023112010450485" class="vr_item"><img
                class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2023112010450485"
                data-original="https://image1.ljcdn.com/110000-inspection/pc1_whKhqipX2_2.jpg.296x216.jpg"
                alt="北京东城永定门"></a>
        <div class="info clear">
            <div class="title"><a class="" href="https://bj.lianjia.com/ershoufang/101121958886.html" target="_blank"
                    data-log_index="30" data-el="ershoufang" data-housecode="101121958886" data-is_focus=""
                    data-sl="">东城区永定门外望陶园小区带电梯中楼层满五唯一</a><!-- 拆分标签 只留一个优先级最高的标签--><span
                    class="goodhouse_tag tagBlock">必看好房</span></div>
            <div class="flood">
                <div class="positionInfo"><span class="positionIcon"></span><a
                        href="https://bj.lianjia.com/xiaoqu/1111027380488/" target="_blank" data-log_index="30"
                        data-el="region">望陶园小区 </a> - <a href="https://bj.lianjia.com/ershoufang/yongdingmen/"
                        target="_blank">永定门</a> </div>
            </div>
            <div class="address">
                <div class="houseInfo"><span class="houseIcon"></span>2室1厅 | 107.38平米 | 南 西 | 简装 | 中楼层(共18层) | 塔楼</div>
            </div>
            <div class="followInfo"><span class="starIcon"></span>10人关注 / 11天以前发布</div>
            <div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span
                    class="taxfree">房本满五年</span></div>
            <div class="priceInfo">
                <div class="totalPrice totalPrice2"><i> </i><span class="">749</span><i>万</i></div>
                <div class="unitPrice" data-hid="101121958886" data-rid="1111027380488" data-price="69753">
                    <span>69,753元/平</span></div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="101121958886"><span class="follow-text">关注</span></div>
            <div class="compareBtn LOGCLICK" data-hid="101121958886" log-mod="101121958886" data-log_evtid="10230">加入对比
            </div>
        </div>
    </li>
</ul><!-- 少结果搜索 --><!-- 无搜索结果且不是扩大召回 -->
<div id="noResultPush" data-recommend_ext_info='{"district_id":["23008614"]}'></div>
<div class="contentBottom clear">
    <div class="crumbs fl"><a href="/">北京房产网</a><span>&nbsp;&gt;&nbsp;</span><a
            href="/ershoufang/">北京二手房</a><span>&nbsp;&gt;&nbsp;</span>
        <h1><a href="/ershoufang/dongcheng/">东城二手房</a></h1>
    </div>
    <div class="page-box fr">
        <div class="page-box house-lst-page-box" comp-module='page' page-url="/ershoufang/dongcheng/pg{page}"
            page-data='{"totalPage":100,"curPage":1}'></div>"""