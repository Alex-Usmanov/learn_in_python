# coding:utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import sql

app = Flask(__name__)
app.secret_key = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'

db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='todos')
    timestamp = db.Column(db.DateTime(timezone=True), default=sql.func.now())

    def __repr__(self):
        return u'< ToDo ,{0} ,{1} ,{2},{3} >'.format(self.id, self.task, self.timestamp, self.user_id)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20))
    email = db.Column(db.String(20))

    def __repr__(self):
        return u'< User,{0},{1},{2},{3} >'.format(self.id, self.username, self.email, self.todos)


def test():
    ur = User(username='dodoru', password='dodoru', email='dodoru@todo.com')
    print ur
    db.session.add(ur)
    db.session.commit()
    print ur

    tt = Todo()
    tt.task = 'task'
    tt.user_id = 1
    # tt.user=ur
    print tt
    db.session.add(tt)
    db.session.commit()
    print tt

    print ur


def test2():
    ur = User(username='dodoru', password='dodoru', email='dodoru@todo.com')
    print ur
    db.session.add(ur)
    db.session.commit()
    print ur


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    print("rebuild database")
    # test2()
    test()