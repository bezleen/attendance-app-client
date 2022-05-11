from requests.structures import CaseInsensitiveDict
from datetime import datetime
import json
import requests
import marshmallow as ma


class Item(ma.Schema):
    class meta:
        ordering = True

    student_oid=ma.fields.Str()



PREFIX_DOMAIN= "http://14.225.254.88:5000/v1"
def add_student_into_class(access_token,student_oid,class_id):
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer "+str(access_token)
    url=PREFIX_DOMAIN+"/api/classroom/"+class_id
    todo={
        "student_oid":str(student_oid)
    }
    todo=Item().load(todo)
    response= requests.put(url=url,json=todo,headers=headers)
    return response.json()
