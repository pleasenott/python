from scrapy import cmdline
cmdline.execute("scrapy crawl gz ".split())
#bupt为爬虫的名字，在spider.py中定义
# """
# 1.对你爬取下来的北京二手房数据，进行数据的预处理，并计算：
# （1）四个区的平均总价、最高总价、最低总价；
# （2）四个区的平均单价、最高单价、最低单价；
# （3）按照房屋建成的年份，计算2000年以前、2000-2009.12.31、2010-至今，这三个时间段的平均单价。
# """
# import pandas as pd
# import numpy as np
# import scipy
# #from matplotlib import pyplot as plt
# from scipy import interpolate
# if __name__=="__main__":
#     # 读取数据
#     df = pd.read_csv('MyData.csv', encoding='utf-8-sig')
#     df = df.drop_duplicates()  # 去重
#     df = df.dropna()  # 去空值
#     zones_chinese = ['东城', '西城', '朝阳', '海淀']
#     """
#     zone_name,building_names,area,total_price,price_per_area,houseInfo
#     东城,京香福苑 ,119.76平米,1580,"131,931元/平",3室1厅 | 119.76平米 | 西 南 北 | 精装 | 中楼层(共6层)  | 板楼
#     东城,后永康胡同2号院4号院 ,72.03平米,680,"94,406元/平",3室1厅 | 72.03平米 | 南 北 | 精装 | 高楼层(共6层)  | 板楼
#     东城,新奥洋房 ,92.08平米,828,"89,922元/平",2室2厅 | 92.08平米 | 东 西 北 | 精装 | 6层 | 2006年 | 板塔结合
#     东城,左安漪园 ,133.04平米,1400,"105,232元/平",3室1厅 | 133.04平米 | 南 北 | 简装 | 中楼层(共10层)  | 板塔结合
#     东城,龙潭西里 ,46.98平米,495,"105,364元/平",1室1厅 | 46.98平米 | 东 西 | 精装 | 6层 | 2000年 | 板楼
#     """
#     # 1.四个区的平均总价、最高总价、最低总价；
#     print("四个区的平均总价、最高总价、最低总价；")
#     for zone in zones_chinese:
#         print(zone)
#         df_zone = df[df['zone_name'] == zone]
#         print(df_zone['total_price'].mean())
#         print(df_zone['total_price'].max())
#         print(df_zone['total_price'].min())
#     # 2.四个区的平均单价、最高单价、最低单价；
#     #去除元/平
#     print("四个区的平均单价、最高单价、最低单价；")
#     for zone in zones_chinese:
#         print(zone)
#         df_zone = df[df['zone_name'] == zone]
#         df_zone['price_per_area'] = df_zone['price_per_area'].apply(lambda x: x.replace('元/平', ''))
#         df_zone['price_per_area'] = df_zone['price_per_area'].apply(lambda x: x.replace(',', ''))
#         df_zone['price_per_area'] = df_zone['price_per_area'].astype('int64')
#         #print("sdsaasd",df_zone)
#         print(df_zone['price_per_area'].mean())
#         print(df_zone['price_per_area'].max())
#         print(df_zone['price_per_area'].min())
#     # 3.按照房屋建成的年份，计算2000年以前、2000-2009.12.31、2010-至今，这三个时间段的平均单价。
#     print("按照房屋建成的年份，计算2000年以前、2000-2009.12.31、2010-至今，这三个时间段的平均单价。")
#     def get_year(x):
#         x=str(x).split("|")
#         for i in x:
#             if "年" in i:
#                 return i.replace("年","")
#     df['houseInfo'] = df['houseInfo'].apply(get_year)
#     #print(df['houseInfo'])
#     #删除None
#     df = df[df['houseInfo'] != 'None']
#     df_cleaned = df.dropna()
#     print(df_cleaned)
#     df_cleaned['houseInfo'] = df_cleaned['houseInfo'].astype('int64')
#     df_cleaned['price_per_area'] = df_cleaned['price_per_area'].apply(lambda x: x.replace('元/平', ''))
#     df_cleaned['price_per_area'] = df_cleaned['price_per_area'].apply(lambda x: x.replace(',', ''))
#     df_cleaned['price_per_area'] = df_cleaned['price_per_area'].astype('int64')
#     df_2000 = df_cleaned[df_cleaned['houseInfo'] < 2000]
#     df_2000_2009 = df_cleaned[(df_cleaned['houseInfo'] >= 2000) & (df_cleaned['houseInfo'] <= 2009)]
#     df_2010 = df_cleaned[df_cleaned['houseInfo'] >= 2010]
#     print("2000 :",df_2000['price_per_area'].mean())
#     print("2000-2009 :",df_2000_2009['price_per_area'].mean())
#     print("2010 :",df_2010['price_per_area'].mean())
#
#
#
#
#     #print(df['houseInfo'])
#
#
#
#
#
#     # print(df)
#