from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """docstring for ClassName"""
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    pwd = Column(String(16), nullable=False)
    wallet = Column(Float)

# def __init__(self, arg):
# 	super(ClassName, self).__init__()
# 	self.arg = arg
