from flask import Flask
from app.models.book import db
# from flask import current_app

def creat_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    regist_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)
    return app

def regist_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)#这里面这个register_blueprint是flask内置函数!!!