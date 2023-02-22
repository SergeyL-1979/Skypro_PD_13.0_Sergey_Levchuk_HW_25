#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from app.services.user import UserService


class TestUserService:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        self.user_service = UserService(dao=user_dao)

    def test_get_one(self):
        user = self.user_service.get_one(1)

        assert user is not None
        assert user.id is not None

    def test_get_all(self):
        users = self.user_service.get_all()

        assert len(users) > 0

    def test_create(self):
        user_d = {
            "name": "Ivan",
            "password": "test"
        }

        user = self.user_service.create(user_d)

        assert user.id is not None

    def test_delete(self):
        self.user_service.delete(1)

    def test_update(self):
        user_d = {
            "id": 3,
            "name": "Niko",
            "password": "admin"
        }

        self.user_service.update(user_d)
