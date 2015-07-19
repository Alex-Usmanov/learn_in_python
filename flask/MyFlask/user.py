# coding: utf-8

import db


user_db_file = 'user.db.txt'
# 创建一个存取数据的文本文件


# load() 打开存取数据的文本文件，然后加载之（返回文件中所有的数据）
def load():
    return db.load(user_db_file)


def save(data):
    db.save(data, user_db_file)


def cover(datas):
    db.cover(datas, user_db_file)


# 检查用户登录
def check_login(user_data):
    with open(user_db_file, 'a') as f:
        # a以追加模式打开 (从 EOF 开始, 必要时创建新文件)
        # refer more: http://www.cnblogs.com/dkblog/archive/2011/02/24/1980651.html
        lines = f.readline()
        for line in lines:
            if line["user_name"] == user_data["user_name"]:
                if line["password"] == user_data["password"]:
                    return True
        # 把数据追加到 文本后面
        return False


def equal_password(passwords):
    return passwords["password1"] == passwords["password2"]

    # 怎样 把注册的页面的用户名和密码传输进数据库文本里？
