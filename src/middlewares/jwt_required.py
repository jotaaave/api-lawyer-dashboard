from functools import wraps
from flask import request, jsonify, g
from config import Config
from jwt import InvalidTokenError, ExpiredSignatureError
import jwt

def jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.headers.get("Authorization")

        if not auth:
            return jsonify({ "error": "Unauthorized" }), 401
        
        try:
            token = jwt.decode(auth.split(' ')[1], Config.JWT_SECRET_KEY, algorithms="HS256")

            g.user_id = token
        except InvalidTokenError:
            return jsonify({ "error": "token invalido "})

        return func(*args, **kwargs)

    return wrapper