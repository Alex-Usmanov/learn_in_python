# coding:utf-8

from flask import Flask
from flask import request
from flask import render_template

import user
# from user import *
# 一般说来，应该避免使用from..import而使用import语句，
# 因为这样可以使你的程序更加易读，也可以避免名称的冲突
app = Flask(__name__)


@app.route('/')
def index():
    # return '<a href="/login">LOGIN</a> &nbsp&nbsp&nbsp&nbsp <a href="/sign">SIGN</a>'
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        userdata = request.form.to_dict()
        # 载入数据库，遍历对比登录信息，当然，这个过程应该写成一个函数放到user.py里，这里就会清爽干净很多
        print 'login - userdata : ', userdata
        # 这里可以调试debug 的时候看看有没有正确把login 里面的用户信息传送进来
        users = user.load()
        for ur in users:
            # if userdata['user_name'] == u['user_name'] and userdata['password'] == u['password1']:
            # 瓜 原来没有对 对password 提出校验的需求，所以用户的数据信息是直接存进去两次输入的密码
            # 所以，这里登陆以第一次输入的密码 password1 为主（key）
            if userdata['user_name'] == ur["user_name"]:
                # user_exist=True
                if userdata['password'] == ur['password']:
                    print "login ok.\(^o^)/"
                    return '<h1>login ok</h1>'
                else:
                    return '<h1> password is not suit for the username. </h1>'
                    # 因为这里返回去查看是否存在用户名没多大用处，所以一般网站都只是显示“用户名和密码不匹配”
                    # 当然，可以设置一个 user_exist 来判定是否存在该用户
    return render_template('login.html')


@app.route('/sign', methods=['POST', 'GET'])
def sign():
    if request.method == 'POST':
        userdata = request.form.to_dict()
        print 'sign - userdata : ', userdata
        # user.save(userdata)
        # 把新注册用户写入数据库（在实际中，会利用js 在页面里过滤不合法的 用户名和密码，然后直接把数据放进去）
        # 但是我决定要模仿瓜实例的 login 也对 sign 改一下，因为js不太熟练，我想尝试新技能
        # '''
        users = user.load()
        for ur in users:
            if userdata['user_name'] == ur['user_name']:
                return '<h1> User name already exists </h1>'

        if userdata['password1'] == userdata['password']:
            del userdata['password1']
            # 两个密码相同，只需要存一个好了，所以把另一个删掉
            user.save(userdata)
            return '<h1> sign OK </h1>'
        else:
            print "前后密码不匹配，请重新输入密码"
    return render_template('sign.html')


# 名字和 user.py 冲突了
# @app.route('/user/<name>')
# def user(name):
# return render_template('user.html')
@app.route('/retrieve_password', methods=['POST', 'GET'])
def retrieve_password():
    if request.method == 'POST':
        user_email = request.form.to_dict()
        print 'user_email: ', user_email
        users = user.load()
        for ur in users:
            if ur['email'] == user_email['email']:
                # 发送用户和密码 送给 该邮箱
                print ur['user_name'], ur['password']
                # return "<h1> 你好, 已经将密码发到 " + user_email['email'] + "</h1>"
                # UnicodeDecodeError: 'gbk' codec can't decode bytes in position 33-34: illegal multibyte sequence
                return "<h1> OK~ ,已经将密码发到你注册的邮箱</h1>"
        return "<h1> 咦？ 这个邮箱还没有注册耶~ ... <br>  come on ，baby  ❤ ~ </h1>"
    return render_template('retrieve_password.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
