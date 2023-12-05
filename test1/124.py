"""

处理北京空气质量数据。



1.对PM指数进行异常值的处理：假设PM指数最高为500，将PM_Dongsi、PM_Dongsihuan、PM_Nongzhanguan三列中超过500的数据，修改为500。



2.对PRES和TEMP数据进行最大最小归一化和标准化归一化，并使用散点图进行展示。



3.针对北京每天的PM平均值（对多个测试站点和多个时间的值求平均），统计不同颜色代表的指数等级（指数等级见课件第23页）各有多少天。
"""
import pandas as pd
import numpy as np
import scipy
from matplotlib import pyplot as plt


if __name__=="__main__":
    filename = 'BeijingPM20100101_20151231.csv'
    df = pd.read_csv(filename, encoding='utf-8-sig')
    #对PM指数进行异常值的处理：假设PM指数最高为500，将PM_Dongsi、PM_Dongsihuan、PM_Nongzhanguan三列中超过500的数据，修改为500。
    print("before apply")
    df_ads=df[df['PM_Dongsi']>500]
    print("PM_Dongsi :\n",df_ads)
    df_ads = df[df['PM_Dongsihuan']>500]
    print("PM_Dongsihuan :\n",df_ads)
    df_ads = df[df['PM_Nongzhanguan']>500]
    print("PM_Nongzhanguan :\n",df_ads)

    df['PM_Dongsi'] = df['PM_Dongsi'].apply(lambda x: 500 if x>500 else x)
    df['PM_Dongsihuan'] = df['PM_Dongsihuan'].apply(lambda x: 500 if x>500 else x)
    df['PM_Nongzhanguan'] = df['PM_Nongzhanguan'].apply(lambda x: 500 if x>500 else x)
    df['PM_Dongsi'] = df['PM_Dongsi'].apply(lambda x: 0 if x<0 else x)
    df['PM_Dongsihuan'] = df['PM_Dongsihuan'].apply(lambda x: 0 if x<0 else x)
    df['PM_Nongzhanguan'] = df['PM_Nongzhanguan'].apply(lambda x: 0 if x<0 else x)
    print("after apply")
    df_ads=df[df['PM_Dongsi']>500]
    print("PM_Dongsi :\n",df_ads)
    df_ads = df[df['PM_Dongsihuan']>500]
    print("PM_Dongsihuan :\n",df_ads)
    df_ads = df[df['PM_Nongzhanguan']>500]
    print("PM_Nongzhanguan :\n",df_ads)

    #对PRES和TEMP数据进行最大最小归一化和标准化归一化，并使用散点图进行展示。
    df['PRES'] = (df['PRES']-df['PRES'].min())/(df['PRES'].max()-df['PRES'].min())
    df['TEMP'] = (df['TEMP']-df['TEMP'].min())/(df['TEMP'].max()-df['TEMP'].min())
    print("after normalize")
    print(df['PRES'].max())
    print(df['PRES'].min())
    print(df['TEMP'].max())
    print(df['TEMP'].min())
    #绘制图形,加上横纵坐标
    plt.scatter(df['PRES'],df['TEMP'],s=1)
    plt.xlabel('PRES')
    plt.ylabel('TEMP')
    #，点调小点

    plt.show()
    #3.针对北京每天的PM平均值（对多个测试站点和多个时间的值求平均），统计不同颜色代表的指数等级（指数等级见课件第23页）各有多少天。
    #0,50,100,150,200,300
    print(df['PM_Dongsi'])
    df['PM_avg'] = df[['PM_Dongsi','PM_Dongsihuan','PM_Nongzhanguan']].mean(axis=1)

    #去除空值
    df = df.dropna(subset=['PM_avg'])
    #对每天求平均
    df['PM_avg_day'] = df.groupby(['year','month','day'])['PM_avg'].transform('mean')

    #print(df['PM_avg'])
    df_ads=pd.cut(df['PM_avg'],bins=[0,50,100,150,200,300,500],labels=['优','良','轻度污染','中度污染','重度污染','严重污染'])
    print(df_ads)
    #统计一下每个等级的天数
    df_ads = df_ads.value_counts()
    print(df_ads)

