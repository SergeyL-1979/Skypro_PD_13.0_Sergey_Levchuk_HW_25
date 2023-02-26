#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
# ==== ИМПОРТИРУЕМ load_dotenv ====
from dotenv import load_dotenv

# ==== НАСТРОЙКА ПУТИ К basedir ====
basedir = os.path.abspath(os.path.dirname(__file__))

# ==== АКТИВАЦИЯ БИБЛИОТЕКИ python-dotenv ====
load_dotenv(override=True)
# load_dotenv(os.path.join(basedir, ".flaskenv"))


class Config(object):
    DEBUG = True
    JSON_AS_ASCII = False
    # SERVER_NAME = '127.0.0.1:15000'
    SERVER_NAME = '127.0.0.1:25000'
    SECRET_KEY = '249y823r9v8238r9u'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///./data/movies.db'
    SQLALCHEMY_DATABASE_URI = "postgresql://flask_app:flask@localhost/flask_pg"
    POSTS_PER_PAGE = 12  # пагинация, вывод данных на страницу
    MAX_PAGE = 100  # максимальное количество страниц

    # ===== ВАРИАНТЫ ИМПОРТА SECRET_KEY ИЗ ПЕРЕМЕНЫХ СРЕД =====
    # **** МОЖНО ИСПОЛЬЗОВАТЬ ВАРИАНТА ****
    # SECRET_KEY = os.getenv('SECRET_KEY')
    # **** ИЛИ ВОТ ТАКОЙ ВАРИАНТ ****
    # SECRET_KEY = os.environ.get('SECRET_KEY')

    # ==== ПАРАМЕТРЫ НАСТРОЙКИ ПОЧТЫ ========
    # MAIL_SERVER = "smtp.gmail.com"
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # =============== ПАМЯТКА КОМАНД ===========================
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///./data/movies.db'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///./data/test.db'
    # SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    # SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'order.db')
    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")

    # # basedir = os.path.abspath(os.path.dirname(__file__))
    # BASE_DIR = os.path.abspath(path="data")
    # POST_PATH = os.path.join(BASE_DIR, "posts.json")
    # COMMENT_PATH = os.path.join(BASE_DIR, "comments.json")
    # BOOKMARKS_PATH = os.path.join(BASE_DIR, "bookmarks.json")
    # UPLOAD_FOLDER = os.path.join(BASE_DIR, "images")
    # MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    # =========================================================
