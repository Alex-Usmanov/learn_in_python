# coding:utf-8
"""
A single page app exmploring how to use SQLAlchemy & Flask.
"""

import os, pdb
from sqlalchemy import sql
from sqlalchemy.orm import scoped_session, sessionmaker
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'secret key'
app.debug = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlalchemy-demo.db'
# 程序使用的数据库 URL 必须保存到 Flask 配置对象的 SQLALCHEMY_DATABASE_URI 键中
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(20))
    email = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime(timezone=True), default=sql.func.now())
    # set default time

    def __repr__(self):
        return u"< {0} , {1} >".format(self.name, self.email)
        # return u"< User {0} , {1}, {2} ,{3}>".format(self.id, self.name, self.email, self.timestamp)


class Problem(db.Model):
    __tablename__ = 'problems'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    detail = db.Column(db.String(1000))
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    creator = db.relationship('User', backref='problems')
    # solution_id = db.Column(db.Integer, db.ForeignKey('solutions.id'))
    # solution = db.relationship('Solution', backref='problem')
    #

    def __repr__(self):
        return u"< Problem {0}, {1}, cid : {2}>".format(self.id, self.title, self.creator_id)


class Solution(db.Model):
    __tablename__ = 'solutions'
    id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.String(2000))
    score = db.Column(db.Integer, default=0)
    candidate_id = db.Column(db.String(50), db.ForeignKey('users.id'))
    candidate = db.relationship('User', backref='solutions')
    problem_id = db.Column(db.Integer, db.ForeignKey('problems.id'))
    problem = db.relationship('Problem', backref='solutions')

    def __repr__(self):
        return u"< Solution {0} , {1}, {2} ,{3} >".format(self.id, self.detail, self.candidate_id, self.problem_id)



if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    print('rebuild database')

'''

# the following save()s and load()s clumsily imitate the  save() and load() in the origin db.py
# please ignore them and take it as a funny joke :D
def save(Object, dict):
    # Object =Person,Problem,Solution,FIXME ,it is wrong
    temp = Object
    for k, w in dict:
        temp.k = w
    db.session.add(temp)
    db.commit()
    return temp

def save_user(name, password, email, problems_id=None, solutions_id=None):
    user = User(name=name, password=password, email=email)
    db.session.add(user)
    if problems_id:
        for i in problems_id:
            problems = Problem(id=i, create_id=user.id)
            db.session.add(problems)
    if solutions_id:
        for k in solutions_id:
            solutions = Solution(id=k, candidate_id=user.id)
            db.session.add(solutions)
    db.session.commit()


def save_problem(title, detail, creator_id):
    problem = Problem(title=title, detail=detail, creator_id=creator_id)
    # solution=Solution(id=problem.id)
    db.session.add(problem)
    # db.session.add(solution)
    db.session.commit()


def save_solution(solution_id, detail, candidate_id):
    solution = Solution(id=solution_id, detail=detail, candidate_id=candidate_id)
    db.session.add(solution)
    db.session.commit()


def get_user_id(username):
    user = User.query.filter(User.name == username)
    return user.id


def get_user_by_name(username):
    user = User.query.filter(User.name == username)
    return user


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
    problems = db.session.query(Problem.id, Problem.title, Problem.detail).join(User).filter(
        Problem.creator_id == user_id).group_by(Problem.id)
    return problems


def load_one_solutions(user_id):
    solutions = db.session.query(Solution.id, Problem.title, Solution.detail, User.name).join(Problem).join(User).join(
        Solution).filter(User.id == user_id, Solution.candidate_id == user_id,
                         Problem.solution_id == Solution.id).group_by(Solution.id)
    return solutions


def main():
    print 'Dropping all...'
    db.drop_all()
    # 粗暴地删掉数据库
    print 'Creating all...'
    db.create_all()


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

    '''