#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   process_img_index.py
@Time    :   2023/09/05 17:53:56
@Author  :   wwb
@Version :   1.0
@Contact :   616562636@qq.com
@License :   (C)Copyright 2023, wwb
@Desc    :   None
'''

# here put the import lib
import os

START = 1

folder_path = "D://Users/User/Desktop/zip_session_b10c3a081fb841d1b394f1c87de9e697"  # 文件夹路径
file_names = os.listdir(folder_path)  # 获取文件夹下所有文件名称

os.chdir(folder_path)

index = START
for file_name in file_names:
    if file_name.endswith(".webp"):
        name_without_extension = os.path.splitext(file_name)[0]
        new_file_name = file_name.replace(name_without_extension, str(index))
        os.rename(file_name, new_file_name)
        index += 1
