# coding:utf-8

from flask.ext.wtf import Form
from flask.ext.sqlalchemy import SQLAlchemy
import os
import flask
from flask import Flask, render_template

# 5.5
# def config_SQLite():
basedir = os.path.abspath(os.path.dirname(__file__))

app = flask.Flask(__name__)
print app.config
'''
<Config {'JSON_AS_ASCII': True, 'USE_X_SENDFILE': False, 'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_DOMAIN': None, 'SESSION_COOKIE_NAME': 'session', 'LOGGER_NAME': '__main__', 'DEBUG': False, 'SECRET_KEY': None, 'MAX_CONTENT_LENGTH': None, 'APPLICATION_ROOT': None, 'SERVER_NAME': None, 'PREFERRED_URL_SCHEME': 'http', 'JSONIFY_PRETTYPRINT_REGULAR': True, 'TESTING': False, 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 'PROPAGATE_EXCEPTIONS': None, 'TRAP_BAD_REQUEST_ERRORS': False, 'JSON_SORT_KEYS': True, 'SESSION_COOKIE_HTTPONLY': True, 'SEND_FILE_MAX_AGE_DEFAULT': 43200, 'PRESERVE_CONTEXT_ON_EXCEPTION': None, 'SESSION_COOKIE_SECURE': False, 'TRAP_HTTP_EXCEPTIONS': False}>

'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# 程序使用的数据库 URL 必须保存到 Flask 配置对象的 SQLALCHEMY_DATABASE_URI 键中
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 即 SQLALCHEMY_COMMIT_ON_TEARDOWN 键，将其设为 True时，每次请求结束后都会自动提交数据库中的变动。
print app.config
'''
<Config {'JSON_AS_ASCII': True, 'USE_X_SENDFILE': False, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///E:\\mydocument\\python\\github\\learn_in_python\\learn_in_python\\flask\\temp_ex\\data.sqlite', 'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_DOMAIN': None, 'SESSION_COOKIE_NAME': 'session', 'LOGGER_NAME': '__main__', 'DEBUG': False, 'SQLALCHEMY_COMMIT_ON_TEARDOWN': True, 'SECRET_KEY': None, 'MAX_CONTENT_LENGTH': None, 'APPLICATION_ROOT': None, 'SERVER_NAME': None, 'PREFERRED_URL_SCHEME': 'http', 'JSONIFY_PRETTYPRINT_REGULAR': True, 'TESTING': False, 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 'PROPAGATE_EXCEPTIONS': None, 'TRAP_BAD_REQUEST_ERRORS': False, 'JSON_SORT_KEYS': True, 'SESSION_COOKIE_HTTPONLY': True, 'SEND_FILE_MAX_AGE_DEFAULT': 43200, 'PRESERVE_CONTEXT_ON_EXCEPTION': None, 'SESSION_COOKIE_SECURE': False, 'TRAP_HTTP_EXCEPTIONS': False}>
'''

db = SQLAlchemy(app)

# 5.6 定义模型
# Flask-SQLAlchemy 要求每个模型都要定义 主键 ，这一列经常命名为 id
class Role(db.Model):
    __tablename__ = 'roles'
    # 类变量 __tablename__ 定义在数据库中使用的表名
    # 如果没有定义 __tablename__ ，Flask-SQLAlchemy 会使用一个默认名字，但默认的表名没有遵守使用复数形式进行命名的约定
    # 其余的类变量都是该模型的属性，被定义为 db.Column类的实例。
    id = db.Column(db.Integer, primary_key=True)
    # db.Column 类构造函数的第一个参数是数据库列和模型属性的类型
    # db.Column 中其余的参数指定属性的配置选项
    name = db.Column(db.String(64), unique=True)

    # FixMe 5.7 关系
    '''
        关系图表示用户和角色之间的一种简单关系。
        这是角色到用户的一对多关系，因为一个角色可属于多个用户，而每个用户都只能有一个角色。
        users 属性将返回与角色相关联的用户组成的列表。
        db.relationship() 的第一个参数表明这个关系的另一端是哪个模型.
        如果模型类尚未定义，可使用字符串形式指定。

        db.relationship() 中的 backref 参数向 User 模型中添加一个 role 属性，从而定义反向关系。
        这一属性可替代 role_id 访问 Role 模型，此时获取的是模型对象，而不是外键的值。
        '''
    # users = db.relationship('User', backref='role')
    users = db.relationship('User', backref='role', lazy='dynamic')


    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    # index 如果设为 True ，为这列创建索引，提升查询效率
    # FixMe 5.7 关系
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    '''
        关系使用 users 表中的外键连接了两行。
        添加到 User 模型中的 role_id 列被定义为外键，就是这个外键建立起了关系。
        传给 db.ForeignKey() 的参数 'roles.id' 表明，这列的值是 roles 表中行的 id 值。
    '''

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/', methods=['POST', 'GET'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['Known'] = False
        else:
            session['Known'] = True
        session['name'] = True
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))


'''
    提交表单后，程序会使用 filter_by() 查询过滤器在数据库中查找提交的名字。
    变量 known 被写入用户会话中，因此重定向之后，可以把数据传给模板，用来显示自定义的欢迎消息。
    注意，要想让程序正常运行，你必须按照前面介绍的方法，在 Python shell 中创建数据库表。
'''
if __name__ == '__main__':
    app.debug = True
    app.run()