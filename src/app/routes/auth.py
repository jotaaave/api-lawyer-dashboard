from flask import Blueprint, request, jsonify
from config import Config
from bcrypt import hashpw, checkpw, gensalt

auth = Blueprint("auth_jwt", __name__)

@auth.post("/auth/login")
def login():
    data = request.get_json()
    email, password = data.get('email'), data.get('password')

    if (email == findedUserFake["email"]):
        if (checkpw(password.encode(), findedUserFake["password"])):
            return jsonify({
                "acess-token": "peguei da api"
            }), 200

    return jsonify({
        "error": "Invalid email or password"
    }), 400