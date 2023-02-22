#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from app.services.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self, filters):
        directors = self.director_service.get_all(filters)
        assert len(directors) > 0

    def test_create(self):
        director_d = {
            "id": 4,
            "name": "Shon"
        }

        director = self.director_service.create(director_d)
        assert director.id is not None

    def test_delete(self):
        self.director_service.delete(did=1)

    def test_update(self):
        director_d = {
            "id": 4,
            "name": "Shoness",
        }

        self.director_service.update(director_d)

