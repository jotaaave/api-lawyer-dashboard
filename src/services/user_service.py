from interfaces.user_repository_type import UserRepositoryInterface
from services.bcrypt_service import BcryptService
from app.errors import NotFound, UserAlreadyExists
from config import Config
import jwt
import uuid

class UserService:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.db = user_repository

    def register_user(self, data):
        email, password = data["email"], data["password"]

        user = self.db.find_by_email(email)

        if user:
            raise UserAlreadyExists
        
        self.db.add_user({
            "email": email,
            "password": BcryptService().hash_password(password),
            "id": str(uuid.uuid4())
        })


    def auth_user(self, data):
        email, password = data["email"], data["password"]

        user = self.db.find_by_email(email)

        if not user:
            raise NotFound

        hashed_password = user["password"]

        is_password = BcryptService().compare_hash(password, hashed_password)
        
        if not is_password:
            raise NotFound
        
        payload = {
            "user_id": user["id"]
        }

        return jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm="HS256")