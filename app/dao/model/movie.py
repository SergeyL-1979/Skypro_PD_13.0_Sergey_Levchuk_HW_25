#!/usr/bin/env python
# -*- coding: utf-8 -*-
from marshmallow import Schema, fields

from app.setup_db import db


class Movie(db.Model):
    """
    - ** id ** - первичный ключ
    - ** title **- название
    - ** description ** - описание
    - ** trailer ** - ссылка на трейлер
    - ** year ** - год выпуска
    - ** rating ** - рейтинг
    - ** genre_id ** - id жанра
    - ** director_id **  - id режиссера
    """
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    trailer = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")

    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
