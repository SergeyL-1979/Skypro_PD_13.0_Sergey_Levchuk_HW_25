#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from flask import request
from app.dao.model.genre import Genre
from app.config import Config


class GenreDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self, filters):
        page = filters.get("page")

        if page is not None:
            result = self.session.query(Genre).\
                paginate(int(page), Config.POSTS_PER_PAGE, max_per_page=Config.MAX_PAGE,
                         error_out=False).items
            return result
        return self.session.query(Genre).all()

    # def get_all(self):
    #     # ==== РЕАЛИЗУЕМ ПАГИНАЦИЮ (вывод на страницу) ====
    #     page = request.args.get('page', 1, type=int)
    #     genre = Genre.query.paginate(page=page, per_page=Config.POSTS_PER_PAGE).items
    #     # return self.session.query(Genre).all()
    #     return genre

    def create(self, data):
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()

        return genre

    def update(self, genre):
        self.session.add(genre)
        self.session.commit()

        return genre

    def delete(self, gid):
        genre = self.get_one(gid)
        self.session.delete(genre)
        self.session.commit()

        return genre
