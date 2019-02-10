from flask import Flask
# from app.models.user import db
from flask_pymongo import PyMongo


class App():

    @classmethod
    def create_app(cls):
        cls.app = Flask(__name__)

        cls.app.config.from_object('app.settings')
        cls.app.config.from_object('app.secure')

        cls.register_blueprint(cls.app)

        cls.mongo = PyMongo(cls.app)

        # db.init_app(app)
        # db.create_all(app=app)
        return cls.app

    @staticmethod
    def register_blueprint(app):
        from .web import web
        app.register_blueprint(web)
        # from .admin import web
        # app.register_blueprint(web)
