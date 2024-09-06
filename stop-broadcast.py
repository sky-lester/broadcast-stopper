import jwt
import random
import string
import datetime
import os
from dotenv import load_dotenv
import requests
import argparse

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

def parse_arguments():
    parser = argparse.ArgumentParser(description="Stop a broadcast")
    parser.add_argument('user_id', type=str, help='User ID for the broadcast')
    args = parser.parse_args()

def stop_streamer():
    parse_arguments()
    url = os.getenv("WEBRTC_URL")
    token = generate_token()
    headers = {
        'Authorization': token
    }

    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        print('Broadcast stopped successfully!')
    else:
        print(f'Failed to stop the broadcast: {response.status_code}, {response.text}')

stop_streamer()
