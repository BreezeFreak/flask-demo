from . import web
from flask import render_template, request, redirect, url_for, jsonify, session
from app import App


@web.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        pwd = request.form['password']

        user = App().mongo.db.user
        result = user.find_one({"name": name})
        if result:
            if name == result['name'] and pwd == result['password']:
                session['username'] = name
                session.permanent = True
                return 'ok'
            else:
                return 'error'
        else:
            return '没有该用户名，请注册'
    return render_template('login.html')


@web.route('/register/', methods=['POST'])
def register():
    name = request.form['username']
    pwd = request.form['password']
    user = App().mongo.db.user
    result = user.find_one({"name": name})
    if result:
        return 'exist'
    else:
        user.insert({"name": name, "password": pwd, "wallet": 0, "purchase_record": {}})
        session['username'] = name
        session.permanent = True
        return 'ok'


@web.route('/logout/')
def logout():
    session.clear()
    return redirect('/login')
