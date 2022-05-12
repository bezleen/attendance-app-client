from requests.structures import CaseInsensitiveDict
from datetime import datetime
import json
import requests
import marshmallow as ma


class Item(ma.Schema):
    class meta:
        ordering = True

    email=ma.fields.Email()
    password=ma.fields.Str()

PREFIX_DOMAIN= "http://14.225.254.88:5000/v1"
def exec_login(email,password):
    #headers = CaseInsensitiveDict()
    #headers["Authorization"] = "Bearer "+str(access_token)
    url=PREFIX_DOMAIN+"/api/user/auth"
    todo={
        "email":email,
        "password":password
    }
    todo=Item().load(todo)
    response= requests.post(url=url,json=todo)
    return response.json()
