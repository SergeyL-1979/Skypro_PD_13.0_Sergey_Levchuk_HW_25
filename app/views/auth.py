#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_restx import Resource, Namespace, Api, reqparse
from flask_restx.inputs import email

# ===== НЕ МОГУ ПОНЯТЬ КАК ЭТИ ИМПОРТЫ ТО РАБОТАЮТ С ТОЧКАМИ ============
# ==================== ТО РАБОТАЮТ БЕЗ НИХ =======================
from app.decorators import auth_required, admin_required

from app.implemented import auth_service, user_service
# ============ ИЛИ ============
# from container import auth_service

auth_ns = Namespace('auth')

# ===== ДЛЯ ПАРАМЕТРОВ В ВЕБ_ИНТЕРФЕЙСЕ FLASK-RESTX (swagger) API ======
# api = Api()
# parser = reqparse.RequestParser()
# parser.add_argument(name='email', type=email(), help='email')
# parser.add_argument(name='password', type=str, help='Password')
#
#
# auth_reqparser = reqparse.RequestParser(bundle_errors=True)
# auth_reqparser.add_argument(name="name", type=str, required=True, nullable=False)
# auth_reqparser.add_argument(name="surname", type=str, required=True, nullable=False)
# auth_reqparser.add_argument(name="email", type=email(), required=True, nullable=False)
# auth_reqparser.add_argument(name="password", type=str, required=True, nullable=False)
# auth_reqparser.add_argument(name="favorite_genre_id", type=str, required=True, nullable=False)
# auth_reqparser.add_argument(name="role", type=str, required=True, nullable=False)


@auth_ns.route('/login')
class AuthView(Resource):
    # @api.doc(parser=parser)  # для API swagger
    # @auth_required
    def post(self):
        data = request.json
        e_mail = data.get("email", None)
        password = data.get("password", None)

        # === ЭТО ВОЗМОЖНОСТЬ ВХОДА ЧЕРЕЗ API_swagger ===
        # data = parser.parse_args()
        # e_mail = data["email"]
        # password = data["password"]

        if None in [e_mail, password]:
            return "", 400

        tokens = auth_service.generate_tokens(e_mail, password)
        return tokens, 201

    def put(self):
        data = request.json

        access_token = data.get("access_token")
        refresh_token = data.get("refresh_token")
        validate = auth_service.validate_tokens(access_token, refresh_token)

        if not validate:
            return "Invalid token", 400

        tokens = auth_service.approve_refresh_token(refresh_token)
        return tokens, 201


@auth_ns.route('/register')
class RegisterView(Resource):
    # @api.doc(parser=auth_reqparser)  # для API swagger
    def post(self):
        req_json = request.json

        e_mail = req_json.get("email")
        password = req_json.get("password")

        if None in [e_mail, password]:
            return "", 400

        # ========= API SWAGGER ================
        # req_json = auth_reqparser.parse_args()

        user_service.create(req_json)
        return f"Пользователь добавлен!", 201
