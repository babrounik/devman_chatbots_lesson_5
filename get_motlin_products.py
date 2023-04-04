import requests
from dotenv import load_dotenv
import os
from pathlib import Path


def main():
    env_file_path = Path.cwd() / ".env"
    load_dotenv(env_file_path)
    store_id = os.environ['STORE_ID']
    client_secret = os.environ['CLIENT_SECRET']
    client_id = os.environ['CLIENT_ID']

    api_base_url = 'https://api.moltin.com'
    products_uri = '/pcm/products'

    auth_url = f'{api_base_url}/oauth/{client_secret}'
    params = {
        'client_id': client_id,
        'grant_type': 'implicit'
    }
    response = requests.post(auth_url, data=params)
    response.raise_for_status()

    print(response.json())


# curl https://api.moltin.com/v2/carts/abc \
#      -H "Authorization: Bearer XXXX"

# response = requests.post(url, json=data, headers=headers)

if __name__ == '__main__':
    main()
