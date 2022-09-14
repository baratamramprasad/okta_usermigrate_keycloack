import requests
import json

URL = "http://localhost:8080/"
openid_url = URL + "realms/mastrorealm/protocol/openid-connect/token"
user_url = URL + "admin/realms/mastrorealm/users"

data = {
    "client_secret": "9Tg8MhfznWaLzgWpqagm9gcTIBMEmC53",
    "grant_type": "client_credentials",
    "client_id": "bh-webpro-client",
}

def get_access_token():
    token_request = requests.post(openid_url, data=data)
    print(f"token response {token_request.json()} \n")
    token_raw = token_request.json()
    token = token_raw.get("access_token")
    return token

def create_user(user_profile,accees_token):
    user_profile=json.loads(user_profile) 
    print(user_profile)
    headers = {"Authorization": "Bearer " + accees_token, "Content-Type": "application/json"}
    user_request = requests.post(user_url, json=user_profile, headers=headers)
    print(f"create_user response: {user_request} with data  {user_request.text} \n")
    return user_request


