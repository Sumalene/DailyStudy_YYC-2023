import numpy as np
print("hello")

import pandas as pd
import os

# 读取原始Excel文件，指定列名
df = pd.read_excel('range_price_page_urls.xlsx', header=None, names=['深圳市区名', '房源URL'])



# 创建一个字典，用于存储各个区的URL
districts = {
    '南山区': [],
    '罗湖区': [],
    '福田区': [],
    '宝安区': [],
    '龙华区': [],
    '龙岗区': [],
    '盐田区': [],
    '坪山区': [],
    '光明区': [],
    '大鹏新区': [],
}

# 遍历原始数据，根据区名把URL添加到相应的列表中
for index, row in df.iterrows():
    district = row['深圳市区名']  # 获取区名
    url = row['房源URL']  # 获取房源URL
    districts[district].append(url)

# 创建各个区的Excel文件
for district, urls in districts.items():
    # 创建一个新的DataFrame，包含该区的房源URL
    df_district = pd.DataFrame({
        '房源URL': urls,
    })
    # 创建Excel文件，文件名是区名，不包含标题行 ，第一列是区名，第二列是url
    df_district.to_excel(f'{district}.xlsx', index=False, header=False)


print("hello")

import pandas as pd

# 以坪山区.xlsx为例，现在只有一列url，以下代码为给该文件添加第一列区名：坪山区（作为第一列），保存为新文件 “PS.xls“
df = pd.read_excel('坪山区.xlsx', header=None, names=['房源URL'])
df.insert(0, '深圳市区名', '坪山区')
df.to_excel('PS.xls', index=False, header=False)


    
