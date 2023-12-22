
"""
把json数据转换成csv格式
"""
import json
import csv
import os



file_list_chinese=['北京','上海','广州','深圳']
filename_list=["BeijingHouseInfo.json","ShanghaiHouseInfo.json","GuangzhouHouseInfo.json","ShenzhenHouseInfo.json"]
file_list=["bj","sh","gz","sz"]
"""输入格式{"name": "整租·华南御景园 2室1厅 西北", "district": "岑村", "total_price": 3600, "area": 86.0, "price_per_m2": 41.86, "direction": "西北", "layout": "2室1厅1卫"}
{"name": "整租·华南御景园 3室2厅 南/北", "district": "岑村", "total_price": 4500, "area": 108.0, "price_per_m2": 41.67, "direction": "南 北", "layout": "3室2厅2卫"}
{"name": "整租·华南御景园 2室1厅 南", "district": "岑村", "total_price": 3800, "area": 86.0, "price_per_m2": 44.19, "direction": "南", "layout": "2室1厅1卫"}
{"name": "整租·华南御景园 3室2厅 北", "district": "岑村", "total_price": 4500, "area": 112.0, "price_per_m2": 40.18, "direction": "北", "layout": "3室2厅2卫"}
{"name": "整租·华南御景园 2室1厅 东南", "district": "岑村", "total_price": 4000, "area": 86.0, "price_per_m2": 46.51, "direction": "东南", "layout": "2室1厅1卫"}
{"name": "整租·蓝天雅苑 4室2厅 南", "district": "岑村", "total_price": 4650, "area": 128.0, "price_per_m2": 36.33, "direction": "南", "layout": "4室2厅2卫"}"""
"""输出格式：name_chinese,block,house_type,direct,area,price"""
for i in range(4):
    with open(filename_list[i],'r',encoding='utf-8') as f:
        with open(file_list[i]+'.csv','w',encoding='utf-8',newline='') as f1:
            writer=csv.writer(f1)
            writer.writerow(['name_chinese','block','house_type','direct','area','price'])
            for line in f.readlines():
                dic=json.loads(line)
                writer.writerow([file_list_chinese[i],dic['district'],dic['layout'],dic['direction'].split(" ")[0],dic['area'],dic['total_price']])