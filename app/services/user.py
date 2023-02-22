#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Метод хеширование пароля
import hashlib
import base64
import jwt

from app.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, JWT_SECRET, JWT_ALGORITHM

from app.dao.user import UserDAO


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_username(self, user_name):
        return self.dao.get_username(user_name)

    def get_user_by_email(self, email):
        return self.dao.get_user_by_email(email)

    def get_all(self):
        return self.dao.get_all()

    def add_favorite_movie(self, email, movie_id):
        """ Получаем по почте айди юзера из токена, после полученное
        айди юзера и айди фильма из переменной передаем в запрос в БД """
        user = self.get_user_by_email(email)
        data_mov = {
            "user_id": user.id,
            "movie_id": movie_id
        }
        self.dao.add_favorite_movie(data_mov)

    def del_favorite_movie(self, email, movie_id):
        user = self.get_user_by_email(email)
        self.dao.del_favorite_movie(user.id, movie_id)

    def add_favorite_genre(self, email, genre_id):
        """ Создаем словарь, который передаем в запрос к БД через ДАО """
        user = self.get_user_by_email(email)
        data_genre = {
            "user_id": user.id,
            "genre_id": genre_id
        }
        self.dao.add_favorite_genre(data_genre)

    def del_favorite_genre(self, email, genre_id):
        user = self.get_user_by_email(email)
        self.dao.del_favorite_genre(user.id, genre_id)

    def create(self, data_user):
        """ Создаем хэшированный пароль """
        data_user["password"] = self.get_hash(data_user["password"])
        return self.dao.create(data_user)

    def update(self, user_d):
        self.dao.update(user_d)
        return self.dao

    # ==== Удаление по имени ====
    def delete(self, name):
        self.dao.delete(name)

    def get_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Преобразовать пароль в байты
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self, password_hash, other_password) -> bool:
        """ Сравниваем пароли """
        return self.dao.compare_passwords(password_hash, other_password)

    def get_user_email(self, head):
        """
        Получаем полностью заголовок, находим токен JWT и декодируем
        :param head: заголовки
        :return: возвращаем идентификатор пользователя
        """
        data = head["Authorization"]
        token = data.split("Bearer ")[-1]

        try:
            data_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            return data_token.get("email")
        except Exception as e:
            return f"No{e}", 401

    # ==== ВАРИАНТ ОБНОВЛЕНИЯ ДАННЫХ ====
    # def update(self, u_data):
    #     uid = u_data.get("id")
    #     user = self.get_one(uid)
    #     if "name" in u_data:
    #         user.name = u_data.get("name")
    #     if "surname" in u_data:
    #         user.surname = u_data.get("surname")
    #     if "email" in u_data:
    #         user.email = u_data.get("email")
    #     if "role" in u_data:
    #         user.role = u_data.get("role")
    #     self.dao.update(user)

    # ==== Удаление по ID ====
    # def delete(self, uid):
    #     self.dao.delete(uid)
