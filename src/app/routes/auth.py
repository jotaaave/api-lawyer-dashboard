from flask import Blueprint, request, jsonify
from services.user_service import UserService
from repository.user_memory_repository import userMemoryRepository
from app.errors import NotFound, UserAlreadyExists

auth = Blueprint("auth_jwt", __name__)

@auth.post("/auth/register")
def register():
    data = request.get_json()
    email, password = data.get('email'), data.get('password')

    try:
        UserService(userMemoryRepository).register_user({
            "email": email,
            "password": password
        })
    except UserAlreadyExists:
        return jsonify({
            "error": "User Already Exists"
        }), 400
    except Exception as e:
        print(e)

    return jsonify({
        "success": "Register ok"
    })

@auth.post("/auth/login")
def login():
    data = request.get_json()
    email, password = data.get('email'), data.get('password')

    try:
        jwt_token = UserService(userMemoryRepository).auth_user({
            "email": email,
            "password": password
        })
    except NotFound:
        return jsonify({
            "error": "Invalid email or password"
        }), 400
    except Exception as e:
        print(e)

    return jsonify({
        "access_token": jwt_token
    })
    