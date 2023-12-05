"""
2. 处理北京空气质量数据
对HUMI、PRES、TEMP三列，进行线性插值处理。修改cbwd列中值为“cv”的单元格，其值用后项数据填充。
"""
import pandas as pd
import numpy as np
import scipy
from matplotlib import pyplot as plt
from scipy import interpolate
"""
No,year,month,day,hour,season,PM_Dongsi,PM_Dongsihuan,PM_Nongzhanguan,PM_US Post,DEWP,HUMI,PRES,TEMP,cbwd,Iws,precipitation,Iprec
1,2010,1,1,0,4,NA,NA,NA,NA,-21,43,1021,-11,NW,1.79,0,0
2,2010,1,1,1,4,NA,NA,NA,NA,-21,47,1020,-12,NW,4.92,0,0
3,2010,1,1,2,4,NA,NA,NA,NA,-21,43,1019,-11,NW,6.71,0,0
"""
if __name__=="__main__":
    filename = 'BeijingPM20100101_20151231.csv'
    df = pd.read_csv(filename, encoding='utf-8-sig')
    #对HUMI、PRES、TEMP三列，进行线性插值处理。
    df_ads=df[df['HUMI'].isna()]
    print("HUMI :\n",df_ads)
    df_ads = df[df['PRES'].isna()]
    print("PRES :\n",df_ads)
    df_ads = df[df['TEMP'].isna()]
    print("TEMP :\n",df_ads)

    df['HUMI'] = df['HUMI'].interpolate()
    df['PRES'] = df['PRES'].interpolate()
    df['TEMP'] = df['TEMP'].interpolate()
    print("after interpolate")
    df_ads=df[df['HUMI'].isna()]
    print("HUMI :\n",df_ads)
    df_ads = df[df['PRES'].isna()]
    print("PRES :\n",df_ads)
    df_ads = df[df['TEMP'].isna()]
    print("TEMP :\n",df_ads)

    #绘制图形

    #修改cbwd列中值为“cv”的单元格，其值用后项数据填充。
    #df['cbwd'] = df['cbwd'].replace('cv', np.nan)
    print("before bfill")
    df_ads = df[df['cbwd'].isna()]
    print("cbwd :\n", df_ads)
    df['cbwd'] = df['cbwd'].fillna(method='bfill')
    print("after bfill")
    df_ads = df[df['cbwd'].isna()]
    print("cbwd :\n",df_ads)