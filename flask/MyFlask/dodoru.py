# coding:utf-8

from flask import Flask
from flask import request
from flask import render_template
import os

import user
import problem

# user_db_file = 'user.db.txt'
# message_db_file = 'message.db.txt'
# problem_db_file = 'problem.db.txt'

# 创建一个存取数据的文本文件
# from user import
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
            if userdata['name'] == ur["name"]:
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
        # users = user.load(user_db_file)
        users = user.load()
        for ur in users:
            if userdata['name'] == ur['name']:
                return '<h1> User name already exists </h1>'
            if len(userdata['name']) <= 2:
                return '<h1> User name should be more than 2 bytes.</h2>'
                # 应该弹出 提示框

        if userdata['password1'] == userdata['password']:
            del userdata['password1']
            # 两个密码相同，只需要存一个好了，所以把另一个删掉
            user.save(userdata)
            return '<h1> sign OK </h1>'
        else:
            return '<h1>前后密码不匹配，请重新输入密码</h1>'
            # 应该弹出 提示框
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


@app.route('/problems_list', methods=['POST', 'GET'])
def problems_list():
    problems_data = problem.load()
    problems_totality = len(problems_data)

    if request.method == 'POST':
        problem_data = request.form.to_dict()
        problem_id = problems_totality + 1
        problem_data['id'] = problem_id

        print "problem_data : ", problem_data

        for pro in problems_data:
            if pro['title'] == problem_data['title']:
                return "<h1> 这个问题题目已经存在，请重新提问。</h1>"
                # 应出现提示框 提醒才对

        if len(problem_data['title']) <= 2:
            return "<h1>the title should more than 2 bytes </h1>"
        else:
            problem_url = "/problems_list/" + str(problem_id)
            problem_data['url'] = problem_url
            problem.save(problem_data)
            # problems=user.load(problem_db_file)
    problems_data = problem.load()
    # 重新加载一次，这样才能立刻显示出新添加的题目
    return render_template('problems_list.html', problems=problems_data)


@app.route('/problems_list/<problem_id>', methods=['POST', 'GET'])
def create_problem_page(problem_id):
    pro_id = problem_id
    problems_data = problem.load()
    problem_data = problems_data[int(pro_id) - 1]
    # problem_data =problems_data[int(pro_id)] 如果不-1，每次post 后，显示的是下一题的页面
    '''
    for pro in problems_data:
        if pro['id'] == problem_id:
            problem_data = pro
            # break
    '''
    print problem_data

    solutions_data = None
    problem_id_solution_file = 'problem_' + str(pro_id) + '_solution.db.txt'
    # 存取这个问题答案的数据文件名
    if request.method == 'POST':
        problem_solution = request.form.to_dict()
        problem_solution["problem_id"] = pro_id
        # 自动生成 problem_id 条目 放在 字典里

        # 生成存取这个问题答案的数据文件
        with open(problem_id_solution_file, 'a') as fb:
            # problem.save(problem_solution, fb)
            # 这样会出错，不明白为什么 coercing to Unicode: need string or buffer, file found
            problem.save(problem_solution, problem_id_solution_file)
        print "problem_solution : ", problem_solution
        solutions_data = problem.load(problem_id_solution_file)

    if os.path.exists(problem_id_solution_file):
        solutions_data = problem.load(problem_id_solution_file)
        # 判断是否已经存在 这个文件

    return render_template('problem_id.html', id=problem_id, problem=problem_data, solutions=solutions_data)


if __name__ == '__main__':
    app.debug = True
    app.run()
