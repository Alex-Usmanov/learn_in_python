# coding:utf-8

from flask import Flask
from flask import request
from flask import render_template
from flask.ext.bootstrap import  Bootstrap

app=Flask(__name__)
bootstrap=Bootstrap(app)

@app.route('/')
def index():
    user_agent=request.headers.get('User_Agent')
    print "<h1>hello world~</h1>"
    # return  "<p>Your browser is %s </p>"%user_agent
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    # return '<h1>hello,%s </h1>' %name
    return render_template('user.html')

@app.route('/error')
def error():
    # return '<h1> bad request </h1>',200
    return '<h1> bad request </h1>',400


if __name__=="__main__":
    app.run(debug=True)
