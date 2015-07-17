# coding:utf-8

import time


user_db_file = 'user.db.txt'
message_db_file = 'message.db.txt'
problem_db_file = 'problem.db.txt'
# 创建一个存取数据的文本文件

# load() 打开存取数据的文本文件，然后加载之（返回文件中所有的数据）
def load(file=user_db_file):
    with open(file) as f:
        # 用with 打开文件 ,读写模式:r只读,r+读写,w新建(会覆盖原有文件),a追加,b二进制文件.常用模式
        lines = f.readlines()
        messages = [eval(line) for line in lines]
        # 因为 readlines() 按行存为字符串 列表，所以用eval()来求值，该数组即为所需的存取信息 Message
        return messages


def save(data,file=user_db_file):
    with open(file, 'a') as f:
        f.write(str(data) + '\n')
        # 把用户数据（用户名和密码）追加到 文本后面


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
