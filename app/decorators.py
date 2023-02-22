#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps

import jwt
from flask import request, abort
from app.constants import JWT_SECRET, JWT_ALGORITHM


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]

        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        try:
            user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            role = user.get("role")
            if role != "admin":
                abort(403)
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


# ================ ОБРАЗЕЦ JWT ============
# decorator for verifying the JWT
# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = None
#         # jwt is passed in the request header
#         if 'x-access-token' in request.headers:
#             token = request.headers['x-access-token']
#         # return 401 if token is not passed
#         if not token:
#             return jsonify({'message': 'Token is missing !!'}), 401
#
#         try:
#             # decoding the payload to fetch the stored details
#             data = jwt.decode(token, app.config['SECRET_KEY'])
#             current_user = User.query.filter_by(public_id=data['public_id']).first()
#         except:
#             return jsonify({
#                 'message': 'Token is invalid !!'
#             }), 401
#         # returns the current logged in users contex to the routes
#         return f(current_user, *args, **kwargs)
#
#     return decorated
