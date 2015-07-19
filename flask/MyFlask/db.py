# coding:utf-8

import os

_db_directory = 'db_files'


def is_exist(db_file):
    filepath = os.path.join(_db_directory, db_file)
    return os.path.exists(filepath)


def load(db_file):
    filepath = os.path.join(_db_directory, db_file)
    if os.path.exists(filepath):
        # 先判断是否存在这个东西
        with open(filepath) as f:
            # 用with 打开文件 ,读写模式:r只读(默认),r+读写,w新建(会覆盖原有文件),a追加,b二进制文件.常用模式
            lines = f.readlines()
            data_list = [eval(line) for line in lines]
            # 因为 readlines() 按行存为字符串 列表，所以用eval()来求值，该数组即为所需的存取信息 Message
            return data_list
    else:
        return None


def save(data, db_file):
    filepath = os.path.join(_db_directory, db_file)
    with open(filepath, 'a') as f:
        f.write(str(data) + '\n')


def cover(datas, db_file):
    filepath = os.path.join(_db_directory, db_file)
    with open(filepath, 'w') as f:
        for data in datas:
            f.write(str(data) + '\n')