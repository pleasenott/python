import numpy as np
import pandas as pd
import time
import scipy
#from matplotlib import pyplot as plt
from scipy import interpolate
#1.打开CSV文件
fileNameStr = 'ShenyangPM20100101_20151231.csv'
df = pd.read_csv(fileNameStr,encoding='utf-8',usecols=[0,1,2,3,4,5,10,12,13])
'''
x=np.arange(1,31)
print(x)
y=df["TEMP"][0:30]
print(y)
plt.plot(x, y,'o')  #使用matplotlib库生成图形
plt.show()
f1 = interpolate.interp1d(x, y,kind = 'linear')  #线性插值
f2 = interpolate.interp1d(x, y, kind = 'quadratic')  #  2阶样条插值
print(f1(x))
#xnew = np.linspace(0, 5,100)
#plt.plot(x, y, 'o', x, f1(x), '-', x, f2(x), '--')
plt.plot(x, y, 'o', x, f1(x), '-')
plt.show()

'''
print("--------------head--------------")
print(df.head())
print("--------------describe--------------")
print(df.describe())
print("--------------info--------------")
print(df.info())
print("================================")
#2.查看是否有缺失值
print(df.isnull().sum().sort_values(ascending=False))
print("================================")

df["TEMP_new"]=df["TEMP"].interpolate() #线性插值
df["cbwd_new"]=df["cbwd"].interpolate()
df["cbwd_new_bfill"]=df["cbwd"].bfill() #用后项填充空白项
df["cbwd_new_ffill"]=df["cbwd"].ffill() #用前项填充空白项
df.to_csv("sy1.csv")


