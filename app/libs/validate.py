from wtforms import Form, StringField, FloatField
from wtforms.validators import Length, NumberRange, EqualTo


class UpdateValidate(Form):
    name = StringField(validators=[Length(min=1, max=20, message='长度介于1到20')])
    password = StringField(validators=[Length(min=3, max=16, message='长度介于3到16')])
    password2 = StringField(
        validators=[Length(min=3, max=16, message='长度介于3到16'), EqualTo('password', message='两次密码不一致')])


class ChargeValidate(Form):
    charge = FloatField(validators=[NumberRange(min=0.01, message='请充值大于0的数额')])

