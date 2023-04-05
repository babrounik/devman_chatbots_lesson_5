import requests
from dotenv import load_dotenv
import os
from pathlib import Path
from urllib.parse import urljoin


def main():
    env_file_path = Path.cwd() / ".env"
    load_dotenv(env_file_path)
    client_id = os.environ['CLIENT_ID']
    api_base_url = 'https://api.moltin.com'
    auth_url = urljoin(api_base_url, 'oauth/access_token')
    print(auth_url)
    params = {'client_id': client_id, 'grant_type': 'implicit'}
    response = requests.post(auth_url, data=params)  # , headers=headers)
    response.raise_for_status()
    response_dict = response.json()
    access_token = response_dict["access_token"]

    headers = {'Authorization': f'Bearer {access_token}'}
    products_url = "https://api.moltin.com/pcm/products"
    products_response = requests.post(products_url, headers=headers)
    products_response.raise_for_status()
    print(products_response.json())


if __name__ == '__main__':
    main()
