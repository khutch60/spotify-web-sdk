import requests
import base64
from bot import access_bot

def get_access_token():
    auth_url = 'https://accounts.spotify.com/authorize'
    token_url = 'https://accounts.spotify.com/api/token'

    redirect_uri = "*********"
    client_id = "**********"
    client_secret = "***********"

    auth_params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": "user-read-private user-read-email streaming",

    }

    response = requests.get(url=auth_url, params=auth_params)   

    auth_code = access_bot(url=response.url, uri=redirect_uri)

    auth_header = base64.urlsafe_b64encode((client_id + ':' + client_secret).encode()).decode('ascii')
    token_headers = {
        "Authorization": "Basic " + auth_header,
        "content-type": "application/x-www-form-urlencoded",
    }
    token_params = {
        "grant_type":  "authorization_code",
        "code": auth_code,
        "redirect_uri": redirect_uri,
    }

    token_response = requests.post(url=token_url, headers=token_headers, data=token_params)
    return [token_response.json(), token_headers]


def refresh_token(refresh_token, headers):

    url = 'https://accounts.spotify.com/api/token'   

    params = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }


    response = requests.post(url=url, headers=headers, params=params)
    response = response.json()
    return response['access_token']


    




