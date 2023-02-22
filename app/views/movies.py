#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_restx import Resource, Namespace

from app.implemented import movie_service
from app.dao.model.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    """
    Запрос всех фильмов. При запросе с параметром
    :parameter- `/movies` — возвращает список всех фильмов, разделенный по страницам;
    :parameter- `/movies/<id>` — возвращает подробную информацию о фильме.

    Организован поиск по режиссерам и жанрам
    :parameter - /movies/?director_id=1
    выводит список фильмов по ID режиссером
    :parameter - /movies/?genre_id=4
    выводит список всех фильмов по ID жанров
    :parameter - /movies/?director_id=2&genre_id=4
    выводит список фильмов по ID режиссера и жанра
    """
    def get(self):
        status = request.args.get("status")
        page = request.args.get("page")

        filters = {
            "status": status,
            "page": page
        }

        all_movies = movie_service.get_all(filters)
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "", 201


@movie_ns.route('/<int:mid>')
class MoviesView(Resource):
    """
    Реализованы все методы
    :parameter- `/movies` — возвращает список всех фильмов, разделенный по страницам;
    :parameter- `/movies/<id>` — возвращает подробную информацию о фильме.

    :parameter- `POST /movies/` —  добавляет кино в фильмотеку,
    :parameter- `PUT /movies/<id>` —  обновляет кино,
    :parameter- `DELETE /movies/<id>` —  удаляет кино.
    """
    def get(self, mid: int):
        try:
            movie = movie_service.get_one(mid)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return str(e), 404

    def put(self, mid):
        req_json = request.json
        req_json["id"] = mid
        movie_service.update(req_json)
        return "", 204

    def patch(self, mid):
        req_json = request.json
        req_json["id"] = mid
        movie_service.update_partial(req_json)
        return "", 204

    def delete(self, mid):
        movie_service.delete(mid)
        return "", 204