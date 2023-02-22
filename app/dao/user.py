#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
# Метод хеширование пароля
import hashlib
import base64
import hmac

from app.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS

from app.dao.model.user import User
from app.dao.model.user import FavoriteMovie
from app.dao.model.user import FavoriteGenre


class UserDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_username(self, user_name):
        return self.session.query(User).filter(User.name == user_name).first()

    def get_user_by_email(self, email):
        return self.session.query(User).filter_by(email=email).first()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return user

    def add_favorite_movie(self, data_mov: dict):
        """ Создаем словарь
        parameter: user_id
        parameter: movie_id
        """
        favorite_mov = FavoriteMovie(**data_mov)
        self.session.add(favorite_mov)
        self.session.commit()

    def del_favorite_movie(self, user_id, movie_id):
        favorite_mov = self.session.query(FavoriteMovie).\
            filter(FavoriteMovie.user_id == user_id, FavoriteMovie.movie_id == movie_id).first()

        self.session.delete(favorite_mov)
        self.session.commit()

    def add_favorite_genre(self, data_genre: dict):
        """ Создаем словарь
        parameter: user_id
        parameter: genre_id
        """
        favorite_genre = FavoriteGenre(**data_genre)
        self.session.add(favorite_genre)
        self.session.commit()

    def del_favorite_genre(self, user_id, genre_id):
        favorite_genre = self.session.query(FavoriteGenre). \
            filter(FavoriteGenre.user_id == user_id, FavoriteGenre.genre_id == genre_id).first()

        self.session.delete(favorite_genre)
        self.session.commit()

    # === ВАРИАНТ ИЗ ВИДЕОРАЗБОРА КУРСОВОЙ ====
    def update(self, user_d):
        user = self.get_one(user_d.get("id"))

        user_d['created_on'] = datetime.fromisoformat(user_d['created_on'])
        user_d['updated_on'] = datetime.now()

        for k, v in user_d.items():
            setattr(user, k, v)

        self.session.add(user)
        self.session.commit()

    # ==== УДАЛЕНИЕ ПО ИМЕНИ ====
    def delete(self, name_d):
        name = self.get_username(name_d)
        self.session.delete(name)
        self.session.commit()
        return name

    def compare_passwords(self, password_hash, other_password) -> bool:
        """ Сравнение паролей """
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac(
                'sha256',
                other_password.encode('utf-8'),
                PWD_HASH_SALT,
                PWD_HASH_ITERATIONS
            )
        )

    # === MY VARIANT =====
    # def update(self, user_d):
    #     self.session.add(user_d)
    #     self.session.commit()
    #     return user_d

    # ==== VARIANT UPDATE ====
    # def update(self, user_d):
    #     user = self.get_one(user_d.get("id"))
    #     user.name = user_d.get("name")
    #     user.password = user_d.get("password")
    #     self.session.add(user)
    #     self.session.commit()

    # ==== УДАЛИТЬ ПО ID ====
    # def delete(self, uid):
    #     user = self.get_one(uid)
    #     self.session.delete(user)
    #     self.session.commit()
    #     return user


