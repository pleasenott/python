import scrapy

from test1.items import Test1Item #从items.py中引入MyItem对象

class LianjiaSpider(scrapy.Spider):
    name = 'hw'
    allowed_domains = ['bj.lianjia.com']
    #https://bj.lianjia.com/zufang/pg2/
    base_url = 'https://'
    zones = ['bj', 'gz', 'sh', 'sz']
    zones_chinese = ['北京', '广州', '上海', '深圳']
    mem='.lianjia.com/zufang/'
    zone_index = 0  # 地区计数
    start_urls = [base_url+zones[zone_index]+mem]
    page_index = 1  # 页数计数
    maxpage=5
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.download_delay = 4

    def parse(self, response, **kwargs):
        for each in response.xpath("//*[@id='content']/div[1]/div[1]/*"):
            item = Test1Item()
            item['price'] = each.xpath("div/span/em/text()").extract_first()
            temp = each.xpath("div/p[1]/a/text()").extract_first()
            #从temp中提取数据
            temp=temp.split(" ")
            item['name'] = temp[0]
            item["house_type"]=""
            item["area"]=""
            item["direct"]=""
            item["name_chinese"]=self.zones_chinese[self.zone_index]
            for i in temp:
                if '室' in i or '厅' in i or '卫' in i:
                    item['house_type'] = i
                if '东' in i or '南' in i or '西' in i or '北' in i:
                    if len(i)< 5:
                        item['direct'] = i
            temp=each.xpath("div/p[2]/text()").extract()
            for i in temp:
                if '㎡'in i:
                    i=i.replace("㎡", "").replace(" ", "").replace("\n", "")
                    if "-" in i:
                        temp = i.split("-")
                        item['area'] = (float(temp[0])+float(temp[1]))/2
                    item['area'] = i

            #获取面积
            #item["area"]=each.xpath("/div/p[2]/text()[2]").extract_first()

            # item["house_type"]=each.xpath("/div/p[2]/text()[7]").extract_first()
            #print(item)
            if item['price'] and item['name'] and item['house_type'] and item['area']:
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
        self.page_index += 1
        if self.page_index <= self.maxpage:
            url = self.base_url + self.zones[self.zone_index] +self.mem+ 'pg' + str(self.page_index)
        else:
            self.page_index = 1
            url = self.base_url + self.zones[self.zone_index] + self.mem+"pg"+str(self.page_index)
            self.zone_index += 1
        if self.zone_index >= len(self.zones):
            return

        print(url)
        yield scrapy.Request(url, callback=self.parse)
"""
<div class="content__list">

    <!--直通车 品牌或门店-->
              <!-- 直升机 广告房源与list去重 && 广告房源插入list第1、3、4位(房源数不足3个时广告可按顺序排列) -->
    
    <!-- 房源列表模块 -->
    <div
class="content__list--item"
data-el="listItem"
data-house_code="BJ1816009503133401088"
data-brand_code="200301001000"
data-ad_code="0"
data-bid_version=""
data-c_type="1"
data-position="0"
data-total="66377"
data-fb_expo_id="786707837408985088"
data-t="default"
data-strategy_id=""
data-click_position="0"
data-ad_type="0"
data-distribution_type="203500000001"
data-event_id="21333"
data-event_action="click_position=0"
data-event_position="click_position"
data-event_send="no"
data-rank_score="-1"
data-operation_score="0"
>
<a
class="content__list--item--aside" target="_blank"      href="/zufang/BJ1816009503133401088.html"
title="整租·乐想汇 1房间 南">
  <img
    alt="整租·乐想汇 1房间 南_乐想汇租房"
    src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20231122104722f2f"
    data-src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182_1.png?_v=20231122104722f2f"
    class="lazyload">
  <!-- 是否展示vr图片 -->
          <!-- 是否展示省心租图片 -->
          <!-- 广告标签 -->
      </a>
<div class="content__list--item--main">
<p class="content__list--item--title">
  <a class="twoline" target="_blank" href="/zufang/BJ1816009503133401088.html">
    整租·乐想汇 1房间 南        </a>
                </p>
<p class="content__list--item--des">
          <a target="_blank" href="/zufang/chaoyang/">朝阳</a>-<a href="/zufang/beiyuan2/" target="_blank">北苑</a>-<a title="乐想汇" href="/zufang/c1111046126379/" target="_blank">乐想汇</a>
  <i>/</i>
  68.00㎡
  <i>/</i>南        <i>/</i>
    1房间1卫        <span class="hide">
    <i>/</i>
    低楼层                        （18层）
            </span>
</p>
<p class="content__list--item--bottom oneline">
      <i class="content__item__tag--gov_certification">官方核验</i>
      <i class="content__item__tag--is_subway_house">近地铁</i>
      <i class="content__item__tag--central_heating">集中供暖</i>
      <i class="content__item__tag--is_key">随时看房</i>
      </p>
<p class="content__list--item--brand oneline">
            <span class="brand">
      链家          </span>
          <span class="content__list--item--time oneline">2天前维护</span>
</p>
      <span class="content__list--item-price"><em>5100</em> 元/月</span>
</div>

</div>
<div class="content__list--item"
data-el="listItem"
data-house_code="580191"
data-brand_code="200306015473"
data-ad_code="92217242489341624"
data-c_type="1"
data-position="1"
data-total="66377"
data-fb_expo_id="786707837408985089"
data-t="default"
data-strategy_id=""
data-click_position="1"
data-ad_type="250"
data-bid_version="v92217577549218912"
data-distribution_type="203500000002"
>
<a class="link" target="_blank" data-id="580191" href="/apartment/66276.html">
<!-- 左边图片 -->
<a
class="content__list--item--aside" target="_blank"      href="/apartment/66276.html"
title="独栋·自隅青年公寓 程远公寓 豪华开间 开间">
  <img
  alt="独栋·自隅青年公寓 程远公寓 豪华开间 开间_程远大厦租房"
  src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20231122104722f2f"
  data-src="https://image1.ljcdn.com/wanjia/21363289d06c57ec84b060c24f7d72ba-1693296506006/b95470325b1577cd5d8a79aa43ec8a87.jpg.250x182.jpg"
  class="lazyload">
  <!-- 是否展示vr图片 -->
          <!-- 广告标签 -->
      </a>
<!-- 右边内容 -->
<div class="content__list--item--main">
<!-- title -->
<p class="content__list--item--title twoline">
  <a target="_blank" href="/apartment/66276.html">
    独栋·自隅青年公寓 程远公寓 豪华开间 开间        </a>
</p>
<!-- house info -->
<p class="content__list--item--des">
            <span class="room__left">仅剩5间</span>
    <i>/</i>
          22.00-32.00㎡
  <i>/</i>5间在租        <i>/</i>
  1室0厅1卫      </p>
<!-- tags -->
<p class="content__list--item--bottom oneline">
            <i class="content__item__tag--authorization_apartment">独栋公寓</i>
            <i class="content__item__tag--rent_period_month">月租</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--open_kitchen">开放厨房</i>
        </p>
<!-- brand -->
<p class="content__list--item--brand oneline">
            <span class="brand">
      自隅青年公寓          </span>
          <span class="content__list--item--time">14天前维护</span>
</p>
<!-- gr -->
      <!-- price -->
<span class="content__list--item-price"><em>4700-5200</em> 元/月</span>
</div>
</a>
</div>
<div
class="content__list--item"
data-el="listItem"
data-house_code="BJ1829437453811843072"
data-brand_code="200301001000"
data-ad_code="0"
data-bid_version=""
data-c_type="1"
data-position="2"
data-total="66377"
data-fb_expo_id="786707837408985090"
data-t="default"
data-strategy_id=""
data-click_position="2"
data-ad_type="0"
data-distribution_type="203500000001"
data-event_id="21333"
data-event_action="click_position=2"
data-event_position="click_position"
data-event_send="no"
data-rank_score="-1"
data-operation_score="0"
>
<a
class="content__list--item--aside" target="_blank"      href="/zufang/BJ1829437453811843072.html"
title="整租·白云观 2室1厅 南">
  <img
    alt="整租·白云观 2室1厅 南_白云观租房"
    src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20231122104722f2f"
    data-src="https://image1.ljcdn.com/110000-inspection/pc1_CkFSS6Dbr.jpg!m_fill,w_250,h_182,l_flianjia_black,o_auto"
    class="lazyload">
  <!-- 是否展示vr图片 -->
              <i class="vr-logo"></i>
          <!-- 是否展示省心租图片 -->
          <!-- 广告标签 -->
      </a>
<div class="content__list--item--main">
<p class="content__list--item--title">
  <a class="twoline" target="_blank" href="/zufang/BJ1829437453811843072.html">
    整租·白云观 2室1厅 南        </a>
                </p>
<p class="content__list--item--des">
          <a target="_blank" href="/zufang/xicheng/">西城</a>-<a href="/zufang/muxidi1/" target="_blank">木樨地</a>-<a title="白云观" href="/zufang/c1111027376247/" target="_blank">白云观</a>
  <i>/</i>
  50.00㎡
  <i>/</i>南        <i>/</i>
    2室1厅1卫        <span class="hide">
    <i>/</i>
    低楼层                        （5层）
            </span>
</p>
<p class="content__list--item--bottom oneline">
      <i class="content__item__tag--gov_certification">官方核验</i>
      <i class="content__item__tag--central_heating">集中供暖</i>
      <i class="content__item__tag--is_key">随时看房</i>
      </p>
<p class="content__list--item--brand oneline">
            <span class="brand">
      链家          </span>
          <span class="content__list--item--time oneline">3天前维护</span>
</p>
      <span class="content__list--item-price"><em>6000</em> 元/月</span>
</div>

</div>
<div class="content__list--item"
data-el="listItem"
data-house_code="593087"
data-brand_code="200306014991"
data-ad_code="91085053061646008"
data-c_type="1"
data-position="3"
data-total="66377"
data-fb_expo_id="786707837408985091"
data-t="default"
data-strategy_id=""
data-click_position="3"
data-ad_type="250"
data-bid_version="v91085053061646009"
data-distribution_type="203500000002"
>
<a class="link" target="_blank" data-id="593087" href="/apartment/66207.html">
<!-- 左边图片 -->
<a
class="content__list--item--aside" target="_blank"      href="/apartment/66207.html"
title="独栋·保利首开乐尚N+公寓 乐尚N+旧宫店 公寓开间 1室1厅">
  <img
  alt="独栋·保利首开乐尚N+公寓 乐尚N+旧宫店 公寓开间 1室1厅_首开保利熙悦林语租房"
  src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20231122104722f2f"
  data-src="https://image1.ljcdn.com/wanjia/a5fff7c25f907f6c1dd8cd0a73bd1fdb-1696900733079/724ad3bd43faa43b9ff038244c4ff260.jpg.250x182.jpg"
  class="lazyload">
  <!-- 是否展示vr图片 -->
          <!-- 广告标签 -->
      </a>
<!-- 右边内容 -->
<div class="content__list--item--main">
<!-- title -->
<p class="content__list--item--title twoline">
  <a target="_blank" href="/apartment/66207.html">
    独栋·保利首开乐尚N+公寓 乐尚N+旧宫店 公寓开间 1室1厅        </a>
</p>
<!-- house info -->
<p class="content__list--item--des">
            <span class="room__left">仅剩4间</span>
    <i>/</i>
          35.00㎡
  <i>/</i>4间在租        <i>/</i>
  1室1厅1卫      </p>
<!-- tags -->
<p class="content__list--item--bottom oneline">
            <i class="content__item__tag--authorization_apartment">独栋公寓</i>
            <i class="content__item__tag--rent_period_month">月租</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--open_kitchen">开放厨房</i>
            <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
        </p>
<!-- brand -->
<p class="content__list--item--brand oneline">
            <span class="brand">
      保利首开乐尚N+公寓          </span>
          <span class="content__list--item--time">27天前维护</span>
</p>
<!-- gr -->
      <!-- price -->
<span class="content__list--item-price"><em>2800</em> 元/月</span>
</div>
</a>
</div>
<div
class="content__list--item"
data-el="listItem"
data-house_code="BJ1811362415988703232"
data-brand_code="200301001000"
data-ad_code="0"
data-bid_version=""
data-c_type="1"
data-position="4"
data-total="66377"
data-fb_expo_id="786707837408985092"
data-t="default"
data-strategy_id=""
data-click_position="4"
data-ad_type="0"
data-distribution_type="203500000001"
data-event_id="21333"
data-event_action="click_position=4"
data-event_position="click_position"
data-event_send="no"
data-rank_score="-1"
data-operation_score="0"
>
<a
class="content__list--item--aside" target="_blank"      href="/zufang/BJ1811362415988703232.html"
title="整租·旭辉26街区 4房间 南">
  <img
    alt="整租·旭辉26街区 4房间 南_旭辉26街区租房"
    src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20231122104722f2f"
    data-src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182_1.png?_v=20231122104722f2f"
    class="lazyload">
  <!-- 是否展示vr图片 -->
          <!-- 是否展示省心租图片 -->
          <!-- 广告标签 -->
      </a>
<div class="content__list--item--main">
<p class="content__list--item--title">
  <a class="twoline" target="_blank" href="/zufang/BJ1811362415988703232.html">
    整租·旭辉26街区 4房间 南        </a>
                </p>
<p class="content__list--item--des">
          <a target="_blank" href="/zufang/shunyi/">顺义</a>-<a href="/zufang/shunyiqita1/" target="_blank">顺义其它</a>-<a title="旭辉26街区" href="/zufang/c118282615852037/" target="_blank">旭辉26街区</a>
  <i>/</i>
  61.59㎡
  <i>/</i>南        <i>/</i>
    4房间1卫        <span class="hide">
    <i>/</i>
    中楼层                        （9层）
            </span>
</p>
<p class="content__list--item--bottom oneline">
      <i class="content__item__tag--gov_certification">官方核验</i>
      <i class="content__item__tag--decoration">精装</i>
      <i class="content__item__tag--central_heating">集中供暖</i>
      </p>
<p class="content__list--item--brand oneline">
            <span class="brand">
      链家          </span>
          <span class="content__list--item--time oneline">15天前维护</span>
</p>
      <span class="content__list--item-price"><em>4600</em> 元/月</span>
</div>

</div>
  </div>
"""