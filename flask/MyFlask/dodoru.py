# coding:utf-8

from flask import Flask
from flask import request
from flask import render_template

from user_data import *
app=Flask(__name__)

@app.route('/')
def index():
    # return '<a href="/login">LOGIN</a> &nbsp&nbsp&nbsp&nbsp <a href="/sign">SIGN</a>'
    return render_template('index.html')


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        userdata=request.form.to_dict()

    return render_template('login.html')

@app.route('/sign',methods=['POST','GET'])
def sign():
    if request.method=='POST':
        userdata=request.form.to_dict()

    return render_template('sign.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html')

if __name__=='__main__':
    app.debug=True
    app.run()
