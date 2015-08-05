# coding:utf-8
# https://github.com/Thinkful/sqlalchemy-demo
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

class Person(db.Model):
    # db.Model 是基类，定义Person 模型
    __tablename__ = 'people'
    # 表名 为 ‘people’，其余类变量为模型的属性（db.Column 类的实例）
    id = db.Column(db.Integer, primary_key=True)
    # 主键，一般为id
    name = db.Column(db.String(100))
    # 属性1= name ,字符长度100以内

    def __repr__(self):
        return self.name
        # 返回具有可读性的字符串来表示模型，调试和测试可以使用


class Job(db.Model):
    # 定义 Job 模型
    __tablename__ = 'jobs'
    # 表名为‘jobs’
    id = db.Column(db.Integer, primary_key=True)
    # 主键id
    title = db.Column(db.String(100))
    # 属性1=title, 字符长度100以内
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    # 属性2=person_id,因为person.id 是Person模型的主键，所以是外键
    person = db.relationship('Person', backref='jobs')
    # 关系 ，一对多，向另一端Person模型添加一个 jobs 的属性，可以访问Job模型，返回模型对象，而不是外键

    employer_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    # 属性3=employer_id,来自Company模型的外键,用来查询工作所在的单位
    employer = db.relationship('Company', backref='staff')
    # 关系，一对多，向另一端的Company模型添加一个staff的属性，可以用来查询它的员工
    def __repr__(self):
        return "%s: %s at %s" % (str(self.person), self.title, str(self.employer))
        # 返回具有可读性的字符串来表示模型，调试和测试可以使用


class Company(db.Model):
    # 定义Company 模型
    __tablename__ = 'companies'
    # 表名为companies
    id = db.Column(db.Integer, primary_key=True)
    # 主键 id
    name = db.Column(db.String(100))
    # 属性1=name ,公司名字字长100以内

    def __repr__(self):
        return self.name
        # 返回具有可读性的字符串来表示模型，调试和测试可以使用


def setup_person(name, work_history):
    # 定义一个初始化人的信息和履历的数据表 模式
    person = Person(name=name)
    # 传值，实例人员
    db.session.add(person)
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

    print jobs
    print titles
    print employers

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
    # 写进darrell 的信息数据表
    setup_dan()
    # 写进dan 的信息数据表
    print 'Starting app...'

    app.run()
    # 运行服务器


if __name__ == '__main__':
    main()

'''
# templates/career_history.html

<html>
<body>
<h1>LinkedIn 0.0.0.0.0.0.1</h1>
<h2>Work History for <em>{{name}}</em>:</h2>

<h3>Jobs ({{jobs.count()}}):</h3>
<!-- <h4>{{jobs}}</h4> -->
<ol>{%for job in jobs%}
    <li>{{job.title}} at {{job.employer.name}}</li>
{%endfor%}</ol>


<h3>Titles ({{titles.count()}}):</h3>
<ol>{%for title in titles%}
	<li>{{title[0]}}</li>
{%endfor%}</ol>

<h3>Employers ({{employers.count()}}):</h3>
<ol>{%for employer, num_jobs in employers%}
	<li>{{employer}} ({{num_jobs}} jobs)</li>
{%endfor%}</ol>

</body>
</html>

'''