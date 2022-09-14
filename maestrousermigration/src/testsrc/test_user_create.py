import sys

sys.path.insert(0, '/Users/ramprasad.b/python_ws/maestrousermigration/src/')
 
import user_create


user_data = {
    "username": "pyuser1",
    "enabled": "true",
    "credentials": [{"type": "password", "value": "ram123"}],
     "firstName": "pyuserRamprasad2",
    "lastName": "Baratam",
    "email": "test2@test.com",
}

user_data1={
    "username": "1111q@gmail.com", 
    "enabled": "true", 
    "email": "1111q@gmail.com"
    }
user_data2='{"username": "ramprasad.baratam@newfold.com", "firstName": "Chiranjit", "lastName": "Dutta", "email": "ramprasad.baratam@newfold.com", "enabled": "true"}'
response = user_create.create_user(user_data2,user_create.get_access_token())

#print(response.text)