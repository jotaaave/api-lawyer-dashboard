from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.clients import clients_bp
    from app.routes.auth import auth

    app.register_blueprint(clients_bp)
    app.register_blueprint(auth)

    return app

app = create_app()
