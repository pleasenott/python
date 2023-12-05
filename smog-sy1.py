import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import time

#1.打开CSV文件
fileNameStr = 'ShenyangPM20100101_20151231.csv'
df = pd.read_csv(fileNameStr,encoding='utf-8',dtype=str)

#fileNameStr = 'BeijingPM20100101_20151231.csv'
#df = pd.read_csv(fileNameStr,encoding='utf-8',usecols=[11,12,13])


#2.查看数据集的基本情况
print("2:head============================================================================")
print(df.head())
print("2:describe============================================================================")
print(df.describe())
print("2:info============================================================================")
print(df.info())

#3.查看是否有缺失值
print("3============================================================================")
print(df.isnull().sum().sort_values(ascending=False))

#4.计算
# df['sum'] = df['PM_Taiyuanjie']+df['PM_US Post']+df['PM_Xiaoheyan'] #直接加是按照字符串相加的
# print("df[sum] is :\n",df['sum'])
#
# print(type(df['PM_Taiyuanjie'][52582]))
# print(type(df['PM_Taiyuanjie'][52583]))
# print(type(df['PM_US Post'][52583]))

print("4============================================================================")
df['sum']=0
df['count']=0
start = time.time()
print("start:",end='')

pd.set_option('mode.chained_assignment', None)

#方案1，使用循环，计算sum和count
for i in range(len(df['PM_Taiyuanjie'])):
    sum = count = 0
    if not(df['PM_Taiyuanjie'][i] is np.nan):
        sum+=int(df['PM_Taiyuanjie'][i])
        count+=1
    if not (df['PM_US Post'][i] is np.nan):
        sum += int(df['PM_US Post'][i])
        count += 1
    if not(df['PM_Xiaoheyan'][i] is np.nan):
        sum+=int(df['PM_Xiaoheyan'][i])
        count+=1

    df['sum'][i]=sum
    df['count'][i] = count
    #df['ave'][i]=sum/count
    if i%5000 == 0:
        print('-',end="")

print('\n',count)
print(df['sum'],df['count'])

#两列直接相除，求得平均值
df['ave']=round(df['sum']/df['count'],2)

end = time.time()
print("-------duration:",end-start)

#5.输出到文件
df.to_csv("smog-sy1-2023.csv")
print("****** done ******")

print("2:describe============================================================================")
print(df.describe())
print("2:info============================================================================")
print(df.info())
#df.drop(["No"],axis=1,inplace=True)
#print(df.groupby("year").mean())




