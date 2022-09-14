# This is used to make the python program as commandline
#

from jproperties import Properties
from pathlib import Path

configs = Properties()
base_path = Path(__file__).parent

file_path = (base_path / "../application.properties").resolve()

with open(file_path, 'rb') as read_prop:
    configs.load(read_prop)

# ('grant_type', PropertyTuple(data='"client_credentials"', meta={}))


URL = configs.get("URL").data
OPENID_ENDPOINT = URL + configs.get("OPENID_URI").data
USERS_ENDPOINT =  URL + configs.get("USER_URI").data
GRANT_TYPE = configs.get("GRANT_TYPE").data
CLIENT_ID = configs.get("CLIENT_ID").data
CLIENT_SECRET = configs.get("CLIENT_SECRET").data
SET_UPDATE_PASSWORD_ACTION = configs.get("SET_UPDATE_PASSWORD_ACTION").data

#{'client_secret': '9Tg8MhfznWaLzgWpqagm9gcTIBMEmC53', 'grant_type': 'client_credentials', 'client_id': 'bh-webpro-client'}
CLIENT_CRED_DATA = {
    "client_secret":  CLIENT_SECRET,
    "grant_type": GRANT_TYPE,
    "client_id": CLIENT_ID,
}

def printProperties():
    print(CLIENT_CRED_DATA)
    print(URL)
    print(OPENID_ENDPOINT)
    print(GRANT_TYPE)
    print(CLIENT_ID)
    print(CLIENT_SECRET)
 
#printProperties()