# coding:utf-8

"""
A single page app exmploring how to use SQLAlchemy & Flask.
"""

import os, pdb
from sqlalchemy import distinct, func
from sqlalchemy.orm import scoped_session, sessionmaker
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)
app.debug = False
# ？？？ 这里我不太明白为什么要 False, 大概是要停止调试？ 等 main（） 再开始？
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlalchemy-demo.db'
# 程序使用的数据库 URL 必须保存到 Flask 配置对象的 SQLALCHEMY_DATABASE_URI 键中
db = SQLAlchemy(app)
# 定义模型
class Person(db.Model):
    __tablename__ = 'people'
    # 定义数据库中的表名为 people
    # db.Column 类构造函数的第一个参数是数据库列和模型属性的类型
    id = db.Column(db.Integer, primary_key=True)
    # 定义主键，SQLAlchemy 要求每个模型都要定义 主键 ，这一列经常命名为 id
    name = db.Column(db.String(100))
    # 定义属性1=name,名字长度100以内

    def __repr__(self):
        return self.name
        # ??? 不太明白为什么要 有这个函数……，大概是为了查看用户（people）表的时候显示方便?
        # 定义了 __repr()__ 方法，返回一个具有可读性的字符串表示模型，可在调试和测试时使用


class Job(db.Model):
    __tablename__ = 'jobs'
    # 定义这个数据表 的表名为 jobs
    id = db.Column(db.Integer, primary_key=True)
    # 主键id
    title = db.Column(db.String(100))
    # 定义属性1=title,标题长度100以内
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    # 定义属性2=person_id，对应做这份工作的人（people 表里的 Person ）的id
    # 因为id在people里是主键，所以这个属性person_id  在jobs里是外键
    person = db.relationship('Person', backref='jobs')
    # 定义关系，一对多关系，向Person 模型（第一个参数）添加 一个 'jobs' 的属性，从而定义反向关系。
    # 这个属性可以替代jobs_id 访问 Job 模型，从而获取模型对象，而不是外键的值

    employer_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    # 定义属性3=employer_id，对应所在公司（companies 表)里的 的id,外键
    employer = db.relationship('Company', backref='staff')
    # 定义关系，一对多，向Company 模型 添加一个 staff 的属性

    def __repr__(self):
        return "%s: %s at %s" % (str(self.person), self.title, str(self.employer))
        # 返回一个具有可读性的字符串表示模型，可在调试和测试时使用


class Company(db.Model):
    __tablename__ = 'companies'
    # d定义这个数据模型的 数据表名为 companies
    id = db.Column(db.Integer, primary_key=True)
    # 主键
    name = db.Column(db.String(100))
    # 公司名字，一百字符以内

    def __repr__(self):
        return self.name
        # 返回一个具有可读性的字符串表示模型，可在调试和测试时使用


def setup_person(name, work_history):
    # 设置 每个人的 数据信息，存取他的
    person = Person(name=name)
    # 传值，创建实例对象 person
    db.session.add(person)
    # 通过数据库会话管理对数据库所做的改动，准备把对象写入数据库之前，先要将其添加到会话中：
    for company_name, title in work_history:
        employer = Company(name=company_name)
        # 传值 创建实例对象 employer
        job = Job(title=title, person=person, employer=employer)
        # 传值 创建实例对象 job
        db.session.add(employer)
        # 把对象添加到会话 session 中，准备写入
        db.session.add(job)
        # # 把对象添加到会话 session 中，准备写入

    db.session.commit()
    # 提交回话，把对象写入数据库


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
    # 初始化 Darrell 的数据


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
    # 初始化 Dan 的数据


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

    # another querying strategy; more common, but uglier, IMO
    titles = db.session.query(Job.title).join(Person) \
        .filter(Person.name == name).distinct()

    # is this any clearer than raw SQL? Seems silly.
    employers = db.session.query(Company.name, func.count(Company.id)) \
        .join(Job).join(Person) \
        .filter(Person.name == name).group_by(Company.name)

    return render_template('career_history.html', name=name, jobs=jobs,
                           titles=titles, employers=employers)


def main():
    app.debug == True
    print 'Dropping all...'
    db.drop_all()
    print 'Creating all...'
    db.create_all()
    setup_darrell()
    setup_dan()
    print 'Starting app...'
    app.run()


if __name__ == '__main__':
    main()

