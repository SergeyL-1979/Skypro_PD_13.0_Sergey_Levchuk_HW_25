#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_restx import Resource, Namespace

from app.implemented import genre_service
from app.dao.model.genre import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenreView(Resource):
    """
    :parameter- `/genres/` —  возвращает все жанры,
    :parameter- `/genres/<id>` — возвращает информацию о жанре с перечислением списка фильмов по жанру,

    :parameter- `POST /genres/` —  добавляет жанр,
    :parameter- `PUT /genres/<id>` —  обновляет жанр,
    :parameter- `DELETE /genres/<id>` —  удаляет жанр.
    """

    def get(self):
        page = request.args.get("page")

        filters = {
            "page": page
        }
        all_genres = genre_service.get_all(filters)
        return genres_schema.dump(all_genres), 200

    def post(self):
        req_json = request.json
        genre_service.create(req_json)
        return "", 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    """
    :parameter- `/genres/` —  возвращает все жанры,
    :parameter- `/genres/<id>` — возвращает информацию о жанре с перечислением списка фильмов по жанру,

    :parameter- `POST /genres/` —  добавляет жанр,
    :parameter- `PUT /genres/<id>` —  обновляет жанр,
    :parameter- `DELETE /genres/<id>` —  удаляет жанр.
    """

    def get(self, gid: int):
        try:
            genre = genre_service.get_one(gid)
            return genre_schema.dump(genre), 200
        except Exception as e:
            return str(e), 404

    def put(self, gid):
        req_json = request.json
        req_json["id"] = gid
        genre_service.update(req_json)
        return "", 204

    def patch(self, gid):
        req_json = request.json
        req_json["id"] = gid
        genre_service.update(req_json)
        return "", 204

    def delete(self, gid):
        genre_service.delete(gid)
        return "", 204
