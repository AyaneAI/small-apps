#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   process_img_index.py
@Time    :   2023/09/05 17:53:56
@Author  :   wwb
@Version :   1.0
@Contact :   616562636@qq.com
@License :   (C)Copyright 2023, wwb
@Desc    :   支持多种格式
'''

# here put the import lib
import os
from PIL import Image

suffixes = [".webp", ".png", ".jpg", ".jpeg", ".jfif"]
png_format = ".png"

folder_path = "D:/Users/User/Desktop/img"  # 文件夹路径
file_names = os.listdir(folder_path)  # 获取文件夹下所有文件名称

file_count = len(file_names)

os.chdir(folder_path)

INIT_INDEX = 1  # 起始编号

digit_set = set()
# 首先查看是否有数字命名的文件，将其加入屏蔽名单里
# 转换图片格式为png
for file_name in file_names:
    name_without_extension = os.path.splitext(file_name)[0]
    if name_without_extension.isdigit():
        digit_set.add(int(name_without_extension))

digit_exist = True if len(digit_set) > 0 else False
# 由于存在场景：不同的格式的文件可能文件名（后缀之前的命名）可能是相同的，例如1.webp、1.jpg、1.png
# 因此选取max_set最大值，作为起始名称
index = max(digit_set) + 1 if digit_exist else INIT_INDEX

for file_name in file_names:
    for suffix in suffixes:
        if file_name.endswith(suffix):
            name_without_extension = os.path.splitext(file_name)[0]
            file_extension = os.path.splitext(file_name)[1]
            # 转换图片格式为png
            if file_extension != png_format:
                # 打开原始图像文件
                with Image.open(file_name) as img:
                    # 将图像转换为PNG格式
                    old_file = file_name
                    file_name = name_without_extension + png_format
                    img.save(file_name)
                    os.remove(old_file)
            new_file_name = file_name.replace(name_without_extension, str(index))
            os.rename(file_name, new_file_name)
            print(f"index: {index}, {file_name} ends with {suffix}")
            index += 1

# 如果文件中存在数字，需要再编码一次
if digit_exist:
    file_names = os.listdir(folder_path)
    index = INIT_INDEX
    for file_name in file_names:
        for suffix in suffixes:
            if file_name.endswith(suffix):
                name_without_extension = os.path.splitext(file_name)[0]
                new_file_name = file_name.replace(name_without_extension, str(index))
                os.rename(file_name, new_file_name)
                print(f"index: {index}, {file_name} ends with {suffix}")
                index += 1
