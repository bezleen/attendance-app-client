from requests.structures import CaseInsensitiveDict
from datetime import datetime
import json
import requests
import marshmallow as ma


class Item(ma.Schema):
    class meta:
        ordering = True

    name=ma.fields.Str()
    student_oid=ma.fields.List(ma.fields.Str(),default=[],missing=[])


PREFIX_DOMAIN= "http://14.225.254.88:5000/v1"
def add_class(access_token,name):
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer "+str(access_token)
    url=PREFIX_DOMAIN+"/api/classroom"
    todo={
        "name":name
    }
    todo=Item().load(todo)
    response= requests.post(url=url,json=todo,headers=headers)
    return response.json()
