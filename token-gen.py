import jwt
import random
import string
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def generate_random_string(length=36):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_token(payload=None):
    if payload is None:
        payload = {
            'iss': 'apollo',
            'aud': generate_random_string(),
            'iat': random.randint(0, 9999),
            'nbf': random.randint(0, 9999),
        }
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    secret = os.getenv("JWT_SECRET")
    token = jwt.encode(payload, secret, algorithm='HS256')
    return token

token = generate_token()
print(f'Bearer {token}')
