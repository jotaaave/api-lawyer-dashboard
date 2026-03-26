from bcrypt import hashpw, checkpw, gensalt

class BcryptService:
    def hash_password(self, password: str):
        password_enconded = password.encode()
        salt = gensalt()
        hashed_password = hashpw(password_enconded, salt)
        return hashed_password

    def compare_hash(self, input: str, hashed_input: str):
        enconded_input = input.encode()
        return checkpw(enconded_input, hashed_input)