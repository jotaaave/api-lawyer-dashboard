from flask import Blueprint, jsonify, request
from repository.client_memory_repository import clientMemoryRepository
from services.client_service import ClientService
from app.errors import InvalidFormBody

clients_bp = Blueprint('clients', __name__)

@clients_bp.get("/clients")
def get_all_clients():
    clients = ClientService(clientMemoryRepository).get_all()
    return jsonify({
        "clients": clients
    })

@clients_bp.get("/client/<int:id>")
def get_one_client(id: int):
    client = ClientService(clientMemoryRepository).get_client_by_id(id)
    return jsonify({
        "client": client
    })

@clients_bp.post("/client")
def add_client():
    try:
        data = request.get_json()
        result = ClientService(clientMemoryRepository).add(data)

        return jsonify(result)
    except InvalidFormBody:
        return jsonify({
            "error": "Invalid Form Body"
        }), 400