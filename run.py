#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Created on 2021年9月15日
@author: yuejing
'''
import os

pylist=[]
#需要修改文件的目录
path="C:\\Users\\yuejing\\Desktop\\test"
#获取目录下所有py文件
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
    	filename=os.path.join(root, name)
    	if filename.endswith(".py"):
    		pylist.append(filename)

#修改文件内容
def alter(file,old_str,new_str):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
        print(file,' 修改成功！')
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

for file in pylist:
	alter(file, "修改前内容", "修改后内容")
