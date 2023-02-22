#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest.mock import MagicMock

import pytest

from app.dao.model.genre import Genre
from app.dao.genre import GenreDAO
from app.services.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name="Драма")
    genre_2 = Genre(id=2, name="Комедия")
    genre_3 = Genre(id=3, name="Триллер")

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
    genre_dao.create = MagicMock(return_value=Genre(id=1))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def movie_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None

    def test_get_all(self, filters):
        genres = self.genre_service.get_all(filters)
        assert len(genres) > 0

    def test_create(self):
        genre_d = {
            "id": 4,
            "name": "Comedy"
        }

        genre = self.genre_service.create(genre_d)
        assert genre.id is not None

    def test_delete(self):
        self.genre_service.delete(gid=1)

    def test_update(self):
        genre_d = {
            "id": 4,
            "name": "Документалка",
        }

        self.genre_service.update(genre_d)

