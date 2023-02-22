#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request

from app.dao.model.movie import Movie

from app.config import Config


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    # ==== РЕАЛИЗАЦИЯ ИЗ ВИДЕОУРОКА ПО РАЗБОРУ КУРСАВОЙ =======
    def get_all(self, filters):
        status = filters.get("status")
        page = filters.get("page")

        if status == "new" and page is not None:
            result = self.session.query(Movie).order_by(Movie.year.desc()).\
                paginate(int(page), Config.POSTS_PER_PAGE, max_per_page=Config.MAX_PAGE,
                         error_out=False).items
            return result

        elif status == "new":
            return self.session.query(Movie).order_by(Movie.year.desc()).all()

        elif page is not None:
            result = self.session.query(Movie).\
                paginate(int(page), Config.POSTS_PER_PAGE, max_per_page=Config.MAX_PAGE,
                         error_out=False).items
            return result

        return self.session.query(Movie).all()

    def create(self, movie_data):
        movie_d = Movie(**movie_data)
        self.session.add(movie_d)
        self.session.commit()
        return movie_d

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()
        return movie

    # def get_all(self):
    #     director = request.args.get("director_id")
    #     genre = request.args.get("genre_id")
    #     year = request.args.get("year")
    #
    #     if year is not None:
    #         movies = Movie.query.filter(Movie.year == year)
    #         return movies
    #
    #     if director and genre is not None:
    #         movies = Movie.query.filter(Movie.director_id == director).filter(Movie.genre_id == genre)
    #         return movies
    #
    #     if genre is not None:
    #         movies = Movie.query.filter(Movie.genre_id == genre)
    #         return movies
    #
    #     if director is None:
    #         # ==== РЕАЛИЗУЕМ ПАГИНАЦИЮ (вывод на страницу) ====
    #         # ТАК КАК ПАГИНАЦИЯ НЕ ИТЕРИРУЕТСЯ ТО ВЫВОД БУДЕТ ПО items
    #         page = request.args.get('page', 1, type=int)
    #         movies = Movie.query.paginate(page=page, per_page=Config.POSTS_PER_PAGE).items
    #         # movies = self.session.query(Movie).all()
    #     else:
    #         movies = Movie.query.filter(Movie.director_id == director)
    #     return movies
