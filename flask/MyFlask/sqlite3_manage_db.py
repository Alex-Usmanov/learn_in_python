# coding:utf-8

import sqlite3
import os

_db_directory = 'sqlite3_db_files'
filename = 'example.db'
filepath = os.path.join(_db_directory, filename)

conn = sqlite3.connect(filepath)
# if the file path is not exist,throw exception :unable to open database file
c = conn.cursor()

"""
c.execute('''CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL UNIQUE CHECK(length(username) >= 2 AND length(username <= 30)),
    password TEXT NOT NULL CHECK(length(password) >=2 AND length(password <= 30)),
    email TEXT,
    timestamp INTEGER DEFAULT (DATETIME('now'))
    )''')
# if the table has exist,can not be create
"""

# c.execute("INSERT into user (username,password,email) values ('foo','pwd','a@b.c')")
# can not be execute again,because the username must be unique
# c.execute("INSERT into user (username,password,email) values ('dodoru','dodoru','do@do.c')")
a = c.execute("SELECT * from user where username='dodoru';")
print a
# <sqlite3.Cursor object at 0x0000000002806B20>
conn.commit()
conn.close()