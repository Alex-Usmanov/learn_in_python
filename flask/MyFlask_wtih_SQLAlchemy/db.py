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
    timestamp = db.Column(db.DateTime, default=db.DateTime)
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
    #
    creator = db.relationship('User', backref='problems')
    # 关系 ，一对多，向另一端Person模型添加一个 problems 的属性，可以访问Problem模型，返回模型对象，而不是外键
    solution_id = db.Column(db.Integer, db.ForeignKey('solutions.id'))
    # 属性3=solution_id,来自Solution模型的外键,用来查询答卷位置
    # FIXME ,怎样才可以让默认 每个Solution.id == Prolblem.id ?
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
    candidate_id = db.Column(db.String(50), db.ForeignKey('users.id'))
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


def save_user(name, password, email, problems_id=None, solutions_id=None):
    # 定义一个初始化人的信息和履历的数据表 模式
    user = User(name=name, password=password, email=email)
    # 传值，实例人员
    db.session.add(user)
    # 通过数据库会话管理对数据库所做的改动，准备把对象写入数据库之前，先要将其添加到会话中：
    if not problems_id:
        for i in problems_id:
            problems = Problem(id=i, create_id=user.id)
            db.session.add(problems)
    if not solutions_id:
        for k in solutions_id:
            solutions = Solution(id=k, candidate_id=user.id)
            db.session.add(solutions)
    db.session.commit()
    # 提交会话，把对象写入数据库


'''
def save_problem(problem_record):
    for title, detail, create_id, solution_id in problem_record:
        problem = Problem(title=title, detail=detail, create_id=create_id, solution_id=solution_id)
        db.session.add(problem)
    db.session.commit()
'''


def save_problem(title, detail, creator_id):
    problem = Problem(title=title, detail=detail, creator_id=creator_id)
    # solution=Solution(id=problem.id)
    db.session.add(problem)
    # db.session.add(solution)
    db.session.commit()


'''
def save_solution(solution_record):
    for detail, candidate_id in solution_record:
        solution = Solution(detail=detail, candidat_ide=candidate_id)
        db.session.add(solution)
    db.session.commit()
'''


def save_solution(solution_id, detail, candidate_id):
    solution = Solution(id=solution_id, detail=detail, candidat_ide=candidate_id)
    db.session.add(solution)
    db.session.commit()


def get_user_id(username):
    user = User.query.filter(User.name == username)
    return user.id


def load_user(user_id):
    user_data = User.query.filter(User.id == user_id)
    return user_data


def load_problem(problem_id):
    problem_data = Problem.query.filter(Problem.id == problem_id)
    return problem_data


def load_solution(solution_id):
    solution_data = Solution.query.filter(Solution.id == solution_id)
    return solution_data


def load_ones_problems(user_id):
    problems = Problem.query(Problem.id, Problem.title, Problem.detail).join(User).filter(
        Problem.creator_id == user_id).group_by(Problem.id)
    return problems


def load_one_solutions(user_id):
    solutions = db.session.query(Solution.id, Problem.title, Solution.detail, User.name).join(Problem).join(User).join(
        Solution).filter(User.id == user_id, Solution.candidate_id == user_id,
                         Problem.solution_id == Solution.id).group_by(Solution.id)

    return solutions


def test_user():
    save(User, {'name': 'dodoru', 'password': 'password', 'email': 'dodoru@do.com', 'timestamp': ''})


def test_all():
    # test_user() FIXME,save() has something wrong
    save_problem('test', 'detail', 1)
    save_user('melon', 'melon', 'melon@email.com')
    save_problem('testmelon', 'datailmelon', 2)
    save_solution(2, 'melon_detail', 1)
    print load_one_solutions(1)
    print load_ones_problems(2)
    print load_problem(2)
    print load_user(2)
    print load_solution(1)
    print load_solution(2)


if __name__ == '__main__':
    test_all()