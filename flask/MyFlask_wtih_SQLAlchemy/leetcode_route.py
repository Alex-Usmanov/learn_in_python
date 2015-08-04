# coding:utf-8
import flask
from flask import Flask, request, render_template, redirect, url_for, flash, make_response
from flask.ext.bootstrap import Bootstrap
# from flask.ext.sqlachemy import SQLAlchemy
from flask.ext.wtf import Form
# import user
# import problem
import db




app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    name = request.cookies.get('username')
    print request.cookies
    return render_template('index.html', username=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        userdata = request.form.to_dict()
        # 载入数据库，遍历对比登录信息，当然，这个过程应该写成一个函数放到user.py里，这里就会清爽干净很多
        print 'login - userdata : ', userdata
        # FIXME 这里可以调试debug 的时候看看有没有正确把login 里面的用户信息传送进来
        users = user.load()
        for ur in users:
            # if userdata['name'] == ur["name"] and userdata['password']== ur['password']:
            if ur[1] == userdata['name']:
                if ur[2] == userdata['password']:
                    flash("login ok.\(^o^)/")
                    # set cookies
                    # response = flask.make_response(flask.redirect(flask.url_for('problems')))
                    # response.set_cookie('username', ur['name'])
                    response = flask.make_response(flask.redirect(flask.url_for('index')))
                    response.set_cookie('username', ur[1])
                    return response
        else:
            print ur[1], userdata['name']
            flash('password is not suit for the username.')
            # return '<h1> password is not suit for the username. </h1>'

    return render_template('login.html')


@app.route('/sign', methods=['POST', 'GET'])
def sign():
    if request.method == 'POST':
        userdata = request.form.to_dict()
        print 'sign - userdata : ', userdata
        # user.save(userdata)
        # 把新注册用户写入数据库（在实际中，会利用js 在页面里过滤不合法的 用户名和密码，然后直接把数据放进去）
        users = user.load()
        for ur in users:
            # if userdata['username'] == ur['name']:
            if userdata['username'] == ur[1]:
                flash(' User name already exists.')
            if len(userdata['name']) <= 2:
                flash(' User name should be more than 2 bytes. ')

        if userdata['password1'] == userdata['password']:
            del userdata['password1']
            # 两个密码相同，只需要存一个好了，所以把另一个删掉
            # FIXME ,存取数据，注意数据库
            user.save(userdata)
            flash('<h1> sign OK </h1>')
            response = make_response(redirect(url_for('index')))
            response.set_cookie('username', userdata['username'])
            return response
        else:
            flash('前后密码不匹配，请重新输入密码')
    return render_template('sign.html')


@app.route('/settings/<name>', methods=['POST', 'GET'])
def settings(name):
    username = request.cookies.get('username')
    if username == name:
        users_data = user.load()
        url = '/settings/' + str(name)
        if request.method == 'POST':
            user_password = request.form.to_dict()
            if user_password['password'] == user_password['password1']:
                del user_password['password1']
                for ur in users_data:
                    # if ur['name'] == name:
                    if ur[1] == name:
                        # ur['password'] = user_passwords['password1']
                        # user.cover(users_data)
                        user.update(ur[0], user_password)
                        return '<h1> 密码更改成功<h2>'
                        # FIXME user
        return render_template('settings.html', username=name, action_url=url)
    else:
        return redirect(url_for('/login'))
        # 必须是当前用户才可以修改密码,如果不是就要重新登陆


@app.route('/retrieve_password', methods=['POST', 'GET'])
def retrieve_password():
    if request.method == 'POST':
        user_email = request.form.to_dict()
        print 'user_email: ', user_email
        users = user.load()
        for ur in users:
            if ur[3] == user_email['email']:
                # 发送用户和密码 送给 该邮箱
                print ur['user_name'], ur['password']
                # return "<h1> 你好, 已经将密码发到 " + user_email['email'] + "</h1>"
                # UnicodeDecodeError: 'gbk' codec can't decode bytes in position 33-34: illegal multibyte sequence
                return "<h1> OK~ ,已经将密码发到你注册的邮箱</h1>"
        return "<h1> 咦？ 这个邮箱还没有注册耶~ ... <br>  come on ，baby  ❤ ~ </h1>"
    return render_template('retrieve_password.html')


# FIXME user


@app.route('/problems', methods=['POST', 'GET'])
def problems():
    # redirect to login page if no cookie
    username = request.cookies.get('username')
    if username is None:
        # FIXME, 注意这个url_for的参数是这个文件中出现的函数名比如 def index 这个index
        return flask.redirect(flask.url_for('login'))

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
            problem_url = "/problems/" + str(problem_id)
            problem_data['url'] = problem_url
            problem.save(problem_data)

    problems_data = problem.load()
    # 重新加载一次，这样才能立刻显示出新添加的题目
    return render_template('problems_list.html', problems=problems_data)


@app.route('/problems/<problem_id>', methods=['POST', 'GET'])
def problem_subpage(problem_id):
    # def create_problem_page(problem_id):
    # FIXME， 这个函数名字取得太烂了，应该叫problem
    # 另外id不对的时候应该abort(404)
    # 树： 然而如果叫problem 就会和 problem.py 命名冲突
    problems_data = problem.load()
    if int(problem_id) > len(problems_data):
        print len(problems_data)
        return '<h1> 没有这道题 <h1>', 404

    problem_data = problems_data[int(problem_id) - 1]
    # 如果不 problem_id -1，每次post 后，显示的是下一题的页面（感觉可以有妙用
    ''' 如果id 并不是自动生成排序，就要这样子判断存取了
    for pro in problems_data:
        if pro['id'] == problem_id:
            problem_data = pro
            # break
    '''
    if request.method == 'POST':
        solution_data = request.form.to_dict()
        solution_data["problem_id"] = problem_id
        problem.save_solution_db_file(problem_id, solution_data)
    solutions_data = problem.load_solution_db_file(problem_id)
    return render_template('problem_id.html', id=problem_id, problem=problem_data, solutions=solutions_data)
    # FIXME, model 的内容不应该放到C 里面来搞  OK
    # 这里根本没必要知道这个数据库存在哪里


# 添加一个新用户
# only admin can operate other users information
@app.route('/settings/user/add', methods=['POST', 'GET'])
def add_user():
    username = request.cookies.get('username')
    if username == 'admin':
        if request.method == 'POST':
            userdata = request.form.to_dict()
            if userdata['password'] == userdata['password1']:
                del userdata['password1']
                print userdata
                for i in userdata:
                    userdata[i] = userdata[i].encode('utf-8')
                user.save(userdata)
                print "add user OK : ", userdata
                usersdata = user.load()
                return flask.redirect(flask.url_for('settings/user/list'))
                # FIXME 添加成功后，进入 user_list 页面，查看资料
            else:
                return render_template('user_add.html', tips="<h1>输入密码前后不一致，请重新设置</h1>")
        return render_template('user_add.html')
    # return flask.redirect(flask.url_for('login'))
    return "<h1> 当前用户无权限查看该页面</h1>"


# /user/list
# 显示所有用户，以 table 的形式，带有 th 标签（表格头）
# 这个页面每个 条目 的最右边有一个 edit 超链接，点击跳转到 edit 页面
@app.route('/settings/user/list', methods=['POST', 'GET'])
def user_list():
    username = request.cookies.get('username')
    if username == 'admin':
        usersdata = user.load()
        return render_template('user_list.html', users_info=usersdata)
    else:
        return "<h1> 当前用户无权限查看该页面</h1>"


'''
/user/edit/<id>
    编辑这个用户的资料（就是密码和 email 可以编辑）
    这个页面由 list 页面跳转而来，id不存在（如果手动输入一个不存在的id）就404
    成功后跳转到 list 页面
    失败后停留在这个页面
'''


@app.route('/settings/user/edit/<id>', methods=['POST', 'GET'])
def edit_user(id):
    username = request.cookies.get('username')
    if username == 'admin':
        if user.search_id(id):
            default_user = user.search_id(id)
            print default_user
            if request.method == 'POST':
                user_data = request.form.to_dict()
                user.update(id, user_data)
                users_data = user.load()

                return render_template('user_list.html', user_id=id, users_info=users_data, default_info=default_user)
        return render_template('user_edit.html', user_id=id)
    else:
        return "<h1> 当前用户无权限查看该页面</h1>"


'''
/user/delete/<id>
    删除这个用户
    成功后跳转到 list 页面
    失败后也跳转到 list 页面（一般不会失败，所以先不管）
#  绝对黑魔法
'''


@app.route('/settings/user/delete/<id>', methods=['POST', 'GET'])
def delete_user(id):
    username = request.cookies.get('username')
    if username == 'admin':
        print 'delete user data : ', user.search_id(id)
        user.delete(id)
        return render_template('user_list.html')
    else:
        return "<h1> 当前用户无权限查看该页面</h1>"


'''
@app.errolhandler(404)
def page_not_found():
    return "<h1>page not found</h1>",404
'''

if __name__ == '__main__':
    app.debug = True
    app.run()
