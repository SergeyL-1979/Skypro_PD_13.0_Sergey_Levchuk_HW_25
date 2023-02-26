#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_restx import Api

from app.config import Config
from app.setup_db import db
from app.setup_db import migrate

from app.views.auth import auth_ns
from app.views.users import user_ns
from app.views.movies import movie_ns
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.favorite import favorite_ns


authentication = {
    "Bearer": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def configure_app(application: Flask):
    # migrate.init_app(application, db)
    db.init_app(application)

    api = Api(
        app=app,
        title="SkyPro: auth_JWT_email",
        # doc="/docs",
        authorizations=authentication
    )
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(favorite_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    app.run()
