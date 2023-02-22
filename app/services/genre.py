#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.dao.genre import GenreDAO


class GenreService:

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self, filters):
        return self.dao.get_all(filters)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        gid = data.get("id")
        director = self.get_one(gid)
        director.name = data.get("name")

        self.dao.update(director)

    def update_partial(self, data):
        gid = data.get("id")
        genre = self.get_one(gid)
        if "name" in data:
            genre.name = data.get("name")

        self.dao.update(genre)

    def delete(self, gid):
        self.dao.delete(gid)
