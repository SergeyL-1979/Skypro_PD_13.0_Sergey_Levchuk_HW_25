#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest.mock import MagicMock

import pytest

from app.dao.model.user import User
from app.dao.user import UserDAO

from app.dao.model.movie import Movie
from app.dao.movie import MovieDAO

from app.dao.model.director import Director
from app.dao.director import DirectorDAO


@pytest.fixture()
def user_dao():
    user_dao = UserDAO(None)

    john = User(id=1, name="John", password="test", role="admin")
    nord = User(id=2, name="Nord", password="test", role="user")
    kate = User(id=3, name="Kate", password="test", role="user")

    user_dao.get_one = MagicMock(return_value=john)
    user_dao.get_all = MagicMock(return_value=[john, nord, kate])
    user_dao.create = MagicMock(return_value=User(id=3))
    user_dao.delete = MagicMock()
    user_dao.update = MagicMock()
    return user_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    zodiac_1 = Movie(
        id=1,
        title="Зодиак_1",
        description="Гороскоп_1",
        trailer="https://example.com",
        year=1985,
        rating=8
    )
    zodiac_2 = Movie(
        id=2,
        title="Зодиак_2",
        description="Гороскоп_2",
        trailer="https://example.com",
        year=1988,
        rating=8.2
    )
    zodiac_3 = Movie(
        id=3,
        title="Зодиак_3",
        description="Гороскоп_3",
        trailer="https://example.com",
        year=1990,
        rating=8.5
    )

    movie_dao.get_one = MagicMock(return_value=zodiac_1)
    movie_dao.get_all = MagicMock(return_value=[zodiac_1, zodiac_2, zodiac_3])
    movie_dao.create = MagicMock(return_value=Movie(id=1))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name="Stallone")
    director_2 = Director(id=2, name="Shell")
    director_3 = Director(id=3, name="King")

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=[director_1, director_2, director_3])
    director_dao.create = MagicMock(return_value=Director(id=1))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao
