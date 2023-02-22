#!/usr/bin/env python
# -*- coding: utf-8 -*-
# === DAO ===
from .dao.user import UserDAO
from .dao.movie import MovieDAO
from .dao.director import DirectorDAO
from .dao.genre import GenreDAO

# === SERVICE ===
from .services.user import UserService
from .services.movie import MovieService
from .services.director import DirectorService
from .services.genre import GenreService

from .services.auth import AuthService

# ==== IMPORT DATABASE ====
from .setup_db import db


user_dao = UserDAO(db.session)
user_service = UserService(user_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

auth_service = AuthService(user_dao)
