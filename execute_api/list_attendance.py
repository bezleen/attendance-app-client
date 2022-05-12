from requests.structures import CaseInsensitiveDict
from datetime import datetime
import json
import requests
import marshmallow as ma


PREFIX_DOMAIN= "http://14.225.254.88:5000/v1"
def exec_list_attendance(access_token,class_id,state,date):
    #headers = CaseInsensitiveDict()
    #headers["Authorization"] = "Bearer "+str(access_token)
    url=PREFIX_DOMAIN+"/api/classroom/"+class_id+"?state="+state+"&date="+date
    headers = CaseInsensitiveDict()
    headers['Authorization']="Bearer "+ access_token
    response= requests.get(url=url,headers=headers)
    return response.json()
