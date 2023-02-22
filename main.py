#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_restx import Api

from app.config import Config
# from app.setup_db import db

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.views.auth import auth_ns
from app.views.users import user_ns
from app.views.movies import movie_ns
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.favorite import favorite_ns


# authentication = {
#     "Bearer": {
#         "type": "apiKey",
#         "in": "header",
#         "name": "Authorization"
#     }
# }


# def create_app(config: Config) -> Flask:
# def create_app():
application = Flask(__name__)
# application.config['DEBUG'] = True
application.config['JSON_AS_ASCII'] = False
# application.config['SERVER_NAME'] = '127.0.0.1:25000'
application.config['SECRET_KEY'] = '249y823r9v8238r9u'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./data/movies.db'
application.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://flask_app:flask@192.168.1.102/flask_app"
application.config['POSTS_PER_PAGE'] = 12  # пагинация, вывод данных на страницу
application.config['MAX_PAGE'] = 100  # максимальное количество страниц
# application.config.from_object(config)
application.config.from_pyfile("app/config.py")
application.config.from_envvar("APP_SETTINGS", silent=True)
application.app_context().push()
    # return application


db = SQLAlchemy()
migrate = Migrate(application, db)

# def configure_app(application: Flas:
db.init_app(application)
api = Api(
    app=application,
    title="SkyPro: auth_JWT_email",
    # doc="/docs",
)
api.add_namespace(auth_ns)
api.add_namespace(user_ns)
api.add_namespace(movie_ns)
api.add_namespace(director_ns)
api.add_namespace(genre_ns)
api.add_namespace(favorite_ns)


if __name__ == '__main__':
    # app_config = Config()
    # app = create_app(app_config)
    # configure_app(app)
    application.run()

