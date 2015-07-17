# coding:gbk

import time


user_db_file = 'user.db.txt'
message_db_file = 'message.db.txt'
problem_db_file = 'problem.db.txt'
# 创建一个存取数据的文本文件

# load() 打开存取数据的文本文件，然后加载之（返回文件中所有的数据）
def load(file=problem_db_file):
    with open(file) as f:
        # 用with 打开文件 ,读写模式:r只读,r+读写,w新建(会覆盖原有文件),a追加,b二进制文件.常用模式
        lines = f.readlines()
        messages = [eval(line) for line in lines]
        # 因为 readlines() 按行存为字符串 列表，所以用eval()来求值，该数组即为所需的存取信息 Message
        return messages


def save(data,file=problem_db_file):
    with open(file, 'a') as f:
        f.write(str(data) + '\n')
        # 把用户数据（用户名和密码）追加到 文本后面

