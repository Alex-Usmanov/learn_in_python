# coding:utf-8

import time


db_file = 'user.db.txt'
# 创建一个存取数据的文本文件

# load() 打开存取数据的文本文件，然后加载之（返回文件中所有的数据）
def load():
    with open(db_file) as f:
    # 用with 打开文件 ,读写模式:r只读,r+读写,w新建(会覆盖原有文件),a追加,b二进制文件.常用模式
        lines = f.readlines()
        messages = [eval(line) for line in lines]
        # 因为 readlines() 按行存为字符串 列表，所以用eval()来求值，该数组即为所需的存取信息 Message
        return messages

# 检查用户登录
def check_login(name,pwd):
    with open(db_file, 'a') as f:
    # a以追加模式打开 (从 EOF 开始, 必要时创建新文件)
    # refer more: http://www.cnblogs.com/dkblog/archive/2011/02/24/1980651.html
        lines=f.readline()
        for line in lines:
            if line["user_name"]==name:
                if line["password"]==pwd:
                    return True
        # 把数据追加到 文本后面
        return False

def equal_password(pwd1,pwd2):
    if pwd1==pwd2:
        pass
        # 怎样 把注册的页面的用户名和密码传输进数据库文本里？
