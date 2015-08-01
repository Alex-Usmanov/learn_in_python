# coding:utf-8

import os
# from sqlite3 import dbapi2 as sqlite3
import sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, make_response

app = Flask(__name__)
'''
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'mini_blog.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('MINI_BLOG_SETTINGS', silent=True)
# 设置一个名为 FLASKR_SETTINGS 环境变量来设定一个配置文件载入后是否覆盖默认值。
# 静默开关告诉 Flask 不去关心这个环境变量键值是否存在。

'''
DATABASE = 'mini_blog.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin',
PASSWORD = 'default'

app.config.from_object(__name__)

def connect_db():
    ''' connects to the specific  database.  '''
    """
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv
    """
    return sqlite3.connect(app.config['DATABASE'])


# FIXME,FIND OUT why

def get_db():
    """Opens a new database connection if there is none yet for the current application context."""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def init_db():
    # db = get_db()
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
    db.commit()
    ''' http://www.pythondoc.com/flask/tutorial/dbinit.html?highlight=executescript
    from contextlib import closing
    closing() 助手函数允许我们在 with 块中保持数据库连接可用。
    应用对象的open_resource() 方法在其方框外也支持这个功能，因此可以在 with 块中直接使用。
    这个函数从资源位置（你的 flaskr 文 件夹）中打开一个文件，并且允许你读取它。
    '''  #


@app.before_request
def before_request():
    g.db = connect_db()


@app.after_request

:
def after_request(excepthon):
    g.db.close()


@app.teardown_appcontext
def close_db(error):
    ''' close the database again at the end of the request '''
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc ')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title,text) values (?,?)', [request.form['title'], request.form['text']])
    db.commit()
    flash('new entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('LOGGING...')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    init_db()
    app.debug = True
    app.run()





