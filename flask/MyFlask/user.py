# coding:utf-8

import sqlite3
import os
import sys

reload(sys)
print sys.getdefaultencoding()
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()
_db_directory = 'sqlite3_db_files'
db_file = 'user_info.db'
db_file_path = os.path.join(_db_directory, db_file)

"""
# INIT db table
conn = sqlite3.connect(db_file_path)
# if the file path is not exist,throw exception :unable to open database file
c = conn.cursor()
c.execute("INSERT INTO user ('username', 'password', 'email') VALUES  ('apple', 'apple', 'apple@email.com')")
conn.commit()
conn.close()

c.execute('''CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL UNIQUE CHECK(length(username) >= 2 AND length(username <= 30)),
    password TEXT NOT NULL CHECK(length(password) >=2 AND length(password <= 30)),
    email TEXT,
    timestamp INTEGER DEFAULT (DATETIME('now'))
    );''')
# if the table has exist,can not be create

c.execute("INSERT into user (username,password,email) values ('foo','pwd','a@b.c');")
# can not be execute again,because the username must be unique
c.execute("INSERT into user (username,password,email) values ('dodoru','dodoru','dodoru@do.c');")
c.execute("INSERT into user (username,password,email) values ('fish','123456','fish@do.c');")
c.execute("INSERT into user (username,password,email) values ('cat','12345678','cat@do.com');")

conn.commit()
a = c.execute("SELECT * from user where username='dodoru';")
print a
# <sqlite3.Cursor object at 0x0000000002802B20>
print a.fetchall()
# [(2, u'dodoru', u'dodoru', u'dodoru@do.c', u'2015-07-21 04:03:58')]
conn.close()

"""


def load(file=db_file_path):
    # with open (file) as f:
    # database parameter must be string or APSW Connection object
    conn = sqlite3.connect(file)
    cu = conn.cursor()
    data_index = cu.execute("SELECT * FROM user ;")
    usersdata = data_index.fetchall()
    print usersdata
    conn.close()
    return usersdata


def save(user_dict):
    conn = sqlite3.connect(db_file_path)
    cu = conn.cursor()
    print (user_dict.values())
    print "INSERT INTO user " + str(tuple(user_dict.keys())) + " VALUES ", (tuple(user_dict.values()))
    # cu.execute("INSERT INTO user (username,password,email) values " + str(tuple(user_dict.values()))
    cu.execute("INSERT INTO user " + str(tuple(user_dict.keys())) + " VALUES  " % (tuple(user_dict.values())))
    # print
    conn.commit()
    conn.close()


def update(user_id, user_dict):
    conn = sqlite3.connect(db_file_path)
    cu = conn.cursor()
    user_phrase = ((str(user_dict).replace(':', '=')).replace('{', '')).replace('}', '')
    print user_phrase
    # update_sentence = "UPDATE user SET " + user_phrase + " WHERE id =" + str(user_id) + ';'
    # print "update_sentence :", update_sentence
    # FIXME，
    cu.execute("UPDATE user SET " + user_phrase + " WHERE id =" + str(user_id))
    # cu.execute("UPDATE user SET " + user_phrase + " WHERE id = ? ", user_id)
    # WHY 用问号可以防注入？
    '''
    cu.execute("UPDATE user SET " + str(tuple(user_dict.keys())) +
               " VALUES " + str(tuple(user_dict.values())) +
               "WHERE id =" + str(id))
    '''
    conn.commit()
    conn.close()


def delete(user_id):
    conn = sqlite3.connect(db_file_path)
    cu = conn.cursor()
    cu.execute("DELETE FROM user WHERE id = " + str(user_id))
    # FIXME，cu.execute("DELETE FROM user WHERE id = ? ",user_id)
    conn.commit()
    conn.close()


def search_id(user_id):
    conn = sqlite3.connect(db_file_path)
    cu = conn.cursor()
    data_index = cu.execute("SELECT * From user where id =" + str(user_id))
    # FIXME ,data_index=cu.execute("SELECT * FROM user WHERE id = ? ",user_id)
    userdata = data_index.fetchall()
    print userdata
    conn.close()
    return userdata


def show_lines(file=db_file_path):
    usersdata = load(file)
    print "ID,  username, password , email ,timestamp "
    for ur in usersdata:
        print ur

        # print usersdata[1][2]


if __name__ == "__main__":
    load()
    # save('testname','test', 'test@test.com')
    # save({'username':'admin','password':'admin','email':'admin@admin.com'})
    load()
    search_id(3)
    search_id(9)
    update(3, {'password': '123456789'})
    search_id(3)
    search_id(4)
    delete(4)
    search_id(4)
    delete(4)
    search_id(4)
    load()
    # save({'username':'pear','password':'pear','email':'pear@email.com'})

    save({'username': u'apple', 'password': u'apple', 'email': u'apple@email.com'})
    load()
    show_lines()

    '''
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
        return passwords["password1"] == passwords["password2"] # 怎样 把注册的页面的用户名和密码传输进数据库文本里？

        '''
