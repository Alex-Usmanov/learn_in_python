# coding:utf-8
"""
A single page app exmploring how to use SQLAlchemy & Flask.
"""

import os, pdb
from sqlalchemy import distinct, func
from sqlalchemy.orm import scoped_session, sessionmaker
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)
app.debug = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlalchemy-demo.db'
# 程序使用的数据库 URL 必须保存到 Flask 配置对象的 SQLALCHEMY_DATABASE_URI 键中
db = SQLAlchemy(app)
# db 对象是 SQLAlchemy 类的实例，表示程序使用的数据库，同时获得 Flask-SQLAlchemy提供的所有功能

# 定义模型,一般是类，属性对应数据库表中的列

class User(db.Model):
    # db.Model 是基类，定义User 模型
    __tablename__ = 'users'
    # 表名 为 ‘users’，其余类变量为模型的属性（db.Column 类的实例）
    id = db.Column(db.Integer, primary_key=True)
    # 主键，一般为id
    name = db.Column(db.String(50), unique=True, nullable=False)
    # 属性1= name ,字符长度100以内
    password = db.Column(db.String(20))
    email = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=db.DateTime.Now)
    # Fixme ,test timestamp db.DateTime.Now  看看能不能自动初始化这个值

    def __repr__(self):
        return "%d -  %s ： %s , %s  ,  %s" % (self.id, self.name, self.password, self.email, str(self.timestamp))
        # 返回具有可读性的字符串来表示模型，调试和测试可以使用


class Problem(db.Model):
    # 定义 Job 模型
    __tablename__ = 'problems'
    # 表名为‘problems’
    id = db.Column(db.Integer, primary_key=True)
    # 主键id
    title = db.Column(db.String(200))
    detail = db.Column(db.String(1000))

    # 属性1=title, 字符长度200以内
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # 属性2=creator_name ,因为name 在 people 是 unique，所以是外键
    creator = db.relationship('User', backref='problems')
    # 关系 ，一对多，向另一端Person模型添加一个 problems 的属性，可以访问Problem模型，返回模型对象，而不是外键
    solution_id = db.Column(db.Integer, db.ForeignKey('solutions.id'))
    # 属性3=solution_id,来自Solution模型的外键,用来查询答卷位置
    solution = db.relationship('Solution', backref='problem')
    # 关系，一对多，向另一端的Solution模型添加一个problem的属性，可以用来查询它的题目
    def __repr__(self):
        return "%d - %s : %s by %s" % (self.id, self.title, self.detail, str(self.creator_name))
        # 返回具有可读性的字符串来表示模型，调试和测试可以使用


class Solution(db.Model):
    # 定义Company 模型
    __tablename__ = 'solutions'
    # 表名为companies
    id = db.Column(db.Integer, primary_key=True)
    # 主键 id
    detail = db.Column(db.String(2000))
    # score=db.Column(db.Integer,default=0)
    candidate_name = db.Column(db.String(50), db.ForeignKey('users.id'))
    candidate = db.relationship('User', backref='solutions')

    def __repr__(self):
        return self.detail
        # 返回具有可读性的字符串来表示模型，调试和测试可以使用


def save(Object, dict):
    # Object =Person,Problem,Solution,FIXME ,it is wrong
    temp = Object
    for k, w in dict:
        temp.k = w
    db.session.add(temp)
    db.commit()
    return temp


def load():
    pass


def save_user(name, password, email):
    # 定义一个初始化人的信息和履历的数据表 模式
    user = User(name=name, password=password, email=email)
    # 传值，实例人员
    db.session.add(user)
    # 通过数据库会话管理对数据库所做的改动，准备把对象写入数据库之前，先要将其添加到会话中：
    for company_name, title in work_history:
        # 传值，构造一个人的履历表
        employer = Company(name=company_name)  # 上家单位（工作单位）
        job = Job(title=title, person=person, employer=employer)  # 工作

        db.session.add(employer)
        # 准备把对象写入数据库之前，先添加到会话中：
        db.session.add(job)
        # 准备把对象写入数据库之前，先添加到会话中：
    db.session.commit()
    # 提交会话，把对象写入数据库


def setup_darrell():
    name = 'Darrell Silver'
    work_history = [
        ('Manhattan Sports', 'Rollerblade salesman'),
        ('Manhattan Sports', 'Private rollerblade lessons'),
        ('Vail Resorts', 'Guest Service'),
        ('Clinton Group', 'Statarb'),
        ('Perpetually', 'CEO'),
        ('Thinkful', 'CEO'),
    ]
    setup_person(name, work_history)
    # 初始化一个叫Darrell 的个人履历表


def setup_dan():
    name = 'Dan Friedman'
    work_history = [
        ('Dylan\'s Candy Shop', 'Associate'),
        ('Dylan\'s Candy Shop', 'Finance intern'),
        ('Ramaquois', 'Camp Counselor'),
        ('RRE', 'Summer analyst'),
        ('Elm City Labs', 'Product manager'),
        ('Thinkful', 'President'),
    ]
    setup_person(name, work_history)
    # 初始化一个叫Dan 的个人履历表


@app.route('/')
def index():
    # note we've not bothered with a template,
    # and encoding the URL will work both ways in modern browsers
    # (though encoding w/ %20 is preferable)
    return """<h1>LinkedIn 0.0.0.0.0.0.1</h1>
<pre>
    <a href="/Darrell%20Silver">Darrell</a>
    <a href="/Dan Friedman">Dan</a>
</pre>"""


@app.route('/<name>')
def career_history(name):
    # one strategy for querying
    jobs = Job.query.join(Person).filter(Person.name == name)
    # 通过查询Job模型里 人名name（外键 Person.name），把Job里面某人的所有工作经验都取出来

    # another querying strategy; more common, but uglier, IMO
    titles = db.session.query(Job.title).join(Person) \
        .filter(Person.name == name).distinct()
    # 通过查询Job模型里  人名name（外键 Person.name），把Job里面某人的所有职衔都取出来

    # is this any clearer than raw SQL? Seems silly.
    employers = db.session.query(Company.name, func.count(Company.id)) \
        .join(Job).join(Person) \
        .filter(Person.name == name).group_by(Company.name)
    # 限定人名，通过联合 Job 模型 和 Person 模型，找到某人的工作单位，并且按字母排列。

    return render_template('career_history.html', name=name, jobs=jobs,
                           titles=titles, employers=employers)
    # 把所有查询到的个人资料都放到这个人的简历模板里去


def main():
    print 'Dropping all...'
    db.drop_all()
    # 粗暴地删掉数据库
    print 'Creating all...'
    db.create_all()
    # 初始化数据库
    setup_darrell()
    print Person
    # 写进darrell 的信息数据表
    setup_dan()
    # 写进dan 的信息数据表
    print 'Starting app...'

    app.run()
    # 运行服务器


def test():
    save(Person, {'name': 'dodoru', 'password': 'password', 'email': 'dodoru@do.com', 'timestamp': ''})


if __name__ == '__main__':
    # main()
    test()

