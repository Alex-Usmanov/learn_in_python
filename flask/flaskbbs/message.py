# coding: utf-8

import time


db_file = 'message.db.txt'
# 创建一个存取数据的文本文件

# load() 打开存取数据的文本文件，然后加载之（返回文件中所有的数据）
def load():
    with open(db_file) as f:
    # 用with 打开文件 ,读写模式:r只读,r+读写,w新建(会覆盖原有文件),a追加,b二进制文件.常用模式
        lines = f.readlines()
        '''
        .readline() 和 .readlines()之间的差异是后者一次读取整个文件，象 .read()一样。
        .readlines()自动将文件内容分析成一个行的列表，该列表可以由 Python 的 for... in ... 结构进行处理。
        另一方面，.readline()每次只读取一行，通常比 .readlines()慢得多。
        仅当没有足够内存可以一次读取整个文件时，才应该使用.readline()。
        refer more: http://blog.csdn.net/zhongyhc/article/details/9026917
        '''
        messages = [eval(line) for line in lines]
        # 因为readlines() 按行存为字符串 列表，所以用eval()来求值，该数组即为所需的存取信息 Message
        return messages

# save() 把信息msg （追加） 写进存取数据的文本文件里
def save(msg):
    with open(db_file, 'a') as f:
    # a以追加模式打开 (从 EOF 开始, 必要时创建新文件)
    # refer more: http://www.cnblogs.com/dkblog/archive/2011/02/24/1980651.html
        f.write(str(msg) + '\n')
        # 把数据追加到 文本后面

'''
if  __name__=="__main__":
    load()
    save()

'''
