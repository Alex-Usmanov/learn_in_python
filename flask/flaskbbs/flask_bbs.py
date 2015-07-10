from flask import Flask
from flask import request
from flask import render_template

import message


app = Flask(__name__)


@app.route('/')
def index():
    return '<a href="/bbs">BBS</a>'


@app.route('/bbs', methods=['POST', 'GET'])
def bbs():
    # print request.method
    # print request.form
    if request.method == 'POST':
        msg = request.form.to_dict()
        print msg
        message.save(msg)
    return str(message.load())


if __name__ == '__main__':
    app.debug = True
    app.run()
