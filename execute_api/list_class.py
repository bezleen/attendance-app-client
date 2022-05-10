from requests.structures import CaseInsensitiveDict
from datetime import datetime
import json
import requests
import marshmallow as ma


PREFIX_DOMAIN= "http://14.225.254.88:5000/v1"
def exec_list_class(access_token):
    #headers = CaseInsensitiveDict()
    #headers["Authorization"] = "Bearer "+str(access_token)
    url=PREFIX_DOMAIN+"/api/classroom"
    headers = CaseInsensitiveDict()
    headers['Authorization']="Bearer "+ access_token
    response= requests.get(url=url,headers=headers)
    return response.json()
