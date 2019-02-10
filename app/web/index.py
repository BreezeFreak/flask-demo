from functools import wraps

from flask import render_template, session, flash, request, redirect

from app.libs.validate import UpdateValidate, ChargeValidate
from app.libs.helper import add_record
from . import web
from app import App


def login_check(func):
    @wraps(func)
    def inner():
        if session.get('username'):
            current_account = session.get('username')
            return func(current_account)
        else:
            return redirect('/login')
    return inner


@web.route('/')
@login_check
def index(current_account):
    flash(current_account)
    return render_template('index.html')


@web.route('/accounts')
@login_check
def account(current_account):
    user = App().mongo.db.user
    result = user.find_one({'name': current_account})
    return render_template('accounts.html', account=result)


@web.route('/records')
@login_check
def records(current_account):
    user = App().mongo.db.user
    result = user.find_one({'name': current_account}).get('purchase_record')
    if result:
        return render_template('records.html', record=result.items())
    else:
        return render_template('records.html')


@web.route('/update', methods=['POST'])
@login_check
def update(current_account):
    forms = UpdateValidate(request.form)
    if forms.validate():
        user = App().mongo.db.user
        result = user.find_one({'name': current_account})
        result["name"] = forms.name.data
        result["password"] = forms.password.data
        user.save(result)

        session['username'] = forms.name.data
        return redirect('/accounts')
    else:
        return str(forms.errors)


@web.route('/charge', methods=['POST'])
@login_check
def charge(current_account):
    forms = ChargeValidate(request.form)
    if forms.validate():
        money = float(forms.charge.data)
        user = App().mongo.db.user
        result = user.find_one({'name': current_account})

        result["wallet"] += money
        user.save(add_record(result, money, charge=True))
        return redirect('/records')
    else:
        return str(forms.errors)


@web.route('/buy')
@login_check
def buy(current_account):
    price = float(request.args.get('price'))
    user = App().mongo.db.user
    result = user.find_one({'name': current_account})
    if result.get("wallet") and result.get("wallet") >= price:
        result["wallet"] -= price
        user.save(add_record(result, price, buy=True))
    else:
        return '余额不足'
    return redirect('/records')


@web.route('/delete')
@login_check
def delete(current_account):
    user = App().mongo.db.user
    result = user.find_one({'name': current_account})
    user.delete_one(result)
    return redirect('/login')
