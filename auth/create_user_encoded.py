import jwt
from app import create_Secret_key

key = create_Secret_key()

def create_user_encoded(payload):
    password_encode = jwt.encode(payload, key, algorithm='HS256')