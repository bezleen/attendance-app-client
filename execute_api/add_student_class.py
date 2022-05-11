from requests.structures import CaseInsensitiveDict
from datetime import datetime
import json
import requests
import marshmallow as ma


class Item(ma.Schema):
    class meta:
        ordering = True

    email=ma.fields.Email()
    name=ma.fields.Str()
    student_id=ma.fields.Str()


PREFIX_DOMAIN= "http://14.225.254.88:5000/v1"
def add_student_class(access_token,email,student_id,name,class_id):
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer "+str(access_token)
    url=PREFIX_DOMAIN+"/api/student?class="+class_id
    todo={
        "email":email,
        "name":name,
        "student_id":student_id
    }
    todo=Item().load(todo)
    response= requests.post(url=url,json=todo,headers=headers)
    return response.json()
