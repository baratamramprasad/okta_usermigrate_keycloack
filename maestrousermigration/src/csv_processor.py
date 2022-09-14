# This is written for purpose of POC for creting users in keycloack from csv file
# The csv file is being created using rockstar chrome extension from okta admin console page.
# If this works,then it is written by Ramprasad else I do not know

import csv
import json
import user_create
import time
import main
from pathlib import Path


def process_data(dataset):
    token = user_create.get_access_token()
    dataset[0].append('migration status')
    sucess_count =0
    failed_count =0
    total_count =0
    header = dataset[0]
    for userdata in dataset[1:]:
        #time.sleep(1)
        total_count +=1
        user_profile = convert_userprofile_tojson(header,userdata)
        #print(user_profile)
        #token = user_create.get_access_token()
        response = user_create.create_user(user_profile,token)
        if response.status_code == 401 :
            print("token is expired and hence resending request with new token")
            token = user_create.get_access_token()
            response = user_create.create_user(user_profile,token)
            print("invalid token error:"+response.text)
        if response.status_code == 201:
            userdata.append('Sucess')
            sucess_count +=1
        else:
           userdata.append('Failed due to'+response.text)
           failed_count +=1
    if total_count == sucess_count + failed_count & sucess_count != 0:
       print('Super sucess')
       print(f'sucess_count = {sucess_count} failed_count = {failed_count} and total_count={total_count} ')
    else :
        print(f'Look seriously {total_count-(sucess_count+failed_count)}  users are missed to be processed.')
        print(f'sucess_count = {sucess_count} failed_count = {failed_count} and total_count={total_count} ')
    
    return dataset
  


def convert_userprofile_tojson(headerline,data):
    datamap = {}
    col=0
    #print(headerline)
    #print(data)
    for key in headerline:
        if key != 'migration status' :
            datamap[key] = data[col]
            col +=1
    datamap["enabled"] = "true"
    if main.SET_UPDATE_PASSWORD_ACTION == "true":
        datamap["requiredActions"]= [ "UPDATE_PASSWORD" ]
    #datamap["email"] = datamap["User"]
    #print(jsonpayload)
    str1=json.dumps(datamap,indent=4)
    return str1

def parse_csv(filepath,outfilepath):
    with open(file_path) as file:
        data = [line for line in csv.reader(file)]
        dataset = process_data(data)
              
    with open(outfilepath,"w") as outfile:
        csv.writer(outfile).writerows(dataset)


base_path = Path(__file__).parent
#file_path = (base_path / "../data/PasswordHealthReport.csv").resolve()
file_path = (base_path / "../data/usersexported.csv").resolve()
file_path_out = (base_path / "../data/PasswordHealthReportout.csv").resolve()
parse_csv(file_path,file_path_out)