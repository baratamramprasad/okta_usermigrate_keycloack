import requests
import json
import main

def get_access_token():
    token_request = requests.post(main.OPENID_ENDPOINT, data=main.CLIENT_CRED_DATA)
    print(f"token response {token_request.json()} \n")
    token_raw = token_request.json()
    token = token_raw.get("access_token")
    return token

def create_user(user_profile,accees_token):
    #{'username': 'rampraaasad.baratam@newfold.com', 'firstName': 'ram', 'lastName': 'prasad', 'email': 'rampraasad.baratam@newfold.com', 'enabled': 'true', 'requiredActions': ['UPDATE_PASSWORD']}
    user_profile=json.loads(user_profile) 
    print(user_profile)
    headers = {"Authorization": "Bearer " + accees_token, "Content-Type": "application/json"}
    user_request = requests.post(main.USERS_ENDPOINT, json=user_profile, headers=headers)
    print(f"create_user response: {user_request} with data  {user_request.text} \n")
    return user_request


