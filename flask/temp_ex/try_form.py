# coding: utf-8

from flask import Flask,render_template,session,redirect,url_for,flash
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextField
from wtforms.validators import Required

from flask.ext.bootstrap import Bootstrap
# 4.2

app=Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'
# 实现 CSRF 保护，Flask-WTF 需要程序设置一个密钥, then 生成加密令牌，再用令牌验证请求中表单数据的真伪。
# app.config 字典可用来存储框架、扩展和程序本身的配置变量。可以在文件（比较安全）或者环境中导入指
boostrap=Bootstrap(app)
# 初始化 Flask-Bootstrap 之后，就可以在程序中使用一个包含所有 Bootstrap 文件的基模板。

class NameForm(Form):
    name = StringField("what id your name ? ", validators=[Required()])
    # br=TextField("<br><br>")
    # StringField类表示属性为 type="text" 的 <input> 元素
    # 字段对象可附属一个或多个验证函数。验证函数用来验证用户提交的输入值是否符合要求。
    submit=SubmitField('Submit')
    #  SubmitField 类表示属性为 type="submit" 的<input> 元素。
    # 字段构造函数的第一个参数是把表单渲染成 HTML 时使用的标号。


@app.route('/',methods=['GET','POST'])
def index():
    # name=None
    form=NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('looks like you have changed your name')
        session['name']=form.name.data
        return redirect(url_for('index'))
        # form.name.data=''
        # 清空
    return render_template('index.html',form=form,name=session.get('name'))


if __name__=="__main__":
    app.debug=True
    app.run()