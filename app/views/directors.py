#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_restx import Resource, Namespace

from app.implemented import director_service
from app.dao.model.director import DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorView(Resource):
    """
    :parameter- `/directors/` — возвращает всех режиссеров,
    :parameter- `/directors/<id>` — возвращает подробную информацию о режиссере,

    :parameter- `POST /directors/` —  добавляет режиссера,
    :parameter- `PUT /directors/<id>` —  обновляет режиссера,
    :parameter- `DELETE /directors/<id>` —  удаляет режиссера.
    """
    def get(self):
        page = request.args.get("page")

        filters = {
            "page": page
        }
        all_directors = director_service.get_all(filters)
        return directors_schema.dump(all_directors), 200

    def post(self):
        req_json = request.json
        director_service.create(req_json)
        return "", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    """
    :parameter- `/directors/` — возвращает всех режиссеров,
    :parameter- `/directors/<id>` — возвращает подробную информацию о режиссере,

    :parameter- `POST /directors/` —  добавляет режиссера,
    :parameter- `PUT /directors/<id>` —  обновляет режиссера,
    :parameter- `DELETE /directors/<id>` —  удаляет режиссера.
    """
    def get(self, did: int):
        try:
            director = director_service.get_one(did)
            return director_schema.dump(director), 200
        except Exception as e:
            return str(e), 404

    def put(self, did):
        req_json = request.json
        req_json["id"] = did
        director_service.update(req_json)
        return "", 204

    def patch(self, did):
        req_json = request.json
        req_json["id"] = did
        director_service.update(req_json)
        return "", 204

    def delete(self, did):
        director_service.delete(did)
        return "", 204

