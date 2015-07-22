# coding:utf-8

from flask import Flask
from flask import request
from flask import render_template

import flask

import user

app = Flask(__name__)


# 添加一个新用户
# only admin can operate other users information
@app.route('/user/add', methods=['POST', 'GET'])
def add_user():
    username = request.cookies.get('username')
    if username == 'admin':
        if request.methods == 'POST':
            userdata = request.form.to_dict()
            if userdata['password'] == userdata['password1']:
                del userdata['password1']
                user.save(userdata)
                print "add user OK : ", userdata

                usersdata = user.load()
                return render_template('user_list.html', users_info=usersdata)
                # FIXME 添加成功后，进入 user_list 页面，查看资料
            else:
                return render_template('user_add.html', tips="<h1>输入密码前后不一致，请重新设置</h1>")
        return render_template('user_add.html')
    # return flask.redirect(flask.url_for('login'))
    return "<h1> 当前用户无权限查看该页面</h1>"


# /user/list
# 显示所有用户，以 table 的形式，带有 th 标签（表格头）
# 这个页面每个 条目 的最右边有一个 edit 超链接，点击跳转到 edit 页面
@app.route('/user/list', methods=['POST', 'GET'])
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


@app.route('/user/edit/<id>', methods=['POST', 'GET'])
def edit_user(id):
    username = request.cookies.get('username')
    if username == 'admin':
        if user.search_id(id):
            edit_id_url = '/user/edit/' + str(id)
            default_data = user.search_id(id)
            if request.methods == 'POST':
                user_data = request.form.to_dict()
                user.update(id, user_data)
                users_data = user.load()

                return render_template('user_list.html', users_info=users_data)
        return render_template('user_edit.html', action_url=edit_id_url, default_info=default_data)
    else:
        return "<h1> 当前用户无权限查看该页面</h1>"

'''
/user/delete/<id>
    删除这个用户
    成功后跳转到 list 页面
    失败后也跳转到 list 页面（一般不会失败，所以先不管）
'''

@app.route('/user/delete/<id>', methods=['POST', 'GET'])
def delete_user(id):
    username = request.cookies.get('username')
    if username == 'admin':
        if request.methods == 'POST':
            print 'delete user data : ', user.search_id(id)
            user.delete(id)
            return render_template('user_list.html')
        userdata = user.search_id(id)
        return render_template('user_delete.html', user_info=userdata)
    else:
        return "<h1> 当前用户无权限查看该页面</h1>"

if __name__ == '__main__':
    app.debug = True
    app.run()