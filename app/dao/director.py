#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.dao.model.director import Director
from app.config import Config


class DirectorDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self, filters):
        page = filters.get("page")

        if page is not None:
            result = self.session.query(Director).\
                paginate(int(page), Config.POSTS_PER_PAGE, max_per_page=Config.MAX_PAGE,
                         error_out=False).items
            return result
        return self.session.query(Director).all()

    # def get_all(self):
    #     return self.session.query(Director).all()

    def create(self, data):
        director = Director(**data)
        self.session.add(director)
        self.session.commit()

        return director

    def update(self, director):
        self.session.add(director)
        self.session.commit()

        return director

    def delete(self, did):
        director = self.get_one(did)
        self.session.delete(director)
        self.session.commit()

        return director
