#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_restx import Resource, Namespace

from app.implemented import user_service

from app.decorators import auth_required

favorite_ns = Namespace('favorites')


@favorite_ns.route('/movies/')
class FavoriteMovieView(Resource):

    @auth_required
    def post(self):
        req_json = request.json
        head = request.headers
        email = user_service.get_user_email(head)
        user_service.add_favorite_movie(email, req_json.get("movie_id"))

        return "", 204

    @auth_required
    def delete(self):
        req_json = request.json
        head = request.headers
        email = user_service.get_user_email(head)
        user_service.del_favorite_movie(email, req_json.get("movie_id"))

        return "", 204


@favorite_ns.route('/genres/')
class FavoriteGenreView(Resource):

    @auth_required
    def post(self):
        req_json = request.json
        head = request.headers
        email = user_service.get_user_email(head)
        user_service.add_favorite_genre(email, req_json.get("genre_id"))

        return "", 204

    @auth_required
    def delete(self):
        req_json = request.json
        head = request.headers
        email = user_service.get_user_email(head)
        user_service.del_favorite_genre(email, req_json.get("genre_id"))

        return "", 204
