#!/usr/bin/env python
# -*- coding: utf-8 -*-
from marshmallow import Schema, fields

from app.setup_db import db


class Genre(db.Model):
    """
    `Genre` **Жанр**

    - `id` — идентификатор
    - `name` — название жанра
    """
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f"<Genre: {self.name}>"


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
