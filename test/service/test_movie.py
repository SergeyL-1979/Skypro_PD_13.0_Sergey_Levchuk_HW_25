#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from app.services.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self, filters):
        movies = self.movie_service.get_all(filters)
        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "id": 4,
            "title": "title",
            "description": "description",
            "trailer": "trailer",
            "year": 3000,
            "rating": 7
        }

        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(mid=1)

    def test_update(self):
        movie_d = {
            "id": 4,
            "title": "title_2",
            "description": "description",
            "trailer": "trailer",
            "year": 3000,
            "rating": 8.8
        }

        self.movie_service.update(movie_d)
