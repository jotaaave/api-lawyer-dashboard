from flask import Blueprint, request, jsonify
from config import Config
from bcrypt import hashpw, checkpw, gensalt

auth = Blueprint("auth_jwt", __name__)

fake_database = [
    {
        "email": "jv1446170@gmail.com",
        "password": hashpw("123456".encode(), gensalt())
    }
]

@auth.post("/auth/login")
def login():
    data = request.get_json()
    email, password = data.get('email'), data.get('password')

    findedUserFake = fake_database[0]

    if (email == findedUserFake["email"]):
        if (checkpw(password.encode(), findedUserFake["password"])):
            return jsonify({
                "acess-token": "peguei da api"
            }), 200

    return jsonify({
        "error": "Invalid email or password"
    }), 400