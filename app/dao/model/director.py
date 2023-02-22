#!/usr/bin/env python
# -*- coding: utf-8 -*-
from marshmallow import Schema, fields

from app.setup_db import db


class Director(db.Model):
    """
    `Director` **Режиссер**

    - `id` — идентификатор
    - `name` — имя режиссера
    """
    __tablename__ = 'director'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f"<Directors: {self.name}>"


class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
